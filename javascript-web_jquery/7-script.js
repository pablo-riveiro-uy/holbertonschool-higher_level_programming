async function logCharacter() {
    const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    const character = await response.json();
    console.log(character);

    $('#character').append(character.name)
}


logCharacter()

