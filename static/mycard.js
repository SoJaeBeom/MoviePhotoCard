$(document).ready(function (){
    posting()
})

function posting() {
    let title = $('.mycard_title').val()
    let date = $('.mycard_date').val()
    let image = $('#url').val()
    let star = $('#star').val()
    let comment = $('#comment').val()

    $.ajax({
        type: 'GET',
        url: '/my-card',
        data: {url_give: url, star_give: star, comment_give: comment},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
    console.log('hi')
}