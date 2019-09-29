$(function () {
    var ue = UE.getEditor('container', {
        'serverUrl': '/ueditor/upload/'
    });
    var tag = $("input:checked").val()
    var title1 = $("#theme1".val())
    $("#submitBtn").click(function (event) {
        event.preventDefault();
        alert("您的帖子已成功提交 可点击查看按钮进行查看")
        var content = ue.getContent();

        $.post({
            'url': '/msg/post_msg/',
            'data': {
                'content': content,
                "title1":title1
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
