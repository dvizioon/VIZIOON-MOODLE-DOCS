# core/utility - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_utility.html

# core/utility

 

 

 

**Description:
 :** 

- 

Javascript handling for HTML attributes. This module gets autoloaded on page load.

With the appropriate HTML attributes, various functionalities defined in this module can be used such as a displaying
an alert or a confirmation modal, etc.

 

**Source:
 :** 

- 
 [lib/amd/src/utility.js](lib_amd_src_utility.js.md), [line 16](lib_amd_src_utility.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript handling for HTML attributes. This module gets autoloaded on page load.

With the appropriate HTML attributes, various functionalities defined in this module can be used such as a displaying
an alert or a confirmation modal, etc.

 

### Example

 

Calling the confirmation modal to delete a block

 

```js
// The following is an example of how to use this module via an indirect PHP call with a button.

$controls[] = new action_menu_link_secondary(
    $deleteactionurl,
    new pix_icon('t/delete', $str, 'moodle', array('class' => 'iconsmall', 'title' => '')),
    $str,
    [
        'class' => 'editing_delete',
        'data-modal' => 'confirmation', // Needed so this module will pick it up in the click handler.
        'data-modal-title-str' => json_encode(['deletecheck_modal', 'block']),
        'data-modal-content-str' => json_encode(['deleteblockcheck', 'block', $blocktitle]),
        'data-modal-yes-button-str' => json_encode(['delete', 'core']),
        'data-modal-toast' => 'true', // Can be set to inform the user that their action was a success.
        'data-modal-toast-confirmation-str' => json_encode(['deleteblockinprogress', 'block', $blocktitle]),
        'data-modal-destination' => $deleteconfirmationurl->out(false), // Where do you want to direct the user?
    ]
);
```
