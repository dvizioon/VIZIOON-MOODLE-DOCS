# core_calendar/calendar - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_calendar_calendar.html

# core_calendar/calendar

 

 

 

**Description:
 :** 

- 

This module is the highest level module for the calendar. It is
responsible for initialising all of the components required for
the calendar to run. It also coordinates the interaction between
components by listening for and responding to different events
triggered within the calendar UI.

 

**Source:
 :** 

- 
 [calendar/amd/src/calendar.js](calendar_amd_src_calendar.js.md), [line 16](calendar_amd_src_calendar.js.md)

 

**Copyright:
 :** 

- 2017 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module is the highest level module for the calendar. It is
responsible for initialising all of the components required for
the calendar to run. It also coordinates the interaction between
components by listening for and responding to different events
triggered within the calendar UI.

 

 

 

 

### Methods

 

#### (inner) init(root, isCalendarBlockopt)

 

**Description:
 :** 

- 

Initializes the calendar view manager and registers event listeners.

 

**Source:
 :** 

- 
 [calendar/amd/src/calendar.js](calendar_amd_src_calendar.js.md), [line 278](calendar_amd_src_calendar.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `root`

 

HTMLElement

 

 

 

 

 

The root element where the calendar view manager and event listeners will be attached.

 
 `isCalendarBlock`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

A flag indicating whether this is a calendar block.

 

 

#### (inner) registerCalendarEventListeners(root, eventFormModalPromise)

 

**Description:
 :** 

- 

Listen to and handle any calendar events fired by the calendar UI.

 

**Source:
 :** 

- 
 [calendar/amd/src/calendar.js](calendar_amd_src_calendar.js.md), [line 129](calendar_amd_src_calendar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The calendar root element

 
 `eventFormModalPromise`

 

object

 

A promise reolved with the event form modal
