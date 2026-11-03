# core/datafilter/filtertypes/binary - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_datafilter_filtertypes_binary.html

# core/datafilter/filtertypes/binary

 

 

 

**Description:
 :** 

- 

Base filter for binary selector ie: (Yes / No).

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 16](lib_amd_src_datafilter_filtertypes_binary.js.md)

 

**Author:
 :** 

- [2022 Ghaly Marc-Alexandre](mailto:marc-alexandreghaly@catalyst-ca.net)

 

 

**Copyright:
 :** 

- 2022 Catalyst IT Australia Pty Ltd

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Base filter for binary selector ie: (Yes / No).

 

 

 

 

### Members

 

#### optionOne :String

 

**Description:
 :** 

- 

Text string for the first binary option.

This option (and {@see optionTwo}) are set by {@see getTextValues()}. The base class will set default values,
a subclass can override the method to define its own option.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 40](lib_amd_src_datafilter_filtertypes_binary.js.md)

Text string for the first binary option.

This option (and {@see optionTwo}) are set by {@see getTextValues()}. The base class will set default values,
a subclass can override the method to define its own option.

##### Type:

- 

String

 

 

#### optionTwo :String

 

**Description:
 :** 

- 

Text string for the second binary option.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 47](lib_amd_src_datafilter_filtertypes_binary.js.md)

Text string for the second binary option.

##### Type:

- 

String

 

 

#### values

 

**Description:
 :** 

- 

Get the list of raw values for this filter type.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 107](lib_amd_src_datafilter_filtertypes_binary.js.md)

Get the list of raw values for this filter type.

 

 

### Methods

 

#### (async) addValueSelector(initialValues)

 

**Description:
 :** 

- 

Add the value selector to the filter row.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 54](lib_amd_src_datafilter_filtertypes_binary.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `initialValues`

 

Array

 

The default value for the filter.

 

 

#### (async) displayBinarySelection(initialValue)

 

**Description:
 :** 

- 

Renders yes/no select input with proper selection.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 75](lib_amd_src_datafilter_filtertypes_binary.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `initialValue`

 

Number

 

 

 `0`

 

The default value for the filter.

 

 

#### getTextValues() → {Promise}

 

**Description:
 :** 

- 

Fetch text values for select options.

Subclasses should override this method to set their own options.

 

**Source:
 :** 

- 
 [lib/amd/src/datafilter/filtertypes/binary.js](lib_amd_src_datafilter_filtertypes_binary.js.md), [line 66](lib_amd_src_datafilter_filtertypes_binary.js.md)

##### Returns:

**
 Type

 :** 

Promise
