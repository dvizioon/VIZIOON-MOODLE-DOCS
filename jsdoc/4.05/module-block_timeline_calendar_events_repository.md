# block_timeline/calendar_events_repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-block_timeline_calendar_events_repository.html

# block_timeline/calendar_events_repository

 

 

 

**Description:
 :** 

- 

A javascript module to retrieve calendar events from the server.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/calendar_events_repository.js](blocks_timeline_amd_src_calendar_events_repository.js.md), [line 16](blocks_timeline_amd_src_calendar_events_repository.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to retrieve calendar events from the server.

 

 

 

 

### Methods

 

#### (inner) queryByCourse(args) → {promise}

 

**Description:
 :** 

- 

Retrieve a list of calendar events for the logged in user for the
given course.

Valid args are:
int courseid Only get events for this course
int starttime Only get events after this time
int endtime Only get events before this time
int limit Limit the number of results returned
int aftereventid Offset the result set from the given id

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/calendar_events_repository.js](blocks_timeline_amd_src_calendar_events_repository.js.md), [line 27](blocks_timeline_amd_src_calendar_events_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

The request arguments

 

##### Returns:

Resolved with an array of the calendar events

**
 Type

 :** 

promise

 

#### (inner) queryByCourses(args) → {promise}

 

**Description:
 :** 

- 

Retrieve a list of calendar events for the given courses for the
logged in user.

Valid args are:
array courseids Get events for these courses
int starttime Only get events after this time
int endtime Only get events before this time
int limit Limit the number of results returned

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/calendar_events_repository.js](blocks_timeline_amd_src_calendar_events_repository.js.md), [line 72](blocks_timeline_amd_src_calendar_events_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

The request arguments

 

##### Returns:

Resolved with an array of the calendar events

**
 Type

 :** 

promise

 

#### (inner) queryByTime(args) → {promise}

 

**Description:
 :** 

- 

Retrieve a list of calendar events for the logged in user after the given
time.

Valid args are:
int starttime Only get events after this time
int endtime Only get events before this time
int limit Limit the number of results returned
int aftereventid Offset the result set from the given id

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/calendar_events_repository.js](blocks_timeline_amd_src_calendar_events_repository.js.md), [line 117](blocks_timeline_amd_src_calendar_events_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

The request arguments

 

##### Returns:

Resolved with an array of the calendar events

**
 Type

 :** 

promise
