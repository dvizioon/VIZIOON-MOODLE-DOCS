# core_table/dynamic - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_table_dynamic.html

# core_table/dynamic

 

 

 

**Description:
 :** 

- 

Module to handle dynamic table features.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 16](lib_table_amd_src_dynamic.js.md)

 

**Copyright:
 :** 

- 2020 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module to handle dynamic table features.

 

 

 

 

### Members

 

#### (static, constant) getFilters

 

**Description:
 :** 

- 

Get the filter data for the specified table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 244](lib_table_amd_src_dynamic.js.md)

Get the filter data for the specified table.

 

#### (static, constant) getFirstInitial

 

**Description:
 :** 

- 

Get the current first initial filter.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 317](lib_table_amd_src_dynamic.js.md)

Get the current first initial filter.

 

#### (static, constant) getLastInitial

 

**Description:
 :** 

- 

Get the current last initial filter.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 336](lib_table_amd_src_dynamic.js.md)

Get the current last initial filter.

 

#### (static, constant) getPageNumber

 

**Description:
 :** 

- 

Get the current page number.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 279](lib_table_amd_src_dynamic.js.md)

Get the current page number.

 

#### (static, constant) getPageSize

 

**Description:
 :** 

- 

Get the current page size.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 298](lib_table_amd_src_dynamic.js.md)

Get the current page size.

 

#### (static, constant) getTableFromId

 

**Description:
 :** 

- 

Fetch the table via its table region id.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 458](lib_table_amd_src_dynamic.js.md)

Fetch the table via its table region id.

 

#### (static, constant) hideColumn

 

**Description:
 :** 

- 

Hide a column in the participants table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 346](lib_table_amd_src_dynamic.js.md)

Hide a column in the participants table.

 

#### (static, constant) init

 

**Description:
 :** 

- 

Set up listeners to handle table updates.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 379](lib_table_amd_src_dynamic.js.md)

Set up listeners to handle table updates.

 

#### (static, constant) refreshTableContent

 

**Description:
 :** 

- 

Update the specified table based on its current values.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 69](lib_table_amd_src_dynamic.js.md)

Update the specified table based on its current values.

 

#### (static, constant) setFilters

 

**Description:
 :** 

- 

Update the specified table using the new filters.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 235](lib_table_amd_src_dynamic.js.md)

Update the specified table using the new filters.

 

#### (static, constant) setFirstInitial

 

**Description:
 :** 

- 

Update the first initial to show.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 308](lib_table_amd_src_dynamic.js.md)

Update the first initial to show.

 

#### (static, constant) setLastInitial

 

**Description:
 :** 

- 

Update the last initial to show.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 327](lib_table_amd_src_dynamic.js.md)

Update the last initial to show.

 

#### (static, constant) setPageNumber

 

**Description:
 :** 

- 

Set the page number.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 270](lib_table_amd_src_dynamic.js.md)

Set the page number.

 

#### (static, constant) setPageSize

 

**Description:
 :** 

- 

Set the page size.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 289](lib_table_amd_src_dynamic.js.md)

Set the page size.

 

#### (static, constant) setSortOrder

 

**Description:
 :** 

- 

Update the sort order.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 259](lib_table_amd_src_dynamic.js.md)

Update the sort order.

 

#### (static, constant) showColumn

 

**Description:
 :** 

- 

Make a hidden column visible in the participants table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 361](lib_table_amd_src_dynamic.js.md)

Make a hidden column visible in the participants table.

 

 

### Methods

 

#### (inner) checkTableIsDynamic(tableRoot) → {Bool}

 

**Description:
 :** 

- 

Ensure that a table is a dynamic table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 38](lib_table_amd_src_dynamic.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) getFiltersetFromTable(tableRoot) → {Object}

 

**Description:
 :** 

- 

Get the filterset data from a known dynamic table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 58](lib_table_amd_src_dynamic.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) getTableData(tableRoot) → {DOMStringMap}

 

**Description:
 :** 

- 

Get the table dataset for the specified tableRoot, ensuring that the provided table is a dynamic table.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 221](lib_table_amd_src_dynamic.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

DOMStringMap

 

#### (inner) resetTablePreferences(tableRoot) → {Promise}

 

**Description:
 :** 

- 

Reset table preferences.

 

**Source:
 :** 

- 
 [lib/table/amd/src/dynamic.js](lib_table_amd_src_dynamic.js.md), [line 374](lib_table_amd_src_dynamic.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Promise
