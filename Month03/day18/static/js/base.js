// 验证用户名不许为空，必须 4-16位之间
function checkUser(){
    var userLength = $("#user").val().length;
    if(userLength != 0){
        if(userLength < 4 || userLength > 16){
            alert("用户名长度位4-16个字符!");
            return false;
        }

    }else{
        alert("请输入用户名!");
        return false;
    }
    return true;
}

// 验证密码 密码不能为空 密码长度  
function checkPassLength(){
    var pwdLength = $("#pwd1").val().length
    if(pwdLength != 0){
        if(pwdLength < 4 || pwdLength > 16){
            alert("密码长度位4-16个字符!");
            return false;
        }

    }else{
        alert("请输入密码!");
        return false;
    }
    return true;
}

// 两个密码是否一致
function checkPassSame(){
    var pwd1 = $("#pwd1").val();
    var pwd2 = $("#pwd2").val();
    if(pwd1 == pwd2){
        return true;
    }else{
        alert("两次输入的密码不一致!");
        return false;
    }
}

// 清空输入框内容
function tectClear(){
    $("#user").val("");
    $("#pwd1").val("");
    $("#pwd2").val("");
}

// 最终验证函数
function checkFormInput(){
    if(checkUser() && checkPassLength() && checkPassSame()){
        return true;
    }else{
        tectClear(); 
        return false;
    }
}

// 参数是对应的输入input控件id值
function eyes(id){
    var typeVal = $("#"+id).prop("type");
    if(typeVal == 'password'){
        // 改成明文显示
        $("#"+id).prop("type",'text');
        $("#"+id+'-eye').prop("src",'image/eye_close.jpg');
    }else{
        // 改成密文显示
        $("#"+id).prop("type",'password');
        $("#"+id+'-eye').prop("src",'image/eye_open.jpg');
    }

}