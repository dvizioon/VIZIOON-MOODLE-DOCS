# tool_lp/tree - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_tree.html

# tool_lp/tree

 

 

 

**Description:
 :** 

- 

Implement an accessible aria tree widget, from a nested unordered list.
Based on http://oaa-accessibility.org/example/41/

To respond to selection changed events - use tree.on("selectionchanged", handler).
The handler will receive an array of nodes, which are the list items that are currently
selected. (Or a single node if multiselect is disabled).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 16](admin_tool_lp_amd_src_tree.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Implement an accessible aria tree widget, from a nested unordered list.
Based on http://oaa-accessibility.org/example/41/

To respond to selection changed events - use tree.on("selectionchanged", handler).
The handler will receive an array of nodes, which are the list items that are currently
selected. (Or a single node if multiselect is disabled).

 

 

 

 

### Members

 

#### (inner) collapsedImage :String

 

**Description:
 :** 

- 

The html for a collapsed tree node twistie.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 32](admin_tool_lp_amd_src_tree.js.md)

The html for a collapsed tree node twistie.

##### Type:

- 

String

 

 

#### (inner) expandedImage :String

 

**Description:
 :** 

- 

The html for an expanded tree node twistie.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 30](admin_tool_lp_amd_src_tree.js.md)

The html for an expanded tree node twistie.

##### Type:

- 

String

 

 

 

### Methods

 

#### (inner) bindEventHandlers()

 

**Description:
 :** 

- 

Bind the event listeners we require.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 597](admin_tool_lp_amd_src_tree.js.md)

 

#### (inner) collapseGroup(item)

 

**Description:
 :** 

- 

Collapse an expanded group.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 126](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 

 

#### (inner) expandGroup(item)

 

**Description:
 :** 

- 

Expand a collapsed group.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 105](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 

 

#### (inner) handleBlur() → {Boolean}

 

**Description:
 :** 

- 

Handle a blur event

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 573](admin_tool_lp_amd_src_tree.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleClick(item, e) → {Boolean}

 

**Description:
 :** 

- 

Handle a click (select).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 551](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleDblClick(item, e) → {Boolean}

 

**Description:
 :** 

- 

Handle a double click (expand/collapse).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 509](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleExpandCollapseClick(item, e) → {Boolean}

 

**Description:
 :** 

- 

Handle a click (select).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 534](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleFocus(item) → {Boolean}

 

**Description:
 :** 

- 

Handle a focus event

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 583](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

item is the jquery id of the parent item of the group

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleKeyDown(item, e) → {Boolean}

 

**Description:
 :** 

- 

Handle a key down event - ie navigate the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 268](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) handleKeyPress(item, e) → {Boolean}

 

**Description:
 :** 

- 

Handle a key press event - ie navigate the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 419](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) init()

 

**Description:
 :** 

- 

Init this tree

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 81](admin_tool_lp_amd_src_tree.js.md)

 

#### (inner) multiSelectItem(item)

 

**Description:
 :** 

- 

Select all the items between the last focused item and this currently focused item.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 173](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the newly selected item.

 

 

#### (inner) on(eventname, handler)

 

**Description:
 :** 

- 

Attach an event listener to the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 494](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventname`

 

String

 

This is the name of the event to listen for. Only 'selectionchanged' is supported for now.

 
 `handler`

 

function

 

The function to call when the event is triggered.

 

 

#### (inner) selectItem(item)

 

**Description:
 :** 

- 

Select a single item. Make sure all the parents are expanded. De-select all other items.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 203](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the newly selected item.

 

 

#### (inner) toggleGroup(item)

 

**Description:
 :** 

- 

Expand or collapse a group.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 146](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group

 

 

#### (inner) toggleItem(item)

 

**Description:
 :** 

- 

Toggle the selected state for an item back and forth.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 224](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the item to toggle.

 

 

#### (inner) triggerChange()

 

**Description:
 :** 

- 

Whenever the currently selected node has changed, trigger an event using this function.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 160](admin_tool_lp_amd_src_tree.js.md)

 

#### (inner) updateFocus(item)

 

**Description:
 :** 

- 

Set the focus to this item.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/tree.js](admin_tool_lp_amd_src_tree.js.md), [line 246](admin_tool_lp_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group
