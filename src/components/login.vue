<template>
        <div class="login_box">
          <div class="login_l_img"><img src="../assets/QQ图片20180810112530.png" /></div>
          <div class="login">
              <div class="login_logo"><a href=""><img src="../assets/aa.png" alt=""></a></div>
              <div class="login_name">
                   <p>学生后台管理系统</p>
              </div>
              <form >
                  <input name="username" type="text" v-model="user" value="用户名" onfocus="this.value=''" onblur="if(this.value==''){this.value='用户名'}" >
                  <input name="password" type="password" v-model="pass" value="密码"  onfocus="this.value=''" onblur="if(this.value==''){this.value='密码'}" >
                  <input value="登录" style="width:100%;" type="button" @click="submit">
              </form>
          </div>
        </div>
</template>

<script>
    export default {
        data(){
            return {
                user: "",
                pass: "",
            }
        },
        methods:{
            submit(){
                console.log(this.user,this.pass)
                var parmas="user="+this.user+"&pass="+this.pass
                fetch("/ajax/login?"+parmas).then(function (e) {
                    return e.text()
                }).then((e)=>{
                    if(e=="ok"){
                        sessionStorage.setItem("user",this.user)
                        sessionStorage.setItem("pass",this.pass)
                        this.$router.push("/")

                    }
                })
            }
        }
    }
</script>

<style scoped>
    html,body{
        background:lemonchiffon;
    }
a { color:orange; text-decoration:none; cursor:pointer; }
img{ border:none;}
.bg{background:lemonchiffon;width: 100%;height:100vh;}
.login_box{ width:100%;height:640px; margin:0 auto;  background-size: cover;background:lemonchiffon;padding-top: 150px;}
.login_box .login_l_img{ float:left; width:432px; height:440px; margin-left:160px;margin-top: -30px;}
.login_box .login_l_img img{width:550px; height:500px; }
.login {height:360px; width:400px; padding:50px; background-color: #ffffff;border-radius:6px;box-sizing: border-box; float:right; margin-right:200px; position:relative; margin-top:50px;}
.login_logo{ width:120px; height:120px; border:5px solid orange;border-radius:100px; background:#fff; text-align:center; line-height:110px; position:absolute; top:-60px; right:140px;}
.iconfont{
    font-size:40px
}
.login_name{ width:100%; float:left; text-align:center; margin-top:20px;}
.login_name p{ width:100%; text-align:center; font-size:18px; color:#444; padding:10px 0 20px;}
.login_logo img{ width:60px; height:60px;display: inline-block; vertical-align: middle;}
input[type=text], input[type=file], input[type=password], input[type=email], select { border: 1px solid #DCDEE0; vertical-align: middle; border-radius: 3px; height: 50px; padding: 0px 16px; font-size: 14px; color: #555555; outline:none; width:267px;margin-bottom: 15px;line-height:50px; color:#888;}
input[type=text]:focus, input[type=file]:focus, input[type=password]:focus, input[type=email]:focus, select:focus { border: 1px solid orange; }
input[type=submit], input[type=button] { display: inline-block; vertical-align: middle; padding: 12px 24px; margin: 0px; font-size:16px; line-height: 24px; text-align: center; white-space: nowrap; vertical-align: middle; cursor: pointer; color: #ffffff; background-color: orange; border-radius: 3px; border: none; -webkit-appearance: none; outline:none; width:100%; }
.copyright { font-size:14px; color:#fff; display:block;width:334px; float:left; text-align:center; margin-top:60px;}

#password_text{border: 1px solid #DCDEE0; vertical-align: middle; border-radius: 3px; height: 50px; padding: 0px 16px; font-size: 14px; color: #888; outline:none; width:267px;margin-bottom: 15px;display: block; line-height:50px;}
.two{
    width:150px;height:16px;
    padding-bottom: 1px;
    margin-bottom: 10px;
    font-size: 12px;
}
.two input{
    width:13px;height:13px;
    margin-top: 3px;margin-right: 10px;
    margin-bottom: 0;
    float: left;
}
.two .zi{
    width:80px;height:16px;
    float: left;color:black;
}
</style>