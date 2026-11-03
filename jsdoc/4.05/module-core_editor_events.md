# core_editor/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_editor_events.html

# core_editor/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `core_editor` subsystem.

 

**Source:
 :** 

- 
 [lib/editor/amd/src/events.js](lib_editor_amd_src_events.js.md), [line 15](lib_editor_amd_src_events.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `core_editor` subsystem.

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for the `core_editor` subsystem.

 

**Source:
 :** 

- 
 [lib/editor/amd/src/events.js](lib_editor_amd_src_events.js.md), [line 32](lib_editor_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `editorContentRestored`

 

String

 

See [event:editorContentRestored](module-core_editor_events.md)

 

Events for the `core_editor` subsystem.

 

 

### Methods

 

#### (inner) notifyEditorContentRestored(editor) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that editor content was restored.

 

**Source:
 :** 

- 
 [lib/editor/amd/src/events.js](lib_editor_amd_src_events.js.md), [line 41](lib_editor_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

HTMLElement
|

null

 

The element that was modified

 

##### Fires:

- [event:editorContentRestored](module-core_editor_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### editorContentRestored

 

**Description:
 :** 

- 

An event triggered when an editor restores auto-saved content.

 

**Source:
 :** 

- 
 [lib/editor/amd/src/events.js](lib_editor_amd_src_events.js.md), [line 33](lib_editor_amd_src_events.js.md)
