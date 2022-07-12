$(document).ready(function () {
    listing();
});

function listing() {
    $.ajax({
        type: 'POST',
        url: '/movie-list',
        data: {},
        success: function (response) {
            let rows = response['movies']
            console.log(rows)
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['movie_name'];
                let img = rows[i]['movie_img'];
                let num = rows[i]['num']
                let temp_html = `
                <div class="col">
                    <div class="card h-100">
                        <img src="${img}" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title">${name}</h5>
                        </div>
                        <div>
                            <button onclick="clickBtn(${num})" class="default_button">만들기</button>
                        </div>
                    </div>
                </div>
                `
                $('#movie_list').append(temp_html)
            }
        }
    });
}

function clickBtn(num) {
    console.log(num)
    window.location.href = "/addcard?id=" + num
}