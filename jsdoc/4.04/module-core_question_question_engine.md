# core_question/question_engine - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_question_question_engine.html

# core_question/question_engine

 

 

 

**Description:
 :** 

- 

JavaScript required by the question engine.

 

**Source:
 :** 

- 
 [question/amd/src/question_engine.js](question_amd_src_question_engine.js.md), [line 16](question_amd_src_question_engine.js.md)

 

**Copyright:
 :** 

- 2021 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JavaScript required by the question engine.

 

 

 

 

### Members

 

#### (static, constant) initForm

 

**Description:
 :** 

- 

Initialise a form that contains questions printed using print_question.
This has the effect of:

  - Turning off browser autocomlete.

  - Stopping enter from submitting the form (or toggling the next flag) unless
keyboard focus is on the submit button or the flag.

  - Removes any '.questionflagsavebutton's, since we have JavaScript to toggle
the flags using ajax.

  - Scroll to the position indicated by scrollpos= in the URL, if it is there.

  - Prevent the user from repeatedly submitting the form.

 

**Source:
 :** 

- 
 [question/amd/src/question_engine.js](question_amd_src_question_engine.js.md), [line 51](question_amd_src_question_engine.js.md)

Initialise a form that contains questions printed using print_question.
This has the effect of:

- Turning off browser autocomlete.

- Stopping enter from submitting the form (or toggling the next flag) unless
keyboard focus is on the submit button or the flag.

- Removes any '.questionflagsavebutton's, since we have JavaScript to toggle
the flags using ajax.

- Scroll to the position indicated by scrollpos= in the URL, if it is there.

- Prevent the user from repeatedly submitting the form.

 

#### (static, constant) initSubmitButton

 

**Description:
 :** 

- 

Initialise a question submit button. This saves the scroll position and
sets the fragment on the form submit URL so the page reloads in the right place.

 

**Source:
 :** 

- 
 [question/amd/src/question_engine.js](question_amd_src_question_engine.js.md), [line 33](question_amd_src_question_engine.js.md)

Initialise a question submit button. This saves the scroll position and
sets the fragment on the form submit URL so the page reloads in the right place.

 

#### (static, constant) preventRepeatSubmission

 

**Description:
 :** 

- 

Event handler to stop a question form being submitted more than once.

 

**Source:
 :** 

- 
 [question/amd/src/question_engine.js](question_amd_src_question_engine.js.md), [line 93](question_amd_src_question_engine.js.md)

Event handler to stop a question form being submitted more than once.
