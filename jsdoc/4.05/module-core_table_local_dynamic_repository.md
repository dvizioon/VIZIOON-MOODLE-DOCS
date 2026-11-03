# core_table/local/dynamic/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_table_local_dynamic_repository.html

# core_table/local/dynamic/repository

 

 

 

**Description:
 :** 

- 

A javascript module to handle calendar ajax actions.

 

**Source:
 :** 

- 
 [lib/table/amd/src/local/dynamic/repository.js](lib_table_amd_src_local_dynamic_repository.js.md), [line 16](lib_table_amd_src_local_dynamic_repository.js.md)

 

**Copyright:
 :** 

- 2017 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle calendar ajax actions.

 

 

 

 

### Methods

 

#### (inner) fetch(component, handler, uniqueid, options, resetPreferences) → {Promise}

 

**Description:
 :** 

- 

Fetch table view.

 

**Source:
 :** 

- 
 [lib/table/amd/src/local/dynamic/repository.js](lib_table_amd_src_local_dynamic_repository.js.md), [line 25](lib_table_amd_src_local_dynamic_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

String

 

The component

 
 `handler`

 

String

 

The name of the handler

 
 `uniqueid`

 

String

 

The unique id of the table

 
 `options`

 

Object

 

The options to use when updating the table

###### Properties

 

 Name

 Type

 Description

 

 

 
 `sortData`

 

Array

 

The list of columns to sort by

 
 `joinType`

 

Number

 

The filterset join type

 
 `filters`

 

Object

 

The filters to apply when searching

 
 `firstinitial`

 

String

 

The first name initial to filter on

 
 `lastinitial`

 

String

 

The last name initial to filter on

 
 `pageNumber`

 

String

 

The page number

 
 `pageSize`

 

Number

 

The page size

 
 `hiddenColumns`

 

Object

 

The columns to hide

 

 

 
 `resetPreferences`

 

Bool

 

 

 

##### Returns:

Resolved with requested table view

**
 Type

 :** 

Promise
