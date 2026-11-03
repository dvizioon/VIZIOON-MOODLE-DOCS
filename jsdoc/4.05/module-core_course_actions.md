# core_course/actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_actions.html

# core_course/actions

 

 

 

**Description:
 :** 

- 

Various actions on modules and sections in the editing mode - hiding, duplicating, deleting, etc.

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 16](course_amd_src_actions.js.md)

 

**Since:
 :** 

- 3.3

 

**Copyright:
 :** 

- 2016 Marina Glancy

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Various actions on modules and sections in the editing mode - hiding, duplicating, deleting, etc.

 

 

 

 

### Methods

 

#### (static) replaceSectionActionItem(sectionelement, selector, image, stringname, stringcomponent, newaction)

 

**Description:
 :** 

- 

Replaces a section action menu item with another one (for example Show->Hide, Set marker->Remove marker)

This method can be used by course formats in their listener to the coursesectionedited event

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 1086](course_amd_src_actions.js.md)

 

**Deprecated::** 

- since Moodle 3.9

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionelement`

 

JQuery

 

 

 
 `selector`

 

String

 

CSS selector inside the section element, for example "a[data-action=show]"

 
 `image`

 

String

 

new image name ("i/show", "i/hide", etc.)

 
 `stringname`

 

String

 

new string for the action menu item

 
 `stringcomponent`

 

String

 

 

 
 `newaction`

 

String

 

new value for data-action attribute of the link

 

 

#### (inner) dispatchEvent(eventName, detail, container, options) → {CustomEvent}

 

**Description:
 :** 

- 

Dispatch event wrapper.

Old jQuery events will be replaced by native events gradually.

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 103](course_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventName`

 

String

 

The name of the event

 
 `detail`

 

Object

 

Any additional details to pass into the eveent

 
 `container`

 

Node
|

HTMLElement

 

The point at which to dispatch the event

 
 `options`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `bubbles`

 

Boolean

 

Whether to bubble up the DOM

 
 `cancelable`

 

Boolean

 

Whether preventDefault() can be called

 
 `composed`

 

Boolean

 

Whether the event can bubble across the ShadowDOM boundary

 

 

 

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (inner) init(courseformat)

 

**Description:
 :** 

- 

Initialises course page

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 913](course_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseformat`

 

String

 

name of the current course format (for fetching strings)

 

 

#### (inner) legacyActivityAction(statemanager, action, cmid, affectedids)

 

**Description:
 :** 

- 

Compatibility function to update Moodle 4.0 course state using legacy actions.

This method only updates some actions which does not require to use cmState mutation
to get updated data form the server.

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 825](course_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `statemanager`

 

Object

 

the current state in read write mode

 
 `action`

 

String

 

the performed action

 
 `cmid`

 

Number

 

the affected course module id

 
 `affectedids`

 

Array

 

all affected cm ids (for duplicate action)

 

 

#### (inner) updateMovedCmState(params)

 

**Description:
 :** 

- 

Update the course state when some cm is moved via YUI.

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 786](course_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

*

 

 

 

 

#### (inner) updateMovedSectionState()

 

**Description:
 :** 

- 

Update the course state when some section is moved via YUI.

 

**Source:
 :** 

- 
 [course/amd/src/actions.js](course_amd_src_actions.js.md), [line 800](course_amd_src_actions.js.md)
