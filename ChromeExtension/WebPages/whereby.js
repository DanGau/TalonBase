// Button handling for Whereby

siteMatchers.push({
    matcher: 'whereby.com/',
    handler: wherebyHandler
});

function wherebyHandler(command) {
    switch (command)
    {
    case 'CustomButton1':
        return wherebyToggleMute;
        break;
    case 'CustomButton2':
        return wherebyShareScreen;
        break;
    case 'CustomButton3':
        return wherebyToggleChat;
        break;
    case 'CustomButton4':
        return wherebyToggleCamera;
        break;
    default:
        console.log(`Unknown whereby command ${command}`);
        return () => {};
        break;
    }
}

// Toggle the mute button
function wherebyToggleMute() {
    document.getElementsByClassName('BaseButton-mQq4 jstest-mute-button')[0].click();
}

// Open the sharing pane
function wherebyShareScreen() {
    document.getElementsByClassName('BaseButton-mQq4 jstest-share-screen-button')[0].click()

    // This hides the flyout that says stuck open (it'll stay hidden until refresh)
    document.getElementsByClassName(
        'jstest-sharepicker-popover Popover-kaw0 react-tiny-popover-container')[0].hidden = true;

    // This throws up a pop up to pick the screen which I have no clue how to command
}

// Toggle chat
function wherebyToggleChat() {
    document.getElementsByClassName('BaseButton-mQq4 jstest-open-chat-button')[0].click()
}

// Toggle camera
function wherebyToggleCamera() {
    document.getElementsByClassName('jstest-button-icon-wrapper buttonIconWrapper-FUFj')[0].click()
}