# block_recentlyaccesseditems/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-block_recentlyaccesseditems_repository.html

# block_recentlyaccesseditems/repository

 

 

 

**Description:
 :** 

- 

A javascript module to handle user ajax actions.

 

**Source:
 :** 

- 
 [blocks/recentlyaccesseditems/amd/src/repository.js](blocks_recentlyaccesseditems_amd_src_repository.js.md), [line 16](blocks_recentlyaccesseditems_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2018 Victor Deniz 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle user ajax actions.

 

 

 

 

### Methods

 

#### (inner) getRecentItems(limit) → {promise}

 

**Description:
 :** 

- 

Get the list of items that the user has most recently accessed.

 

**Source:
 :** 

- 
 [blocks/recentlyaccesseditems/amd/src/repository.js](blocks_recentlyaccesseditems_amd_src_repository.js.md), [line 25](blocks_recentlyaccesseditems_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `limit`

 

int

 

Only return this many results

 

##### Returns:

Resolved with an array of items

**
 Type

 :** 

promise
