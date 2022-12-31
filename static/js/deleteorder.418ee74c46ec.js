function getCsrfFromPage() {
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    return csrftoken;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCsrfFromPage());
        }
    }
});

function deleteOrder(obj) {
    var id = obj.id.split('delete_')[1];
    $.ajax({
        method: "POST",
        url: `/order/${id}/delete`,
    });
    var card = $(obj).parent().parent();
    card.remove();
}

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
