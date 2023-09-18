async function logCharacter() {
    const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const movies = await response.json();
    console.log(movies.results);
    let films = movies.results;

    films.forEach(film => {
        let new_li = `<li>${film.title}</li>`
        $('#list_movies').append(new_li)
    });
}


logCharacter()
