# core_question/refresh_ui - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_question_refresh_ui.html

# core_question/refresh_ui

 

 

 

**Description:
 :** 

- 

Question bank UI refresh utility

 

**Source:
 :** 

- 
 [question/amd/src/refresh_ui.js](question_amd_src_refresh_ui.js.md), [line 16](question_amd_src_refresh_ui.js.md)

 

**Copyright:
 :** 

- 2023 Catalyst IT Europe Ltd.

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Question bank UI refresh utility

 

 

 

 

### Methods

 

#### (static) refresh(uiRoot, returnUrl) → {Promise}

 

**Description:
 :** 

- 

Reload the question bank UI, retaining the current filters and sort data.

 

**Source:
 :** 

- 
 [question/amd/src/refresh_ui.js](question_amd_src_refresh_ui.js.md), [line 36](question_amd_src_refresh_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `uiRoot`

 

Element

 

The root element of the UI to be refreshed. Must contain "component", "callback" and "contextid" in
its data attributes, to be passed to the Fragment API.

 
 `returnUrl`

 

URL

 

The url of the current page, containing filter and sort parameters.

 

##### Returns:

Resolved when the refresh is complete.

**
 Type

 :** 

Promise
