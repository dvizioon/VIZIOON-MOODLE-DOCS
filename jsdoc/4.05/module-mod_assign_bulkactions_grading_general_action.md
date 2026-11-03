# module:mod_assign/bulkactions/grading/general_action - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_bulkactions_grading_general_action.html

# module:mod_assign/bulkactions/grading/general_action

 

## 

 module:mod_assign/bulkactions/grading/general_action

 

 

 

 

#### new (require("mod_assign/bulkactions/grading/general_action"))(cmid, sesskey, actionKey, buttonLabel, buttonIcon, confirmationTitle, confirmationQuestion, confirmationYes)

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/bulkactions/grading/general_action.js](mod_assign_amd_src_bulkactions_grading_general_action.js.md), [line 71](mod_assign_amd_src_bulkactions_grading_general_action.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

int

 

The course module ID.

 
 `sesskey`

 

string

 

The session key.

 
 `actionKey`

 

string

 

The action key.

 
 `buttonLabel`

 

Promise.<string>

 

The action button's label.

 
 `buttonIcon`

 

Promise.<string>

 

The action button's icon.

 
 `confirmationTitle`

 

Promise.<string>

 

Title of the confirmation dialog.

 
 `confirmationQuestion`

 

Promise.<string>

 

Question of the confirmation dialog.

 
 `confirmationYes`

 

Promise.<string>

 

Text for the confirmation yes button.

 

 

 

 

### Members

 

#### actionKey :string

 

**Description:
 :** 

- 

The action key.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/bulkactions/grading/general_action.js](mod_assign_amd_src_bulkactions_grading_general_action.js.md), [line 36](mod_assign_amd_src_bulkactions_grading_general_action.js.md)

The action key.

##### Type:

- 

string
