# core/sortable_list - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/core_sortable_list.html

# core/sortable_list

 

## 

 core/sortable_list

 

 

 

 

#### new core/sortable_list()

 

**Description:
 :** 

- 

A javascript module to handle list items drag and drop

Example of usage:

Create a list (for example `<ul>` or `<tbody>`) where each draggable element has a drag handle.
The best practice is to use the template core/drag_handle:
$OUTPUT->render_from_template('core/drag_handle', ['movetitle' => get_string('movecontent', 'moodle', ELEMENTNAME)]);

Attach this JS module to this list:

Space between define and ( critical in comment but not allowed in code in order to function
correctly with Moodle's requirejs.php

For the full list of possible parameters see var defaultParameters below.

The following jQuery events are fired:

  - SortableList.EVENTS.DRAGSTART : when user started dragging a list element

  - SortableList.EVENTS.DRAG : when user dragged a list element to a new position

  - SortableList.EVENTS.DROP : when user dropped a list element

  - SortableList.EVENTS.DROPEND : when user finished dragging - either fired right after dropping or
if "Esc" was pressed during dragging

 

**Source:
 :** 

- 
 [lib/amd/src/sortable_list.js](lib_amd_src_sortable_list.js.md), [line 16](lib_amd_src_sortable_list.js.md)

 

**Copyright:
 :** 

- 2018 Marina Glancy

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

##### Example

 

```js
define (['jquery', 'core/sortable_list'], function($, SortableList) {
    var list = new SortableList('ul.my-awesome-list'); // source list (usually <ul> or <tbody>) - selector or element

    // Listen to the events when element is dragged.
    $('ul.my-awesome-list > *').on(SortableList.EVENTS.DROP, function(evt, info) {
        console.log(info);
    });

    // Advanced usage. Overwrite methods getElementName, getDestinationName, moveDialogueTitle, for example:
    list.getElementName = function(element) {
        return $.Deferred().resolve(element.attr('data-name'));
    }
});
```
