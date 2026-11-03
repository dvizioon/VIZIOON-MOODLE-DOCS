# core_calendar/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_calendar_repository.html

# core_calendar/repository

 

 

 

**Description:
 :** 

- 

A javascript module to handle calendar ajax actions.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 16](calendar_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2017 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle calendar ajax actions.

 

 

 

 

### Members

 

#### (static, constant) deleteSubscription

 

**Description:
 :** 

- 

Delete calendar subscription by id.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 206](calendar_amd_src_repository.js.md)

Delete calendar subscription by id.

 

#### (static, constant) getCourseGroupsData

 

**Description:
 :** 

- 

Get the groups by course id.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 189](calendar_amd_src_repository.js.md)

Get the groups by course id.

 

#### (static, constant) updateEventStartDay

 

**Description:
 :** 

- 

Change the start day for the given event id. The day timestamp
only has to be any time during the target day because only the
date information is extracted, the time of the day is ignored.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 151](calendar_amd_src_repository.js.md)

Change the start day for the given event id. The day timestamp
only has to be any time during the target day because only the
date information is extracted, the time of the day is ignored.

 

 

### Methods

 

#### (inner) deleteEvent(eventId, deleteSeries) → {promise}

 

**Description:
 :** 

- 

Delete a calendar event.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 25](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventId`

 

number

 

The event id.

 
 `deleteSeries`

 

boolean

 

Whether to delete all events in the series

 

##### Returns:

Resolved with requested calendar event

**
 Type

 :** 

promise

 

#### (inner) getCalendarDayData(year, month, day, courseId, categoryId) → {promise}

 

**Description:
 :** 

- 

Get calendar data for the day view.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 116](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `year`

 

number

 

Year

 
 `month`

 

number

 

Month

 
 `day`

 

number

 

Day

 
 `courseId`

 

number

 

The course id.

 
 `categoryId`

 

number

 

The id of the category whose events are shown

 

##### Returns:

Resolved with the day view data.

**
 Type

 :** 

promise

 

#### (inner) getCalendarMonthData(year, month, courseId, categoryId, includeNavigation, mini, day, view) → {promise}

 

**Description:
 :** 

- 

Get calendar data for the month view.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 84](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `year`

 

number

 

Year

 
 `month`

 

number

 

Month

 
 `courseId`

 

number

 

The course id.

 
 `categoryId`

 

number

 

The category id.

 
 `includeNavigation`

 

boolean

 

Whether to include navigation.

 
 `mini`

 

boolean

 

Whether the month is in mini view.

 
 `day`

 

number

 

Day (optional)

 
 `view`

 

string

 

The calendar view mode.

 

##### Returns:

Resolved with the month view data.

**
 Type

 :** 

promise

 

#### (inner) getCalendarUpcomingData(courseId, categoryId) → {promise}

 

**Description:
 :** 

- 

Get calendar upcoming data.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 163](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

number

 

The course id.

 
 `categoryId`

 

number

 

The category id.

 

##### Returns:

Resolved with the month view data.

**
 Type

 :** 

promise

 

#### (inner) getEventById(eventId) → {promise}

 

**Description:
 :** 

- 

Get a calendar event by id.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 47](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventId`

 

number

 

The event id.

 

##### Returns:

Resolved with requested calendar event

**
 Type

 :** 

promise

 

#### (inner) submitCreateUpdateForm(formData) → {promise}

 

**Description:
 :** 

- 

Submit the form data for the event form.

 

**Source:
 :** 

- 
 [calendar/amd/src/repository.js](calendar_amd_src_repository.js.md), [line 66](calendar_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formData`

 

string

 

The URL encoded values from the form

 

##### Returns:

Resolved with the new or edited event

**
 Type

 :** 

promise
