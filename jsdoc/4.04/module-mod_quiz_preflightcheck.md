# mod_quiz/preflightcheck - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_quiz_preflightcheck.html

# mod_quiz/preflightcheck

 

 

 

**Description:
 :** 

- 

This class manages the confirmation pop-up (also called the pre-flight check)
that is sometimes shown when a use clicks the start attempt button.

This is also responsible for opening the pop-up window, if the quiz requires to be in one.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/preflightcheck.js](mod_quiz_amd_src_preflightcheck.js.md), [line 16](mod_quiz_amd_src_preflightcheck.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2016 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This class manages the confirmation pop-up (also called the pre-flight check)
that is sometimes shown when a use clicks the start attempt button.

This is also responsible for opening the pop-up window, if the quiz requires to be in one.

 

 

 

 

### Methods

 

#### (static) displayDialogue(e)

 

**Description:
 :** 

- 

Display the dialogue.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/preflightcheck.js](mod_quiz_amd_src_preflightcheck.js.md), [line 75](mod_quiz_amd_src_preflightcheck.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Y.EventFacade

 

the event being responded to, if any.

 

 

#### (static) hideDialogue(e)

 

**Description:
 :** 

- 

Hide the dialogue.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/preflightcheck.js](mod_quiz_amd_src_preflightcheck.js.md), [line 86](mod_quiz_amd_src_preflightcheck.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Y.EventFacade

 

the event being responded to, if any.

 

 

#### (static) init(startButton, confirmationTitle, confirmationForm, popupoptions)

 

**Description:
 :** 

- 

Initialise the start attempt button.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/preflightcheck.js](mod_quiz_amd_src_preflightcheck.js.md), [line 43](mod_quiz_amd_src_preflightcheck.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `startButton`

 

String

 

the id of the start attempt button that we will be enhancing.

 
 `confirmationTitle`

 

String

 

the title of the dialogue.

 
 `confirmationForm`

 

String

 

selector for the confirmation form to show in the dialogue.

 
 `popupoptions`

 

String

 

If not null, the quiz should be launced in a pop-up.

 

 

#### (static) launchQuizPopup(e, popupoptions)

 

**Description:
 :** 

- 

Event handler for the quiz start attempt button.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/preflightcheck.js](mod_quiz_amd_src_preflightcheck.js.md), [line 98](mod_quiz_amd_src_preflightcheck.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

the event being responded to

 
 `popupoptions`

 

Object
