$(document).ready(function (){
    posting()
})

function posting() {
    $.ajax({
        type: 'GET',
        url: '/mycard',
        data: {},
        success: function (response) {
            let rows = response['cards']
            for (let i = 0; i < rows.length; i++){
                let movie_img = rows[i]['movie_img']
                let movie_name = rows[i]['movie_name']
                let date = rows[i]['date']
                let star = rows[i]['star']
                let comment = rows[i]['comment']

                let star_img = '★'.repeat(star)

                let temp_html = `<div class="mycard" style="background-image:url(${movie_img})">
                                    <div class="mycard_opacity"></div>
                                    <div class="mycard_top">
                                        <div class="mycard_title">${movie_name}</div>
                                        <div class="mycard_date">${date}</div>
                                    </div>
                                    <div class="mycard_bottom">
                                        <div class="mycard_star">${star_img}</div>
                                        <div class="mycard_comment">${comment}</div>
                                    </div>
                                </div>
                `
                $('#mycard_box').append(temp_html)
            }

        }
    });
}

// <div className="mycard"
//      style="background-image:url('https://file.mk.co.kr/meet/yonhap/2021/12/08/image_readtop_2021_1123769_0_152311.jpg')">
//     <div className="mycard_opacity"></div>
//     <div className="mycard_top">
//         <div className="mycard_title">dd</div>
//         <div className="mycard_date">dd</div>
//     </div>
//     <div className="mycard_bottom">
//         <div className="mycard_star">★★★★</div>
//         <div className="mycard_comment">dd</div>
//     </div>
// </div>