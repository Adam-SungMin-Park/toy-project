$(document).ready(function () {
    loadHomePage()
});



function detailPage(num){

    console.log(num)
    $.ajax({
        type:"GET",
        url:'/home/detail',
        contentType: "application/json",
        data:JSON.stringify({data: num}),
        dataType: "json",
        success: function(res){
            console.log(res['msg'])
        }
    })
}



function loadHomePage() {
    $.ajax({
        type: 'GET',
        url: '/home/data',
        data: {},
        success: function (response) {
            let data = response.msg
            console.log(response)
            for (let i = 0; i < data.length; i++) {
                let detailNumber = data[i].image.slice(66, 74)
                let imageSrc = data[i].image
                let eventId = data[i].id
                let eventSinger = data[i].singer
                let eventLocation = data[i].location
                let html = `
                        <div class="col">
                          <div onclick = detailPage(${eventId}) class="card" id = "${detailNumber}">
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


            }


        }
    })

}
