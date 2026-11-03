# core/modal_backdrop - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_modal_backdrop.html

# core/modal_backdrop

 

 

 

**Description:
 :** 

- 

Contain the logic for modal backdrops.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 16](lib_amd_src_modal_backdrop.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for modal backdrops.

 

 

 

### Classes

 

**[core/modal_backdrop](module-core_modal_backdrop-core_modal_backdrop.md)
 :** 

 

 

 

### Methods

 

#### (inner) attachToDOM()

 

**Description:
 :** 

- 

Add the modal backdrop to the page, if it hasn't already been added.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 66](lib_amd_src_modal_backdrop.js.md)

 

#### (inner) destroy()

 

**Description:
 :** 

- 

Remove this backdrop from the DOM.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 152](lib_amd_src_modal_backdrop.js.md)

 

#### (inner) getRoot() → {object}

 

**Description:
 :** 

- 

Get the root element of this modal backdrop.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 47](lib_amd_src_modal_backdrop.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) hasTransitions() → {bool}

 

**Description:
 :** 

- 

Check if this backdrop has CSS transitions applied.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 101](lib_amd_src_modal_backdrop.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hide()

 

**Description:
 :** 

- 

Hide this backdrop.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 127](lib_amd_src_modal_backdrop.js.md)

 

#### (inner) isVisible() → {bool}

 

**Description:
 :** 

- 

Check if this backdrop is visible.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 91](lib_amd_src_modal_backdrop.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) setZIndex(value)

 

**Description:
 :** 

- 

Set the z-index value for this backdrop.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 81](lib_amd_src_modal_backdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

int

 

The z-index value

 

 

#### (inner) show()

 

**Description:
 :** 

- 

Display this backdrop. The backdrop will be attached to the DOM if it hasn't
already been.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_backdrop.js](lib_amd_src_modal_backdrop.js.md), [line 111](lib_amd_src_modal_backdrop.js.md)
