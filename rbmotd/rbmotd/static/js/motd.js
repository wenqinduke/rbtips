/**
 * Remove an element from tipsList and trim each item.
 */
function remove_list_elements (tipsList, element){
    var processedList = tipsList.filter(function(tip){
        if (tip.trim() !== element){
            return true;
        }
    });

    processedList.forEach(function(tip){
      tip = tip.trim();
    });
    return processedList;
}

/**
 * Get an array of tips from tip string.
 */
function getTipsList(tips){
    return tips.replace('\r\n', '\n').split('\n');
}

/**
 * Close the banner and set the cookie.
 */
function closeBanner(motdClose, cookie, cookieValue, motd){
    motdClose.click(function() {
        $.cookie(cookie, cookieValue, {
            path: SITE_ROOT
        });
        motd.remove();
        return false;
    });
}