# core_course/actionbar/initials - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_actionbar_initials.html

# core_course/actionbar/initials

 

 

 

**Description:
 :** 

- 

A small dropdown to filter users.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 16](course_amd_src_actionbar_initials.js.md)

 

**Copyright:
 :** 

- 2022 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A small dropdown to filter users.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Our initial hook into the module which will eventually allow us to handle the dropdown initials bar form.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 62](course_amd_src_actionbar_initials.js.md)

Our initial hook into the module which will eventually allow us to handle the dropdown initials bar form.

 

#### (inner) registered :boolean

 

**Description:
 :** 

- 

Whether the event listener has already been registered for this module.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 34](course_amd_src_actionbar_initials.js.md)

Whether the event listener has already been registered for this module.

##### Type:

- 

boolean

 

 

 

### Methods

 

#### (inner) onClickVariables() → {Object}

 

**Description:
 :** 

- 

A small abstracted helper function which allows us to ensure we have up-to-date lists of nodes.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 157](course_amd_src_actionbar_initials.js.md)

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) registerListenerEvents(callingLink, firstInitialParam, lastInitialParam, additionalParams)

 

**Description:
 :** 

- 

Register event listeners.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 85](course_amd_src_actionbar_initials.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `callingLink`

 

String

 

 

 

The link to redirect upon form submission.

 
 `firstInitialParam`

 

String

 

 

 `sifirst`

 

The URL parameter to set for the first name initial.

 
 `lastInitialParam`

 

String

 

 

 `silast`

 

The URL parameter to set for the last name initial.

 
 `additionalParams`

 

Array

 

 

 

Any additional parameters to set for the URL.

 

 

#### (inner) swapActiveItems(itemToReset, e)

 

**Description:
 :** 

- 

Given we are provided the old li and current click event, swap around the active properties.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/initials.js](course_amd_src_actionbar_initials.js.md), [line 175](course_amd_src_actionbar_initials.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `itemToReset`

 

HTMLElement

 

 

 
 `e`

 

Event
