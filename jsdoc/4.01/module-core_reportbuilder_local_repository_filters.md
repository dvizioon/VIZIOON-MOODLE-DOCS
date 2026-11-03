# core_reportbuilder/local/repository/filters - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_reportbuilder_local_repository_filters.html

# core_reportbuilder/local/repository/filters

 

 

 

**Description:
 :** 

- 

Module to handle filter AJAX requests

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 16](reportbuilder_amd_src_local_repository_filters.js.md)

 

**Copyright:
 :** 

- 2021 Paul Holden 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module to handle filter AJAX requests

 

 

 

 

### Members

 

#### (static, constant) addFilter

 

**Description:
 :** 

- 

Add a filter to the given report

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 68](reportbuilder_amd_src_local_repository_filters.js.md)

Add a filter to the given report

 

#### (static, constant) deleteFilter

 

**Description:
 :** 

- 

Remove filter from given report

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 84](reportbuilder_amd_src_local_repository_filters.js.md)

Remove filter from given report

 

#### (static, constant) reorderFilter

 

**Description:
 :** 

- 

Reorder a filter in a given report

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 101](reportbuilder_amd_src_local_repository_filters.js.md)

Reorder a filter in a given report

 

 

### Methods

 

#### (static) resetFilters(reportId, reportParameters) → {Promise}

 

**Description:
 :** 

- 

Reset all filters for given report

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 34](reportbuilder_amd_src_local_repository_filters.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reportId`

 

Number

 

 

 
 `reportParameters`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) setFilters(reportId, reportParameters, filterValues) → {Promise}

 

**Description:
 :** 

- 

Set filter values for given report

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/filters.js](reportbuilder_amd_src_local_repository_filters.js.md), [line 52](reportbuilder_amd_src_local_repository_filters.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reportId`

 

Number

 

 

 
 `reportParameters`

 

String

 

 

 
 `filterValues`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise
