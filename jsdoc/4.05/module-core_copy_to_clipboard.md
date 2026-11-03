# core/copy_to_clipboard - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_copy_to_clipboard.html

# core/copy_to_clipboard

 

 

 

**Description:
 :** 

- 

A JavaScript module that enhances a button and text container to support copy-to-clipboard functionality.

This module needs to be loaded by pages/templates/modules that require this functionality.

To enable copy-to-clipboard functionality, we need a trigger element (usually a button) and a copy target element
(e.g. a div, span, text input, or text area).

In the trigger element, we need to declare the `data-action="copytoclipboard"` attribute and set the
`data-clipboard-target` attribute which is the CSS selector that points to the target element that contains the text
to be copied.

When the text is successfully copied to the clipboard, a toast message that indicates that the copy operation was a success
will be shown. This success message can be customised by setting the `data-clipboard-success-message` attribute in the
trigger element.

 

**Source:
 :** 

- 
 [lib/amd/src/copy_to_clipboard.js](lib_amd_src_copy_to_clipboard.js.md), [line 16](lib_amd_src_copy_to_clipboard.js.md)

 

**Copyright:
 :** 

- 2021 Jun Pataleta

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A JavaScript module that enhances a button and text container to support copy-to-clipboard functionality.

This module needs to be loaded by pages/templates/modules that require this functionality.

To enable copy-to-clipboard functionality, we need a trigger element (usually a button) and a copy target element
(e.g. a div, span, text input, or text area).

In the trigger element, we need to declare the `data-action="copytoclipboard"` attribute and set the
`data-clipboard-target` attribute which is the CSS selector that points to the target element that contains the text
to be copied.

When the text is successfully copied to the clipboard, a toast message that indicates that the copy operation was a success
will be shown. This success message can be customised by setting the `data-clipboard-success-message` attribute in the
trigger element.

 

### Example

 

Markup for the trigger and target elements

 

```js
<input type="text" id="textinputtocopy" class="form-control" value="Copy me!" readonly />
<button id="copybutton" data-action="copytoclipboard" data-clipboard-target="#textinputtocopy"
        data-clipboard-success-message="Success!" class="btn btn-secondary">
    Copy to clipboard
</button>
```
