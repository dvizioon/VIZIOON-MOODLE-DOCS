# mod_data/deletepreset - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_data_deletepreset.html

# mod_data/deletepreset

 

 

 

**Description:
 :** 

- 

Javascript module for deleting a database as a preset.

 

**Source:
 :** 

- 
 [mod/data/amd/src/deletepreset.js](mod_data_amd_src_deletepreset.js.md), [line 16](mod_data_amd_src_deletepreset.js.md)

 

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
 [mod/data/amd/src/deletepreset.js](mod_data_amd_src_deletepreset.js.md), [line 37](mod_data_amd_src_deletepreset.js.md)

Initialize module

 

 

### Methods

 

#### (async, inner) deletePreset(dataId, presetName) → {promise}

 

**Description:
 :** 

- 

Delete site user preset.

 

**Source:
 :** 

- 
 [mod/data/amd/src/deletepreset.js](mod_data_amd_src_deletepreset.js.md), [line 88](mod_data_amd_src_deletepreset.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dataId`

 

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

 

#### (inner) deletePresetConfirm(deleteOption)

 

**Description:
 :** 

- 

Show the confirmation modal to delete the preset.

 

**Source:
 :** 

- 
 [mod/data/amd/src/deletepreset.js](mod_data_amd_src_deletepreset.js.md), [line 67](mod_data_amd_src_deletepreset.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `deleteOption`

 

HTMLElement

 

the element to delete.

 

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events for delete preset option in action menu.

 

**Source:
 :** 

- 
 [mod/data/amd/src/deletepreset.js](mod_data_amd_src_deletepreset.js.md), [line 52](mod_data_amd_src_deletepreset.js.md)
