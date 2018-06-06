(function() {
    /*
     * A widget extended from ListEditView, with an extra 'Clear Items' button to clear all entries.
     *
     * This is the Javascript view for `ListEditWidgetWithClearButton`
     */
    Djblets.Forms.ListEditViewWithClearButton = Djblets.Forms.ListEditView.extend({

    initialize: function(options) {
        Djblets.Forms.ListEditView.prototype.initialize.apply(this,[options]);
        this.events['click .list-clear-items'] = '_clearItems';
    },

      /**
       * Remove all items.
       *
       * When there is only a single item in the list, we clear it instead of
       * removing it so there is always at least one ``<input>`` element and
       * value in the list.
       *
       * Args:
       *     e (Event):
       *         The click event that triggered this event handler.
       */
    _clearItems: function(e){
        e.preventDefault();
        e.stopPropagation();

        var existingEntryLength = $('.list-edit-entry input').length;
        for (var i = existingEntryLength - 1; i >= 1; i--) {
          $($('.list-edit-remove-item')[i]).click();
        }
        $($('.list-edit-entry input')[0]).val('').blur();//call blur to force the model to update;
    }
});

})();


$( document ).ready(function(){
    /**
     * Load file context into list, one tip per line.
     *
     * When user selects a file, read the file and populate tips into the list, and remove empty entry.
     * Note that when user selects the same file twice, it does not call the function.
     * User needs to de-select the file, and select again to trigger the function.
     */
    $('#id_tips_file').change(function(){
        if ($('#id_tips_file').val() !== ''){
            readTextFile(this.files[0], function (e) {
                var fileContent = e.target.result;
                var tips = getTipsList(fileContent);
                tips = remove_list_elements(tips, "");
                addItems(tips);
                cleanItems();
            });
        }
    });
});

/**
 * Read text file content and then trigger onLoadCallback.
 *
 * Args:
 *     file (object):
 *         The File object from which to read.
 *     onLoadCallback (function):
 *         The call back function.
 */
function readTextFile(file, onLoadCallback){
    var fReader = new FileReader();

    fReader.onload = onLoadCallback;
    fReader.readAsText(file);
}

/**
 * Add tips to the list.
 *
 * Args:
 *     tips (list):
 *        The tips list going to be added to the list.
 */
function addItems(tips){
    tips.forEach(function(tip){
        $(".list-edit-add-item").click();
        $('.list-edit-entry input').last().val(tip).blur();//call blur to force the model to update
    })
}

/**
 * Removes empty items in the list.
 */
function cleanItems(){
    var listEditRemoveItem = $('.list-edit-remove-item');

    $('.list-edit-entry input').filter(function(index){
        if (!this.value){
            $(listEditRemoveItem[index]).click();
        }
    })
}
