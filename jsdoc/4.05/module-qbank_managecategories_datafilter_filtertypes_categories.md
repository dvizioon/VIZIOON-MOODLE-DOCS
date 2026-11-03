# module:qbank_managecategories/datafilter/filtertypes/categories - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-qbank_managecategories_datafilter_filtertypes_categories.html

# module:qbank_managecategories/datafilter/filtertypes/categories

 

## 

 module:qbank_managecategories/datafilter/filtertypes/categories

 

 

 

 

#### new (require("qbank_managecategories/datafilter/filtertypes/categories"))(filterType, rootNode, initialValues, filterOptions)

 

**Description:
 :** 

- 

Construct a new categoires filter

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/datafilter/filtertypes/categories.js](question_bank_managecategories_amd_src_datafilter_filtertypes_categories.js.md), [line 44](question_bank_managecategories_amd_src_datafilter_filtertypes_categories.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterType`

 

String

 

The type of filter that this relates to (categories)

 
 `rootNode`

 

HTMLElement

 

The root node for the participants filterset

 
 `initialValues`

 

Array

 

The currently selected category IDs.

 
 `filterOptions`

 

Object

 

An object containing the additional options for the filter, currently "includesubcategories"
is supported, which if true will display the "Also show questions from subcategories" checkbox as checked.
