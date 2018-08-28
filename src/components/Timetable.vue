<template>
    <div class="right1">
     <table>
        <tr><th>搜索</th></tr>
        <tr>
            <td>
                学号：<input type="text" placeholder="请输入学号...">&nbsp;&nbsp;&nbsp;姓名：<input type="text" placeholder="请输入班级...">
            </td>
        </tr>
        <tr>
            <td>
                <input type="button" value="查找" class="btn">

            </td>
        </tr>
    </table>
     <table>
        <tr>
            <th>序号</th><th>班级</th><th>科目</th><th>开始考试时间</th><th>结束考试时间</th><th>操作</th>
        </tr>
        <tr >
            <td>01</td>
            <td>ui班</td>
            <td>语文</td>
            <td>12：00</td>
            <td>2：00</td>
            <td><span class="btn2">开始考试</span>&nbsp;</td>
        </tr>
        <tr v-for="row in date">
            <td >{{row.id}}</td>
            <td>{{row.cname}}</td>
            <td>{{row.staname}}</td>
            <td>{{row.startime}}</td>
            <td>{{row.endtime}}</td>
            <td><span class="btn2" @click="kaoshi(row.id)">开始考试</span>&nbsp;</td>
        </tr>
    </table>

        <div class="tishi">
            <h5> 友情提示：</h5>
            <h5>1.各位考试请注意考试时间。</h5>
            <h5>2.遵循考试规则，保持良好心态</h5>
        </div>
    </div>
</template>

<script>
    // import '@/assets/bootstrap.js/bootstrap.min.js'
    export default {
        data(){
            return{
                date:"",
                id:""
            }
        },
        mounted(){
             var user= sessionStorage.getItem("user")
             fetch("/ajax/selInfo?user="+user).then(function (e) {
                return e.json()
            }).then((e)=>{
                console.log(e)
                this.date=e
            })
            // 获取到学号，通过学号知道班级，从而查到题组，返回
        },
        methods:{
            kaoshi(id){
                this.id=id
                this.$router.push({path:"/test",query:{id:this.id}})
            }
        }
    }
</script>

<style scoped>
table{
    width: 100%;height:auto;border-collapse: collapse;
}
th{
    color: white;font-size: 16px;font-weight:bold;
}
tr{
   background-color: #666;font-size: 14px;height:50px;width: 100%;
    color:white;border:1px solid #DFDFDF;
}
td{
    width:auto;height:50px;background-color:#F8F8F8;color: #909090;border:1px solid #DFDFDF;padding-left: 10px;text-align: center;color:black;
}
.btn{
    width:70px;height:25px;float: right;margin-right: 15px;border-radius: 5px;
    border:1px solid #7C7C7C;background-color: white;outline: none;

}
a,span{
  color: #909090;text-decoration:none;cursor: pointer;
}
.right1{
    width: 800px;height: auto;margin-left:135px;padding: 0;margin-top: 20px;
}

</style>