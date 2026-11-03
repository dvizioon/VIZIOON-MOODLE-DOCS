# qbank_managecategories/categorymanager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-qbank_managecategories_categorymanager.html

# qbank_managecategories/categorymanager

 

 

 

**Description:
 :** 

- 

Reactive module for category manager

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 16](question_bank_managecategories_amd_src_categorymanager.js.md)

 

Reactive module for category manager

 

 

 

### Classes

 

**[CategoryManager](module-qbank_managecategories_categorymanager-CategoryManager.md)
 :** 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Load the initial state.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 224](question_bank_managecategories_amd_src_categorymanager.js.md)

Load the initial state.

 

 

### Methods

 

#### (async, inner) loadState(reactive) → {Promise.<void>}

 

**Description:
 :** 

- 

Load the initial state.

This iterates over the initial tree of category items, and captures the data required for the state from each category.
It also captures a count of the number of children in each list.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 53](question_bank_managecategories_amd_src_categorymanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reactive`

 

Reactive

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<void>
