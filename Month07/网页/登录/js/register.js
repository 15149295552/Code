function checkUserName() {    //验证用户名
    var fname = document.myform.username.value;
    var reg = /^[0-9a-zA-Z]/;
    if (fname.length != 0) {
        for (i = 0; i < fname.length; i++) {
            if (!reg.test(fname)) {
                alert("只能输入字母或数字");
                return false;
            }
        }
        if (fname.length < 4 || fname.length > 16) {
            alert("只能输入4-16个字符");
            return false;
        }
    }
    else {
        alert("请输入用户名");
        document.myform.username.focus();
        return false;
    }
    return true;
}

function passCheck() { //验证密码
    var userpass = document.myform.password.value;
    if (userpass == "") {
        alert("未输入密码 \n" + "请输入密码");
        document.myform.password.focus();
        return false;
    }
    if (userpass.length < 6 || userpass.length > 12) {
        alert("密码必须在 6-12 个字符。\n");
        return false;
    }
    return true;
}

function passCheck2() {
    var p1 = document.myform.password.value;
    var p2 = document.myform.password2.value;
    if (p1 != p2) {
        alert("确认密码与密码输入不一致");
        return false;
    } else {
        return true;
    }
}

function clearText() {
    document.forms["myform"]["username"].value=""
    document.forms["myform"]["password"].value="";
    document.forms["myform"]["password2"].value="";
}

// 检测函数
function validateform() {
    if (checkUserName() && passCheck() && passCheck2())
        return true;
    else{
        clearText();
        return false;
    }
}


//显示隐藏对应的密码方法:
function show_hide_pwd(id)
{
    let type = $("#"+id).attr('type')
    if (type === "password") {
        $("#"+id+"eye").attr('src', "img/eye_close.jpg"); 
        $("#"+id).attr("type", "text");
    } else {
        $("#"+id+"eye").attr('src', "img/eye_open.jpg"); 
        $("#"+id).attr("type", "password");
    }
}