function deleteOrder(obj) {
    var id = obj.id.split('delete_')[1];
    $.ajax({
        method: "GET",
        url: `/order/${id}/delete`,
    });
    var card = $(obj).parent().parent();
    card.remove();
}

