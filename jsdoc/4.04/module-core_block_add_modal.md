# core_block/add_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_block_add_modal.html

# core_block/add_modal

 

 

 

**Description:
 :** 

- 

Show an add block modal instead of doing it on a separate page.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 16](blocks_amd_src_add_modal.js.md)

 

**Copyright:
 :** 

- 2016 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Show an add block modal instead of doing it on a separate page.

 

 

 

 

### Methods

 

#### (inner) buildAddBlockModal() → {Promise}

 

**Description:
 :** 

- 

Method that creates the 'add block' modal.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 95](blocks_amd_src_add_modal.js.md)

##### Returns:

The modal promise (modal's body will be rendered later).

**
 Type

 :** 

Promise

 

#### (inner) getAddableBlocks(pagehash) → {Promise}

 

**Description:
 :** 

- 

Method that fetches all addable blocks in a given page.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 126](blocks_amd_src_add_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pagehash`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) init(addBlockUrl, pagehash)

 

**Description:
 :** 

- 

Set up the actions.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 148](blocks_amd_src_add_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `addBlockUrl`

 

String

 

The add block URL

 
 `pagehash`

 

String

 

 

 

 

#### (inner) registerListenerEvents(addBlockUrl, pagehash)

 

**Description:
 :** 

- 

Register related event listeners.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 38](blocks_amd_src_add_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `addBlockUrl`

 

String
|

null

 

The add block URL

 
 `pagehash`

 

String

 

 

 

 

#### (inner) renderBlocks(addBlockUrl, pagehash, region) → {Promise}

 

**Description:
 :** 

- 

Method that renders the list of available blocks.

 

**Source:
 :** 

- 
 [blocks/amd/src/add_modal.js](blocks_amd_src_add_modal.js.md), [line 105](blocks_amd_src_add_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `addBlockUrl`

 

String

 

The add block URL

 
 `pagehash`

 

String

 

 

 
 `region`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise
