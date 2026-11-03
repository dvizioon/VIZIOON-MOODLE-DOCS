# module:core/datafilter/filtertype - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_datafilter_filtertype.html

# module:core/datafilter/filtertype

 

## 

 module:core/datafilter/filtertype

 

 

 

 

#### new (require("core/datafilter/filtertype"))(filterType, rootNode, initialValues)

 

**Description:
 :** 

- 

Constructor for a new filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 49](lib_amd_src_datafilter_filtertype.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterType`

 

String

 

The type of filter that this relates to

 
 `rootNode`

 

HTMLElement

 

The root node for the participants filterset

 
 `initialValues`

 

Array

 

The initial values for the selector

 

 

 

 

### Members

 

#### filterOptions

 

**Description:
 :** 

- 

Get options specific to this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 240](lib_amd_src_datafilter_filtertype.js.md)

Get options specific to this filter type.

 

#### filterRoot

 

**Description:
 :** 

- 

Get the root node for this filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 172](lib_amd_src_datafilter_filtertype.js.md)

Get the root node for this filter.

 

#### filterValue

 

**Description:
 :** 

- 

Get the composed value for this filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 249](lib_amd_src_datafilter_filtertype.js.md)

Get the composed value for this filter.

 

#### jointype

 

**Description:
 :** 

- 

Get the type of join specified.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 210](lib_amd_src_datafilter_filtertype.js.md)

Get the type of join specified.

 

#### name

 

**Description:
 :** 

- 

Get the name of this filter.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 201](lib_amd_src_datafilter_filtertype.js.md)

Get the name of this filter.

 

#### placeholder

 

**Description:
 :** 

- 

Get the placeholder to use when showing the value selector.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 75](lib_amd_src_datafilter_filtertype.js.md)

Get the placeholder to use when showing the value selector.

 

#### rawValues

 

**Description:
 :** 

- 

Get the list of raw values for this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 219](lib_amd_src_datafilter_filtertype.js.md)

Get the list of raw values for this filter type.

 

#### showSuggestions

 

**Description:
 :** 

- 

Whether to show suggestions in the autocomplete.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 84](lib_amd_src_datafilter_filtertype.js.md)

Whether to show suggestions in the autocomplete.

 

#### values

 

**Description:
 :** 

- 

Get the list of values for this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 231](lib_amd_src_datafilter_filtertype.js.md)

Get the list of values for this filter type.

 

 

### Methods

 

#### (async) addValueSelector(initialValues) → {Promise}

 

**Description:
 :** 

- 

Add the value selector to the filter row.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 94](lib_amd_src_datafilter_filtertype.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `initialValues`

 

Array

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### getFilterValueNode() → {HTMLElement}

 

**Description:
 :** 

- 

Get the HTMLElement which contains the value selector.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 192](lib_amd_src_datafilter_filtertype.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### getSourceDataForFilter() → {Array}

 

**Description:
 :** 

- 

Get the possible data for this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 181](lib_amd_src_datafilter_filtertype.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### tearDown()

 

**Description:
 :** 

- 

Perform any tear-down for this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 66](lib_amd_src_datafilter_filtertype.js.md)

 

#### (inner) getOptionsForSelect(select) → {Array.<HTMLOptionElement>}

 

**Description:
 :** 

- 

Fetch all checked options in the select.

This is a poor-man's polyfill for select.selectedOptions, which is not available in IE11.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertype.js](lib_amd_src_datafilter_filtertype.js.md), [line 36](lib_amd_src_datafilter_filtertype.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `select`

 

HTMLSelectElement

 

 

 

##### Returns:

All selected options

**
 Type

 :** 

Array.<HTMLOptionElement>
