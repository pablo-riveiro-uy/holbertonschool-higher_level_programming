async function logCharacter() {
    const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
    const hi = await response.json();
    console.log(history);

    $('#hello').text(hi.hello)

}

logCharacter()


