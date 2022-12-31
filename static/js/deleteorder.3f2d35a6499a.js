function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

function deleteOrder(obj) {
    var id = obj.id.split('delete_')[1];
    const csrfToken = getCookie('CSRF-TOKEN');
    $.ajax({
        method: "DELETE",
        url: `/order/${id}/delete`,
        data: {
            "X-CSRFToken":csrfToken
        }
    });
    var card = $(obj).parent().parent();
    card.remove();
}

