// Button handling for messenger

siteMatchers.push({
    matcher: 'messenger.com/',
    handler: messengerHandler
});

function messengerHandler(command) {
    switch (command)
    {
    case 'CustomButton1':
        return messengerSendLike;
        break;
    case 'CustomButton2':
        return messengerOpenNextChat;
        break;
    case 'CustomButton3':
        return messengerOpenLastChat;
        break;
    case 'CustomButton4':
        return messengerNewChat;
        break;
    case 'CustomButton5':
        return messengerFirstChat;
        break;
    default:
        console.log(`Unknown messenger command ${command}`);
        return () => {};
        break;
    }
}

// This should focus the message box if that functionality is needed
// document.querySelector('[aria-label^=\'Message\'][contenteditable=true]').focus()

// New chat but the focus is weird:
// document.querySelector('[role=\"link\"').click()

// First chat:
// document.querySelectorAll('[role=\"link\"')[1].click()

// Current open chat index:
// let allChats = document.querySelectorAll('[role=\"link\"]')
// let allChatsArr = Array.from(allChats)
// let currentChatIndex = allChatsArr.findIndex(entry => entry.ariaCurrent === "page")

// Send a like (or whatever emoji fills that role)
function messengerSendLike() {
    document.querySelector('[aria-label^=\'Send a \']').click();
}

// Opens the next chat in the list
function messengerOpenNextChat() {
    // Query for all the elements with the "link" role which are the messenger conversations
    // Convert it to an array so we can find the index of the currently open chat
    var allChatsArray = Array.from(document.querySelectorAll('[role=\"link\"]'));

    // The active chat has "page" while others have "false"
    var chatIndex = allChatsArray.findIndex(entry => entry.ariaCurrent === "page");

    // Open the next chat
    if (chatIndex+1 < allChatsArray.length) {
        allChatsArray[chatIndex+1].click();
    }
}

// Opens the last chat in the list
function messengerOpenLastChat() {
    var allChatsArray = Array.from(document.querySelectorAll('[role=\"link\"]'));

    // The active chat has "page" while others have "false"
    var chatIndex = allChatsArray.findIndex(entry => entry.ariaCurrent === "page");

    // Open the last chat. Don't let it go lower than 1, 0 is the new chat field.
    if (chatIndex > 1) {
        allChatsArray[chatIndex-1].click();
    }
}

// Open the new chat view
function messengerNewChat() {
    document.querySelector('[role=\"link\"]').click();
}

// Open the first chat in the menu
function messengerFirstChat() {
    document.querySelectorAll('[role=\"link\"]')[1].click();
}