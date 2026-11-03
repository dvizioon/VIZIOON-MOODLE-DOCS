# core_form/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_form_events.html

# core_form/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `core_form` subsystem.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 16](lib_form_amd_src_events.js.md)

 

**Since:
 :** 

- 3.10

 

**Copyright:
 :** 

- 2021 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `core_form` subsystem.

 

### Example

 

Example of listening to a form event.

 

```js
import {eventTypes as formEventTypes} from 'core_form/events';

document.addEventListener(formEventTypes.formSubmittedByJavascript, e => {
    window.console.log(e.target); // The form that was submitted.
    window.console.log(e.detail.skipValidation); // Whether form validation was skipped.
});
```

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for `core_form`.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 58](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `formError`

 

String

 

See event:core_form/error

 
 `formFieldValidationFailed`

 

String

 

See [event:core_form/fieldValidationFailed](module-core_form_events.md)

 
 `formSubmittedByJavascript`

 

String

 

See [event:core_form/submittedByJavascript](module-core_form_events.md)

 
 `uploadChanged`

 

String

 

See [event:core_form/uploadChanged](module-core_form_events.md)

 
 `fieldStructureChanged`

 

String

 

See [event:core_form/fieldStructureChanged](module-core_form_events.md)

 

Events for `core_form`.

 

#### (static, constant) types

 

**Description:
 :** 

- 

List of the events.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 263](lib_form_amd_src_events.js.md)

 

**Deprecated::** 

- since Moodle 4.0. See [eventTypes](module-core_form_events.md) instead.

List of the events.

 

 

### Methods

 

#### (static) notifyFieldStructureChanged(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to notify the field structure has changed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 294](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

string

 

The element which was changed

 

##### Fires:

- event:fieldStructureChanged

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) notifyFormSubmittedByJavascript(form, skipValidation, fallbackHandled) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indiciate that a form was submitted by Javascript.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 148](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

HTMLElement

 

The form that was submitted

 
 `skipValidation`

 

Boolean

 

Submit the form without validation. E.g. "Cancel".

 
 `fallbackHandled`

 

Boolean

 

The legacy YUI event has been handled

 

##### Fires:

- event:formSubmittedByJavascript

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) notifyUploadChanged(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to notify the file upload field has been changed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 276](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

string

 

The element which was changed

 

##### Fires:

- event:uploadChanged

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) notifyUploadCompleted(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that an upload was completed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 221](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

The element which was uploaded to

 

##### Fires:

- event:uploadCompleted

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) notifyUploadStarted(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that an upload was started.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 197](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

The element which was uploaded to

 

##### Fires:

- event:uploadStarted

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) triggerUploadCompleted(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger upload complete event.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 256](lib_form_amd_src_events.js.md)

 

**Deprecated::** 

- Since Moodle 4.0 See [notifyUploadCompleted](module-core_form_events.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

 

 

##### Fires:

- event:uploadCompleted

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) triggerUploadStarted(elementId) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger upload start event.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 245](lib_form_amd_src_events.js.md)

 

**Deprecated::** 

- Since Moodle 4.0 See [notifyUploadStarted](module-core_form_events.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

 

 

##### Fires:

- event:uploadStarted

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (inner) changesMadeCheck(e)

 

**Description:
 :** 

- 

Prevent user navigate away when upload progress still running.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 42](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event

 

 

#### (inner) notifyFieldValidationFailure(field, message) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that a form field contained an error.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 169](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `field`

 

HTMLElement

 

The field which failed validation

 
 `message`

 

String

 

The message displayed

 

##### Fires:

- event:formFieldValidationFailed

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (inner) notifyFormError(field) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that a form field contained an error.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 128](lib_form_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `field`

 

HTMLElement

 

The form field causing the error

 

##### Fires:

- [event:formError](module-core_form_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### core_form/fieldStructureChanged

 

**Description:
 :** 

- 

An event triggered when a form field structure has changed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 118](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The form field that has changed

 

##### Type:

- 

CustomEvent

 

 

#### core_form/fieldValidationFailed

 

**Description:
 :** 

- 

An event triggered upon form field validation failure.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 80](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The field that failed validation

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `message`

 

String

 

The message displayed upon failure

 

 

 

##### Type:

- 

CustomEvent

 

 

#### core_form/submittedByJavascript

 

**Description:
 :** 

- 

An event triggered when an mform is about to be submitted via javascript.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 68](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The form that was submitted

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `skipValidation`

 

boolean

 

Whether the form was submitted without validation (i.e. via a Cancel button)

 
 `fallbackHandled`

 

boolean

 

Whether the legacy YUI event has been handled

 

 

 

##### Type:

- 

CustomEvent

 

 

#### core_form/uploadChanged

 

**Description:
 :** 

- 

An event triggered when a file upload field has been changed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 109](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The form field which was changed

 

##### Type:

- 

CustomEvent

 

 

#### core_form/uploadCompleted

 

**Description:
 :** 

- 

An event triggered when an upload completes

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 100](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The location where the upload completed

 

##### Type:

- 

CustomEvent

 

 

#### core_form/uploadStarted

 

**Description:
 :** 

- 

An event triggered when an upload is started

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 91](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The location where the upload began

 

##### Type:

- 

CustomEvent

 

 

#### formError

 

**Description:
 :** 

- 

An event triggered when a form contains an error

 

**Source:
 :** 

- 
 [lib/form/amd/src/events.js](lib_form_amd_src_events.js.md), [line 59](lib_form_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The form field which errored

 

##### Type:

- 

CustomEvent
