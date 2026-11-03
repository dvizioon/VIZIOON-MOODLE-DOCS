# Handler - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/Handler.html

# Handler

 

## 

 Handler

 

 

The proxy handler.

This class will inform any value change directly to the state manager.

The proxied variable will throw an error if it is altered when the state manager is
in read only mode.

 

 

 

 

## Constructor

#### new Handler(name, stateManager, proxyValues)

 

**Description:
 :** 

- 

Class constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 646](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

string

 

the variable name used for identify triggered actions

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the state manager object

 
 `proxyValues`

 

boolean

 

if new values must be proxied (used only at state root level)

 

 

 

 

### Methods

 

#### deleteProperty(obj, prop) → {boolean}

 

**Description:
 :** 

- 

Delete property trap to trigger state change events.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 712](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `obj`

 

*

 

the affected object (not proxied)

 
 `prop`

 

*

 

the prop to delete

 

##### Returns:

if prop is deleted

**
 Type

 :** 

boolean

 

#### set(obj, prop, value, receiver) → {boolean}

 

**Description:
 :** 

- 

Set trap to trigger events when the state changes.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 670](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `obj`

 

object

 

the source object (not proxied)

 
 `prop`

 

string

 

the attribute to set

 
 `value`

 

*

 

the value to save

 
 `receiver`

 

*

 

the proxied element to be attached to events

 

##### Returns:

if the value is set

**
 Type

 :** 

boolean
