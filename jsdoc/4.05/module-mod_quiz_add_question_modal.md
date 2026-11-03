# mod_quiz/add_question_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_quiz_add_question_modal.html

# mod_quiz/add_question_modal

 

 

 

**Description:
 :** 

- 

Contain the logic for the add random question modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal.js](mod_quiz_amd_src_add_question_modal.js.md), [line 16](mod_quiz_amd_src_add_question_modal.js.md)

 

**Copyright:
 :** 

- 2023 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for the add random question modal.

 

 

 

 

### Methods

 

#### (inner) getAddOnPageId() → {Number}

 

**Description:
 :** 

- 

Returns the saved page id for the question to be added to.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal.js](mod_quiz_amd_src_add_question_modal.js.md), [line 82](mod_quiz_amd_src_add_question_modal.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getContextId() → {Number}

 

**Description:
 :** 

- 

Retrieve the saved Moodle context id.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal.js](mod_quiz_amd_src_add_question_modal.js.md), [line 61](mod_quiz_amd_src_add_question_modal.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) setAddOnPageId(id)

 

**Description:
 :** 

- 

Set the id of the page that the question should be added to
when the user clicks the add to quiz link.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal.js](mod_quiz_amd_src_add_question_modal.js.md), [line 71](mod_quiz_amd_src_add_question_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

 

 

 

#### (inner) setContextId(id)

 

**Description:
 :** 

- 

Save the Moodle context id that the question bank is being
rendered in.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal.js](mod_quiz_amd_src_add_question_modal.js.md), [line 50](mod_quiz_amd_src_add_question_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number
