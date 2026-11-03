# exports - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module.exports_module.exports.html

# exports

 

## 

 exports

 

 

 

 

#### new exports()

 

**Description:
 :** 

- 

Constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/logger.js](lib_amd_src_local_reactive_logger.js.md), [line 47](lib_amd_src_local_reactive_logger.js.md)

 

 

 

## 

 exports

 

 

 

 

#### new exports(descriptor)

 

**Description:
 :** 

- 

The class constructor.

The only param this method gets is a constructor with all the mandatory
and optional component data. Component will receive the same descriptor
as create method param.

This method will call the "create" method before registering the component into
the reactive module. This way any component can add default selectors and events.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 61](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

[descriptor](global.md)

 

data to create the object.

 

 

 

 

## 

 exports

 

 

 

 

#### new exports(reactive)

 

**Description:
 :** 

- 

Class constructor.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 32](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reactive`

 

CourseEditor

 

the course editor object

 

 

 

 

## 

 exports

 

 

 

 

#### new exports(mainElement, selectors, preventcache)

 

**Description:
 :** 

- 

Setup the core/tree keyboard navigation.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 43](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `mainElement`

 

Element
|

undefined

 

an alternative main element in case it is not from the parent component

 
 `selectors`

 

Object
|

undefined

 

alternative selectors

 
 `preventcache`

 

boolean

 

if the elements cache must be disabled.

 

 

 

 

## 

 exports

 

 

 

 

#### new exports(config)

 

**Description:
 :** 

- 

Constructor.

To make a list draggable, create a new instance of this object, passing the necessary config.
For example:
{
// Selector for the list (or lists) to be reordered.
list: 'ul.my-list',

```js
 // Selector, relative to the list selector, for the items that can be moved.
 item: '> li',

 // While the proxy is being dragged, this class is added to the item being moved.
 // You can probably use "osep-itemmoving" here.
 itemMovingClass: "osep-itemmoving",

 // This is a callback which, when called with the DOM node for an item,
 // returns the string that uniquely identifies each item.
 // Therefore, the result of the drag action will be represented by the array
 // obtained by calling this method on each item in the list in order.
 idGetter: function(item) { return node.id; },

 // Function that will be called when a re-order starts (optional, can be not set).
 // Useful if you need to save information about the initial state.
 // This function should have two parameters. The first will be a
 // jQuery object for the list that was reordered, the second will
 // be the jQuery object for the item moved - which will not yet have been moved.
 // Note, it is quite possible for reorderStart to be called with no
 // subsequent call to reorderDone.
 reorderStart: function($list, $item) { ... }

 // Function that will be called when a drag has finished, and the list
 // has been reordered. This function should have three parameters. The first will be
 // a jQuery object for the list that was reordered, the second will be the jQuery
 // object for the item moved, and the third will be the new order, which is
 // an array of ids obtained by calling idGetter on each item in the list in order.
 // This callback will only be called in the new order is actually different from the old order.
 reorderDone: function($list, $item, newOrder) { ... }

 // Function that is always called when a re-order ends (optional, can be not set)
 // whether the order has changed. Useful if you need to undo changes made
 // in reorderStart, since reorderDone is only called if the new order is different
 // from the original order.
 reorderEnd: function($list, $item) { ... }

```

}

There is a subtlety, If you have items in your list that do not have a drag handle,
they are considered to be placeholders in otherwise empty containers.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 97](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

Object

 

As above.
