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
            let html = `
                          <div class="col">
                            <div class="card" id = "${eventId}">
                              <img src="${imageSrc}" class="card-img-top" alt="...">
                              <div class="card-body">
                                <h5 class="card-title">${eventSinger}</h5>
                                <p class="card-text">${eventLocation}</p>
                              </div>
                            </div>
                          </div>
                         `
         $('.row').append(html)
         }
      }
   })
}
