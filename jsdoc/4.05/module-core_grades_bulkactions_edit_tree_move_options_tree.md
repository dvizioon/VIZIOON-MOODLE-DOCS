# module:core_grades/bulkactions/edit/tree/move_options_tree - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_grades_bulkactions_edit_tree_move_options_tree.html

# module:core_grades/bulkactions/edit/tree/move_options_tree

 

## 

 module:core_grades/bulkactions/edit/tree/move_options_tree

 

 

 

 

#### new (require("core_grades/bulkactions/edit/tree/move_options_tree"))(afterSelectMoveOptionCallback) → {void}

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 49](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `afterSelectMoveOptionCallback`

 

function
|

null

 

Callback function used to define actions that should be run
after selecting a move option.

 

##### Returns:

**
 Type

 :** 

void

 

 

 

### Members

 

#### afterSelectMoveOptionCallback

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 37](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `afterSelectMoveOptionCallback`

 

function
|

null

 

Callback function to run after selecting a move option.

 

 

#### selectedMoveOption

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 40](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `selectedMoveOption`

 

HTMLElement
|

null

 

The selected move option.

 

 

#### (inner, constant) The :Object

 

**Description:
 :** 

- 

object containing the relevant selectors.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 27](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

object containing the relevant selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### handleItemClick(event, item) → {void}

 

**Description:
 :** 

- 

Handle an item click.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 76](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

The click event.

 
 `item`

 

jQuery

 

The item clicked.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) handleKeyDown(e)

 

**Description:
 :** 

- 

Handle a key down event.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 54](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

 

#### (inner) selectMoveOption(moveOption)

 

**Description:
 :** 

- 

Select a move option.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move_options_tree.js](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md), [line 87](grade_amd_src_bulkactions_edit_tree_move_options_tree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `moveOption`

 

HTMLElement

 

The move option to select.
