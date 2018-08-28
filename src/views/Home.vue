<template>
 <div id="app" >
   <div class="index_top">
      <img src="../assets/images/longintos.png" alt="" class="logntop">
      <img src="../assets/images/loginconter.png" alt="" class="lognconter">
   </div>
   <div class="index_conter">
    <span class="index_conter_top"></span>
       <!--<span class="err">{{message}}</span>-->
     <div class="index_conter_input">
       <div class="boeder">
          <img src="../assets/images/people.png" alt="" class="imgs">
        <input type="text" placeholder="输入您得学号/工号" class="stu_num" size="25" v-model="uid" >
         <div>
          <div class="numcuowu"  v-bind:style="userguifan">请输入正确得账号</div>
          <div class="numcuowu"  v-bind:style="userxianshi">用户名称不符合规范</div>
           <div class="numcuowu"  v-bind:style="userno">用户名或者密码不符</div>
         </div>
       </div>
       <div class="border">
          <img src="../assets/images/suo.png" alt="" class="imgs">
         <input type="password" placeholder="输入您得密码" size="25" class="stu_nums" v-model="upass" >
         <div >
          <div class="numcuowus" v-bind:style="passguifan">您可以找回密码</div>
          <div class="numcuowus" v-bind:style="passxianshi">密码最少是6位</div>
           </div>
       </div>
       <div class="alink">
         <router-link to="/amend" class="passs" >更改密码</router-link>
         <router-link to="/register" class="passinst">立即注册</router-link>
       </div>
        <button type="primary" class="primary" @click="submit()">登陆</button>
     </div>
   </div>
   <div class="index_bottom">
     <div class="bottom_xian">
     </div>
     <span>使用第三方登陆</span>
     <div class="bottom_xians">

     </div>
     </div>
   <div class="index_images">
     <img src="../assets/images/weixing.png" alt="" class="weixing">
     <img src="../assets/images/qq.png" alt="" class="qq">
   </div>
</div>
</template>
<script>
export default{
  data(){
    return{
    uid:"",
    upass:"",
    message:"",
    userguifan:{display:"none"},
    userxianshi:{display:"none"},
    passguifan:{display:"none"},
    passxianshi:{display:"none"},
    userno:{display:'none'},
    }
  },
 methods: {
  submit(){
      fetch("/ajax/userindex/",{
              method: "post",
              headers: new Headers({
              'Content-Type': 'application/x-www-form-urlencoded'
              }),
              body:new URLSearchParams([["uid", this.uid],["upass",this.upass]]).toString()
          }).then((res) => {
              // console.log(res.text())
              return res.text()
          }).then((res)=>{
             if (res=="ok"){
                 // sessionStorage["upass"]=res.upass;
                 // sessionStorage["uid"]=res.uid;
               this.$router.push("/amend")
                 // alert('添加成功')
               console.log(res)
              }else{
               this.userno.display='block'
                 this.uname=""
                  this.pass=""
                  // this.message="用户名或密码出错"
               this.$router.push("/")
             }
          })
          //  fetch("/ajax/index/?uid="+this.uid+"&upass="+this.upass).then((res) => {
          //     return res.text()
          // }).then((res)=>{
          //    if (res=="ok"){
          //        sessionStorage["upass"]=this.upass;
          //        sessionStorage["uid"]=this.uid;
          //       // this.$router.push("/")
          //      this.$router.push("/password")
          //     }else{
          //         this.uname=""
          //         this.pass=""
          //         this.message="用户名或密码出错"
          //         this.userno.display='block'
          //         this.$router.push("/")
          //    }
          // })
  },
 },
  watch:{
    user:function(){
      this.userxianshi.display="block";
      var reg=/^[a-zA-Z]+\w$/;
      var result=reg.test(this.user)
      if(result==true){
        this.userxianshi.display="none";
      }else if(this.user==""){
        this.userxianshi.display="none";
        this.userno.display='none';
      }
      else{
        this.userxianshi.display="block";
      }
    },
    passs:function(){
    this.passxianshi.display="block";
    if (this.passs.length>5){
      this.passxianshi.display="none";
    }else if(this.passs==""){
      this.passxianshi.display="none";
    }
    else{
      this.passxianshi.display="block";
      }
    }

  }
}
</script>

<style scoped>
    #app{
        width:100%;
        height: 100%;
        position: absolute;left:0;top:0;
    }
.numcuowu{
    position: absolute;
    top: 1.1rem;
    left: 2.3rem;
    width: 2.2rem;
    height: 0.4rem;
    background-color: #FF6067;
    border-radius: 0px 20px 20px 20px ;
    display: flex;
    font-size: 11px;
    text-align: center;
    line-height: 0.4rem;
}
.numcuowus{
    position: absolute;
    top: 2.1rem;
    left: 2.3rem;
    width: 2.2rem;
    height: 0.4rem;
    background-color: #FF6067;
    border-radius: 0px 20px 20px 20px ;
    display: flex;
    font-size: 11px;
}
.imgs{
  width: 0.4rem;
  height: 0.5rem;
  display: block;
  margin-top: 0.1rem;
  padding-left: 0.4rem;

}
.index_top{
  display: flex;
}

.logntop{
  position: absolute;
  display: block;
  top: 2rem;
  width:1.70rem;
  height:1.6rem;
  margin-left:2.8rem ;

}
  .lognconter{
    position: absolute;
    display: block;
    top: 4rem;
    width:3.5rem;
    height:1rem;
    margin-left:1.9rem ;
  }
  .index_conter{
    width: 5.1rem;
    height: 3.8rem;
    position: absolute;
    display: flex;
    flex-direction:column;
    top: 5.7rem;
    left: 1.2rem;
    /*background-color: #FAFAFA;*/
  }
  .index_conter_top{
    width: 4.4rem;
    height: 0.2rem;
    background-color: #80BAF6;
    margin-left: 0.35rem;
    border-radius:15px 15px 0px 0px;
  }
  .index_conter_input{
    width: 5.1rem;
    height: 3.3rem;
    background-color:  #FAFAFA;
    border-radius:10px 10px 10px 10px;
    /*display: flex;*/
  }
  .stu_num{
    display: block;
    width: 3.8rem;
    height: 0.5rem;
    margin-left: 0.2rem;
    background-color: #FAFAFA;

    border: none;
    outline:none;
    font-size: 11px;
    border-bottom: 1px solid #ccc;
  }
  .stu_nums{
    font-size: 11px;
    display: block;
    width: 3.8rem;
    height: 0.5rem;
    margin-left: 0.2rem;
    background-color: #FAFAFA;
    border: none;
    outline:none;
    border-bottom: 1px solid #ccc;
  }
  .boeder{
    margin-top: 0.5rem;
    height: 0.7rem;
    display: flex;

  }
  .border{
     margin-top: 0.2rem;
    height: 0.7rem;
    display: flex;

  }
  .primary{
    display: block;
    width: 2.5rem;
    height: 0.7rem;
    line-height: 0.7rem;
    margin-top: 0.4rem;
    margin-left: 1.2rem;
    font-size: 11px;
    border-radius: 25px 25px 25px 25px ;
    background-color: #26A2FF;
      color: white;
      border: none;
  }
  .alink{
    font-size: 11px;
    font-weight: 200;
    margin-top: 0.1rem;


  }
  .passs{
    float: left;
    padding-left: 0.7rem;
     text-decoration: none;
    color: black;
  }
  .passinst{
    padding-left: 0.5rem;
     text-decoration: none;
    color: black;
  }
  .index_bottom{
    width: 5.1rem ;
    height: 1.3rem;
    position: absolute;
    top: 10rem;
    left: 1.2rem;
    display: flex;
    font-size: 11px;
    /*text-align: center;*/
    line-height: 1.3rem;
  }
  .index_bottom span{
    text-align: center;
    /*margin-left: 0.6rem;*/
  }
  .bottom_xian{
    width: 1rem;
    height: 0.65rem;
    border-bottom: 1px solid #CCCCCC;
    margin-left: 0.6rem;


  }
  .bottom_xians{
    width: 1rem;
    height: 0.65rem;
    border-bottom: 1px solid #CCCCCC;
    /*margin-left: 0.6rem;*/

  }
  .index_images{
    position:absolute;
    width: 5.1rem ;
    height: 1.3rem;
     top: 11rem;
    left: 1.2rem;
    display: flex;
  }
  .weixing{
    width: 0.75rem;
    height: 0.75rem;
    margin-left: 1.22rem;
  }
  .qq{
    width: 0.75rem;
    height: 0.75rem;
    padding-left: 0.8rem;
  }
      .err{
      width:100px;
      font-size: 16px;
  }
</style>