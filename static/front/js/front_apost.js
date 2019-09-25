$(function () {
    var ue = UE.getEditor('container', {
        'serverUrl': '/ueditor/upload/'
    });
    var title = $("input:checked").val()

    $("#submitBtn").click(function (event) {
        event.preventDefault();

        var content = ue.getContent();
        $.post({
            'url': '/msg/post_msg/',
            'data': {
                'content': content,
                "title":title
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
