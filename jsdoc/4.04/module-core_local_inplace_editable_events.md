# core/local/inplace_editable/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_inplace_editable_events.html

# core/local/inplace_editable/events

 

 

 

**Description:
 :** 

- 

Inplace editable module events

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 16](lib_amd_src_local_inplace_editable_events.js.md)

 

**Copyright:
 :** 

- 2021 Paul Holden 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Inplace editable module events

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Module events

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 34](lib_amd_src_local_inplace_editable_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `elementUpdated`

 

String

 

See [event:core/inplace_editable:updated](module-core_local_inplace_editable_events.md)

 
 `elementUpdateFailed`

 

String

 

See [event:core/inplace_editable:updateFailed](module-core_local_inplace_editable_events.md)

 

Module events

 

 

### Methods

 

#### (static) notifyElementUpdateFailed(element, exception, newvalue) → {CustomEvent}

 

**Description:
 :** 

- 

Notify element of failed update

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 90](lib_amd_src_local_inplace_editable_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The element that failed to update

 
 `exception`

 

Object

 

The raised exception

 
 `newvalue`

 

String

 

The intended value of the element

 

##### Fires:

- [event:core/inplace_editable:updateFailed](module-core_local_inplace_editable_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (static) notifyElementUpdated(element, ajaxreturn, oldvalue) → {CustomEvent}

 

**Description:
 :** 

- 

Notify element of successful update

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 71](lib_amd_src_local_inplace_editable_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The element that was updated

 
 `ajaxreturn`

 

Object

 

The data returned from the update AJAX request

 
 `oldvalue`

 

String

 

The previous value of the element

 

##### Fires:

- [event:core/inplace_editable:updated](module-core_local_inplace_editable_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### core/inplace_editable:updateFailed

 

**Description:
 :** 

- 

Event triggered when an element update has failed

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 48](lib_amd_src_local_inplace_editable_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The element that failed to update

 
 `detail`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `exception`

 

Object

 

The raised exception

 
 `newvalue`

 

String

 

The intended value of the element

 

 

 

##### Type:

- 

CustomEvent

 

 

#### core/inplace_editable:updated

 

**Description:
 :** 

- 

Event triggered when an element has been updated

 

**Source:
 :** 

- 
 [lib/amd/src/local/inplace_editable/events.js](lib_amd_src_local_inplace_editable_events.js.md), [line 36](lib_amd_src_local_inplace_editable_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The element that was updated

 
 `detail`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `ajaxreturn`

 

Object

 

The data returned from the update AJAX request

 
 `oldvalue`

 

String

 

The previous value of the element

 

 

 

##### Type:

- 

CustomEvent
