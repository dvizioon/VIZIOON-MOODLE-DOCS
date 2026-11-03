# core/local/process_monitor/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_process_monitor_events.html

# core/local/process_monitor/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `process_monitor` module.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/events.js](lib_amd_src_local_process_monitor_events.js.md), [line 15](lib_amd_src_local_process_monitor_events.js.md)

 

**Since:
 :** 

- 4.2

 

**Copyright:
 :** 

- 2022 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `process_monitor` module.

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for the `core_editor` subsystem.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/events.js](lib_amd_src_local_process_monitor_events.js.md), [line 30](lib_amd_src_local_process_monitor_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `processMonitorStateChange`

 

String

 

See [event:processMonitorStateChange](module-core_local_process_monitor_events.md)

 

Events for the `core_editor` subsystem.

 

 

### Methods

 

#### (inner) dispatchStateChangedEvent(detail, target)

 

**Description:
 :** 

- 

Trigger a state changed event.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/events.js](lib_amd_src_local_process_monitor_events.js.md), [line 39](lib_amd_src_local_process_monitor_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

Object

 

the full state

 
 `target`

 

Object

 

the custom event target (document if none provided)

###### Properties

 

 Name

 Type

 Description

 

 

 
 `dispatchEvent`

 

function

 

the component dispatch event method.

 

 

 

 

 

### Events

 

#### processMonitorStateChange

 

**Description:
 :** 

- 

An event triggered when the monitor state has changed.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/events.js](lib_amd_src_local_process_monitor_events.js.md), [line 31](lib_amd_src_local_process_monitor_events.js.md)
