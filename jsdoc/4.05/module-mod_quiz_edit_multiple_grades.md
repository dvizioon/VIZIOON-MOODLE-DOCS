# mod_quiz/edit_multiple_grades - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_quiz_edit_multiple_grades.html

# mod_quiz/edit_multiple_grades

 

 

 

**Description:
 :** 

- 

JavaScript for managing multiple grade items for a quiz.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 16](mod_quiz_amd_src_edit_multiple_grades.js.md)

 

**Copyright:
 :** 

- 2023 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JavaScript for managing multiple grade items for a quiz.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Entry point.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 527](mod_quiz_amd_src_edit_multiple_grades.js.md)

Entry point.

 

#### (inner, constant) SELECTORS :Object

 

**Description:
 :** 

- 

selectors used in this code.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 36](mod_quiz_amd_src_edit_multiple_grades.js.md)

selectors used in this code.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) autoSetupGradeItems(quizId) → {Promise}

 

**Description:
 :** 

- 

Call the Ajax service to setup one grade item for each quiz section.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 131](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `quizId`

 

Number

 

id of the quiz to update.

 

##### Returns:

Promise that resolves to the context required to re-render the page.

**
 Type

 :** 

Promise

 

#### (inner) callServiceAndReturnRenderingData(methodCall) → {Promise.<Object>}

 

**Description:
 :** 

- 

Make a web service call, and also call mod_quiz_get_edit_grading_page_data to get the date to re-render the page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 146](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `methodCall`

 

Object

 

a web service call to pass to fetchMany. Must include methodCall.args.quizid.

 

##### Returns:

a promise that resolves to the template context required to re-render the page.

**
 Type

 :** 

Promise.<Object>

 

#### (inner) callServicesAndReturnRenderingData(methodCalls) → {Promise.<Object>}

 

**Description:
 :** 

- 

Make a web service call, and also call mod_quiz_get_edit_grading_page_data to get the date to re-render the page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 154](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `methodCalls`

 

Array.<Object>

 

web service calls to pass to fetchMany. Must include methodCalls[0].args.quizid.

 

##### Returns:

a promise that resolves to the template context required to re-render the page.

**
 Type

 :** 

Promise.<Object>

 

#### (inner) createGradeItem(quizId) → {Promise.<Object>}

 

**Description:
 :** 

- 

Call the Ajax service to create a quiz grade item.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 57](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `quizId`

 

Number

 

id of the quiz to update.

 

##### Returns:

a promise that resolves to the template context required to re-render the page.

**
 Type

 :** 

Promise.<Object>

 

#### (inner) deleteGradeItem(quizId, gradeItemId) → {Promise}

 

**Description:
 :** 

- 

Call the Ajax service to delete a quiz grade item.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 94](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `quizId`

 

Number

 

id of the quiz to update.

 
 `gradeItemId`

 

Number

 

id of the grade item to delete.

 

##### Returns:

Promise that resolves to the context required to re-render the page.

**
 Type

 :** 

Promise

 

#### (inner) handleAddGradeItemClick(e)

 

**Description:
 :** 

- 

Handle clicks on the 'Add grade item' button.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 407](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleAutoSetup(e)

 

**Description:
 :** 

- 

Handle clicks on the reset button - show a confirmation.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 428](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleButtonClick(e)

 

**Description:
 :** 

- 

Handle clicks on the buttons.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 390](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleGradeItemClick(e)

 

**Description:
 :** 

- 

Handle clicks in the table the shows the grade items.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 367](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleGradeItemDelete(e)

 

**Description:
 :** 

- 

Handle click events on the delete icon.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 170](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleGradeItemEditStart(e)

 

**Description:
 :** 

- 

Handle click events on the start rename icon.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 214](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleGradeItemFocusOut(e)

 

**Description:
 :** 

- 

Handle focus out of the editable.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 313](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

event.

 

 

#### (inner) handleGradeItemKeyDown(e)

 

**Description:
 :** 

- 

Handle key down in the editable.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 245](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

key event.

 

 

#### (inner) handleGradeItemKeyUp(e)

 

**Description:
 :** 

- 

Handle key up in the editable.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 292](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

key event.

 

 

#### (inner) handleResetAllClick(e)

 

**Description:
 :** 

- 

Handle clicks on the reset button - show a confirmation.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 448](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event.

 

 

#### (inner) handleSlotGradeItemChanged(e)

 

**Description:
 :** 

- 

Handle when the selected grade item for a slot is changed.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 335](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

event.

 

 

#### (inner) reRenderPage(editGradingPageData) → {Promise.<void>}

 

**Description:
 :** 

- 

Replace the contents of the page with the page re-rendered from the provided data, once that promise resolves.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 283](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editGradingPageData`

 

Object

 

the template context data required to re-render the page.

 

##### Returns:

a promise that will resolve when the page is updated.

**
 Type

 :** 

Promise.<void>

 

#### (inner) reallyResetAll(button)

 

**Description:
 :** 

- 

Really reset all if the confirmation is OKed.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 466](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `button`

 

HTMLElement

 

the reset button.

 

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Replace the container with a new version.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 513](mod_quiz_amd_src_edit_multiple_grades.js.md)

 

#### (inner) stopEditingGadeItem(editableSpan)

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 201](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editableSpan`

 

HTMLElement

 

the editable to turn off.

 

 

#### (inner) updateGradeItem(quizId, gradeItemId, newName) → {Promise}

 

**Description:
 :** 

- 

Call the Ajax service to update a quiz grade item.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 75](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `quizId`

 

Number

 

id of the quiz to update.

 
 `gradeItemId`

 

Number

 

id of the grade item to update.

 
 `newName`

 

String

 

the new name to set.

 

##### Returns:

Promise that resolves to the context required to re-render the page.

**
 Type

 :** 

Promise

 

#### (inner) updateSlotGradeItem(quizId, slotId, gradeItemId) → {Promise}

 

**Description:
 :** 

- 

Call the Ajax service to update the quiz grade item used by a slot.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/edit_multiple_grades.js](mod_quiz_amd_src_edit_multiple_grades.js.md), [line 113](mod_quiz_amd_src_edit_multiple_grades.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `quizId`

 

Number

 

id of the quiz to update.

 
 `slotId`

 

Number

 

id of the slot to update.

 
 `gradeItemId`

 

Number
|

null

 

new grade item ot set, or null to un-set.

 

##### Returns:

Promise that resolves to the context required to re-render the page.

**
 Type

 :** 

Promise
