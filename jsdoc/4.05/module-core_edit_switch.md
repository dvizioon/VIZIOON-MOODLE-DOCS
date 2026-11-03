# core/edit_switch - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_edit_switch.html

# core/edit_switch

 

 

 

**Description:
 :** 

- 

Controls the edit switch.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 16](lib_amd_src_edit_switch.js.md)

 

**Copyright:
 :** 

- 2021 Bas Brands 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the edit switch.

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Names of events for core/edit_switch.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 73](lib_amd_src_edit_switch.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `editModeSet`

 

String

 

See [event:core/edit_switch/editModeSet](module-core_edit_switch.md)

 

Names of events for core/edit_switch.

 

#### (static, constant) init

 

**Description:
 :** 

- 

Add the eventlistener for the editswitch.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 111](lib_amd_src_edit_switch.js.md)

Add the eventlistener for the editswitch.

 

 

### Methods

 

#### (protected, inner) notifyEditModeSet(container, editMode) → {CustomEvent}

 

**Description:
 :** 

- 

Dispatch the editModeSet event after changing the edit mode.

This event is cancelable.

The default action is to reload the page after toggling the edit mode.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 99](lib_amd_src_edit_switch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

HTMLElement

 

 

 
 `editMode`

 

bool

 

 

 

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (inner) setEditMode(context, setmode) → {Promise}

 

**Description:
 :** 

- 

Change the Edit mode.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 36](lib_amd_src_edit_switch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `context`

 

number

 

The contextid that editing is being set for

 
 `setmode`

 

bool

 

Whether editing is set or not

 

##### Returns:

Resolved with an array file the stored file url.

**
 Type

 :** 

Promise

 

#### (protected, inner) toggleEditSwitch(editSwitch)

 

**Description:
 :** 

- 

Toggle the edit switch

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 51](lib_amd_src_edit_switch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editSwitch`

 

HTMLElement

 

 

 

 

 

### Events

 

#### core/edit_switch/editModeSet

 

**Description:
 :** 

- 

An event triggered when the edit mode toggled.

 

**Source:
 :** 

- 
 [lib/amd/src/edit_switch.js](lib_amd_src_edit_switch.js.md), [line 74](lib_amd_src_edit_switch.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The switch used to toggle the edit mode

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `editMode`

 

bool

 

 

 

 

 

##### Type:

- 

CustomEvent
