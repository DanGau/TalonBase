// Handling for the google homepage

siteMatchers.push({
    matcher: 'bing.com',
    handler: bingHandler
});

function bingHandler(command) {
    switch (command)
    {
    case 'CustomButton1':
        return bingSearch;
        break;
    default:
        console.log(`Unknown messenger command ${command}`);
        return () => {};
        break;
    }
}

function bingSearch() {
    fetch('http://127.0.0.1:5000/')
        .then(r => r.json())
        .then(responseString => {
            responseJSON = JSON.parse(responseString)
            
            // Protected against undefined by using an empty object if one of the
            // keys is missing.
            var textToSearch = ((responseJSON || {}).bing || {}).searchText;

            if (textToSearch && textToSearch !== '') {
                // Insert the text
                document.querySelector('[aria-label^=\'Enter your search term\']').value = textToSearch;
                // Click search
                document.querySelector('[aria-label^=\'Search the web\']').click();
            }
        });
}

