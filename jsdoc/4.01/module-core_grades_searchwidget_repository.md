# core_grades/searchwidget/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_grades_searchwidget_repository.html

# core_grades/searchwidget/repository

 

 

 

**Description:
 :** 

- 

A repo for the search widget.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/repository.js](grade_amd_src_searchwidget_repository.js.md), [line 16](grade_amd_src_searchwidget_repository.js.md)

 

**Copyright:
 :** 

- 2022 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A repo for the search widget.

 

 

 

 

### Methods

 

#### (inner) gradeitemFetch(courseid) → {object}

 

**Description:
 :** 

- 

Given a course ID, we want to fetch the gradable items, so we may fetch reports based on activity items.
Note: This will be worked upon in the single view issue.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/repository.js](grade_amd_src_searchwidget_repository.js.md), [line 66](grade_amd_src_searchwidget_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

ID of the course to fetch the users of.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) groupFetch(courseid, actionBaseUrl) → {object}

 

**Description:
 :** 

- 

Given a course ID, we want to fetch the groups, so we may fetch their users.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/repository.js](grade_amd_src_searchwidget_repository.js.md), [line 47](grade_amd_src_searchwidget_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

ID of the course to fetch the users of.

 
 `actionBaseUrl`

 

string

 

The base URL for the group action.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) userFetch(courseid, actionBaseUrl, groupId) → {object}

 

**Description:
 :** 

- 

Given a course ID, we want to fetch the enrolled learners, so we may fetch their reports.

 

**Source:
 :** 

- 
 [grade/amd/src/searchwidget/repository.js](grade_amd_src_searchwidget_repository.js.md), [line 26](grade_amd_src_searchwidget_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

ID of the course to fetch the users of.

 
 `actionBaseUrl`

 

string

 

The base URL for the user option.

 
 `groupId`

 

int

 

ID of the group to fetch the users of.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
