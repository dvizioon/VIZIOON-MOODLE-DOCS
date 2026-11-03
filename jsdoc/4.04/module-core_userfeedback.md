# core/userfeedback - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_userfeedback.html

# core/userfeedback

 

 

 

**Description:
 :** 

- 

Handle clicking on action links of the feedback alert.

 

**Source:
 :** 

- 
 [lib/amd/src/userfeedback.js](lib_amd_src_userfeedback.js.md), [line 16](lib_amd_src_userfeedback.js.md)

 

**Copyright:
 :** 

- 2020 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle clicking on action links of the feedback alert.

 

 

 

 

### Members

 

#### (static, constant) registerEventListeners

 

**Description:
 :** 

- 

Attach the necessary event handlers to the action links

 

**Source:
 :** 

- 
 [lib/amd/src/userfeedback.js](lib_amd_src_userfeedback.js.md), [line 39](lib_amd_src_userfeedback.js.md)

Attach the necessary event handlers to the action links

 

 

### Methods

 

#### (inner) hideRoot(clickedItem) → {HTMLElement}

 

**Description:
 :** 

- 

Hide the root node of the CTA notification.

 

**Source:
 :** 

- 
 [lib/amd/src/userfeedback.js](lib_amd_src_userfeedback.js.md), [line 93](lib_amd_src_userfeedback.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clickedItem`

 

HTMLElement

 

The action element that the user chose.

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) recordAction(clickedItem) → {Promise}

 

**Description:
 :** 

- 

Record the action that the user took.

 

**Source:
 :** 

- 
 [lib/amd/src/userfeedback.js](lib_amd_src_userfeedback.js.md), [line 73](lib_amd_src_userfeedback.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clickedItem`

 

HTMLElement

 

The action element that the user chose.

 

##### Returns:

**
 Type

 :** 

Promise
