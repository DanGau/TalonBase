// This is the main chunk of logic for the Talon Keyboard Extension.
// The extension enables executing custom javascript injected into a matching web page
// via keyboard shortcuts. The intended use is to write a talon file that is active on
// a web page that will invoke the common keyboard shortcuts. When the extension is
// invoked it will find the correct javascript snippet for the web page and key combination.
//
// To add support for a new web page:
// 1. Create a new <page_name>.js in .\WebPages
// 2. Add an entry to the siteMatchers array with two fields: matcher and handler
//    matcher (string): this is the URL prefix indicating when this matcher should be active.
//      The matcher string should be as scoped as possible for the target use case. Matcher
//      strings can be prefixes of one another; for a given site the longest will be used.
//    handler (function): The handler should be a function that takes a string command parameter
//      and returns void functions to be injected into the site. The handler's responsibility is to
//      select the appropriate action function (the functions that do things on the target site)
//      for the given command and return in. The list of potential command values is in the
//      commands node in the manifest.json file.
// 3. Implement the action functions the handler may return. The action functions are
//      injected into the target page and execute within that context. Common implementation
//      may include finding an element by its ID and clicking it.
// 4. Add a call to TryImportScript for the new <page_name>.js file below.
// 5. That's all for the extension, now extend talon to hit the key definitions on 
//      the appropriate web page. See <root>\apps\chrome\TalonKeyBoardExtension\ for examples.

// Site matchers is an array of objects with matcher and handler fields that is used to
// determine which handler should be invoked given the currently focused tab.
//
// {
//      // The matcher string should always end in with a '/' and not contain http(s)
//      // or www. prefixes. When the current url is prefixed by the matcher string
//      // this handler will be active.
//      matcher: 'nytimes.com/games/wordle/',
//
//      // The handler is a function that takes a command string and returns an action method
//      // to be invoked when that command string is given to the extension. The action method
//      // returned will be injected into the target page when activated.
//      handler: (command) => { return (void) => {}}  
// }
const siteMatchers = [];

function TryImportScript(path) {
    try {
        importScripts(path);
    } catch (e) {
        console.error(e);
    }
}

TryImportScript('WebPages/whereby.js');
TryImportScript('WebPages/wordle.js');
TryImportScript('WebPages/messenger.js');
TryImportScript('SyncPages/azureDevOps.js');

// Add a listener for the commands listed in the manifest
chrome.commands.onCommand.addListener(handleCommands);

// This is the core logic of the extension. Given a command entered by the user
// via the keyboard, the command string is routed to an appropriate handler
// by finding a suitable match for the currently active window. Once a function
// to perform an action is returned it's injected into the active tab to execute.
async function handleCommands(command) {
    // Find the currently active tab
    let tabs = await chrome.tabs.query({active: true, lastFocusedWindow: true});

    // Get the handler associated to the site longest matcher that matches the given URL
    let commandHandler = findClosestMatchingSite(tabs[0].url);

    // Invoke the handler to get the function associated to the given command
    let functionToInject = commandHandler(command);

    // Inject the function returned by the commandHandler into the active tab
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        func: functionToInject
    });
}

// Iterates through the siteMatchers list and finds the longest matcher
// that is a prefix of the given urlStr. The returned handler will be
// from the best suited matcher or the generic handler if no matches are found.
function findClosestMatchingSite(urlStr) {
    let url = formatUrlForPrefixMatch(urlStr);

    let longestMatchIndex = -1;
    let longestPathLength = 0;

    for (let i = 0; i < siteMatchers.length; i++) {
        if (url.startsWith(siteMatchers[i].matcher)) {
            let matcherLength = siteMatchers[i].matcher.length;
            if (matcherLength > longestPathLength) {
                longestPathLength = matcherLength;
                longestMatchIndex = i;
            }
        }
    }

    return (longestMatchIndex === -1) ?
        getGenericCommandHandler() :
        siteMatchers[longestMatchIndex].handler;
}

// Formats a URL string for the matches.
// This invokes stripping the http(s) prefix and the www.
// and ensuring it's terminated with a '/'.
function formatUrlForPrefixMatch(urlStr) {
    let formattedUrlStr = urlStr;

    // Strip http[s]://
    if (formattedUrlStr.startsWith('http://')) {
        formattedUrlStr = formattedUrlStr.substr(7);
    } else if (formattedUrlStr.startsWith('https://')) {
        formattedUrlStr = formattedUrlStr.substr(8);
    }

    // Strip www.
    if (formattedUrlStr.startsWith('www.')) {
        formattedUrlStr = formattedUrlStr.substr(4);
    }

    // Ensure the URL ends with '/' to avoid partial matches
    if (!formattedUrlStr.endsWith('/')) {
        formattedUrlStr += '/';
    }

    return formattedUrlStr;
}

// Generic handler implementation when no entry in the siteMatchers matches
// the current URL. This function returns an anonymous function that takes
// a command and returns an anonymous void(void) function.
//
// Since this is easier with types, this would be...
// std::function<std::function<void(void)>(std::string command)> getGenericCommandHandler(void)  
function getGenericCommandHandler() {
    return (command) => {
        console.log(`Generic handler invoked for command ${command}`);
        return () => {
            console.log(`Generic handler invoked`);
        };
    };
}
