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
            <div class="kuai1">设置头像</div>
        </div>
        <div class="line1"></div>
        <div class="con">
            <input type="file" value="file" class="file">
            <div class="tip">支持jpg、png格式的图片，且文件小于2M</div>
            <div class="img">
                <img src="../assets/2018-08-12_114109.png" alt="">
            </div>
            <input type="button" value="保存" class="dd">
            <input type="button" value="取消" class="dd">
        </div>
        <div class="con1">
            <div class="one">头像预览</div>
            <div class="two"></div>
            <div class="three">大尺寸头像（234×234像素）</div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "page2"
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
.bg .con{
    width: 340px;height: 400px;margin-left: 20px;margin-top: 20px;
    float: left;text-align: left;
}
.bg .con .file{
    width:70px;height:35px;margin-top: 20px;margin-left:15px;float: left;
}
.bg .con .tip{
    width:230px;height: 35px;float: left;font-size:12px;color: #C8C8C8;
    text-align: center;line-height: 35px;margin-top:17px;
}
.bg .con .img{
    width: 265px;height: 265px;border:2px solid #EFEFEF;margin-top:70px;margin-left:35px;
}
.bg .con .img img{
    width: 265px;height: 265px;
}
.bg .con .dd{
    width:80px;height:30px;margin-left:35px;margin-top: 20px;
    background-color: #E2DEDE;border: none;border-radius:5px;
}
.bg .con1{
    width: 200px;height: 267px;margin-top:92px;border-left: 2px solid #E5E5E5;float:left;
}
.bg .con1 .one{
    width: 200px;height:30px;font-size: 14px;line-height: 30px;color:black;text-align: left;
    margin-left: 15px;
}
.bg .con1 .two{
     width:180px;height:180px;background-color: #E1E1E1;margin-left: 15px;
}
.bg .con1 .three{
    width: 200px;height:25px;font-size: 12px;line-height:25px;color:#C8C8C8;text-align: left;
    margin-left:15px;
}
</style>