// Button execution logic for wordle

siteMatchers.push({
    matcher: 'nytimes.com/games/wordle/',
    handler: wordleHandler
});

function wordleHandler(command) {
    switch (command)
    {
    case 'CustomButton1':
        return wordleButton1;
        break;
    case 'CustomButton2':
        return wordleButton2;
        break;
    default:
        console.log(`Unknown wordle command ${command}`);
        return () => {};
        break;
    }
}

function wordleButton1() {
    console.log('Wordle button 1');

    // If this breaks they probably moved the shadow root, go hunting in the DOM
    document.body.children[4].shadowRoot.getElementById('help-button').click();
}

function wordleButton2() {
    console.log('Wordle button 2');
}