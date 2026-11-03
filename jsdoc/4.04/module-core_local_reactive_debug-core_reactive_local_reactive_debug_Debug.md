# core/reactive/local/reactive/debug/Debug - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_reactive_debug-core_reactive_local_reactive_debug_Debug.html

# core/reactive/local/reactive/debug/Debug

 

## 
 [core/local/reactive/debug](module-core_local_reactive_debug.md)~

 
 core/reactive/local/reactive/debug/Debug

 

 

 

 

#### new core/reactive/local/reactive/debug/Debug()

 

**Description:
 :** 

- 

Reactive module debug tools.

If debug is enabled, this reactive module will spy all the reactive instances and keep a record
of the changes and components they have.

It is important to note that the Debug class is also a Reactive module. The debug instance keeps
the reactive instances data as its own state. This way it is possible to implement development tools
that whatches this data.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 33](lib_amd_src_local_reactive_debug.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
