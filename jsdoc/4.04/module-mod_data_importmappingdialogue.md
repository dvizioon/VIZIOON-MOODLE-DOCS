# mod_data/importmappingdialogue - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_data_importmappingdialogue.html

# mod_data/importmappingdialogue

 

 

 

**Description:
 :** 

- 

Javascript module for deleting a database as a preset.

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 16](mod_data_amd_src_importmappingdialogue.js.md)

 

**Copyright:
 :** 

- 2022 Amaia Anabitarte 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript module for deleting a database as a preset.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 42](mod_data_amd_src_importmappingdialogue.js.md)

Initialize module

 

 

### Methods

 

#### (inner) buildModal(params) → {Object}

 

**Description:
 :** 

- 

Given an object we want to build a modal ready to show

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 92](mod_data_amd_src_importmappingdialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

Object

 

the modal params

###### Properties

 

 Name

 Type

 Description

 

 

 
 `title`

 

Promise

 

 

 
 `body`

 

Promise

 

 

 
 `footer`

 

Promise

 

 

 

 

 

##### Returns:

The modal ready to display immediately and render body in later.

**
 Type

 :** 

Object

 

#### (inner) getMappingButtons(cmId, presetName) → {array}

 

**Description:
 :** 

- 

Add buttons to render on mapping modal.

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 119](mod_data_amd_src_importmappingdialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmId`

 

int

 

The id of the current database activity.

 
 `presetName`

 

string

 

The preset name to delete.

 

##### Returns:

Same data with buttons.

**
 Type

 :** 

array

 

#### (inner) getMappingInformation(cmId, presetName) → {promise}

 

**Description:
 :** 

- 

Check whether we should show the mapping dialogue or not.

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 154](mod_data_amd_src_importmappingdialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmId`

 

int

 

The id of the current database activity.

 
 `presetName`

 

string

 

The preset name to delete.

 

##### Returns:

Resolved with the result and warnings of deleting a preset.

**
 Type

 :** 

promise

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events.

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 49](mod_data_amd_src_importmappingdialogue.js.md)

 

#### (inner) showMappingDialogue(usepreset)

 

**Description:
 :** 

- 

Show the confirmation modal for uploading a preset.

 

**Source:
 :** 

- 
 [mod/data/amd/src/importmappingdialogue.js](mod_data_amd_src_importmappingdialogue.js.md), [line 64](mod_data_amd_src_importmappingdialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `usepreset`

 

HTMLElement

 

the preset to import.
