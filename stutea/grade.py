from django.views import View
from django.shortcuts import HttpResponse,render,redirect
from .sqlfenzhung import sql
import json
class grade(View):
    def get(self,req):
        db=sql()
        result=db.select("select *,group_concat(stage.staname) as stanames from grade left join stage on find_in_set(stage.staid,grade.staid) group by grade.id")
        return render(req,"grade.html",{"date":result})
    def post(self,req):
        gid = req.POST.get("gid")
        db = sql()
        result=db.one("select group_concat(stage.staid) as staids, group_concat(stage.staname) as stanames from grade left join stage on find_in_set(stage.staid,grade.staid) where grade.gid=%s",[gid])
        print(result)
        return HttpResponse(json.dumps(result))
class gradeadd(View):
    def get(self,req):
        db=sql()
        result1 = db.select("select * from stage")
        return HttpResponse(json.dumps(result1))
    def post(self,req):
        gid = req.POST.get("gid")
        gname = req.POST.get("gname")
        staid = req.POST.getlist("staname")
        print(gid,gname,staid)
        db = sql()
        staids=''
        for item in staid:
            staids+=item+","
        staids=staids[:-1]
        db.exec("insert into grade (gname,gid,staid) values (%s,%s,%s)", [gname,gid,staids])
        db.close()
        return redirect("/grade/")
#验证年级号是否重复
class grajax(View):
    def get(self,req):
        gid=req.GET.get("gid")
        db=sql()
        result=db.one("select * from grade where gid=%s",[gid])
        db.close()
        if result:
            return HttpResponse("false")
        else:
            return HttpResponse("true")
class gradedit(View):
    def get(self,req):
        id=req.GET.get("id")
        db=sql()
        date=db.select("select * from grade where id=%s",[id])
        date1=db.select("select * from stage")
        date.append(date1)
        db.close()
        return HttpResponse(json.dumps(date))
        # return render(req,"gradedit.html",{"date":date,"date1":date1})
    def post(self,req):
        id=req.POST.get("id")
        gname=req.POST.get("gname")
        gid=req.POST.get("gid")
        staid=req.POST.getlist("staname")
        print(id,gname,gid,staid)
        # 这是年级，不需要修改其他数据
        staids=""
        for item in staid:
            staids+=item+","
        print(staids)
        staids=staids[:-1]
        db=sql()
        db.update("update grade set gname=%s,gid=%s,staid=%s where gid=%s",[gname,gid,staids,id])
        db.close()
        return redirect('/grade/')
class gradedele(View):
    def get(self,req):
        gid = req.GET.get("id")
        db=sql()
        db.delete("delete from grade where gid=%s",[gid])
        date = db.one("select cnum,cname from classr where find_in_set('%s',gid)" % (gid))
        db.update("update classr set gid='' where gid=%s",[gid])
        # 年级表
        db.close()
        return redirect('/grade/')
class gradetype(View):
    def get(self,req):
        db=sql()
        date=db.select("select * from grade")
        db.close()
        return HttpResponse(json.dumps(date))
