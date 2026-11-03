# core/addblockmodal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_addblockmodal.html

# core/addblockmodal

 

 

 

**Description:
 :** 

- 

Show an add block modal instead of doing it on a separate page.

 

**Source:
 :** 

- 
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 16](lib_amd_src_addblockmodal.js.md)

 

**Deprecated::** 

- since Moodle 4.2 - please use core_block/add_modal instead.

 

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
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 72](lib_amd_src_addblockmodal.js.md)

##### Returns:

The modal promise (modal's body will be rendered later).

**
 Type

 :** 

Promise

 

#### (inner) getAddableBlocks(pageType, pageLayout, subPage) → {Promise}

 

**Description:
 :** 

- 

Method that fetches all addable blocks in a given page.

 

**Source:
 :** 

- 
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 104](lib_amd_src_addblockmodal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pageType`

 

String

 

The type of the page

 
 `pageLayout`

 

String

 

The layout of the page

 
 `subPage`

 

String

 

The subpage identifier

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) init(pageType, pageLayout, addBlockUrl, subPage)

 

**Description:
 :** 

- 

Set up the actions.

 

**Source:
 :** 

- 
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 127](lib_amd_src_addblockmodal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pageType`

 

String

 

The type of the page

 
 `pageLayout`

 

String

 

The layout of the page

 
 `addBlockUrl`

 

String
|

null

 

The add block URL

 
 `subPage`

 

String

 

The subpage identifier

 

 

#### (inner) registerListenerEvents(pageType, pageLayout, addBlockUrl, subPage)

 

**Description:
 :** 

- 

Register related event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 37](lib_amd_src_addblockmodal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pageType`

 

String

 

The type of the page

 
 `pageLayout`

 

String

 

The layout of the page

 
 `addBlockUrl`

 

String
|

null

 

The add block URL

 
 `subPage`

 

String

 

The subpage identifier

 

 

#### (inner) renderBlocks(addBlockUrl, pageType, pageLayout, subPage) → {Promise}

 

**Description:
 :** 

- 

Method that renders the list of available blocks.

 

**Source:
 :** 

- 
 [lib/amd/src/addblockmodal.js](lib_amd_src_addblockmodal.js.md), [line 84](lib_amd_src_addblockmodal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `addBlockUrl`

 

String

 

The add block URL

 
 `pageType`

 

String

 

The type of the page

 
 `pageLayout`

 

String

 

The layout of the page

 
 `subPage`

 

String

 

The subpage identifier

 

##### Returns:

**
 Type

 :** 

Promise
