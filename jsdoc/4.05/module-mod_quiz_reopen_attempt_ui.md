# mod_quiz/reopen_attempt_ui - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_quiz_reopen_attempt_ui.html

# mod_quiz/reopen_attempt_ui

 

 

 

**Description:
 :** 

- 

This module has the code to make the Re-open attempt button work, if present.

That is, it looks for buttons with HTML like
<button type="button" data-action="reopen-attempt" data-attempt-id="227000" data-after-action-url="/mod/quiz/report.php">
and if that is clicked, it first shows an 'Are you sure' pop-up, and if they are sure,
the attempt is re-opened, and then the page reloads.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/reopen_attempt_ui.js](mod_quiz_amd_src_reopen_attempt_ui.js.md), [line 16](mod_quiz_amd_src_reopen_attempt_ui.js.md)

 

**Copyright:
 :** 

- 2023 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module has the code to make the Re-open attempt button work, if present.

That is, it looks for buttons with HTML like
<button type="button" data-action="reopen-attempt" data-attempt-id="227000" data-after-action-url="/mod/quiz/report.php">
and if that is clicked, it first shows an 'Are you sure' pop-up, and if they are sure,
the attempt is re-opened, and then the page reloads.

 

 

 

 

### Methods

 

#### (async, inner) reopenButtonClicked(e)

 

**Description:
 :** 

- 

Handle a click if it is on one of our buttons.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/reopen_attempt_ui.js](mod_quiz_amd_src_reopen_attempt_ui.js.md), [line 39](mod_quiz_amd_src_reopen_attempt_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

the click event.
