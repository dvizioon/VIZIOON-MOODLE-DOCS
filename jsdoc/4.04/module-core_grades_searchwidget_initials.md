# core_grades/searchwidget/initials - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_grades_searchwidget_initials.html

# core_grades/searchwidget/initials

 

 

 

**Description:
 :** 

- 

A small dropdown to filter users within the gradebook.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 16](grade_amd_src_searchwidget_initials.js.md)

 

**Copyright:
 :** 

- 2022 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A small dropdown to filter users within the gradebook.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Our initial hook into the module which will eventually allow us to handle the dropdown initials bar form.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 61](grade_amd_src_searchwidget_initials.js.md)

Our initial hook into the module which will eventually allow us to handle the dropdown initials bar form.

 

#### (inner) registered :boolean

 

**Description:
 :** 

- 

Whether the event listener has already been registered for this module.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 34](grade_amd_src_searchwidget_initials.js.md)

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
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 152](grade_amd_src_searchwidget_initials.js.md)

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) registerListenerEvents(callingLink, gpr_userid, gpr_search)

 

**Description:
 :** 

- 

Register event listeners.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 82](grade_amd_src_searchwidget_initials.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `callingLink`

 

String

 

 

 

The link to redirect upon form submission.

 
 `gpr_userid`

 

Null
|

Number

 

 

 `null`

 

The user id to filter by.

 
 `gpr_search`

 

Null
|

String

 

 

 `null`

 

The search value to filter by.

 

 

#### (inner) swapActiveItems(itemToReset, e)

 

**Description:
 :** 

- 

Given we are provided the old li and current click event, swap around the active properties.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/initials.js](grade_amd_src_searchwidget_initials.js.md), [line 170](grade_amd_src_searchwidget_initials.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `itemToReset`

 

HTMLElement

 

 

 
 `e`

 

Event
