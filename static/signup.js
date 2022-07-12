function save_user_info() {
    let user_id = $('.user_id').val()
    let user_pw = $('.user_pw').val()
    let user_name = $('.user_name').val()

    console.log(user_id, user_pw, user_name)

    $.ajax({
        type: "POST",
        url: "/MoviePhotoCard_local",
        data: {
            user_id_give: user_id,
            user_pw_give: user_pw,
            user_name_give: user_name
        }
        // success: function (response) {
        //     if (response['result'] == 'success') {
        //         alert('회원가입이 완료되었습니다.')
        //         //window.location.href = '/login' 회원가입이 완료되면 로그인창으로 넘겨준다
        //     } else {
        //         //alert(response['msg']) //아니면 메세지 띄우기
        //     }
        // }
    })
}