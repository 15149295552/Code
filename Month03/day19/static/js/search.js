function checkWord(){
    var wordLength = $("#word").val().length;
    if(wordLength == 0){
       return false
    }
    return true;
}