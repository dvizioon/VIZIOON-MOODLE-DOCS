# core/reactive/local/reactive/debug - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_reactive_local_reactive_debug.html

# core/reactive/local/reactive/debug

 

 

 

**Description:
 :** 

- 

Reactive module debug tools.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 16](lib_amd_src_local_reactive_debug.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Reactive module debug tools.

 

 

 

### Classes

 

**[DebugInstance](module-core_reactive_local_reactive_debug-DebugInstance.md)
 :[core/reactive/local/reactive/debug/Debug](module-core_reactive_local_reactive_debug-core_reactive_local_reactive_debug_Debug.md)
 :[core/reactive/local/reactive/debug/DebugInstance](module-core_reactive_local_reactive_debug-core_reactive_local_reactive_debug_DebugInstance.md)
 :[core/reactive/local/reactive/debug/Mutations](module-core_reactive_local_reactive_debug-core_reactive_local_reactive_debug_Mutations.md)
 :** 

 

 

 

### Members

 

#### (static, constant) initDebug

 

**Description:
 :** 

- 

The main init method to initialize the reactive debug.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 352](lib_amd_src_local_reactive_debug.js.md)

The main init method to initialize the reactive debug.

 

 

### Methods

 

#### (inner) dispatch(args)

 

**Description:
 :** 

- 

Dispatch a change in the state.

Usually reactive modules throw an error directly to the components when something
goes wrong. However, course editor can directly display a notification.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 279](lib_amd_src_local_reactive_debug.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

*

 

 

 

 

#### (inner) dispatchStateChangedEvent(detail, target)

 

**Description:
 :** 

- 

Internal state changed event.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 326](lib_amd_src_local_reactive_debug.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

the full state

 
 `target`

 

object

 

the custom event target (document if none provided)
