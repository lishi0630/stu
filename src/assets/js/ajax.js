function ajax(params) {
        // 参数的类型
        if(typeof params!=="object"){
            console.error("参数类型不对")
            return false
        }
        // 检测url是否输入
        if(!params.url){
            console.error("请传入请求的地址");
            return false
        }
        // 参数初始化
        var url=params.url;
        var type=params.type||"get";
        var dataType=params.dataType||"text";

        if(typeof params.data=="object"){
            var str="";
            for(var i in params.data){
                str+=i+"="+params.data[i]+"&"
            }
            var data="?"+str.slice(0,-1);
        }else {
            var data = params.data?"?"+params.data:"";


        }

        var async=params.async===false?false:true

        var xmlobj=new XMLHttpRequest();
        xmlobj.onload=function () {
            if(dataType=="text"){
                var result=xmlobj.responseText;
            }else if(dataType=="xml"){
                var result=xmlobj.responseXML;
            }else if(dataType=="json"){
                var result=JSON.parse(xmlobj.response);
            }
            params.success(result);

        }
        if(type=="get"){
            xmlobj.open(type,url+data,async)
            xmlobj.send();
        }else if(type=="post"){
            xmlobj.open(type,url,async);
            xmlobj.setRequestHeader("content-type","application/x-www-form-urlencoded")
            xmlobj.send(data.slice(1))
        }
    }

window.ajax=ajax