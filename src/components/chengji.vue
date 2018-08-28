<template>
    <div class="bg">
        <div class="menu">
            <div class="kuai"></div>
            <div class="kuai1">信息设置</div>
        </div>
        <div class="line1"></div>
         <table>
        <tr>
           <th>姓名</th><th>班级</th> <th>学号</th><th>考试科目</th><th>考试成绩</th>
        </tr>
         <tr v-for="item in date">
            <td v-text="item.sname">{{ item.sname }}</td>
            <td v-text="item.cname">{{item.cname}}</td>
            <td v-text="item.snuion">{{item.snuion}}</td>
            <td v-text="item.zutiid">{{item.zutiid}}</td>
            <td v-text="item.fenshu">{{item.fenshu}}</td>
        </tr>
        <!--<tr>-->
            <!--<td>张三</td>-->
            <!--<td>UAIF-1805</td>-->
            <!--<td>001</td>-->
            <!--<td>数学</td>-->
            <!--<td>88</td>-->
        <!--</tr>-->
    </table>
    </div>
</template>

<script>
export default {
        data(){
            return {
                date:""
            }
        },
        mounted(){
            fetch("/ajax/chengjiinfo/?snuion="+sessionStorage.getItem("user")).then((e)=>{
                return e.json()
            }).then((e)=>{
                console.log(e)
                this.date=e;
            })
        },
}
</script>

<style scoped>
*{
	margin: 0;
	padding: 0;
	list-style: none;
}
img{
	display: block;
}
a{
	text-decoration: none;color:#333;
}
.bg{
    width:1100px;height:661px;cursor: pointer;
}
.bg .top{
    width: 100%;height:80px;
}
.bg .top .cen{
    width:800px;height: 80px;float: right;
    font-size:24px;color: black;text-align: center;line-height: 80px;font-weight: bold;
}
.bg .top .right{
    width:120px;height: 80px;float: right;
    font-size: 14px;color: #AFAFAF;text-align: center;line-height: 80px;
}
.bg .top .right1{
    width:200px;height:80px;float: right;
    font-size: 14px;color: #5D5D5D;text-align: center;line-height: 80px;
}
.bg .line{
    width: 100%;height:8px;background-color:#C9c9c9;
}
.bg .menu{
     width: 100%;height:30px;
}
.bg .menu .kuai{
    width:6px;height:24px;background-color:#ffc017;float: left;margin-left: 20px;margin-top: 3px;
}
.bg .menu .kuai1{
    width:100px;height:100%;float: left;font-size: 14px;line-height: 30px;color: #242424;
}
.bg .line1{
    width: 100%;height:8px;background-color:#35363A;
}
table{
    width:800px;height:auto;border-collapse: collapse;margin-top:20px;margin-left: 20px;
}
th{
    border-right:1px solid #DFDFDF;color:white;font-size: 16px;font-weight:bold;
}
tr{
    background-color: #666;font-size: 14px;height:50px;width: 100%;
    color:white;border:1px solid #DFDFDF;
}
td{
    width:auto;height:50px;background-color:#F8F8F8;color: #909090;border: 1px solid #ECECEC;border:1px solid #DFDFDF;padding-left: 10px;text-align: center;color:black;
}


</style>