<template>
    <div class="right list">
        <div class="testtype" >
            <div class="typetitle" >
                <div class="fenleidian"></div>
                <div class="fenlei">请选择你的试题类型</div>
            </div>
            <div class="kecheng">
                课程：<span class="kechen" :class="{active:row.style==1}" v-for="row in date" value="row.staid" @click="xk(row)">{{row.staname}}</span>
            </div>
            <div class="star" @click="quekaoti">确认考题</div>
            <div class="end">清空选项</div>
        </div >
        <div class="kaoti" style="display: none;">
             <form v-for="(item,index1) in shiti">
                <ol type="1"  >
                    <li type="1" v-if="item.tyid=='tixing-01'">
                        <h1>单选题</h1>
                        <h3 style="text-align: left">
                        <input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;(5分)</h3>
                        <ol type="A" start="A" >
                            <div  v-for="(row,index) in item.opt.split('|')">
                                <input type="radio" :name="index1" :value="index"  @click="aa(index,item.shitiid,item.answer)">
                                <li style="text-align:left">{{ row }}</li>
                            </div>
                        </ol>
                    </li>
                </ol>
                <ol type="1" >
                    <li type="1" v-if="item.tyid=='tixing-02'" >
                        <h1>多选题</h1>
                        <h3 style="text-align: left">
                        <input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;(5分)</h3>
                        <ol type="A" start="A" >
                            <div  v-for="(row,index) in item.opt.split('|')">
                                <input type="checkbox" :name="index1" :value="index"  @click="bb(index,item.shitiid,item.answer)">
                                <li style="text-align:left">{{ row }}</li>
                            </div>
                        </ol>
                    </li>
                </ol>
                <ol type="1" >
                        <li type="1" v-if="item.tyid=='tixing-03'">
                            <h3>简答题</h3>
                            <h3 style="text-align: left">
                            <input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;({10分)</h3>
                            请输入您的答案：
                            <textarea :name="index1" style="margin: 0;" cols="30" rows="10"></textarea>
                        </li>
                    </ol>
             </form>
             <div class="fenye">
            <span @click="get(0)">首页</span>
            <span v-if="page>0" @click="get(page-1)">上一页</span>
            <span v-else-if="page<=0">上一页</span>
            <span @click="get(page)">{{this.page+1}}</span>
            <span v-if="page==count">下一页</span>
            <span v-else-if="page<count" @click="get(page+1)">下一页</span>
            <span @click="get(count-1)">尾页</span>
            <span >共{{count}}页</span>
        </div>
            <div class="tijiao" @click="jiaojuan">交卷</div>
            <div class="score" style="display: none;width: 100px;height: 100px;"></div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                date:"",
                banji:"",
                xueke:"",
                shiti:[],
                index:{},
                score:5,
                answer:{},
                defen:0,
                page :0, //当前页码
                count : 0, //总记录数
            }
        },
        mounted(){
            fetch("/ajax/stageStu").then(function (e) {
                return e.json()
            }).then((e)=>{
                this.date=e
            })
        },
        methods:{
            xk(row){
                this.xueke=row.staid
                for(var i in this.date){
                    this.date[i].style=0
                }
                row.style=1
            },
            quekaoti(){
                fetch("/ajax/suijikaoshi/?staid="+this.xueke+"&page="+this.page).then(function (e) {
                    return e.json()
                }).then((e)=>{
                    this.shiti=e;
                    this.page=e[1]["page"]
                    this.count=e[1]["count"]
                    console.log(e,this.page,this.count);
                })
                var kaoti=document.querySelector(".kaoti")
                kaoti.style.display="block"
            },
            aa(index,id,answer){
                console.log(index,id,answer);
                this.index[id]=index+1
                this.answer[id]=answer
            },
            bb(index,id,answer){
                this.answer[id]=answer.split(",")
                if(!this.index[id]){
                    this.index[id]=[index+1]
                }else if(parseInt(this.index[id])!=index+1){
                    this.index[id].push(index+1)
                }
                this.answer[id]=answer.split(",")
            },
            jiaojuan(){
                for(var i in this.index){
                    if(this.index[i]==parseInt(this.answer[i])){
                        this.defen+=this.score
                    }else if(typeof this.index[i]=="object"){
                        if(this.index[i].length==this.answer[i].length){
                            for (var a in this.index[i]){
                                for(var b in this.answer[i]){
                                    if(parseInt(this.index[i][a])==parseInt(this.answer[i][b])){
                                        a++;b++;
                                    }else {
                                        b++
                                    }
                                }
                    }
                            if(a>=this.index[i].length){
                                this.defen+=this.score
                            }else {
                                this.defen+=0
                            }
                        }else {
                            this.defen+=0
                        }
                    }
                }
                fetch("/ajax/jiaojuan/?snuion="+sessionStorage.getItem("user")+"&zutiid="+this.date[0]["id"]+"&fenshu="+this.defen).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    if(e=="ok"){
                        alert("试题提交成功")
                    }
                })
               var score=document.querySelector(".score")
                score.style.display="block";
                score.append(`您的客观题得分是${this.defen}`)
            },
            get(page){
                fetch("/ajax/suijikaoshi?staid="+this.xueke+"&page="+page).then(function (e) {
                    return e.json()
                }).then((e) => {
                    this.shiti=e
                    this.page=e[1]["page"]
                    this.count=e[1]["count"]
                })
            }
        }
    }
</script>

<style scoped>
    .active{
        color: red;
    }
    .box{
    width: 100vw;
    height: 100vh;
}
.right{
    width:100%;
    height: 100%;
    #background: #ffc017;
    float: left;
    overflow: hidden;
}
.right .title{
    /*width: 100%;*/
    height: 40px;
    #background: red;
    overflow: hidden;
}
.title1{
    width: 200px;height: 100%;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    line-height: 40px;
    margin-left: 450px;
    float: left;
}
.person{
    width: 150px;height: 100%;
    font-size: 14px;
    text-align: center;
    line-height: 60px;
    float: right;
}
.quit{
    width: 150px;height: 100%;
    font-size: 14px;
    text-align: center;
    line-height: 60px;
    float: right;
    color: #B8B8B8;
    display: block;
    margin-right: 100px;
}
.search{
    width: 300px;height: 40px;
    border: 2px solid #35363A;
    border-radius: 50px;
    margin-left: 20px;
    margin-top: 5px;
}
.search input{
    width: 220px;height: 35px;
    padding: 0 10px;
    outline: 0;
    border-radius: 50px;
    box-sizing: border-box;
    display: block;
    float: left;
    border: 0;
}
.search button{
    width: 60px;height: 30px;
    border-radius: 20px;
    padding: 2px 10px;
    background: white;
    box-sizing: border-box;
    background: #35363A;
    border: #35363A;
    color: white;
    margin-top: 5px;
}
.testtype{
    width: 300px;height: 200px;
    #background: red;
    margin-left: 20px;
    margin-top:20px;
}
.typetitle{
    width: 100%;height: 30px;
    overflow: hidden;
}
.fenleidian{
    width: 10px;height: 6px;
    background: #ffc017;
    border-radius: 3px;
    margin-top: 12px;
    margin-left: 10px;
    float: left;
}
.fenlei{
    width: 150px;height: 20px;
    float: left;
    margin-top: 5px;
    margin-left: 20px;
}
.banji{
    width: 240px;height: 20px;
    margin-top: 5px;
    margin-left: 40px;
    #background: pink;
}
.kecheng{
    width: 240px;height: 20px;
    margin-top: 15px;
    margin-left:40px;
    #background: pink;text-align: left;
}
.kechen{
    margin-right: 15px;
}
.leixing{
    width: 240px;height: 20px;
    margin-top: 15px;
    margin-left: 40px;
    #background: pink;
}
.star{
    width: 100px;height: 30px;
    margin-top:30px;
    margin-left: 10px;
    border: 2px solid #35363A;
    border-radius: 15px;
    text-align: center;
    line-height: 30px;
    float: left;
}
.end {
    width: 100px;
    height: 30px;
    margin-top:30px;
    margin-right:20px;
    border: 2px solid #35363A;
    border-radius: 15px;
    text-align: center;
    line-height: 30px;
    float: right;
}
</style>