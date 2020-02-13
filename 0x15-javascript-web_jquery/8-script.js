$.get('https://swapi.co/api/films/?format=json', function (data) {
    for (const film of data.results) {
	$('UL#list_movies').append(`<li>${film.title}</li>`);
    }
});
