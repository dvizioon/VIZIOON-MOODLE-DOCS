# core_calendar/view_manager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_calendar_view_manager.html

# core_calendar/view_manager

 

 

 

**Description:
 :** 

- 

A javascript module to handler calendar view changes.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 16](calendar_amd_src_view_manager.js.md)

 

**Copyright:
 :** 

- 2017 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handler calendar view changes.

 

 

 

 

### Members

 

#### (static, constant) changeDay

 

**Description:
 :** 

- 

Handle changes to the current calendar view.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 406](calendar_amd_src_view_manager.js.md)

Handle changes to the current calendar view.

 

#### (static, constant) changeMonth

 

**Description:
 :** 

- 

Handle changes to the current calendar view.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 293](calendar_amd_src_view_manager.js.md)

Handle changes to the current calendar view.

 

#### (static, constant) foldDayEvents

 

**Description:
 :** 

- 

Hide day events if more than 5.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 48](calendar_amd_src_view_manager.js.md)

Hide day events if more than 5.

 

#### (static, constant) refreshDayContent

 

**Description:
 :** 

- 

Refresh the day content.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 345](calendar_amd_src_view_manager.js.md)

Refresh the day content.

 

#### (static, constant) refreshMonthContent

 

**Description:
 :** 

- 

Refresh the month content.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 254](calendar_amd_src_view_manager.js.md)

Refresh the month content.

 

#### (static, constant) registerEventListenersForMonthDetailed

 

**Description:
 :** 

- 

Register and handle month calendar events.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 109](calendar_amd_src_view_manager.js.md)

Register and handle month calendar events.

 

#### (static, constant) reloadCurrentDay

 

**Description:
 :** 

- 

Reload the current day view data.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 382](calendar_amd_src_view_manager.js.md)

Reload the current day view data.

 

#### (static, constant) reloadCurrentMonth

 

**Description:
 :** 

- 

Reload the current month view data.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 315](calendar_amd_src_view_manager.js.md)

Reload the current month view data.

 

#### (static, constant) reloadCurrentUpcoming

 

**Description:
 :** 

- 

Reload the current month view data.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 468](calendar_amd_src_view_manager.js.md)

Reload the current month view data.

 

#### (static, constant) updateUrl

 

**Description:
 :** 

- 

Update calendar URL.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 425](calendar_amd_src_view_manager.js.md)

Update calendar URL.

 

#### (inner, constant) LIMIT_DAY_EVENTS

 

**Description:
 :** 

- 

Limit number of events per day

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 42](calendar_amd_src_view_manager.js.md)

Limit number of events per day

 

 

### Methods

 

#### (inner) getEventTypeClassFromType(eventType) → {string}

 

**Description:
 :** 

- 

Get the CSS class to apply for the given event type.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 501](calendar_amd_src_view_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventType`

 

string

 

The calendar event type

 

##### Returns:

**
 Type

 :** 

string

 

#### (inner) registerEventListeners(root)

 

**Description:
 :** 

- 

Register event listeners for the module.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 148](calendar_amd_src_view_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element.

 

 

#### (inner) renderEventSummaryModal(eventId) → {Promise}

 

**Description:
 :** 

- 

Render the event summary modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 511](calendar_amd_src_view_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventId`

 

Number

 

The calendar event id.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) startLoading(root)

 

**Description:
 :** 

- 

Set the element state to loading.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 434](calendar_amd_src_view_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element

 

 

#### (inner) stopLoading(root)

 

**Description:
 :** 

- 

Remove the loading state from the element.

 

**Source:
 :** 

- 
 [calendar/amd/src/view_manager.js](calendar_amd_src_view_manager.js.md), [line 446](calendar_amd_src_view_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element
