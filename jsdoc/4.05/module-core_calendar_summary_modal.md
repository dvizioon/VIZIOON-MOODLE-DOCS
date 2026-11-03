# core_calendar/summary_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_calendar_summary_modal.html

# core_calendar/summary_modal

 

 

 

**Description:
 :** 

- 

A javascript module to handle summary modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 16](calendar_amd_src_summary_modal.js.md)

 

**Copyright:
 :** 

- 2017 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle summary modal.

 

 

 

 

### Methods

 

#### (inner) getDeleteButton() → {object}

 

**Description:
 :** 

- 

Get the delete button element from the footer. The button is cached
as it's not expected to change.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 56](calendar_amd_src_summary_modal.js.md)

##### Returns:

button element

**
 Type

 :** 

object

 

#### (inner) getEditButton() → {object}

 

**Description:
 :** 

- 

Get the edit button element from the footer. The button is cached
as it's not expected to change.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 41](calendar_amd_src_summary_modal.js.md)

##### Returns:

button element

**
 Type

 :** 

object

 

#### (inner) getEventCount() → {int}

 

**Description:
 :** 

- 

Get the number of events in the series for the event being shown in
this modal. This value is not cached because it will change
depending on which event is being displayed.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 95](calendar_amd_src_summary_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getEventId() → {int}

 

**Description:
 :** 

- 

Get the id for the event being shown in this modal. This value is
not cached because it will change depending on which event is
being displayed.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 71](calendar_amd_src_summary_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getEventTitle() → {String}

 

**Description:
 :** 

- 

Get the title for the event being shown in this modal. This value is
not cached because it will change depending on which event is
being displayed.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 83](calendar_amd_src_summary_modal.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getEventUrl() → {String}

 

**Description:
 :** 

- 

Get the url for the event being shown in this modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 107](calendar_amd_src_summary_modal.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getEventUrl() → {String}

 

**Description:
 :** 

- 

Is this an action event.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 117](calendar_amd_src_summary_modal.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/summary_modal.js](calendar_amd_src_summary_modal.js.md), [line 127](calendar_amd_src_summary_modal.js.md)
