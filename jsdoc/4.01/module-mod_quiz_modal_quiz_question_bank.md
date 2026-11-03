# mod_quiz/modal_quiz_question_bank - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_quiz_modal_quiz_question_bank.html

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

 

#### (inner) getAddOnPageId() → {int}

 

**Description:
 :** 

- 

Returns the saved page id for the question to be added it.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 100](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getContextId() → {int}

 

**Description:
 :** 

- 

Retrieve the saved Moodle context id.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 79](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) handleAddToQuizEvent(e, anchorElement)

 

**Description:
 :** 

- 

Update the URL of the anchor element that the user clicked on to make
sure that the question is added to the correct page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 149](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

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

 

 

#### (inner) handleDisplayOptionFormEvent(e)

 

**Description:
 :** 

- 

Reload the modal body with the new display options the user has selected.

A query string is built using the form elements to be used to generate the
new body content.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 196](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

event

 

A JavaScript event

 

 

#### (inner) handlePreviewContainerEvent(e, anchorElement)

 

**Description:
 :** 

- 

Open a popup window to show the preview of the question.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 166](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

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

 

 

#### (inner) registerDisplayOptionListeners()

 

**Description:
 :** 

- 

Listen for changes to the display options form.

This handles the user changing:
- The quiz category select box
- The tags to filter by
- Show/hide questions from sub categories
- Show/hide old questions

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 216](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 249](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

 

#### (inner) reloadBodyContent(queryString)

 

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
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 125](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `queryString`

 

string

 

URL encoded string.

 

 

#### (inner) setAddOnPageId(id)

 

**Description:
 :** 

- 

Set the id of the page that the question should be added to
when the user clicks the add to quiz link.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 89](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

 

#### (inner) setContextId(id)

 

**Description:
 :** 

- 

Save the Moodle context id that the question bank is being
rendered in.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 68](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

 

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
 [mod/quiz/amd/src/modal_quiz_question_bank.js](mod_quiz_amd_src_modal_quiz_question_bank.js.md), [line 110](mod_quiz_amd_src_modal_quiz_question_bank.js.md)

##### Returns:

**
 Type

 :** 

void
