<template>
    <div class="shiti">
        <table>
            <tr>
                <th>班级</th><th>科目</th><th>开始考试时间</th><th>结束考试时间</th><th>退出考试</th><th>完成考试</th>
            </tr>
            <tr v-for="row in date">
                <td>{{row.cname}}</td>
                <td>{{row.staname}}</td>
                <td>{{row.startime}}</td>
                <td>{{row.endtime}}</td>
                <td>退出</td>
                <td @click="jiaojuan">交卷</td>
            </tr>
        </table>
        <form v-for="(item,index1) in shiti">
            <ol type="1"  v-if="item.tyid=='tixing-01'" >
                <h3>单选题</h3>
                <li type="1">
                    <h3 style="text-align: left"><input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;({{item.score}}分)</h3>
                        <ol type="A" start="A" >
                            <div  v-for="(row,index) in item.opt.split('|')">
                                <input type="radio" :name="item.shitiid" :value="index" @click="aa(index,item.shitiid,item.answer,item.score)">
                                <li style="text-align:left">{{ row }}</li>
                            </div>
                        </ol>
                </li>
            </ol>
            <ol type="1" v-else-if="item.tyid=='tixing-02'" >
                <h3>多选题</h3>
                <li type="1" >
                    <h3 style="text-align: left"><input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;({{item.score}}分)</h3>
                        <ol type="A" start="A" >
                            <div  v-for="(row,index) in item.opt.split('|')">
                                <input type="checkbox" :name="item.shitiid" :value="index"  @click="bb(index,item.shitiid,item.answer,item.score)">
                                <li style="text-align:left">{{ row }}</li>
                            </div>
                        </ol>
                </li>
            </ol>
            <ol type="1" v-else="item.tyid=='tixing-03'" >
                <h3>简答题</h3>
            <li type="1" >
                <h3 style="text-align: left"><input type="checkbox" style="display:none" value="item.id" >{{ item.tigan }} &nbsp;({{item.score}}分)</h3>
                请输入您的答案：
                <textarea :name="index1" style="margin: 0;" cols="30" rows="10"></textarea>
            </li>
        </ol>
       </form>
        <div class="score" style="display: none;width: 100px;height: 100px;">
        </div>
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
    </div>
</template>

<script>
import MoPaging from '@/components/fenyeCop.vue'
import fenye from '@/components/fenye.vue'
      export default {
        components : {
            MoPaging,fenye
        },
        data(){
            return{
                date:"",
                shiti:[],
                index:{},
                score:{},
                answer:{},
                defen:0,
                page :0, //当前页码
                count : 0, //总记录数
                save:this.index
            }
        },
        computed:{

        },
        mounted() {
            var user = sessionStorage.getItem("user")
            fetch("/ajax/selInfo?user=" + user).then(function (e) {
                return e.json()
            }).then((e) => {
                this.date = e
            })

            // 获取到学号，通过学号知道班级，从而查到题组，返回
            fetch("/ajax/timetest?id=" + this.$route.query.id+"&page="+this.page).then(function (e) {
                return e.json()
            }).then((e) => {
                console.log(e)
                this.shiti=e
                this.page=e[0]["page"]
                this.count=e[0]["count"]
            })
        },
        methods:{
            aa(index,id,answer,score){
                console.log(index,id,answer,score);
                this.score[id]=score
                this.index[id]=index+1
                this.answer[id]=answer
            },
            bb(index,id,answer,score){
                this.score[id]=score
                this.answer[id]=answer.split(",")
                if(!this.index[id]){
                    this.index[id]=[index+1]
                }else if(parseInt(this.index[id])!=index+1){
                    this.index[id].push(index+1)
                }
                this.answer[id]=answer.split(",")
                // this.score1=parseInt(score)
                // this.answer=answer
                // if(this.xuanxiang.length>0){
                //      for(var j in this.xuanxiang) {
                //          if (this.xuanxiang[j] == index) {
                //              break;
                //          }
                //      }
                //      this.xuanxiang.push(index+",")
                // }else{
                //      this.xuanxiang.push(index+",")
                // }
            },
            jiaojuan(){
                for(var i in this.index){
                    if(this.index[i]==parseInt(this.answer[i])){
                        this.defen+=parseInt(this.score[i])
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
                                this.defen+=parseInt(this.score[i])
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
                fetch("/ajax/timetest?id=" + this.$route.query.id+"&page="+page).then(function (e) {
                    return e.json()
                }).then((e) => {
                    this.shiti=e
                    this.page=e[0]["page"]
                    this.count=e[0]["count"]
                })
            }
        }
    }
</script>

<style scoped>
    table{
    width: 95%;height:auto;border-collapse: collapse;margin-top: 10px;margin-left:28px;
}
th{
    border-right: 1px solid #ECECEC;
}
tr{
    background-color: #666;color: white;font-size: 14px;height: 40px;width: 100%;
}
td{
    width:auto;height: 40px;background-color: white;color: #909090;
    border: 1px solid #ECECEC;padding-left: 10px;text-align: center;
}
.btn{
    width:70px;height:25px;float: right;margin-right: 15px;
}
a,span{
  color: #909090;text-decoration:none;cursor: pointer;
}
h1{
    font-size: 18px;
}
h3{
    font-size: 16px;margin-bottom: 0;
}
ol{
   font-size: 14px;
}
</style>
