# filter_glossary/autolinker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-filter_glossary_autolinker.html

# filter_glossary/autolinker

 

 

 

**Description:
 :** 

- 

Module for auto-linking glossary entries.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 16](filter_glossary_amd_src_autolinker.js.md)

 

**Copyright:
 :** 

- 2023 Mihail Geshoski 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module for auto-linking glossary entries.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize the module.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 148](filter_glossary_amd_src_autolinker.js.md)

Initialize the module.

 

#### (inner, constant) The :Object

 

**Description:
 :** 

- 

object containing the relevant selectors.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 29](filter_glossary_amd_src_autolinker.js.md)

object containing the relevant selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) fetchGlossaryEntry(entryId) → {Promise}

 

**Description:
 :** 

- 

Fetch the linked glossary entry.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 84](filter_glossary_amd_src_autolinker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entryId`

 

int

 

The id of the linked glossary entry.

 

##### Returns:

The glossary entry promise.

**
 Type

 :** 

Promise

 

#### (inner) generateTagListData(tags) → {Object}

 

**Description:
 :** 

- 

Generates an object that contains the data required to render a tag list.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 118](filter_glossary_amd_src_autolinker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tags`

 

array

 

The array containing the tags related to the linked glossary entry.

 

##### Returns:

The data required to render a tag list.

**
 Type

 :** 

Object

 

#### (inner) glossaryEntryViewed(entryId) → {Promise}

 

**Description:
 :** 

- 

Notify that the linked glossary entry was viewed.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 101](filter_glossary_amd_src_autolinker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entryId`

 

int

 

The id of the linked glossary entry.

 

##### Returns:

The promise object.

**
 Type

 :** 

Promise

 

#### (inner) registerEventListeners() → {void}

 

**Description:
 :** 

- 

Register the event listeners for the glossary entry auto-linker.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 39](filter_glossary_amd_src_autolinker.js.md)

##### Returns:

**
 Type

 :** 

void

 

#### (inner) showGlossaryEntry(entryId) → {Promise}

 

**Description:
 :** 

- 

Show the linked glossary entry in a modal.

 

**Source:
 :** 

- 
 [filter/glossary/amd/src/autolinker.js](filter_glossary_amd_src_autolinker.js.md), [line 51](filter_glossary_amd_src_autolinker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entryId`

 

int

 

The id of the linked glossary entry.

 

##### Returns:

The modal promise.

**
 Type

 :** 

Promise
