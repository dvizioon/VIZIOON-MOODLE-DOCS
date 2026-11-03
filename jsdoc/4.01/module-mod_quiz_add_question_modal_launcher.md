# mod_quiz/add_question_modal_launcher - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_quiz_add_question_modal_launcher.html

# mod_quiz/add_question_modal_launcher

 

 

 

**Description:
 :** 

- 

Initialise the an add question modal on the quiz page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal_launcher.js](mod_quiz_amd_src_add_question_modal_launcher.js.md), [line 16](mod_quiz_amd_src_add_question_modal_launcher.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Initialise the an add question modal on the quiz page.

 

 

 

 

### Methods

 

#### (inner) init(modalType, selector, contextId, preShowCallback, showNewCategory) → {promise}

 

**Description:
 :** 

- 

Create a modal using the modal factory and add listeners to launch the
modal when clicked.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_question_modal_launcher.js](mod_quiz_amd_src_add_question_modal_launcher.js.md), [line 47](mod_quiz_amd_src_add_question_modal_launcher.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalType`

 

string

 

Which modal to create

 
 `selector`

 

string

 

The selectors for the elements that trigger the modal

 
 `contextId`

 

int

 

The current context id

 
 `preShowCallback`

 

function

 

A callback to execute before the modal is shown

 
 `showNewCategory`

 

boolean

 

Display the New category tab when selecting random questions.

 

##### Returns:

Resolved with the modal

**
 Type

 :** 

promise
