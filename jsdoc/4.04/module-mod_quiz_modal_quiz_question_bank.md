# mod_quiz/modal_quiz_question_bank - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_quiz_modal_quiz_question_bank.html

# mod_quiz/modal_quiz_question_bank

 

 

 

**Description:
 :** 

- 

Contain the logic for the question bank modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 16](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for the question bank modal.

 

 

 

 

### Methods

 

#### (inner) handleAddToQuizEvent(e, anchorElement)

 

**Description:
 :** 

- 

Update the URL of the anchor element that the user clicked on to make
sure that the question is added to the correct page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 104](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

event

 

A JavaScript event

 
 `anchorElement`

 

object

 

The anchor element that was triggered

 

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 122](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

 

#### (inner) reloadBodyContent(querystring)

 

**Description:
 :** 

- 

Replaces the current body contents with a new version of the question
bank.

The contents of the question bank are generated using the provided
query string.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 82](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `querystring`

 

string

 

URL encoded string.

 

 

#### (inner) show() → {void}

 

**Description:
 :** 

- 

Override the parent show function.

Reload the body contents when the modal is shown. The current
window URL is used to inform the new content that should be
displayed.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 67](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Returns:

**
 Type

 :** 

void
