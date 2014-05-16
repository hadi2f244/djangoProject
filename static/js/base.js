/*
function logoF()
{
	var logo=document.getElementById("logo");
	logo.
}
*/
for( var i =0 ; i<10 ;i++)
{
setInterval(function()
        {var x = window.innerWidth;
        var c = document.getElementById('logo');
        c.style.left = (x-325)/2;
        }, 2000);
       
}


