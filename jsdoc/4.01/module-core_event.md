# core/event - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_event.html

# core/event

 

 

 

**Description:
 :** 

- 

Global registry of core events that can be triggered/listened for.

 

**Source:
 :** 

- 
 [lib/amd/src/event.js](lib_amd_src_event.js.md), [line 16](lib_amd_src_event.js.md)

 

**Since:
 :** 

- 3.0

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Global registry of core events that can be triggered/listened for.

 

 

 

 

### Methods

 

#### (inner) getLegacyEvents() → {Promise}

 

**Description:
 :** 

- 

Load the legacy YUI module which defines events in M.core.event and return it.

 

**Source:
 :** 

- 
 [lib/amd/src/event.js](lib_amd_src_event.js.md), [line 39](lib_amd_src_event.js.md)

 

**Deprecated::** 

- Yes

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) getRenamedLegacyFunction(oldFunctionName, newModule, newFunctionName, newFunctionRef) → {function}

 

**Description:
 :** 

- 

Get a curried function to warn that a function has been moved and renamed

 

**Source:
 :** 

- 
 [lib/amd/src/event.js](lib_amd_src_event.js.md), [line 65](lib_amd_src_event.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `oldFunctionName`

 

String

 

 

 
 `newModule`

 

String

 

 

 
 `newFunctionName`

 

String

 

 

 
 `newFunctionRef`

 

function

 

 

 

##### Returns:

**
 Type

 :** 

function
