function clearText() {
    // 可以使用name，或者id属性获取具体的元素
    document.forms["myform"].username.value=""
    document.forms["myform"].password.value="";
}

function validateform() {
    if (checkUserName() && passCheck())
        return true;
    else{
        clearText();
        return false; 
    }   
            
}

