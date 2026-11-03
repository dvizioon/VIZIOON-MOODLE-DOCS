# core_course/manual_completion_toggle - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_course_manual_completion_toggle.html

# core_course/manual_completion_toggle

 

 

 

**Description:
 :** 

- 

Provides the functionality for toggling the manual completion state of a course module through
the manual completion button.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 16](course_amd_src_manual_completion_toggle.js.md)

 

**Copyright:
 :** 

- 2021 Jun Pataleta 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Provides the functionality for toggling the manual completion state of a course module through
the manual completion button.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Registers the click event listener for the manual completion toggle button.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 60](course_amd_src_manual_completion_toggle.js.md)

Registers the click event listener for the manual completion toggle button.

 

#### (inner, constant) SELECTORS :Object

 

**Description:
 :** 

- 

Selectors in the manual completion template.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 36](course_amd_src_manual_completion_toggle.js.md)

Selectors in the manual completion template.

##### Type:

- 

Object

 

 

#### (inner, constant) TOGGLE_TYPES :Object

 

**Description:
 :** 

- 

Toggle type values for the data-toggletype attribute in the core_course/completion_manual template.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 45](course_amd_src_manual_completion_toggle.js.md)

Toggle type values for the data-toggletype attribute in the core_course/completion_manual template.

##### Type:

- 

Object

 

 

#### (inner) registered :boolean

 

**Description:
 :** 

- 

Whether the event listener has already been registered for this module.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 55](course_amd_src_manual_completion_toggle.js.md)

Whether the event listener has already been registered for this module.

##### Type:

- 

boolean

 

 

 

### Methods

 

#### (async, inner) toggleManualCompletionState(toggleButton) → {Promise.<void>}

 

**Description:
 :** 

- 

Toggles the manual completion state of the module for the given user.

 

**Source:
 :** 

- 
 [course/amd/src/manual_completion_toggle.js](course_amd_src_manual_completion_toggle.js.md), [line 80](course_amd_src_manual_completion_toggle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleButton`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<void>
