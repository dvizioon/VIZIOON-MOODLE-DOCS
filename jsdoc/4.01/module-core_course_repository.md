# core_course/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_course_repository.html

# core_course/repository

 

 

 

**Description:
 :** 

- 

A javascript module to handle course ajax actions.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 16](course_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle course ajax actions.

 

 

 

 

### Methods

 

#### (inner) activityModules(courseid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 24](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the modules for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) favouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 41](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) fetchFooterData(courseid, sectionid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 81](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the data for

 
 `sectionid`

 

Number

 

What section to fetch the data for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) getEnrolledCoursesByTimelineClassification(classification, limit, offset, sort) → {object}

 

**Description:
 :** 

- 

Get the list of courses that the logged in user is enrolled in for a given
timeline classification.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 36](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `classification`

 

string

 

past, inprogress, or future

 
 `limit`

 

int

 

Only return this many results

 
 `offset`

 

int

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

Column to sort by and direction, e.g. 'shortname asc'

 

##### Returns:

jQuery promise resolved with courses.

**
 Type

 :** 

object

 

#### (inner) getEnrolledCoursesWithEventsByTimelineClassification(classification, limit, offset, sort, searchValue, eventsFrom, eventsTo) → {object}

 

**Description:
 :** 

- 

Get a list of courses that the logged in user is enrolled in, where they have at least one action event,
for a given timeline classification.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 74](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `classification`

 

string

 

 

 

past, inprogress, or future

 
 `limit`

 

int

 

 

 `0`

 

The maximum number of courses to return

 
 `offset`

 

int

 

 

 `0`

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

 

 `null`

 

Column to sort by and direction, e.g. 'shortname asc'

 
 `searchValue`

 

string

 

 

 `null`

 

Optional text search value

 
 `eventsFrom`

 

int

 

 

 `null`

 

Optional start timestamp (inclusive) that the course should have event(s) in

 
 `eventsTo`

 

int

 

 

 `null`

 

Optional end timestamp (inclusive) that the course should have event(s) in

 

##### Returns:

jQuery promise resolved with courses.

**
 Type

 :** 

object

 

#### (inner) getEnrolledUsersFromCourseModuleID(cmid, groupID, onlyActive) → {Promise}

 

**Description:
 :** 

- 

Get the list of users enrolled in this cmid.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 140](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `cmid`

 

Number

 

 

 

Course Module from which the users will be obtained

 
 `groupID`

 

Number

 

 

 

Group ID from which the users will be obtained

 
 `onlyActive`

 

Boolean

 

 

 `false`

 

Whether to fetch only the active enrolled users or all enrolled users in the course.

 

##### Returns:

Promise containing a list of users

**
 Type

 :** 

Promise

 

#### (inner) getGradabaleUsersFromCourseID(courseid, groupID, onlyActive) → {Promise}

 

**Description:
 :** 

- 

Get the list of gradable users enrolled in this course.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 161](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `courseid`

 

Number

 

 

 

Course ID from which the users will be obtained

 
 `groupID`

 

Number

 

 

 

Group ID from which the users will be obtained

 
 `onlyActive`

 

Boolean

 

 

 `false`

 

Whether to fetch only the active enrolled users or all enrolled users in the course.

 

##### Returns:

Promise containing a list of users

**
 Type

 :** 

Promise

 

#### (inner) getLastAccessedCourses(userid, limit, offset, sort) → {promise}

 

**Description:
 :** 

- 

Get the list of courses that the user has most recently accessed.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 95](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userid`

 

int

 

User from which the courses will be obtained

 
 `limit`

 

int

 

Only return this many results

 
 `offset`

 

int

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

Column to sort by and direction, e.g. 'shortname asc'

 

##### Returns:

Resolved with an array of courses

**
 Type

 :** 

promise

 

#### (inner) toggleManualCompletion(cmid, completed) → {object}

 

**Description:
 :** 

- 

Toggle the completion state of an activity with manual completion.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 181](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

Number

 

The course module ID.

 
 `completed`

 

Boolean

 

Whether to set as complete or not.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) unfavouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is no longer a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 61](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

 

 

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 16](course_amd_src_local_activitychooser_repository.js.md)

 

**Copyright:
 :** 

- 2019 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

 

 

 

### Methods

 

#### (inner) activityModules(courseid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 24](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the modules for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) favouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 41](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) fetchFooterData(courseid, sectionid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 81](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the data for

 
 `sectionid`

 

Number

 

What section to fetch the data for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) getEnrolledCoursesByTimelineClassification(classification, limit, offset, sort) → {object}

 

**Description:
 :** 

- 

Get the list of courses that the logged in user is enrolled in for a given
timeline classification.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 36](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `classification`

 

string

 

past, inprogress, or future

 
 `limit`

 

int

 

Only return this many results

 
 `offset`

 

int

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

Column to sort by and direction, e.g. 'shortname asc'

 

##### Returns:

jQuery promise resolved with courses.

**
 Type

 :** 

object

 

#### (inner) getEnrolledCoursesWithEventsByTimelineClassification(classification, limit, offset, sort, searchValue, eventsFrom, eventsTo) → {object}

 

**Description:
 :** 

- 

Get a list of courses that the logged in user is enrolled in, where they have at least one action event,
for a given timeline classification.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 74](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `classification`

 

string

 

 

 

past, inprogress, or future

 
 `limit`

 

int

 

 

 `0`

 

The maximum number of courses to return

 
 `offset`

 

int

 

 

 `0`

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

 

 `null`

 

Column to sort by and direction, e.g. 'shortname asc'

 
 `searchValue`

 

string

 

 

 `null`

 

Optional text search value

 
 `eventsFrom`

 

int

 

 

 `null`

 

Optional start timestamp (inclusive) that the course should have event(s) in

 
 `eventsTo`

 

int

 

 

 `null`

 

Optional end timestamp (inclusive) that the course should have event(s) in

 

##### Returns:

jQuery promise resolved with courses.

**
 Type

 :** 

object

 

#### (inner) getEnrolledUsersFromCourseModuleID(cmid, groupID, onlyActive) → {Promise}

 

**Description:
 :** 

- 

Get the list of users enrolled in this cmid.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 140](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `cmid`

 

Number

 

 

 

Course Module from which the users will be obtained

 
 `groupID`

 

Number

 

 

 

Group ID from which the users will be obtained

 
 `onlyActive`

 

Boolean

 

 

 `false`

 

Whether to fetch only the active enrolled users or all enrolled users in the course.

 

##### Returns:

Promise containing a list of users

**
 Type

 :** 

Promise

 

#### (inner) getGradabaleUsersFromCourseID(courseid, groupID, onlyActive) → {Promise}

 

**Description:
 :** 

- 

Get the list of gradable users enrolled in this course.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 161](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `courseid`

 

Number

 

 

 

Course ID from which the users will be obtained

 
 `groupID`

 

Number

 

 

 

Group ID from which the users will be obtained

 
 `onlyActive`

 

Boolean

 

 

 `false`

 

Whether to fetch only the active enrolled users or all enrolled users in the course.

 

##### Returns:

Promise containing a list of users

**
 Type

 :** 

Promise

 

#### (inner) getLastAccessedCourses(userid, limit, offset, sort) → {promise}

 

**Description:
 :** 

- 

Get the list of courses that the user has most recently accessed.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 95](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userid`

 

int

 

User from which the courses will be obtained

 
 `limit`

 

int

 

Only return this many results

 
 `offset`

 

int

 

Skip this many results from the start of the result set

 
 `sort`

 

string

 

Column to sort by and direction, e.g. 'shortname asc'

 

##### Returns:

Resolved with an array of courses

**
 Type

 :** 

promise

 

#### (inner) toggleManualCompletion(cmid, completed) → {object}

 

**Description:
 :** 

- 

Toggle the completion state of an activity with manual completion.

 

**Source:
 :** 

- 
 [course/amd/src/repository.js](course_amd_src_repository.js.md), [line 181](course_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

Number

 

The course module ID.

 
 `completed`

 

Boolean

 

Whether to set as complete or not.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) unfavouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is no longer a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 61](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
