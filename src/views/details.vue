<template>
    <div id="app">
        <div class="top">
            <a href=""><img src="../assets/images/returns.png" alt="" class="imgs"></a>
            <div class="top_conter">
                <span class="yuan1"></span>
                <span class="yuan2"></span>
                <span class="yuan3"></span>
                <span class="xianqing">详情</span>
                <span class="yuan3"></span>
                <span class="yuan2"></span>
                <span class="yuan1"></span>
            </div>
        </div>
        <div class="center_top">
            <div class="zhongwai">
                <div class="zhongwai_left">
                    <img src="../assets/images/1901074775_ii_cover.jpg" alt="" class="imgss_top">
                </div>
                <div class="zhongwai_right">
                    <div class="pingfen">
                        <div class="pingfenleft">
                            <div class="leftwenzi">
                            <span class="wenzismall" style="color: black">我想要的</span>
                            <span class="wenzismall wenzi1">DAVD</span>
                                </div>
                            <div class="rightwenzi">
                            <span class="wenzismall huanhang">我想要的生活</span>
                                </div>
                        </div>
                        <div class="pingfenright">
                            <img src="../assets/images/wujiao.png" alt="" class="wujiaoxing">
                            <img src="../assets/images/wujiao.png" alt="" class="wujiaoxing">
                            <img src="../assets/images/wujiao.png" alt="" class="wujiaoxing">
                            <img src="../assets/images/wujiao.png" alt="" class="wujiaoxing">
                        </div>
                    </div>
                    <div class="wenxue">
                        <span class="xiaowenzi">
                            这是一段文字，这是一段文字，这是一段文字，这是一段文字，这是一段文字，这是一段文字，这是一段文字，这是一段文字，这是一段文字，
                        </span >
                        <span class="biaoqian">
                            <span class="yuanwenzi">文学</span>
                            <span class="yuanwenzi">生活</span>
                            <span class="yuanwenzi">爱情</span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="zhongwao_xia">
                <div class="lookmulu">
                    <span class="chakanmulu">
                        <img src="../assets/images/mulu.png" alt="" class="imgshujia">
                        <span>查看目录</span>
                    </span>
                    <span class="chakanmulu">
                        <img src="../assets/images/shujia.png" alt="" class="imgshujia">
                        <span>加入书架</span>
                    </span>
                </div>
                <div class="lookxia">
                    <a href="" class="xiahuaxian">
                        <span class="tijiao">
                            <span class="dianji">点击查看</span>
                        </span>
                    </a>
                </div>
            </div>
        </div>
        <div class="kuaiji">
            <div class="kuaijileft">
                <img src="../assets/images/book.png" alt="" class="shu">
            </div>
            <div class="kuairight">
                <span class="shup">最新书评</span>
                <span class="shups">THE LATEST BOOK RESOUT</span>
                <span class="xian"></span>
            </div>
        </div>
        <div class="tianjia">
            <img src="../assets/images/jia.png" alt="" class="jiahao">
            <span class="tianjiashuping">添加书评</span>
        </div>
         <div class="kuaiji">
            <div class="kuaijileft">
                <img src="../assets/images/shuqian.png" alt="" class="shu">
            </div>
            <div class="kuairight">
                <span class="shup">我的书签</span>
                <span class="shups">THE LATEST BOOK RESOUT</span>
                <span class="xian"></span>
            </div>
        </div>
        <div class="tianjia">
            <img src="../assets/images/jia.png" alt="" class="jiahao">
            <span class="tianjiashuping">添加书评</span>
        </div>
         <div class="kuaiji">
            <div class="kuaijileft">
                <img src="../assets/images/biji.png" alt="" class="shu">
            </div>
            <div class="kuairight">
                <span class="shup">我的笔记</span>
                <span class="shups">THE LATEST BOOK RESOUT</span>
                <span class="xian"></span>
            </div>
        </div>
        <div class="tianjia">
            <img src="../assets/images/jia.png" alt="" class="jiahao">
            <span class="tianjiashuping">添加书评</span>
        </div>
    </div>
</template>
<script>
    export default {
        name: "details"
    }
</script>
<style scoped>
/*添加*/
.tianjiashuping{
    font-size: 14px;
    font-weight: 200;
    display: block;
    margin-top: 0.2rem;
}
.jiahao{
    width: 0.5rem;
    height:0.5rem;
    margin-top: 0.16rem;
    margin-left: 2.5rem;

}
.tianjia{
    width: 7rem;
    height: 0.8rem;
    border: 1px solid #cccccc;
    border-radius: 8px 8px 8px 8px ;
    margin: auto;
    margin-top: 0.1rem;
    display: flex;
}
/*书评*/
.xian{
    margin-top: 0.15rem;
    margin-left:0.32rem;
    width: 1rem;
    border-bottom: 1px solid #7FA7FE;
}
.shups{

    display: block;
    margin-left:-1.75rem;
     font-size: 10px;
    font-weight: 400;
    margin-top: 0.15rem;
}
.shup{
    display: block;
    margin-left:-3.5rem;
    font-size: 12px;
    font-weight: 600;
    margin-top: 0.1rem;
}
.kuairight{
    width: 5rem;
    height: 100%;
    /*background-color: #cccccc;*/
    display: flex;
    flex-direction: column;
}
.shu{
    width: 0.6rem;
    height: 0.6rem;
    display: block;
    margin-top: 0.1rem;
    margin-left: 0.1rem;
    border-radius: 50%;
}
.kuaijileft{
    width: 0.8rem;
    height:0.8rem;
    border-radius: 50%;
    display: flex;
    margin-left: 0.2rem;
    margin-top: 0.2rem;
}
.kuaiji{
    width: 7rem;
    height: 1.2rem;
    /*background-color: red;*/
    display: flex;
    margin: auto;
    margin-top: 0.2rem;
}
/*书籍信息*/
.pingfenleft .wenzi1{
    font-size: 8px;
     padding-top: 0.25rem;
}
.wenzismall{

    padding-left: 0.2rem;
    padding-top: 0.2rem;
}
.pingfenleft{
    width: 50%;
    height: 100%;
    display: flex;
    text-align: center;
    flex-direction: column ;
    color: #8C8C8C;
}
.pingfen{
    width: 100%;
    height: 35%;
    font-size: 12px;
    display: flex;
}
.zhongwai_right{
    width: 60%;
    height: 100%;
    /*background-color: #ff6700;*/
    display: flex;
    flex-direction:column;
}
.imgss_top{
    width:2.8rem;
    margin-left: 0.1rem;
}
.zhongwai_left{
    width: 40%;
    height: 100%;
    /*background-color: #1b6d85;*/
    display: flex;
}
.zhongwai{
    width: 100%;
    height: 3rem;
    /*background-color: red;*/
    display: flex;
}
.center_top{
    width: 7rem;
    height: 5rem;
    margin: auto;
    margin-top: 0.25rem;
    /*background-color: #1b6d85;*/
    display: flex;
    flex-direction:column;
    border: 1px solid #cccccc;
    border-radius: 8px 8px 8px 8px ;
}
.leftwenzi{
    width: 100%;
    height: 50%;
    display:flex;
}
.rightwenzi{
    width: 100%;
    height: 50%;
    display:flex;

}
.pingfenright{
    width: 50%;
    height: 100%;
    display: flex;
}
.wujiaoxing{
    width: 0.3rem;
    height: 0.3rem;
    margin-top: 0.655rem;
    margin-left: 0.02rem;
}
.wenxue{
    width: 100%;
    height: 70%;
    /*background-color: #cccccc;*/
     display: flex;
    flex-direction:column;

}
.xiaowenzi{
    margin-top: 0.2rem;
    font-size: 3px;
}
.biaoqian{
    width: 100%;
    height: 50%;
    /*background-color: #1b6d85;*/
    display: flex;
}
.yuanwenzi{
    width:1rem;
    height: 0.3rem;
    border-radius:10px 10px 10px 10px;
    background-color: #66E479;
    margin-top: 0.6rem;
    margin-left: 0.1rem;
    font-size: 3px;
    color: white;
    line-height: 0.35rem;

}
.zhongwao_xia{
    width: 100%;
    height: 40%;
    /*background-color: red;*/
    display: flex;
    flex-direction:column;

}
.lookmulu{
    width: 100%;
    height: 40%;
    /*background-color: #2b542c;*/
    display: flex;
}
.lookxia{
    width: 100%;
    height: 60%;
    /*background-color: #1b6d85;*/
}
.chakanmulu{
    width: 2.5rem;
    height: 0.6rem;
    background-color: white;
    border: 1.5px solid #cccccc;
    border-radius: 20px 20px 20px 20px ;
    text-align: center;
    line-height: 0.6rem;
    font-size: 8px;
    margin-top: 0.08rem;
    margin-left: 0.6rem;
    display: flex;
}
.imgshujia{
    width: 0.5rem;
    height: 0.5rem;
    margin-left: 0.4rem;
}
.chakanmulu span{
    margin-left: 0.1rem;
}
.tijiao{
    display: block;
    width: 3.5rem;
    height: 0.8rem;
    border-radius: 30px 30px 30px 30px;
    background-color: #4E84FF;
    margin: auto;
     margin-top:0.2rem;
    text-align: center;
    line-height: 0.3rem;
    font-size: 12px;
    text-decoration: none;

}
.xiahuaxian{
    text-decoration:none
}
.dianji{
    display: block;
    color: white;
    line-height: 0.8rem;
    font-weight: 200;
}
/*头部信息*/
.top{
    display: flex;
    width: 7.5rem;
    height: 1.26rem;
    background-color:#2D7EFF;

}
.imgs{
    width: 0.7rem;
    height: 0.7rem;
    margin-top: 0.28rem;
    margin-left: 0.2rem;


}
.top_conter {
    width: 4rem;
    height: 0.8rem;
    /*background-color: red;*/
    display: flex;
    margin-left: 1.4rem;
    margin-top: 0.23rem;
    line-height: 0.8rem;

}
.xianqing{
    font-size: 18px;
    margin-left: 0.3rem;
    margin-right: 0.15rem;
    color: white;
}
.yuan1{
    width: 0.08rem;
    height: 0.08rem;
    border-radius: 50%;
    background-color: white;
    margin-left: 0.17rem;
    margin-top: 0.365rem;
    /*line-height: 0.8rem;*/

}
.yuan2{
width: 0.11rem;
height: 0.11rem;
border-radius: 50%;
background-color: white;
margin-left: 0.17rem;
    margin-top: 0.348rem;
}
.yuan3{
width: 0.13rem;
height: 0.13rem;
border-radius: 50%;
background-color: white;
margin-left: 0.17rem;
    margin-top: 0.337rem;
}
</style>