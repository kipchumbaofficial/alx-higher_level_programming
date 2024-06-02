$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (response) {
    const name = response.name;
    $('DIV#character').text(name);
  }).fail(function (error) {
    $('DIV#character').text('Error: ' + error.statusText);
  });
});
