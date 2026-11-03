# gradereport_grader/feedback_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_grader_feedback_modal.html

# gradereport_grader/feedback_modal

 

 

 

**Description:
 :** 

- 

Javascript module for displaying feedback in a modal window

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/feedback_modal.js](grade_report_grader_amd_src_feedback_modal.js.md), [line 16](grade_report_grader_amd_src_feedback_modal.js.md)

 

**Copyright:
 :** 

- 2023 Kevin Percy 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript module for displaying feedback in a modal window

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/feedback_modal.js](grade_report_grader_amd_src_feedback_modal.js.md), [line 114](grade_report_grader_amd_src_feedback_modal.js.md)

Initialize module

 

 

### Methods

 

#### (inner) fetchFeedback(courseid, userid, itemid) → {Promise}

 

**Description:
 :** 

- 

Fetch the feedback data.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/feedback_modal.js](grade_report_grader_amd_src_feedback_modal.js.md), [line 80](grade_report_grader_amd_src_feedback_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

 

 
 `userid`

 

int

 

 

 
 `itemid`

 

int

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (async, inner) getModal(courseid, userid, itemid) → {Promise}

 

**Description:
 :** 

- 

Create the modal to display the feedback.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/feedback_modal.js](grade_report_grader_amd_src_feedback_modal.js.md), [line 40](grade_report_grader_amd_src_feedback_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

 

 
 `userid`

 

int

 

 

 
 `itemid`

 

int

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the View Feedback links.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/feedback_modal.js](grade_report_grader_amd_src_feedback_modal.js.md), [line 95](grade_report_grader_amd_src_feedback_modal.js.md)
