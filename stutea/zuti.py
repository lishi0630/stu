from django.views import View
from django.shortcuts import HttpResponse,redirect,render
from .sqlfenzhung import sql
from django import forms
import xlrd
from .fenye import pages
import math
import json
class mycheck(forms.Form):
    # name=forms.CharField(error_messages={"required":"此项必填"})
    file=forms.FileField(error_messages={"required":'上传文件'})
class zuti(View):
    def get(self,req):
        return render(req, "zuti.html")
temp=""
class zutiadd(View):
    def get(self,req):
        curr_page = req.GET.get("page") if req.GET.get("page") else 0
        num = 4
        curr_page = int(curr_page)
        db = sql()
        result = db.select("select * from classr")
        tixingres=db.select("select * from types")
        xueke = db.select("select * from stage")

        count = db.select("select count(*) from shiti left join stage on shiti.staid=stage.staid left join types on shiti.tyid=types.tyid left join grade on shiti.gid=grade.gid")
        total = math.ceil(count[0]['count(*)'] / num)
        print(count,total,curr_page)
        page=pages()
        str=page.fenye(total, curr_page,"/zutiadd/")
        #创建临时表
        global temp
        temp=sql()
        temp.exec("create TEMPORARY table temps(id int(10) primary key auto_increment,info varchar(5000),cnum varchar(30),staid varchar(32))")
        return render(req,"zutiadd.html",{"result":result,"tixingres":tixingres,"xueke":xueke,"str":str})
class zutisearch(View):
    def get(self,req):
        curr_page = req.GET.get("page") if req.GET.get("page") else 0
        num = 4
        curr_page = int(curr_page)

        cnum=int(req.GET.get("cnum")) if req.GET.get("cnum") else ""
        staid=req.GET.get("staid")
        tyid=req.GET.get("tyid")
        con=req.GET.get("con")
        db=sql()

        #[{'id': 1, 'info': '1-4,12-4', 'cnum': '1', 'staid': 'xueke-01'}]
        #[{shiti.id,shiti.shitiid,shiti.tigan,shiti.opt,shiti.answer,grade.gname,stage.staname,types.tyname
        if cnum:
            gids=db.select("select gid from classr where cnum=%s",[cnum])[0]["gid"]
        contion=''' where 1=1 '''
        contion+=''' and shiti.gid='%s' '''%(gids) if gids else ""
        contion +=''' and shiti.staid= '%s' '''%(staid) if staid else ""
        contion += ''' and shiti.tyid='%s' '''%(tyid) if tyid else ""
        contion += '''and shiti.tigan like "%%{0}%%" '''.format(con) if con else ""
        contion+= '''limit %s,%s'''%(curr_page*num,num)

        result1=db.select("select shiti.id,shiti.shitiid,shiti.tigan,shiti.opt,shiti.answer,grade.gname,stage.staname,types.tyname from shiti left join stage on shiti.staid=stage.staid left join types on shiti.tyid=types.tyid left join grade on shiti.gid=grade.gid "+contion)
        result = db.select("select * from classr")
        tixingres = db.select("select * from types")
        xueke = db.select("select * from stage")

        #临时表
        global temp
        if not temp=="":
            score=temp.select("select * from temps")
        ti={}
        if len(score)>0:
            for item in score:
                for item in item["info"].split(","):
                    ti[item.split("-")[0]] = item.split("-")[1]
        for id in ti.keys():
            for item in result1:
                if item["id"] == int(id):
                    item["score"] = ti[id]
        count = db.select("select count(*) from shiti left join stage on shiti.staid=stage.staid left join types on shiti.tyid=types.tyid left join grade on shiti.gid=grade.gid "+contion)
        total = math.ceil(count[0]['count(*)'] / num)
        db.close()
        page = pages()
        return render(req, "zutiadd.html", {"date": result1,"result":result,"tixingres":tixingres,"xueke":xueke,"str":page.fenye(total, curr_page, "/zutisearch/"),"cnum":cnum,"staid":staid,"tyid":tyid})
class fileload(View):
    def get(self,req):
        db=sql()
        result = db.select("select * from grade")
        db.close()
        return render(req,"fileload.html",{"date":result})
    def post(self,req):
        obj=mycheck(req.POST,req.FILES)
        gid=req.POST.get("gid")
        staid=req.POST.get("staid")
        if  obj.is_valid():
            file = req.FILES["file"]
            sheet=xlrd.open_workbook(filename=None,file_contents=file.read())
            date=sheet.sheet_by_index(0)
            arrs=[]
            for item in range(1,date.nrows):
                arr=date.row_values(item)
                db=sql()
                arr[0]=db.one("select tyid from types where tyname=%s",[arr[0]])["tyid"]
                arr[2] = "|".join(arr[2].split("\n"))
                arr.insert(0, gid)
                arr.insert(1, staid)
                arrs.append(arr)
            db.exec_many("insert ignore into shiti (gid,staid,tyid,tigan,opt,answer) values (%s,%s,%s,%s,%s,%s)",arrs)
            db.close()
        else:
            abc = obj.errors
            return render(req, "fileload.html", {"file": abc})
class xuantitemp(View):
    def get(self,req):
        info = req.GET.get("info")
        cnum = req.GET.get("cnum")
        staid = req.GET.get("staid")
        temp.exec("insert into temps(info,cnum,staid) values (%s,%s,%s)", [info, cnum, staid])
        return HttpResponse("ok")
class temp(View):
    def get(self,req):
        aa = temp.select("select * from temps")
        ti={}
        for item in aa:
            for item in item["info"].split(","):
                ti[item.split("-")[0]]=item.split("-")[1]
        arr=[]
        for item in ti.keys():
            abc=temp.select("select tigan,opt from shiti where id=%s", [item])[0]
            abc["score"]=ti[item]
            arr.append(abc)
        return HttpResponse("组题完成")
class tempzuti(View):
    def get(self,req):
        startime=req.GET.get("startime")
        endtime=req.GET.get("endtime")
        print()
        aa = temp.select("select * from temps")
        print(aa)
        ti={}
        for item in aa:
            if not ti:
                ti["info"]=item["info"]
            else:
                ti["info"] += ","+item["info"]
            ti["cnum"]=item["cnum"]
            ti["staid"]=item["staid"]
        db=sql()
        print(ti["info"])
        db.exec("insert into zuti (info,cnum,staid,startime,endtime) values (%s,%s,%s,%s,%s)",[ti["info"],ti["cnum"],ti["staid"],startime,endtime])
        return HttpResponse("ok")






