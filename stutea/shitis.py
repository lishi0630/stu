from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .sqlfenzhung import *
import json
import math
import xlrd
from django import forms
#类型
def getpages(total,current,url):
    items=3
    str1='''
    <a href="%s?page=0">首页</a>
    '''%(url)
    up=current-1 if current-1 > 0 else 0
    str1 += '''
        <a href="%s?page=%s">上一页</a>
        '''%(url,up)

    before=current if current < math.floor(items/2) else math.floor(items/2)
    for item in range(before,0,-1):
        num=current-item
        if num == current:
            str1+='''<a href="%s?page=%s" style="color:red">%s</a>'''%(url,num,num+1)
        else:
            str1 += '''<a href="%s?page=%s">%s</a>''' % (url, num, num + 1)

    after=items-before
    for item in range(after):
        num = current +item
        if (num<items):
            if num==current:
                str1 += '''<a href="%s?page=%s" style="color:red">%s</a>''' % (url, num, num + 1)
            else:
                str1 += '''<a href="%s?page=%s">%s</a>''' % (url, num, num + 1)

    next=current+1 if current+1 < total else current
    str1 += '''
            <a href="%s?page=%s">下一页</a>
            '''%(url,next)
    str1 += '''
            <a href="%s?page=%s">尾页</a>
            '''%(url,total-1)
    return str1

class shititypeInfo(View):
    def get(self,req):
        db=sql()
        result=db.select("select * from shitileixing")
        db.close()
        return render(req, "shitis/shititypeInfo.html", {"data":result})
    def post(self,req):
        pass
class shititypeAdd(View):
    def get(self,req):
        return render(req,"shitis/shititypeAdd.html")
    def post(self,req):
        tiname=req.POST.get("tiname")
        tiid=req.POST.get("tiid")
        db=sql()
        db.exec("insert into shitileixing (tiname,tiid) values (%s,%s)",[tiname,tiid])
        db.close()
        return redirect("/shititypeInfo/")
class shititypedel(View):
    def get(self,req):
        tiid=req.GET.get("tiid")
        db=sql()
        db.delete("delete from shitileixing where tiid=%s",[tiid])
        db.update("update tiku set leixing=0 where leixing=%s",[tiid])
        db.close()
        return redirect("/shititypeInfo/")
    def post(self,req):
        pass
class editshititype(View):
    def get(self,req):
        tiid=req.GET.get("tiid")
        db=sql()
        result=db.one("select * from shitileixing where tiid=%s",[tiid])
        db.close()
        return render(req,"shitis/shititypeedit.html",{"data":result})
        # return HttpResponse("123")
    def post(self,req):
        id=req.GET.get("id")
        tiname=req.POST.get("tiname")
        tiid=req.POST.get("tiid")
        db=sql()
        db.update("update shitileixing set tiname=%s,tiid=%s where tiid=%s",[tiname,tiid,id])
        # db.one("select id from tiku where leixing=%s")
        db.update("update tiku set leixing=%s where leixing=%s",[tiid,id])
        db.close()
        return redirect("/shititypeInfo/")
        # return HttpResponse("123")
#试题
class shitiInfo(View):
    def get(self,req):
        nums = 10
        page = int(req.GET.get("page")) if req.GET.get("page") else 0
        shuliang = math.ceil(one("select count(*) from tiku")["count(*)"] / nums)
        jiid=req.GET.get("jiid")
        jieid=req.GET.get("jieid")
        leixing=req.GET.get("tiid")
        search=req.GET.get("search")
        option=" where 1=1 "
        option+=''' and tiku.jiid=%s '''%(jiid) if jiid else ""
        option+=''' and tiku.jieid='%s' '''%(jieid) if jieid else ""
        option+=''' and tiku.leixing=%s '''%(leixing) if leixing else ""
        option+=''' and tiku.tigan like "%%{0}%%" '''.format(search) if search else ""
        option+=" limit %s,%s"%(nums*page,nums)
        db=sql()
        result=db.select("SELECT tiku.id,tiku.tigan,nianji.nianjiname,jieduan.jieduanname,shitileixing.tiname from tiku LEFT JOIN nianji on tiku.jiid=nianji.jiid LEFT JOIN jieduan on tiku.jieid=jieduan.jieid LEFT JOIN shitileixing on shitileixing.tiid=tiku.leixing "+option)
        nianji=db.select("select nianjiname,jiid from nianji")
        jieduan=db.select("select jieduanname,jieid from jieduan")
        leixing=db.select("select tiid,tiname from shitileixing")
        db.close()
        return render(req,"shitis/shitiInfo.html",{"data":result,"nianji":nianji,"jieduan":jieduan,"leixing":leixing,"pages":getpages(shuliang,page,"/shitiInfo/")})
    def post(self,req):
        pass
class shitiInfoAdd(View):
    def get(self,req):
        db=sql()
        result=db.select("select * from nianji")
        db.close()
        return render(req,"shitis/shitiInfoAdd.html",{"data":result})
    def post(self,req):
        jiid=req.POST.get("jiid")
        jieid=req.POST.get("jieid")
        tigan=req.POST.get("tigan")
        xuanxiang=req.POST.get("xuanxiang")
        daan=req.POST.get("daan")
        leixing=req.POST.get("leixing")
        db=sql()
        db.exec("insert IGNORE into tiku (jiid,jieid,tigan,xuanxiang,daan,leixing) values (%s,%s,%s,%s,%s,%s)",[jiid,jieid,tigan,xuanxiang,daan,leixing])
        db.close()
        return HttpResponse("ok")
class delshiti(View):
    def get(self,req):
        id=req.GET.get("id")
        print(id)
        # id=3
        db=sql()
        db.delete("delete from tiku where id=%s",[id])
        result=db.select("select zuti.tiinfo,zuti.id from zuti")
        print(result)
        if result:
            obj={}
            for item in result:
                result1=item["tiinfo"].split(",")
                print(result1)
                for item1 in result1:
                    result2=item1.split("-")
                    if result2[0]!=str(id):
                        obj[result2[0]]=result2[1]
                keys=list(obj.keys())
                vals=list(obj.values())
                arr=[]
                for key in range(len(keys)):
                     arr.append(keys[key]+"-"+vals[key])
                str1=""
                str1=",".join(arr)
                print(str1)
                db.update("update zuti set tiinfo=%s where id=%s",[str1,item["id"]])
        else:
            return
        db.close()
        return redirect("/shitiInfo/")
    def post(self,req):
        pass
class editshiti(View):
    def get(self,req):
        id=req.GET.get("id")
        db=sql()
        result=db.one("select * from tiku where id=%s",[id])
        nianji=db.select("select nianji.jiid,nianji.nianjiname from nianji")
        jieduan=db.select("select jieduan.jieid,jieduan.jieduanname from jieduan")
        leixing=db.select("select shitileixing.tiname,shitileixing.tiid from shitileixing")
        db.close()
        return render(req,"shitis/editshiti.html",{"data":result,"nianji":nianji,"jieduan":jieduan,"leixing":leixing})
    def post(self,req):
        id=req.POST.get("id")
        jiid = req.POST.get("jiid")
        jieid = req.POST.get("jieid")
        tigan = req.POST.get("tigan")
        xuanxiang = req.POST.get("xuanxiang")
        daan = req.POST.get("daan")
        leixing = req.POST.get("leixing")
        db=sql()
        db.update("update tiku set jiid=%s,jieid=%s,tigan=%s,xuanxiang=%s,daan=%s,leixing=%s where id=%s",[jiid,jieid,tigan,xuanxiang,daan,leixing,id])
        db.close()
        return HttpResponse("ok")
class leixingajax(View):
    def get(self,req):
        db=sql()
        result=db.select("select * from shitileixing")
        db.close()
        return HttpResponse(json.dumps(result))
    def post(self,req):
        pass
class shujuajax(View):
    def get(self,req):
        id=req.GET.get("id")
        db=sql()
        result=db.one("select * from tiku where id=%s",[id])
        db.close()
        return HttpResponse(json.dumps(result))
    def post(self,req):
        pass
class jieduanajax1(View):
    def get(self,req):
        db=sql()
        result=db.select("select * from jieduan")
        db.close()
        return HttpResponse(json.dumps(result))
class typeshiti(View):
    def get(self,req):
        db=sql()
        result=db.select("select * from shitileixing")
        db.close()
        return HttpResponse(json.dumps(result))
    def post(self,req):
        pass
class yanzheng(forms.Form):
    jiid=forms.CharField(required=True,error_messages={"required":"必须选择一个年级"})
    jieid=forms.CharField(required=True,error_messages={"required":"必须选择一个课程"})
    filed=forms.FileField(required=True,error_messages={"required":"必须选择一个文件"})
class piliangshangchuan(View):
    def get(self,req):
        db=sql()
        result=db.select("select nianji.jiid,nianji.nianjiname from nianji")
        result1=db.select("select jieduan.jieid,jieduan.jieduanname from jieduan")
        db.close()
        return render(req,"shitis/piliangshangchuan.html",{"result":result,"result1":result1})
    def post(self,req):
        obj=yanzheng(req.POST,req.FILES)
        if obj.is_valid():
            filed=req.FILES["filed"]
            jiid=req.POST.get("jiid")
            jieid=req.POST.get("jieid")
            sleet=xlrd.open_workbook(file_contents=filed.read())
            data=sleet.sheet_by_index(0)
            arrs=[]
            db=sql()
            result=db.select("select shitileixing.tiname,shitileixing.tiid from shitileixing")
            arr={}
            for item in result:
                arr[item["tiname"]]=item["tiid"]
            for row in range(1, data.nrows):
                arr1=data.row_values(row)
                arr1[0]=arr[data.row_values(row)[0]]
                arr1[2]="|".join(data.row_values(row)[2].split("\n"))
                arr1.append(jiid)
                arr1.append(jieid)
                arrs.append(arr1)
            # db.exec_many("insert ignore into tiku")
            db.exec_many("INSERT ignore INTO tiku (leixing,tigan,xuanxiang,daan,jiid,jieid) VALUES (%s,%s,%s,%s,%s,%s)",arrs)
            # db.exec_many("insert ignore into tiku (leixing,tigan,xuanxiang,daan,jiid,jieid) values (%s,%s,%s,%s,%s,%s)",arrs)
            db.close()
            # f=open("demo.xlsx","wb")
            # for item in data.chunks():
            #     f.write(item)
            # f.close()
            return redirect("/shitiInfo/")
        else:
            objerr=obj.errors
            db = sql()
            result = db.select("select nianji.jiid,nianji.nianjiname from nianji")
            result1 = db.select("select jieduan.jieid,jieduan.jieduanname from jieduan")
            db.close()
            # jiiderr=obj.errors["jiid"][0]
            # jieiderr=obj.errors["jieid"][0]
            # fileerr=obj.errors["filed"][0]
            # return HttpResponse("123")
            # return render(req, "shitis/piliangshangchuan.html",{"fileerr":fileerr,})
            return render(req,"shitis/piliangshangchuan.html",{"objerr":objerr,"result":result,"result1":result1})