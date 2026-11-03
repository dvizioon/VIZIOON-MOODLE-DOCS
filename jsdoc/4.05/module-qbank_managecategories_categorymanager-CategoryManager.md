# CategoryManager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-qbank_managecategories_categorymanager-CategoryManager.html

# CategoryManager

 

## 
 [qbank_managecategories/categorymanager](module-qbank_managecategories_categorymanager.md)~

 
 CategoryManager

 

 

Reactive instance for the category manager.

 

 

 

 

## Constructor

#### new CategoryManager()

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 87](question_bank_managecategories_amd_src_categorymanager.js.md)

 

 

 

### Methods

 

#### getSave(isEdit) → {String}

 

**Description:
 :** 

- 

Return save button label for the add/edit modal.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 143](question_bank_managecategories_amd_src_categorymanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `isEdit`

 

boolean

 

is 'add' or 'edit' form

 

##### Returns:

save string

**
 Type

 :** 

String

 

#### getTitle(isEdit) → {String}

 

**Description:
 :** 

- 

Return title for the add/edit modal.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 133](question_bank_managecategories_amd_src_categorymanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `isEdit`

 

boolean

 

is 'add' or 'edit' form

 

##### Returns:

title string

**
 Type

 :** 

String

 

#### moveCategory(categoryId, targetParentId, precedingSiblingId)

 

**Description:
 :** 

- 

Move a category to a new position within the given parent.

This will call the move_category web service function to re-order the categories, then update
the state with the returned updates.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 99](question_bank_managecategories_amd_src_categorymanager.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `categoryId`

 

Number

 

 

 

The ID of the category being moved.

 
 `targetParentId`

 

Number

 

 

 

The ID of the destination parent category (this may not have changed).

 
 `precedingSiblingId`

 

Number

 

 

 `null`

 

The ID of the category to put the moved category after.
This may be null if moving to the top of a list.

 

 

#### showEditModal(e)

 

**Description:
 :** 

- 

Function handling display of modal form.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/categorymanager.js](question_bank_managecategories_amd_src_categorymanager.js.md), [line 152](question_bank_managecategories_amd_src_categorymanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The click event triggering the modal.
