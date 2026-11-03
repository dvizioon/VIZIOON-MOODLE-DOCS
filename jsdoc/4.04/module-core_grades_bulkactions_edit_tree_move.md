# module:core_grades/bulkactions/edit/tree/move - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_grades_bulkactions_edit_tree_move.html

# module:core_grades/bulkactions/edit/tree/move

 

## 

 module:core_grades/bulkactions/edit/tree/move

 

 

 

 

#### new (require("core_grades/bulkactions/edit/tree/move"))(courseId) → {void}

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 56](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

int

 

The course ID.

 

##### Returns:

**
 Type

 :** 

void

 

 

 

### Members

 

#### courseId

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 42](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

int
|

null

 

The course ID.

 

 

#### gradeTree

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 48](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `gradeTree`

 

string
|

null

 

The grade tree structure.

 

 

#### moveOptionsTree

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 45](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `moveOptionsTree`

 

MoveOptionsTree
|

null

 

The move options tree object.

 

 

#### (inner, constant) The :Object

 

**Description:
 :** 

- 

object containing the relevant selectors.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 32](grade_amd_src_bulkactions_edit_tree_move.js.md)

object containing the relevant selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### getBulkActionTriggerSelector() → {string}

 

**Description:
 :** 

- 

Defines the selector of the element that triggers the bulk move action.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 66](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

The bulk move action trigger selector.

**
 Type

 :** 

string

 

#### (inner) executeBulkAction() → {void}

 

**Description:
 :** 

- 

Defines the behavior once the bulk move action is triggered.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 70](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

**
 Type

 :** 

void

 

#### (inner) fetchGradeTree() → {Promise}

 

**Description:
 :** 

- 

Fetch the grade tree structure for the current course.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 124](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

The grade tree promise

**
 Type

 :** 

Promise

 

#### (inner) registerCustomClickListenerEvents(modal) → {void}

 

**Description:
 :** 

- 

Register custom event listeners.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 91](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Object

 

The modal object.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) renderBulkActionTrigger() → {Promise}

 

**Description:
 :** 

- 

Renders the bulk move action trigger element.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 81](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

The bulk move action trigger promise

**
 Type

 :** 

Promise

 

#### (inner) renderModalBody() → {Promise}

 

**Description:
 :** 

- 

Renders the bulk move modal body.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 140](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

The modal body promise

**
 Type

 :** 

Promise

 

#### (inner) showModal() → {Promise}

 

**Description:
 :** 

- 

Show the bulk move modal.

 

**Source:
 :** 

- 
 [grade/amd/src/bulkactions/edit/tree/move.js](grade_amd_src_bulkactions_edit_tree_move.js.md), [line 156](grade_amd_src_bulkactions_edit_tree_move.js.md)

##### Returns:

The modal promise

**
 Type

 :** 

Promise
