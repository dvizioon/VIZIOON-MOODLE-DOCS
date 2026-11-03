# core/modal_factory - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_modal_factory.html

# core/modal_factory

 

 

 

**Description:
 :** 

- 

Create a modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_factory.js](lib_amd_src_modal_factory.js.md), [line 16](lib_amd_src_modal_factory.js.md)

 

**Deprecated::** 

- since Moodle 4.3

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

**To Do:
 :** 

- Final deprecation in Moodle 4.7/5.2. See MDL-79128/

 

 

Create a modal.

 

 

 

 

### Members

 

#### (static, constant) types

 

**Description:
 :** 

- 

The available standard modals.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_factory.js](lib_amd_src_modal_factory.js.md), [line 47](lib_amd_src_modal_factory.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `DEFAULT`

 

String

 

The default modal

 
 `SAVE_CANCEL`

 

String

 

A modal which can be used to either save, or cancel.

 
 `DELETE_CANCEL`

 

String

 

A modal which can be used to either delete, or cancel.

 
 `CANCEL`

 

String

 

A modal which displayed a cancel button

 
 `ALERT`

 

String

 

An information modal which only displays information.

 

The available standard modals.

 

 

### Methods

 

#### (inner) create(modalConfig, triggerElement) → {promise}

 

**Description:
 :** 

- 

Create a Modal instance.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_factory.js](lib_amd_src_modal_factory.js.md), [line 124](lib_amd_src_modal_factory.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalConfig`

 

object

 

The configuration to create the modal instance

 
 `triggerElement`

 

object

 

The trigger HTML jQuery object

 

##### Returns:

Resolved with a Modal instance

**
 Type

 :** 

promise
