// Say hello

$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    $('DIV#hello').text(response.hello);
  }).fail(function (error) {
    $('DIV#hello').text('Erorr: ' + error.statusText);
  });
});
