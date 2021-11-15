$(document).ready(function() {
    $('.api__notifications__delete').on('click', function() {
        var $this = $(this),
            notification_id = $this.data('id'),
            csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

        $.ajax({
            url: `/api/notifications/${notification_id}/`,
            type: 'DELETE',
            headers: {
                "X-CSRFToken": csrf_token
            },
            success: function () {
                $this.parent('li').remove();
                console.log('successfully removed');
            },
            error: function (data) {
                alert(`Error: ${data.status}`);
            }
        });
    });
});
