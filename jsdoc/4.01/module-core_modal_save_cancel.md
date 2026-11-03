# module:core/modal_save_cancel - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_modal_save_cancel.html

# module:core/modal_save_cancel

 

## 

 module:core/modal_save_cancel

 

 

The Save/Cancel Modal.

 

 

 

 

## Constructor

#### new (require("core/modal_save_cancel"))()

 

**Source:
 :** 

- 
 [lib/amd/src/modal_save_cancel.js](lib_amd_src_modal_save_cancel.js.md), [line 33](lib_amd_src_modal_save_cancel.js.md)

 

 

### Extends

- module:core/modal

 

 

### Methods

 

#### setFooter()

 

**Description:
 :** 

- 

Override parent implementation to prevent changing the footer content.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_save_cancel.js](lib_amd_src_modal_save_cancel.js.md), [line 61](lib_amd_src_modal_save_cancel.js.md)

 

#### setSaveButtonText(value)

 

**Description:
 :** 

- 

Set the title of the save button.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_save_cancel.js](lib_amd_src_modal_save_cancel.js.md), [line 72](lib_amd_src_modal_save_cancel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

String
|

Promise

 

The button text, or a Promise which will resolve it
