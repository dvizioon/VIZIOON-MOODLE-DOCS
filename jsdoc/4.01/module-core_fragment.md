# core/fragment - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_fragment.html

# core/fragment

 

 

 

**Description:
 :** 

- 

A way to call HTML fragments to be inserted as required via JavaScript.

 

**Source:
 :** 

- 
 [lib/amd/src/fragment.js](lib_amd_src_fragment.js.md), [line 16](lib_amd_src_fragment.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2016 Adrian Greeve 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A way to call HTML fragments to be inserted as required via JavaScript.

 

 

 

 

### Methods

 

#### (inner) fragmentAppend(component, callback, contextid, params) → {Deferred}

 

**Description:
 :** 

- 

Appends HTML and JavaScript fragments to specified nodes.
Callbacks called by this AMD module are responsible for doing the appropriate security checks
to access the information that is returned. This only does minimal validation on the context.

 

**Source:
 :** 

- 
 [lib/amd/src/fragment.js](lib_amd_src_fragment.js.md), [line 96](lib_amd_src_fragment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

Component where callback is located.

 
 `callback`

 

string

 

Callback function name.

 
 `contextid`

 

integer

 

Context ID of the fragment.

 
 `params`

 

object

 

Parameters for the callback.

 

##### Returns:

new promise that is resolved with the html and js.

**
 Type

 :** 

Deferred

 

#### (inner) loadFragment(component, callback, contextid, params) → {Promise}

 

**Description:
 :** 

- 

Loads an HTML fragment through a callback.

 

**Source:
 :** 

- 
 [lib/amd/src/fragment.js](lib_amd_src_fragment.js.md), [line 26](lib_amd_src_fragment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

Component where callback is located.

 
 `callback`

 

string

 

Callback function name.

 
 `contextid`

 

integer

 

Context ID of the fragment.

 
 `params`

 

object

 

Parameters for the callback.

 

##### Returns:

JQuery promise object resolved when the fragment has been loaded.

**
 Type

 :** 

Promise

 

#### (inner) processCollectedJavascript(js) → {string}

 

**Description:
 :** 

- 

Converts the JS that was received from collecting JS requirements on the $PAGE so it can be added to the existing page

 

**Source:
 :** 

- 
 [lib/amd/src/fragment.js](lib_amd_src_fragment.js.md), [line 124](lib_amd_src_fragment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `js`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

string
