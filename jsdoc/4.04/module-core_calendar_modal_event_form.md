# module:core_calendar/modal_event_form - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_calendar_modal_event_form.html

# module:core_calendar/modal_event_form

 

## 

 module:core_calendar/modal_event_form

 

 

 

 

#### new (require("core_calendar/modal_event_form"))(root)

 

**Description:
 :** 

- 

Constructor for the Modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 48](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root jQuery element for the modal

 

 

 

 

### Methods

 

#### (inner) disableButtons()

 

**Description:
 :** 

- 

Disable the buttons in the footer.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 216](calendar_amd_src_modal_event_form.js.md)

 

#### (inner) enableButtons()

 

**Description:
 :** 

- 

Enable the buttons in the footer.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 225](calendar_amd_src_modal_event_form.js.md)

 

#### (inner) getCategoryId() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current category id, if any.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 116](calendar_amd_src_modal_event_form.js.md)

##### Returns:

The event id

**
 Type

 :** 

Number
|

null

 

#### (inner) getContextId() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current context id, if any.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 76](calendar_amd_src_modal_event_form.js.md)

##### Returns:

The event id

**
 Type

 :** 

Number
|

null

 

#### (inner) getCourseId() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current course id, if any.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 96](calendar_amd_src_modal_event_form.js.md)

##### Returns:

The event id

**
 Type

 :** 

Number
|

null

 

#### (inner) getEventId() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current event id, if any.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 156](calendar_amd_src_modal_event_form.js.md)

##### Returns:

The event id

**
 Type

 :** 

Number
|

null

 

#### (inner) getForm() → {object}

 

**Description:
 :** 

- 

Get the form element from the modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 206](calendar_amd_src_modal_event_form.js.md)

##### Returns:

**
 Type

 :** 

object

 

#### (inner) getFormData() → {string}

 

**Description:
 :** 

- 

Get the serialised form data.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 371](calendar_amd_src_modal_event_form.js.md)

##### Returns:

serialised form data

**
 Type

 :** 

string

 

#### (inner) getStartTime() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current start time, if any.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 186](calendar_amd_src_modal_event_form.js.md)

##### Returns:

The start time

**
 Type

 :** 

Number
|

null

 

#### (inner) hasCategoryId() → {bool}

 

**Description:
 :** 

- 

Check if the modal has an category id.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 136](calendar_amd_src_modal_event_form.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hasCourseId() → {bool}

 

**Description:
 :** 

- 

Check if the modal has an course id.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 126](calendar_amd_src_modal_event_form.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hasEventId() → {bool}

 

**Description:
 :** 

- 

Check if the modal has an event id.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 166](calendar_amd_src_modal_event_form.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hasStartTime() → {bool}

 

**Description:
 :** 

- 

Check if the modal has start time.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 196](calendar_amd_src_modal_event_form.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hide()

 

**Description:
 :** 

- 

Clear the event id from the modal when it's closed so
that it is loaded fresh next time it's displayed.

The event id will be set by the calling code if it wants
to edit a specific event.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 354](calendar_amd_src_modal_event_form.js.md)

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 449](calendar_amd_src_modal_event_form.js.md)

##### Fires:

- event:uploadStarted

- event:formSubmittedByJavascript

 

#### (inner) reloadAllContent() → {object}

 

**Description:
 :** 

- 

Reload both the title and body content.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 328](calendar_amd_src_modal_event_form.js.md)

##### Returns:

promise

**
 Type

 :** 

object

 

#### (inner) reloadBodyContent(formData) → {object}

 

**Description:
 :** 

- 

Send a request to the server to get the event_form in a fragment
and render the result in the body of the modal.

If serialised form data is provided then it will be sent in the
request to the server to have the form rendered with the data. This
is used when the form had a server side error and we need the server
to re-render it for us to display the error to the user.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 268](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formData`

 

string

 

The serialised form data

 

##### Returns:

A promise resolved with the fragment html and js from

**
 Type

 :** 

object

 

#### (inner) reloadTitleContent() → {object}

 

**Description:
 :** 

- 

Reload the title for the modal to the appropriate value
depending on whether we are creating a new event or
editing an existing event.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 234](calendar_amd_src_modal_event_form.js.md)

##### Returns:

A promise resolved with the new title text

**
 Type

 :** 

object

 

#### (inner) save() → {object}

 

**Description:
 :** 

- 

Send the form data to the server to create or update
an event.

If there is a server side validation error then we re-request the
rendered form (with the data) from the server in order to get the
server side errors to display.

On success the modal is hidden and the page is reloaded so that the
new event will display.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 381](calendar_amd_src_modal_event_form.js.md)

##### Returns:

A promise

**
 Type

 :** 

object

 

#### (inner) setCategoryId(id)

 

**Description:
 :** 

- 

Set the category id to the given value.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 106](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The event id

 

 

#### (inner) setContextId(id)

 

**Description:
 :** 

- 

Set the context id to the given value.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 66](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The event id

 

 

#### (inner) setCourseId(id)

 

**Description:
 :** 

- 

Set the course id to the given value.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 86](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The event id

 

 

#### (inner) setEventId(id)

 

**Description:
 :** 

- 

Set the event id to the given value.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 146](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The event id

 

 

#### (inner) setStartTime(time)

 

**Description:
 :** 

- 

Set the start time to the given value.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 176](calendar_amd_src_modal_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `time`

 

Number

 

The start time

 

 

#### (inner) show()

 

**Description:
 :** 

- 

Kick off a reload the modal content before showing it. This
is to allow us to re-use the same modal for creating and
editing different events within the page.

We do the reload when showing the modal rather than hiding it
to save a request to the server if the user closes the modal
and never re-opens it.

 

**Source:
 :** 

- 
 [calendar/amd/src/modal_event_form.js](calendar_amd_src_modal_event_form.js.md), [line 338](calendar_amd_src_modal_event_form.js.md)
