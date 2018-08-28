from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .sqlfenzhung import sql
from .hash import *
import json
import datetime
from .fenye import *
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        #if isinstance(obj, datetime):
            #return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)
class selInfo(View):
    def get(self,req):
        user=req.GET.get("user")
        db=sql()
        result=db.select("select cnum from stu where snuion=%s",[user])
        # [{'cnum': 3}, {'cnum': 1}]1-3,12-1,13-5,2-2
        date=db.select("select * from zuti where cnum=%s",[result[0]["cnum"]])
        xueke=db.select("select staname from stage where staid=%s",[date[0]["staid"]])
        date[0]["staname"]=xueke[0]["staname"]
        banji = db.select("select cname from classr where cnum=%s", [date[0]["cnum"]])
        date[0]["cname"] = banji[0]["cname"]
        return HttpResponse(json.dumps(date,cls=CJsonEncoder))
class loginStu(View):
    def get(self,req):
        user=req.GET.get("user")
        pass1=req.GET.get("pass")
        db=sql()
        result=db.select("select * from stu where snuion=%s and pass=%s",[user,md5(pass1)])
        if len(result)>0:
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
class timetest(View):
    def get(self,req):
        curr_page = req.GET.get("page") if req.GET.get("page") else 0
        num = 1
        curr_page = int(curr_page)
        id=req.GET.get("id")
        db=sql()
        date=db.select("select * from zuti where id=%s",[id])
        ti = {}
        for item in date:
            for item in item["info"].split(","):
                ti[item.split("-")[0]] = item.split("-")[1]
        arr = []
        #abc=db.select("select shitiid,tigan,opt,tyid,answer from shiti where id=%s limit %s,%s",[item, curr_page * num, num])[0]
        abc = db.select("select shitiid,tigan,opt,tyid,answer from shiti where id=%s limit %s,%s", [list(ti.keys())[curr_page],0,num])[0]
        abc["score"] = ti[list(ti.keys())[curr_page]]
        abc['count']=math.ceil(len(ti.keys())/num)
        abc['page']=curr_page
        arr.append(abc)
        return HttpResponse(json.dumps(arr,cls=CJsonEncoder))
class stageStu(View):
    def get(self,req):
        db=sql()
        date=db.select("select * from stage")
        db.close()
        return HttpResponse(json.dumps(date))
class suijikaoshi(View):
    def get(self,req):
        staid=req.GET.get("staid")
        curr_page = req.GET.get("page") if req.GET.get("page") else 0
        num = 1
        curr_page = int(curr_page)
        db = sql()
        date = db.select("select * from shiti where find_in_set(%s,shiti.staid) limit %s,%s",[staid,num*curr_page,num])
        count=db.select("select count(*) from shiti where find_in_set(%s,shiti.staid)",[staid])[0]['count(*)']
        ye={}
        ye["count"]=count
        ye["page"]=curr_page
        date.append(ye)
        db.close()
        return HttpResponse(json.dumps(date))
class typeStu(View):
    def get(self,req):
        db = sql()
        date = db.select("select * from types")
        db.close()
        return HttpResponse(json.dumps(date))
class unique(View):
    def get(self,req):
        curr_page = req.GET.get("page") if req.GET.get("page") else 0
        num = 1
        curr_page = int(curr_page)
        staid = req.GET.get("staid")
        tyid = req.GET.get("tyid")
        db = sql()
        date = db.select("select * from shiti where staid=%s and tyid=%s limit %s,%s", [staid,tyid,num*curr_page,num])
        count=db.select("select count(*) from shiti where staid=%s and tyid=%s",[staid,tyid])[0]['count(*)']
        ye = {}
        ye["count"] = count
        ye["page"] = curr_page
        date.append(ye)
        db.close()
        return HttpResponse(json.dumps(date))
class chengjiinfo(View):
    def get(self,req):
        snuion=req.GET.get("snuion")
        db = sql()
        score=db.select("select zutiid,fenshu,stu.snuion,stu.sname,classr.cname from score left join stu on score.snuion=stu.snuion left join classr on stu.cnum=classr.cnum where score.snuion=%s",[snuion])
        db.close()
        print(score)
        return HttpResponse(json.dumps(score,cls=CJsonEncoder))
class jiaojuan(View):
    def get(self,req):
        snuion = req.GET.get("user")
        zutiid = req.GET.get("zutiid")
        fenshu = req.GET.get("fenshu")
        db=sql()
        db.exec("insert into score (snuion,zutiid,fenshu) values (%s,%s,%s)",[snuion,zutiid,fenshu])
        return HttpResponse("ok")

