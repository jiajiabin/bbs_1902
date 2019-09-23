$(function () {
    var ue = UE.getEditor('container', {
        'serverUrl': '/ueditor/upload/'
    });

    $("#submitBtn").click(function (event) {
        event.preventDefault();
        // var titleInput = $('input[name="title"]');
        // var boardSelect = $('select[name="board_id"]');
        // var title = titleInput.val();
        // var board_id = boardSelect.val();
        var content = ue.getContent();
        // console.log(content)

        // ajax_1902.post({
        //     'url':'/msg/post_msg/',
        //     'data':{
        //         'content':content
        //     },
        //     'success':function (data) {
        //         if(data['code'] == 200){
        //
        //         }else {
        //
        //         }
        //         console.log(content)
        //     }
        // })
        $.post({
            'url': '/msg/post_msg/',
            'data': {
                'content': content
            },
            "success": function (data) {
                if (data['code'] == 200) {
                    window.location = '/'
                } else {
                    var message = data['message'];
                    $("#message-p").html(message);
                    $("#message-p").show();
                }
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        });

    })


})
