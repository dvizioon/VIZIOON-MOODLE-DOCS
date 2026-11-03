# editor_atto/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-editor_atto_events.html

# editor_atto/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `editor_atto` plugin.

 

**Source:
 :** 

- 
 [lib/editor/atto/amd/src/events.js](lib_editor_atto_amd_src_events.js.md), [line 15](lib_editor_atto_amd_src_events.js.md)

 

**Since:
 :** 

- 3.10.5

 

**Copyright:
 :** 

- 2021 Jun Pataleta 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `editor_atto` plugin.

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for the `editor_atto` plugin.

 

**Source:
 :** 

- 
 [lib/editor/atto/amd/src/events.js](lib_editor_atto_amd_src_events.js.md), [line 32](lib_editor_atto_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `attoButtonHighlightToggled`

 

String

 

See [event:attoButtonHighlightToggled](module-editor_atto_events.md)

 

Events for the `editor_atto` plugin.

 

 

### Methods

 

#### (inner) notifyButtonHighlightToggled(attoButton, buttonName, highlight) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that a button's highlight was toggled.

 

**Source:
 :** 

- 
 [lib/editor/atto/amd/src/events.js](lib_editor_atto_amd_src_events.js.md), [line 46](lib_editor_atto_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `attoButton`

 

HTMLElement

 

The button object.

 
 `buttonName`

 

String

 

The button name.

 
 `highlight`

 

Boolean

 

True when the button was highlighted. False, otherwise.

 

##### Fires:

- [event:attoButtonHighlightToggled](module-editor_atto_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### attoButtonHighlightToggled

 

**Description:
 :** 

- 

An event triggered when a toolbar button's highlight gets toggled.

 

**Source:
 :** 

- 
 [lib/editor/atto/amd/src/events.js](lib_editor_atto_amd_src_events.js.md), [line 33](lib_editor_atto_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The button which had its highlight toggled.

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `buttonName`

 

String

 

The name of the Atto button that has had its highlight toggled.

 
 `highlight`

 

Boolean

 

True when the button was highlighted. False, otherwise.

 

 

 

##### Type:

- 

CustomEvent
