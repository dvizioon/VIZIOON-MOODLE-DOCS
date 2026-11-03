# module:core_grades/bulkactions/edit/tree/bulk_actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_grades_bulkactions_edit_tree_bulk_actions.html

# module:core_grades/bulkactions/edit/tree/bulk_actions

 

## 

 module:core_grades/bulkactions/edit/tree/bulk_actions

 

 

 

 

#### new (require("core_grades/bulkactions/edit/tree/bulk_actions"))(courseID) → {void}

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 52](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseID`

 

int

 

The course ID.

 

##### Returns:

**
 Type

 :** 

void

 

 

 

### Members

 

#### courseID

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 34](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `courseID`

 

int
|

null

 

The course ID.

 

 

 

### Methods

 

#### (inner) deselectItem(selectedItem) → {void}

 

**Description:
 :** 

- 

Defines the action for deselecting a selected item.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 93](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectedItem`

 

HTMLElement

 

The selected element.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) getBulkActions() → {Array}

 

**Description:
 :** 

- 

Returns the array of the relevant bulk action objects for the gradebook setup page.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 57](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getSelectedItems() → {Array}

 

**Description:
 :** 

- 

Returns the array of selected items.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 69](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) registerItemSelectChangeEvent(eventHandler) → {void}

 

**Description:
 :** 

- 

Adds the listener for the item select change event.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/bulk_actions.js](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md), [line 79](grade_amd_src_bulkactions_edit_tree_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventHandler`

 

function

 

The event handler function.

 

##### Returns:

**
 Type

 :** 

void
