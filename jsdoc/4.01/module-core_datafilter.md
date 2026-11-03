# module:core/datafilter - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_datafilter.html

# module:core/datafilter

 

## 

 module:core/datafilter

 

 

 

 

#### new (require("core/datafilter"))(filterSet, applyCallback)

 

**Description:
 :** 

- 

Initialise the filter on the element with the given filterSet and callback.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 42](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterSet`

 

HTMLElement

 

The filter element.

 
 `applyCallback`

 

function

 

Callback function when updateTableFromFilter

 

 

 

 

### Methods

 

#### (async) addFilter(filterRow, filterType, initialFilterValues) → {Filter}

 

**Description:
 :** 

- 

Add a filter to the list of active filters, performing any necessary setup.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 176](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterRow`

 

HTMLElement

 

 

 
 `filterType`

 

String

 

 

 
 `initialFilterValues`

 

Array

 

The initially selected values for the filter

 

##### Returns:

**
 Type

 :** 

Filter

 

#### addFilterRow() → {Promise}

 

**Description:
 :** 

- 

Add an unselected filter row.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 117](lib_amd_src_datafilter.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (async) getAvailableFilterLegends() → {array}

 

**Description:
 :** 

- 

Fetch the strings used to populate the fieldset legends for the maximum number of filters possible.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 414](lib_amd_src_datafilter.js.md)

##### Returns:

**
 Type

 :** 

array

 

#### getFilterDataSource(filterType) → {HTMLElement}

 

**Description:
 :** 

- 

Get the filter data source node fro the specified filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 162](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterType`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### getFilterObject(name) → {Object}

 

**Description:
 :** 

- 

Get the registered filter class for the named filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 206](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

String

 

 

 

##### Returns:

See the Filter class.

**
 Type

 :** 

Object

 

#### getFilterRegion() → {HTMLElement}

 

**Description:
 :** 

- 

Get the filter list region.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 108](lib_amd_src_datafilter.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### removeAllFilters() → {Promise}

 

**Description:
 :** 

- 

Remove all filters.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 332](lib_amd_src_datafilter.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### removeEmptyFilters()

 

**Description:
 :** 

- 

Remove any empty filters.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 343](lib_amd_src_datafilter.js.md)

 

#### removeFilterObject(filterName)

 

**Description:
 :** 

- 

Remove the Filter Object from the register.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 315](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterName`

 

string

 

The name of the filter to be removed

 

 

#### (async) removeFilterRow(filterRow, refreshContent)

 

**Description:
 :** 

- 

Remove the specified filter row and associated class.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 232](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `filterRow`

 

HTMLElement

 

 

 

 

 
 `refreshContent`

 

Bool

 

 

 `true`

 

Whether to refresh the table content when removing

 

 

#### removeOrReplaceFilterRow(filterRow, refreshContent)

 

**Description:
 :** 

- 

Remove or replace the specified filter row and associated class, ensuring that if there is only one filter row,
that it is replaced instead of being removed.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 217](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterRow`

 

HTMLElement

 

 

 
 `refreshContent`

 

Bool

 

Whether to refresh the table content when removing

 

 

#### replaceFilterRow(filterRow, refreshContent, rowNum) → {Promise}

 

**Description:
 :** 

- 

Replace the specified filter row with a new one.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 267](lib_amd_src_datafilter.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `filterRow`

 

HTMLElement

 

 

 

 

 
 `refreshContent`

 

Bool

 

 

 `true`

 

Whether to refresh the table content when removing

 
 `rowNum`

 

Number

 

 

 `1`

 

The number used to label the filter fieldset legend (eg Row 1). Defaults to 1 (the first filter).

 

##### Returns:

**
 Type

 :** 

Promise

 

#### updateFiltersOptions()

 

**Description:
 :** 

- 

Update the list of filter types to filter out those already selected.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 356](lib_amd_src_datafilter.js.md)

 

#### updateTableFromFilter()

 

**Description:
 :** 

- 

Update the Dynamic table based upon the current filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter.js](lib_amd_src_datafilter.js.md), [line 396](lib_amd_src_datafilter.js.md)
