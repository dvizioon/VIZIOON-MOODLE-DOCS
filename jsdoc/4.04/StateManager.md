# StateManager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/StateManager.html

# StateManager

 

## 

 StateManager

 

 

 

 

#### new StateManager()

 

**Description:
 :** 

- 

Reactive simple state manager.

The state manager contains the state data, trigger update events and
can lock and unlock the state data.

This file contains the three main elements of the state manager:

  - State manager: the public class to alter the state, dispatch events and process update messages.

  - Proxy handler: a private class to keep track of the state object changes.

  - StateMap class: a private class extending Map class that triggers event when a state list is modifed.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 16](lib_amd_src_local_reactive_statemanager.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
