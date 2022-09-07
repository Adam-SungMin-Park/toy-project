function testing() {
    alert('!')
}


$(document).ready(function () {
    loadHomePage()
});

function detailPage(key){
   console.log(key)
   location.href='/detail'
}

function loadHomePage() {
    $.ajax({
       type: 'GET',
       url: '/home',
       data: {},
       success: function (response) {
          let data = response.msg
          for (let i = 0; i < data.length; i++) {
             let detailNumber = data[i].image.slice(66, 74)
             let imageSrc = data[i].image
             let eventId = data[i].id
             let eventSinger = data[i].singer
             let eventLocation = data[i].location
             let html = `
                        <div class="col">
                          <div class="card" id = "${detailNumber}">
                            <img src="${imageSrc}" class="card-img-top" alt="...">
                            <a>
                               <div class="card-body">
                                 <h5 class="card-title">${eventSinger}</h5>
                                 <p class="card-text">${eventLocation}</p>
                               </div>
                           </a>
                          </div>
                        </div>
                       `
             $('.row').append(html)
             const entry = document.getElementsByClassName('card')

             for(let j = 0 ; j < entry.length; j++){
                entry[j].addEventListener('click',(imageSrc)=>{
                   let eventKey = entry[j].id
                   detailPage(eventKey)
                })
             }



          }


       }
    })

}
