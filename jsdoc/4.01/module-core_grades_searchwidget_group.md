# core_grades/searchwidget/group - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_grades_searchwidget_group.html

# core_grades/searchwidget/group

 

 

 

**Description:
 :** 

- 

A widget to search groups within the gradebook.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/group.js](grade_amd_src_searchwidget_group.js.md), [line 16](grade_amd_src_searchwidget_group.js.md)

 

**Copyright:
 :** 

- 2022 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A widget to search groups within the gradebook.

 

 

 

 

### Members

 

#### (inner) registered :boolean

 

**Description:
 :** 

- 

Whether the event listener has already been registered for this module.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/group.js](grade_amd_src_searchwidget_group.js.md), [line 36](grade_amd_src_searchwidget_group.js.md)

Whether the event listener has already been registered for this module.

##### Type:

- 

boolean

 

 

 

### Methods

 

#### (inner) init()

 

**Description:
 :** 

- 

Our entry point into starting to build the group search widget.

It'll eventually, based upon the listeners, open the search widget and allow filtering.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/group.js](grade_amd_src_searchwidget_group.js.md), [line 38](grade_amd_src_searchwidget_group.js.md)

 

#### (inner) registerListenerEvents()

 

**Description:
 :** 

- 

Register event listeners.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/group.js](grade_amd_src_searchwidget_group.js.md), [line 55](grade_amd_src_searchwidget_group.js.md)

 

#### (inner) registerListenerEvents() → {function}

 

**Description:
 :** 

- 

Define how we want to search and filter groups when the user decides to input a search value.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/group.js](grade_amd_src_searchwidget_group.js.md), [line 105](grade_amd_src_searchwidget_group.js.md)

##### Returns:

**
 Type

 :** 

function
