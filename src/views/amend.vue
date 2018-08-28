
<template>
 <div id="app" >
     <div class="top">
         <router-link class="return" to="/">
             <img src="../assets/images/return.png" alt="" class="config">
         </router-link>
         <span>
             验证密码前
         </span>

     </div>
   <div class="index_top">
      <img src="../assets/images/longintos.png" alt="" class="logntop">
      <img src="../assets/images/loginconter.png" alt="" class="lognconter">
   </div>
   <div class="index_conter">
    <span class="index_conter_top"></span>
     <div class="index_conter_input">
       <div class="boeder">
         <img src="../assets/images/people.png" alt="" class="imgs">
        <input type="text" placeholder="输入您得学号/工号" class="stu_num" size="25" v-model="uid">
       </div>
       <div class="border">
         <img src="../assets/images/suo.png" alt="" class="imgs">
         <input type="text" placeholder="输入您得姓名" size="25" class="stu_nums" v-model="uname">
       </div>
        <button type="primary" class="primary" @click="submit()">确定</button>
     </div>
   </div>

</div>
</template>
<script>
export default{
     data(){
      return {
        uid: "",
        uname: "",
      }
    },
     methods: {
  submit(){
           fetch(" /ajax/uspa/",{
              method: "post",
              headers: new Headers({
              'Content-Type': 'application/x-www-form-urlencoded'
              }),
               // console.log('123')
              body:new URLSearchParams([["uid",this.uid], ["uname",this.uname]]).toString()

          }).then((res) => {
              return res.text()
               // console.log('123')
          }).then((res)=>{
             if (res=="ok"){
                 // console.log('123')
               this.$router.push("/password/"+this.uid)
               console.log(res)
              }else{
               this.$router.push("/amend")
             }
          })

  },

}
}
</script>

<style scoped>
    #app{
        width: 100%;
        height: 100%;
    }
    .config{
        width: 0.5rem;
        height: 0.5rem;
        margin-top: 0.2rem;
    }
        .return{
        font-size: 17px;
        margin-left: 0.2rem;
        text-decoration: none;
    }
    .top span{
        margin: auto;
         font-size: 16px;
        margin-left: 2.15rem;
        font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    }
    .top{
        width: 7.5rem;
        height: 0.9rem;
        background-color: #26A2FF;
        font-size: 20px;
        font-weight: 200;
        line-height: 0.9rem;
        display: flex;
        position: absolute;
        left:0;
        top: 0;

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
    height:3.3rem;
    background-color:  #FAFAFA;
    border-radius:10px 10px 10px 10px;
    /*display: flex;*/
  }
  .stu_num{
    display: block;
    width: 3.8rem;
    height: 0.5rem;
    margin-left: 0.3rem;
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
    margin-left: 0.3rem;
    background-color: #FAFAFA;
    border: none;
    outline:none;
    border-bottom: 1px solid #ccc;
  }
  .boeder{
    display: flex;
    margin-top: 0.5rem;
    height: 0.7rem;

  }
  .border{
    display: flex;
     margin-top: 0.3rem;
    height: 0.7rem;
  }
  .primary{
     display: block;
    width: 2.5rem;
    height: 0.7rem;
    line-height: 0.7rem;
    margin-top: 0.6rem;
    margin-left: 1.2rem;
    font-size: 11px;
    border-radius: 25px 25px 25px 25px ;
    background-color: #26A2FF;
      color: white;
      border: none;
  }
  .alink{
    font-size: 12px;


  }
  .passs{
    float: left;
    padding-left: 0.5rem;
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
    /*background-color: red;*/
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
    /*background-color: red;*/
  }
</style>
