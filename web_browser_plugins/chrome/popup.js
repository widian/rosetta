chrome.extension.onMessage.addListener(function(request, sender) {
    if (request.action == "onTextExtracted") {
    var texts = [];
    for (var i = 0; i != request.source.length; i++ ) {
        texts.push(i + ':' + request.source[i].tag + ':' + request.source[i].text);
    }
    texts = texts.join('\n---------------\n');
    message.innerText = texts;
    }
});

function onWindowLoad() {
    chrome.tabs.executeScript(null, {
        file: "html_text_extractor.js"
    }, function() {
        if (chrome.extension.lastError) {
            var message = document.querySelector('#message');
            message.innerText = 'There was an error injecting script : \n' +
        chrome.extension.lastError.message;
        }
    });

    $('button#debug-button').on('click', function(e) {
//      페이지로부터 가져온 문장을 보여주는 부분을 토글함. Debug용 버튼
        $('div#message').toggle();
    });
    $('button#translate').on('click', function(e) {
//      문장을 번역할 수 있는 페이지를 오픈함.
    
    });
    $('button#show-translation').on('click', function(e) {
//      번역된 문장을 불러와서 볼 수 있게함.
        
    });


}

window.onload = onWindowLoad;


