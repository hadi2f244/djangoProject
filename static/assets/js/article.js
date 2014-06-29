function my_callback(data){
    var like=document.getElementById("likesTag");
    like.innerHTML=data.likes_num+" poeple liked this article";
    //alert(data.message);
}