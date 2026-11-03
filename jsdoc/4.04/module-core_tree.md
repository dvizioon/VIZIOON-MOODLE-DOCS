# core/tree - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_tree.html

# core/tree

 

 

 

**Description:
 :** 

- 

Implement an accessible aria tree widget, from a nested unordered list.
Based on http://oaa-accessibility.org/example/41/.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 16](lib_amd_src_tree.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Implement an accessible aria tree widget, from a nested unordered list.
Based on http://oaa-accessibility.org/example/41/.

 

 

 

 

### Methods

 

#### (inner) bindEventHandlers()

 

**Description:
 :** 

- 

Bind the event listeners we require.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 529](lib_amd_src_tree.js.md)

 

#### (inner) collapseGroup(item)

 

**Description:
 :** 

- 

Collapse an expanded group.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 313](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group.

 

 

#### (inner) expandAllChildGroups(item)

 

**Description:
 :** 

- 

Find all child group nodes from the given node and expand them.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 233](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the group.

 

 

#### (inner) expandAllGroups()

 

**Description:
 :** 

- 

Expand all group nodes within the tree.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 216](lib_amd_src_tree.js.md)

 

#### (inner) expandGroup(item) → {Object}

 

**Description:
 :** 

- 

Expand a collapsed group.

Handles expanding nodes that are ajax loaded (marked with a data-requires-ajax attribute).

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 251](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group.

 

##### Returns:

a promise that is resolved when the group has been expanded.

**
 Type

 :** 

Object

 

#### (inner) finishExpandingGroup(item)

 

**Description:
 :** 

- 

Perform the necessary DOM changes to display a group item.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 297](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group.

 

 

#### (inner) getVisibleItems() → {Object}

 

**Description:
 :** 

- 

Get all visible tree items.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 85](lib_amd_src_tree.js.md)

##### Returns:

visible items

**
 Type

 :** 

Object

 

#### (inner) handleClick(event)

 

**Description:
 :** 

- 

Handle a click (select).

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 498](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

The event.

 

 

#### (inner) handleFocus(e)

 

**Description:
 :** 

- 

Handle a focus event.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 519](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

 

#### (inner) handleKeyDown(e)

 

**Description:
 :** 

- 

Handle a key down event - ie navigate the tree.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 348](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

 

#### (inner) initialiseNodes(node)

 

**Description:
 :** 

- 

Performs the tree initialisation for all child items from the given node,
such as removing everything from the tab order and setting aria selected
on items.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 173](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

object

 

jquery object representing a node.

 

 

#### (inner) isGroupCollapsed(item) → {bool}

 

**Description:
 :** 

- 

Determines if the given group item (contains child tree items) is collapsed.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 151](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

jquery object representing a group item on the tree.

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isGroupCollapsible(item) → {bool}

 

**Description:
 :** 

- 

Determines if the given group item (contains child tree items) can be collapsed.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 162](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

jquery object representing a group item on the tree.

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isGroupItem(item) → {bool}

 

**Description:
 :** 

- 

Determines if the given item is a group item (contains child tree items) in the tree.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 123](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

jquery object representing an item on the tree.

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isGroupItem(item) → {bool}

 

**Description:
 :** 

- 

Determines if the given item is a group item (contains child tree items) in the tree.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 134](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

jquery object representing an item on the tree.

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) refreshVisibleItemsCache()

 

**Description:
 :** 

- 

Find all visible tree items and save a cache of them on the tree object.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 76](lib_amd_src_tree.js.md)

 

#### (inner) removeAllFromTabOrder(node)

 

**Description:
 :** 

- 

Removes all child DOM elements of the given node from the tab order.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 195](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

object

 

jquery object representing a node.

 

 

#### (inner) setActiveItem(item)

 

**Description:
 :** 

- 

Mark the given item as active within the tree and fire the callback for when the active item is set.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 95](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

jquery object representing an item on the tree.

 

 

#### (inner) setAriaSelectedFalseOnItems(node)

 

**Description:
 :** 

- 

Find all child tree items from the given node and set the aria selected attribute to false.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 206](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

object

 

jquery object representing a node.

 

 

#### (inner) toggleGroup(item)

 

**Description:
 :** 

- 

Expand or collapse a group.

 

**Source:
 :** 

- 
 [lib/amd/src/tree.js](lib_amd_src_tree.js.md), [line 334](lib_amd_src_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery id of the parent item of the group.
