# StateMap - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/StateMap.html

# StateMap

 

## 

 StateMap

 

 

Class to add events dispatching to the JS Map class.

When the state has a list of objects (with IDs) it will be converted into a StateMap.
StateMap is used almost in the same way as a regular JS map. Because all elements have an
id attribute, it has some specific methods:

- add: a convenient method to add an element without specifying the key ("id" attribute will be used as a key).

- loadValues: to add many elements at once wihout specifying keys ("id" attribute will be used).

Apart, the main difference between regular Map and MapState is that this one will inform any change to the
state manager.

 

 

 

 

## Constructor

#### new StateMap(name, stateManager, iterable)

 

**Description:
 :** 

- 

Create a reactive Map.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 739](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

string

 

the property name

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the state manager

 
 `iterable`

 

iterable

 

an iterable object to create the Map

 

 

 

 

### Methods

 

#### add(value) → {Map}

 

**Description:
 :** 

- 

Insert a new element int a list.

Each value needs it's own id attribute. Objects withouts id will be rejected.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 841](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

object

 

the value to add (needs an id attribute)

 

##### Returns:

the resulting Map object

**
 Type

 :** 

Map

 

#### checkValue(value)

 

**Description:
 :** 

- 

Check if a value is valid to be stored in a a State List.

Only objects with id attribute can be stored in State lists.

This method throws an error if the value is not valid.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 810](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

object

 

(with ID)

 

 

#### delete(key) → {boolean}

 

**Description:
 :** 

- 

Delete an element from the map.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 872](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

*

 

 

 

##### Returns:

**
 Type

 :** 

boolean

 

#### get(key) → {Object}

 

**Description:
 :** 

- 

Return a state map element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 852](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

*

 

the element id

 

##### Returns:

**
 Type

 :** 

Object

 

#### has(key) → {boolean}

 

**Description:
 :** 

- 

Check whether an element with the specified key exists or not.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 862](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

*

 

the key to find

 

##### Returns:

**
 Type

 :** 

boolean

 

#### loadValues(values) → {[StateMap](StateMap.md)}

 

**Description:
 :** 

- 

Insert a full list of values using the id attributes as keys.

This method is used mainly to initialize the list. Note each element is indexed by its "id" attribute.
This is a basic restriction of StateMap. All elements need an id attribute, otherwise it won't be saved.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 919](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `values`

 

iterable

 

the values to load

 

##### Returns:

return the this value

**
 Type

 :** 

[StateMap](StateMap.md)

 

#### normalizeKey(key) → {string}

 

**Description:
 :** 

- 

Return a normalized key value for state map.

Regular maps uses strict key comparissons but state maps are indexed by ID.JSON conversions
and webservices sometimes do unexpected types conversions so we convert any integer key to string.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 829](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

*

 

the provided key

 

##### Returns:

**
 Type

 :** 

string

 

#### set(key, value) → {Map}

 

**Description:
 :** 

- 

Set an element into the map.

Each value needs it's own id attribute. Objects without id will be rejected.
The function will throw an error if the value id and the key are not the same.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 765](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

*

 

the key to store

 
 `value`

 

*

 

the value to store

 

##### Returns:

the resulting Map object

**
 Type

 :** 

Map

 

#### toJSON() → {array}

 

**Description:
 :** 

- 

Return a suitable structure for JSON conversion.

This function is needed because new values are compared in JSON. StateMap has Private
attributes which cannot be stringified (like this.stateManager which will produce an
infinite recursivity).

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 902](lib_amd_src_local_reactive_statemanager.js.md)

##### Returns:

**
 Type

 :** 

array
