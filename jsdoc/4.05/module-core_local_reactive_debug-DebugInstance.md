# DebugInstance - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_local_reactive_debug-DebugInstance.html

# DebugInstance

 

## 
 [core/local/reactive/debug](module-core_local_reactive_debug.md)~

 
 DebugInstance

 

 

 

 

#### new DebugInstance(instance)

 

**Description:
 :** 

- 

Constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 197](lib_amd_src_local_reactive_debug.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `instance`

 

Reactive

 

the reactive instance

 

 

 

 

### Members

 

#### changes

 

**Description:
 :** 

- 

List all the state changes evenet pending to dispatch.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 273](lib_amd_src_local_reactive_debug.js.md)

List all the state changes evenet pending to dispatch.

 

#### components

 

**Description:
 :** 

- 

List all the components registered in this instance.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 264](lib_amd_src_local_reactive_debug.js.md)

List all the components registered in this instance.

 

#### elements

 

**Description:
 :** 

- 

Return all the HTML elements registered in the instance components.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 301](lib_amd_src_local_reactive_debug.js.md)

Return all the HTML elements registered in the instance components.

 

#### highlight

 

**Description:
 :** 

- 

Tooggle the reactive HTML element highlight registered in this reactive instance.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 242](lib_amd_src_local_reactive_debug.js.md)

Tooggle the reactive HTML element highlight registered in this reactive instance.

 

#### highlight

 

**Description:
 :** 

- 

Get the current highligh value.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 255](lib_amd_src_local_reactive_debug.js.md)

Get the current highligh value.

 

#### readOnly

 

**Description:
 :** 

- 

Set the read only mode.

Quick access to the instance setReadOnly method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 215](lib_amd_src_local_reactive_debug.js.md)

Set the read only mode.

Quick access to the instance setReadOnly method.

 

#### readOnly

 

**Description:
 :** 

- 

Get the read only value

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 224](lib_amd_src_local_reactive_debug.js.md)

Get the read only value

 

#### state

 

**Description:
 :** 

- 

Return the current state object.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 233](lib_amd_src_local_reactive_debug.js.md)

Return the current state object.

 

#### stateData

 

**Description:
 :** 

- 

Return a plain copy of the state data.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 314](lib_amd_src_local_reactive_debug.js.md)

Return a plain copy of the state data.

 

 

### Methods

 

#### processUpdates(updates)

 

**Description:
 :** 

- 

Process an update state array.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debug.js](lib_amd_src_local_reactive_debug.js.md), [line 323](lib_amd_src_local_reactive_debug.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `updates`

 

array

 

an array of update state messages
