# qbank_columnsortorder/user_actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-qbank_columnsortorder_user_actions.html

# qbank_columnsortorder/user_actions

 

 

 

**Description:
 :** 

- 

Javascript for customising the user's view of the question bank

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 16](question_bank_columnsortorder_amd_src_user_actions.js.md)

 

**Author:
 :** 

- [Ghaly Marc-Alexandre](mailto:marc-alexandreghaly@catalyst-ca.net)

 

 

**Copyright:
 :** 

- 2021 Catalyst IT Australia Pty Ltd

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript for customising the user's view of the question bank

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module

Add containers for the drag handles to each column header, then render handles, enable show/hide behaviour, set up drag/drop
column sorting, then enable the move and resize modals to be triggered from menu actions.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 380](question_bank_columnsortorder_amd_src_user_actions.js.md)

Initialize module

Add containers for the drag handles to each column header, then render handles, enable show/hide behaviour, set up drag/drop
column sorting, then enable the move and resize modals to be triggered from menu actions.

 

#### (inner) currentHeader

 

**Description:
 :** 

- 

To track mouse event on a table header

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 46](question_bank_columnsortorder_amd_src_user_actions.js.md)

To track mouse event on a table header

 

#### (inner) currentMin

 

**Description:
 :** 

- 

Minimum size for the column currently being resized.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 52](question_bank_columnsortorder_amd_src_user_actions.js.md)

Minimum size for the column currently being resized.

 

#### (inner) currentX

 

**Description:
 :** 

- 

Current mouse x postion, to track mouse event on a table header

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 49](question_bank_columnsortorder_amd_src_user_actions.js.md)

Current mouse x postion, to track mouse event on a table header

 

#### (inner) suspendShowHideHandles :boolean

 

**Description:
 :** 

- 

Flag to temporarily prevent move and resize handles from being shown or hidden.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 59](question_bank_columnsortorder_amd_src_user_actions.js.md)

Flag to temporarily prevent move and resize handles from being shown or hidden.

##### Type:

- 

boolean

 

 

 

### Methods

 

#### (inner) addHandleContainers(uiRoot) → {Promise}

 

**Description:
 :** 

- 

Add handle containers for move and resize handles.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 67](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

The root element of the quesiton bank UI.

 

##### Returns:

Resolved after the containers have been added to each column header.

**
 Type

 :** 

Promise

 

#### (inner) getMinWidth(header) → {Number}

 

**Description:
 :** 

- 

Find the minimum width for a header, based on the width of its contents.

This is to simulate `min-width: min-content;`, which doesn't work on Chrome because
min-width is ignored width `table-layout: fixed;`.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 144](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `header`

 

Element

 

The table header

 

##### Returns:

The minimum width in pixels

**
 Type

 :** 

Number

 

#### (inner) reorderColumns(event)

 

**Description:
 :** 

- 

Event handler for sortable list DROP event.

Find all table cells corresponding to the column of the dropped header, and move them to the new position.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 352](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

 

 

 

#### (inner) serialiseColumnSizes(uiRoot) → {String}

 

**Description:
 :** 

- 

Serialise the current column sizes.

This finds the current width set in each column header's style property, and returns them encoded as a JSON string.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 118](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

The root element of the quesiton bank UI.

 

##### Returns:

JSON array containing a list of objects with column and width properties.

**
 Type

 :** 

String

 

#### (inner) setUpMoveActions(uiRoot)

 

**Description:
 :** 

- 

Event handler for move actions in each column header.

This will listen for a click on any move action, pass the click to the corresponding move handle, causing its modal to be shown.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 303](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

Question bank UI root element.

 

 

#### (inner) setUpMoveHandles(moveActions)

 

**Description:
 :** 

- 

Render move handles in each container.

This takes a list of the move actions rendered in each column header, and creates a corresponding drag handle for each.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 88](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `moveActions`

 

NodeList

 

Menu actions for moving columns.

 

 

#### (inner) setUpResizeActions(uiRoot)

 

**Description:
 :** 

- 

Event handler for resize actions in each column header.

This will listen for a click on any resize action, and activate the corresponding resize modal.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 248](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

Question bank UI root element.

 

 

#### (inner) setUpResizeHandles(uiRoot)

 

**Description:
 :** 

- 

Render resize handles in each container.

This takes a list of the resize actions rendered in each column header, and creates a corresponding drag handle for each.
It also initialises the event handlers for the drag handles and resize modal.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 158](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

Question bank UI root element.

 

 

#### (inner) setupShowHideHandles(uiRoot)

 

**Description:
 :** 

- 

Event handler for showing and hiding handles when the mouse is over a column header.

Implementing this behaviour using the :hover CSS pseudoclass is not sufficient, as the mouse may move over the neighbouring
header while dragging, leading to some odd behaviour. This allows us to suspend the show/hide behaviour while a handle is being
dragged, and so keep the active handle visible until the drag is finished.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 324](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

Question bank UI root element.

 

 

#### (async, inner) showResizeModal(currentHeader, uiRoot) → {Promise.<void>}

 

**Description:
 :** 

- 

Show a modal containing a number input for changing a column width without click-and-drag.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/user_actions.js](question_bank_columnsortorder_amd_src_user_actions.js.md), [line 266](question_bank_columnsortorder_amd_src_user_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentHeader`

 

Element

 

The header element that is being resized.

 
 `uiRoot`

 

Element

 

The question bank UI root element.

 

##### Returns:

**
 Type

 :** 

Promise.<void>
