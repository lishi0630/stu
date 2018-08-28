<template>
     <div class="bg">
        <!--<div class="top">-->
            <!--<div class="right">[退出登陆]</div>-->
            <!--<div class="right1">欢迎您：猪八戒的小仙女</div>-->
            <!--<div class="cen">学生个人系统</div>-->
        <!--</div>-->
        <!--<div class="line"></div>-->
        <div class="menu">
            <div class="kuai"></div>
            <div class="kuai1">修改密码</div>
        </div>
        <div class="line1"></div>
         <table>
        <tr>
            <th>修改登陆密码</th>
        </tr>
    </table>
     <div class="con">
        旧密码：<input type="text" class="aa"><br>
        新密码：<input type="text" class="bb"><br>
        确认新密码：<input type="text" class="cc"><br>
         <input type="submit" value="提交" class="submit">
     </div>

     </div>
</template>

<script>
    export default {
        name: "page1"
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
    width:1366px;height:661px;cursor: pointer;
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
    width:600px;height:auto;border-collapse: collapse;margin-top:20px;margin-left: 20px;
}
th{
   color: white;font-size: 16px;font-weight:bold;text-align: left;padding-left: 15px;background-color:#666
}
tr{
    background-color:#FFC017;font-size: 14px;height:40px;width: 100%;
    color: black;margin-top:20px;margin-left: 20px;
}
td{
    width:auto;height:50px;;color: #909090;text-align: center;color:black;border: 1px solid #ECECEC;border-right:3px solid #DFDFDF;padding-left: 10px;
}
.bg .con{
    width: 585px;height:300px;background-color:#F8F8F8 ;margin-left:20px;text-align: left;
    padding-left:15px;
}
.bg .con .aa{
    width: 200px;height:30px;margin-top: 20px;font-size:16px;border: none;
    border-bottom: 1px solid #7C7C7C;background-color: #F8F8F8;outline: none;
}
.bg .con .bb{
    width: 200px;height:30px;margin-top: 20px;font-size:16px;border: none;
    border-bottom: 1px solid #7C7C7C;background-color: #F8F8F8;outline: none;
}
.bg .con .cc{
    width: 168px;height:30px;margin-top: 20px;font-size:16px;border: none;
    border-bottom:1px solid #7C7C7C;background-color: #F8F8F8;outline: none;
}
.bg .con .submit{
    width:150px;height:30px;margin-top:40px;font-size:16px;
    border: 1px solid #7C7C7C;background-color: #F8F8F8;outline: none;border-radius: 5px;
}
</style>