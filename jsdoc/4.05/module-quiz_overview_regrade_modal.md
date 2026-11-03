# quiz_overview/regrade_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-quiz_overview_regrade_modal.html

# quiz_overview/regrade_modal

 

 

 

**Description:
 :** 

- 

Regrade modal form is used to regrade or dryrun the attempts and questions.

 

**Source:
 :** 

- 
 [mod/quiz/report/overview/amd/src/regrade_modal.js](mod_quiz_report_overview_amd_src_regrade_modal.js.md), [line 16](mod_quiz_report_overview_amd_src_regrade_modal.js.md)

 

**Copyright:
 :** 

- 2024 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Regrade modal form is used to regrade or dryrun the attempts and questions.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize the regrade button to open the modal.

 

**Source:
 :** 

- 
 [mod/quiz/report/overview/amd/src/regrade_modal.js](mod_quiz_report_overview_amd_src_regrade_modal.js.md), [line 106](mod_quiz_report_overview_amd_src_regrade_modal.js.md)

Initialize the regrade button to open the modal.

 

#### (inner, constant) SELECTORS :Object

 

**Description:
 :** 

- 

selectors used in this code.

 

**Source:
 :** 

- 
 [mod/quiz/report/overview/amd/src/regrade_modal.js](mod_quiz_report_overview_amd_src_regrade_modal.js.md), [line 32](mod_quiz_report_overview_amd_src_regrade_modal.js.md)

selectors used in this code.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (async, inner) showModal(e) → {Promise.<void>}

 

**Description:
 :** 

- 

Show the regrade modal.

 

**Source:
 :** 

- 
 [mod/quiz/report/overview/amd/src/regrade_modal.js](mod_quiz_report_overview_amd_src_regrade_modal.js.md), [line 48](mod_quiz_report_overview_amd_src_regrade_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

click event that opened the modal.

 

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (inner) updateButtonStates()

 

**Description:
 :** 

- 

Enables and disables controls when the selected options are changed.

 

**Source:
 :** 

- 
 [mod/quiz/report/overview/amd/src/regrade_modal.js](mod_quiz_report_overview_amd_src_regrade_modal.js.md), [line 88](mod_quiz_report_overview_amd_src_regrade_modal.js.md)
