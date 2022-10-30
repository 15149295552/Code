function checkFormInput(){
    if(checkUser() && checkPassLength()){
        return true;
    }else{
        tectClear(); 
        return false;
    }
}