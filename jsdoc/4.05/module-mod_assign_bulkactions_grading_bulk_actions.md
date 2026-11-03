# module:mod_assign/bulkactions/grading/bulk_actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_bulkactions_grading_bulk_actions.html

# module:mod_assign/bulkactions/grading/bulk_actions

 

## 

 module:mod_assign/bulkactions/grading/bulk_actions

 

 

 

 

#### new (require("mod_assign/bulkactions/grading/bulk_actions"))(options)

 

**Description:
 :** 

- 

The class constructor

 

**Source:
 :** 

- 
 [mod/assign/amd/src/bulkactions/grading/bulk_actions.js](mod_assign_amd_src_bulkactions_grading_bulk_actions.js.md), [line 105](mod_assign_amd_src_bulkactions_grading_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `options`

 

Object

 

The options object.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

number

 

The course module ID.

 
 `message`

 

string

 

Whether to show the message action.

 
 `submissiondrafts`

 

boolean

 

Whether to show the revert to draft action.

 
 `removesubmission`

 

boolean

 

Whether to show the remove submission action.

 
 `extend`

 

boolean

 

Whether to show the grant extension action.

 
 `grantattempt`

 

boolean

 

Whether to show the grant attempt action.

 
 `workflowstate`

 

boolean

 

Whether to show the set workflow state action.

 
 `markingallocation`

 

boolean

 

Whether to show the set marking allocation action.

 
 `pluginoperations`

 

Array

 

The list of plugin operations.

 
 `sesskey`

 

string

 

The session key.

 

 

 

 

 

 

### Methods

 

#### (static) init(options) → {this}

 

**Description:
 :** 

- 

Returns the instance of the class.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/bulkactions/grading/bulk_actions.js](mod_assign_amd_src_bulkactions_grading_bulk_actions.js.md), [line 86](mod_assign_amd_src_bulkactions_grading_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `options`

 

Object

 

The options object.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

number

 

The course module ID.

 
 `message`

 

string

 

Whether to show the message action.

 
 `submissiondrafts`

 

boolean

 

Whether to show the revert to draft action.

 
 `removesubmission`

 

boolean

 

Whether to show the remove submission action.

 
 `extend`

 

boolean

 

Whether to show the grant extension action.

 
 `grantattempt`

 

boolean

 

Whether to show the grant attempt action.

 
 `workflowstate`

 

boolean

 

Whether to show the set workflow state action.

 
 `markingallocation`

 

boolean

 

Whether to show the set marking allocation action.

 
 `pluginoperations`

 

Array

 

The list of plugin operations.

 
 `sesskey`

 

string

 

The session key.

 

 

 

##### Returns:

An instance of the anonymous class extending BulkActions.

**
 Type

 :** 

this
