function pageIsPending(acitve) {
    if (acitve) {
        $('.loader').css('display', "inline-block")
    } else {
        $('.loader').css('display', "none")
    }
}

function btnIsPending(acitve, parent) {
    var btnText = parent.children[0]
    var loader = parent.children[1]
    if (acitve) {
        loader.style.display = 'inline-block'
        btnText.style.display = 'none'
    } else {
        loader.style.display = 'none'
        btnText.style.display = 'inline-block'
    }
}