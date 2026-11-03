# GlobalDebugPanel - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_reactive_debugpanel-GlobalDebugPanel.html

# GlobalDebugPanel

 

## 
 [core/local/reactive/debugpanel](module-core_local_reactive_debugpanel.md)~

 
 GlobalDebugPanel

 

 

Component for the main reactive dev panel.

This component shows the list of reactive instances and handle the buttons
to open a specific instance panel.

 

 

 

 

## Constructor

#### new GlobalDebugPanel()

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 80](lib_amd_src_local_reactive_debugpanel.js.md)

 

 

 

### Methods

 

#### _createLoader(instance)

 

**Description:
 :** 

- 

Create a debug panel button for a specific reactive instance.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 147](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `instance`

 

object

 

hte instance data

 

 

#### (async) _openPanel(btn, instance)

 

**Description:
 :** 

- 

Open a debug panel.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 167](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `btn`

 

Element

 

the button element

 
 `instance`

 

object

 

the instance data

 

 

#### _updateReactivesPanels(args)

 

**Description:
 :** 

- 

Update the list of reactive instances.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 129](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state

 

 

 

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 85](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 118](lib_amd_src_local_reactive_debugpanel.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 107](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

object

 

the initial state
