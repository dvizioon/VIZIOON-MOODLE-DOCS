# DebugInstanceSubpanel - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_local_reactive_debugpanel-DebugInstanceSubpanel.html

# DebugInstanceSubpanel

 

## 
 [core/local/reactive/debugpanel](module-core_local_reactive_debugpanel.md)~

 
 DebugInstanceSubpanel

 

 

Component for the main reactive dev panel.

This component shows the list of reactive instances and handle the buttons
to open a specific instance panel.

 

 

 

 

## Constructor

#### new DebugInstanceSubpanel()

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 185](lib_amd_src_local_reactive_debugpanel.js.md)

 

 

 

### Methods

 

#### _checkJSON() → {undefined|array}

 

**Description:
 :** 

- 

Check that the edited state JSON is valid.

Not all valid JSON are suitable for transforming the state. For example,
the first level attributes cannot change the type.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 376](lib_amd_src_local_reactive_debugpanel.js.md)

##### Returns:

Array of state updates.

**
 Type

 :** 

undefined
|

array

 

#### _cleanAreas()

 

**Description:
 :** 

- 

Listener method to clean the log area.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 330](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _generateStateUpdates(currentStateData, newStateData) → {array}

 

**Description:
 :** 

- 

Check that the edited state JSON is valid.

Not all valid JSON are suitable for transforming the state. For example,
the first level attributes cannot change the type. This method do a two
steps comparison between the current state data and the new state data.

A reactive state cannot be overridden like any other variable. To keep
the watchers updated is necessary to transform the current state into
the new one. As a result, this method generates all the necessary state
updates to convert the state into the new state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 439](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentStateData`

 

object

 

 

 
 `newStateData`

 

object

 

 

 

##### Throws:

**

 

is the structure is not compatible

 
 :

 

**
 Type

 :** 

Error

 

 :** 

##### Returns:

Array of state updates.

**
 Type

 :** 

array

 

#### _pin()

 

**Description:
 :** 

- 

Pin the panel into the footer.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 576](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _refreshLog(args)

 

**Description:
 :** 

- 

Watcher method to refresh the log panel.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 311](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 

 

 

 

#### _refreshReadOnly()

 

**Description:
 :** 

- 

Watcher to update the read only information.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 348](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _refreshState()

 

**Description:
 :** 

- 

Watcher to refresh the state information.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 340](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _saveState()

 

**Description:
 :** 

- 

Listener to save the current edited state into the real state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 413](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _toggleButtonText(element)

 

**Description:
 :** 

- 

Toogle the button text with the data-alt value.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 597](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

the button element

 

 

#### _toggleEditMode()

 

**Description:
 :** 

- 

Listener to toggle the edit mode of the component.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 364](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _togglePin()

 

**Description:
 :** 

- 

Pin and unpin the panel.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 538](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### _unpin()

 

**Description:
 :** 

- 

Unpin the panel form the footer.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 551](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 190](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### destroy()

 

**Description:
 :** 

- 

Remove all subcomponents dependencies.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 286](lib_amd_src_local_reactive_debugpanel.js.md)

 

#### dragEnd(dropdata, event)

 

**Description:
 :** 

- 

The element drop end hook.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 530](lib_amd_src_local_reactive_debugpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 
 `event`

 

Event

 

the dropdata

 

 

#### getDraggableData() → {Object}

 

**Description:
 :** 

- 

Get the draggable data of this component.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 520](lib_amd_src_local_reactive_debugpanel.js.md)

##### Returns:

exported course module drop data

**
 Type

 :** 

Object

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 297](lib_amd_src_local_reactive_debugpanel.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### stateReady()

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/debugpanel.js](lib_amd_src_local_reactive_debugpanel.js.md), [line 223](lib_amd_src_local_reactive_debugpanel.js.md)
