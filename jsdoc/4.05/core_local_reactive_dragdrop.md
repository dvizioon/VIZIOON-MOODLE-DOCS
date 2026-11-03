# core/local/reactive/dragdrop - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/core_local_reactive_dragdrop.html

# core/local/reactive/dragdrop

 

## 

 core/local/reactive/dragdrop

 

 

 

 

#### new core/local/reactive/dragdrop()

 

**Description:
 :** 

- 

Drag and drop helper component.

This component is used to delegate drag and drop handling.

To delegate the logic to this particular element the component should create a new instance
passing "this" as param. The component will use all the necessary callbacks and add all the
necessary listeners to the component element.

Component attributes used by dragdrop module:

  - element: the draggable or dropzone element.

  - (optional) classes: object with alternative CSS classes

  - (optional) fullregion: page element affeted by the elementy dragging. Use this attribute if
the draggable element affects a bigger region (for example a draggable
title).

  - (optional) autoconfigDraggable: by default, the component will be draggable if it has a
getDraggableData method. If this value is false draggable
property must be defined using setDraggable method.

  - (optional) relativeDrag: by default the drag image is located at point (0,0) relative to the
mouse position to prevent the mouse from covering it. If this attribute
is true the drag image will be located at the click offset.

Methods the parent component should have for making it draggable:

  - 

getDraggableData(): Object|data
Return the data that will be passed to any valid dropzone while it is dragged.
If the component has this method, the dragdrop module will enable the dragging,
this is the only required method for dragging.
If at the dragging moment this method returns a false|null|undefined, the dragging
actions won't be captured.

  - 

(optional) dragStart(Object dropdata, Event event): void

  - 

(optional) dragEnd(Object dropdata, Event event): void
Callbacks dragdrop will call when the element is dragged and getDraggableData
return some data.

Methods the parent component should have for enabling it as a dropzone:

  - 

validateDropData(Object dropdata): boolean
If that method exists, the dragdrop module will automathically configure the element as dropzone.
This method will return true if the dropdata is accepted. In case it returns false, no drag and
drop event will be listened for this specific dragged dropdata.

  - 

(Optional) showDropZone(Object dropdata, Event event): void

  - 

(Optional) hideDropZone(Object dropdata, Event event): void
Methods called when a valid dragged data pass over the element.

  - 

(Optional) drop(Object dropdata, Event event): void
Called when a valid dragged element is dropped over the element.

Note that none of this methods will be called if validateDropData
returns a false value.

This module will also add or remove several CSS classes from both dragged elements and dropzones.
See the "this.classes" in the create method for more details. In case the parent component wants
to use the same classes, it can use the getClasses method. On the other hand, if the parent
component has an alternative "classes" attribute, this will override the default drag and drop
classes.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 16](lib_amd_src_local_reactive_dragdrop.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
