# block_recentlyaccesseditems/main - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-block_recentlyaccesseditems_main.html

# block_recentlyaccesseditems/main

 

 

 

**Description:
 :** 

- 

Javascript to initialise the Recently accessed items block.

 

**Source:
 :** 

- 
 [blocks/recentlyaccesseditems/amd/src/main.js](blocks_recentlyaccesseditems_amd_src_main.js.md), [line 17](blocks_recentlyaccesseditems_amd_src_main.js.md)

 

**Copyright:
 :** 

- 2018 Victor Deniz 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript to initialise the Recently accessed items block.

 

 

 

 

### Methods

 

#### (inner) getRecentItems(limit) → {array}

 

**Description:
 :** 

- 

Get recent items from backend.

 

**Source:
 :** 

- 
 [blocks/recentlyaccesseditems/amd/src/main.js](blocks_recentlyaccesseditems_amd_src_main.js.md), [line 66](blocks_recentlyaccesseditems_amd_src_main.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `limit`

 

int

 

Only return this many results

 

##### Returns:

Items user most recently has accessed

**
 Type

 :** 

array

 

#### (inner) renderItems(root, items) → {promise}

 

**Description:
 :** 

- 

Render the block content.

 

**Source:
 :** 

- 
 [blocks/recentlyaccesseditems/amd/src/main.js](blocks_recentlyaccesseditems_amd_src_main.js.md), [line 77](blocks_recentlyaccesseditems_amd_src_main.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the items view.

 
 `items`

 

array

 

containing array of returned items.

 

##### Returns:

Resolved with HTML and JS strings

**
 Type

 :** 

promise
