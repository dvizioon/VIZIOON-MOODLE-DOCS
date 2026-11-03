# core/inplace_editable - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_inplace_editable.html

# core/inplace_editable

 

 

 

**Description:
 :** 

- 

AJAX helper for the inline editing a value.

This script is automatically included from template core/inplace_editable
It registers a click-listener on [data-inplaceeditablelink] link (the "inplace edit" icon),
then replaces the displayed value with an input field. On "Enter" it sends a request
to web service core_update_inplace_editable, which invokes the specified callback.
Any exception thrown by the web service (or callback) is displayed as an error popup.

 

**Source:
 :** 

- 
 [lib/amd/src/inplace_editable.js](lib_amd_src_inplace_editable.js.md), [line 16](lib_amd_src_inplace_editable.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2016 Marina Glancy

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

AJAX helper for the inline editing a value.

This script is automatically included from template core/inplace_editable
It registers a click-listener on [data-inplaceeditablelink] link (the "inplace edit" icon),
then replaces the displayed value with an input field. On "Enter" it sends a request
to web service core_update_inplace_editable, which invokes the specified callback.
Any exception thrown by the web service (or callback) is displayed as an error popup.

 

 

 

 

### Methods

 

#### (inner) getInplaceEditable(parent) → {Object|undefined}

 

**Description:
 :** 

- 

Return an object to interact with the current inplace editables at a frontend level.

 

**Source:
 :** 

- 
 [lib/amd/src/inplace_editable.js](lib_amd_src_inplace_editable.js.md), [line 357](lib_amd_src_inplace_editable.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `parent`

 

Element

 

the parent element containing a inplace editable

 

##### Returns:

an object to interact with the inplace element, or undefined
if no inplace editable is found.

**
 Type

 :** 

Object
|

undefined

 

#### (inner) getItemId() → {string}

 

**Description:
 :** 

- 

Return the inplace editable itemid.

 

**Source:
 :** 

- 
 [lib/amd/src/inplace_editable.js](lib_amd_src_inplace_editable.js.md), [line 388](lib_amd_src_inplace_editable.js.md)

##### Returns:

the current itemid

**
 Type

 :** 

string

 

#### (inner) getValue() → {string}

 

**Description:
 :** 

- 

Get the value from the inplace editable.

 

**Source:
 :** 

- 
 [lib/amd/src/inplace_editable.js](lib_amd_src_inplace_editable.js.md), [line 370](lib_amd_src_inplace_editable.js.md)

##### Returns:

the current inplace value

**
 Type

 :** 

string

 

#### (inner) setValue(newvalue)

 

**Description:
 :** 

- 

Force a value change.

 

**Source:
 :** 

- 
 [lib/amd/src/inplace_editable.js](lib_amd_src_inplace_editable.js.md), [line 380](lib_amd_src_inplace_editable.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newvalue`

 

string

 

the new value

 

##### Fires:

- [event:core/inplace_editable:updated](module-core_local_inplace_editable_events.md)

- [event:core/inplace_editable:updateFailed](module-core_local_inplace_editable_events.md)
