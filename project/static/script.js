$(document).ready(function () {
    $('#genPass').click(function () {
        $('span.far').css('display', 'block');
        $('span.fas').css('display', 'none')
        $.getJSON('/get_pass', function (dat) {
            $('#show').text(dat);

        });
    });
    $('#genToken').click(function () {
        $('span.far').css('display', 'block');
        $('span.fas').css('display', 'none')
        $.getJSON('/get_token', function (dat) {
            $('#show').text(dat);

        });
    });
    $('#genWords').click(function () {
        $('span.far').css('display', 'block');
        $('span.fas').css('display', 'none')
        $.getJSON('/get_words', function (dat) {
            $('#show').text(dat);

        });
    });
    // $("#copy").click(function () {
    //     $("#show").select();
    //     alert("Success");
    //     document.execCommand('copy');
    //     console.log(
    //         'Great!!',
    //         'Content copied to clipboard',
    //         'success'
    //     )
    // });
});