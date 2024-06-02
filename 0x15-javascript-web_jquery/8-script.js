// Starwars Movies

$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
    $.each(response.results, function (index, item) {
      $('UL#list_movies').append(`<li>${item.title}</li>`);
    });
  }).fail(function (error) {
    $('UL#list_movies').text('Error: ', +error);
  });
});
