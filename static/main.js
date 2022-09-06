function testing(){
   alert('!')
}


 $(document).ready(function () {
    loadHomePage()
 });

function loadHomePage(){
   $.ajax({
      type:'GET',
      url:'/home',
      data:{},
      success: function (response){
         let data = response.msg
         for(let i = 0 ; i < data.length ; i++){
            let imageSrc = data[i].image
            let eventId = data[i].id
            let eventSinger = data[i].singer
            let eventLocation = data[i].location
            let html = `<div class = ${eventId}>
                            <img src = "${imageSrc}">
                            <p>${eventSinger}</p>
                            <p>${eventLocation}</p>
                        </div>`
         $('.wrapper').append(html)
         }
      }
   })
}
