function testing(){
   alert('!')
}


 $(document).ready(function () {
    loadHomePage()
 });

function loadHomePage(){
   $.ajax({
      type:'GET',
      url:'/',
      data:{},
      success: function (response){
         console.log(response)
      }
   })
}
