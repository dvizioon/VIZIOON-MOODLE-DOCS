# core_grades/edittree_index - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_grades_edittree_index.html

# core_grades/edittree_index

 

 

 

**Description:
 :** 

- 

Enhance the gradebook tree setup with various facilities.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 16](grade_amd_src_edittree_index.js.md)

 

**Copyright:
 :** 

- 2016 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Enhance the gradebook tree setup with various facilities.

 

 

 

 

### Methods

 

#### (inner) collapseGradeCategories(courseId, userId)

 

**Description:
 :** 

- 

Method that collapses all relevant grade categories based on the locally stored state of collapsed grade categories
for a given user.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 97](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

int

 

The ID of course.

 
 `userId`

 

int

 

The ID of the current logged user.

 

 

#### (inner) init(courseId, userId)

 

**Description:
 :** 

- 

Initialize module.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 244](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

int

 

The ID of course.

 
 `userId`

 

int

 

The ID of the current logged user.

 

 

#### (inner) registerListenerEvents(courseId, userId)

 

**Description:
 :** 

- 

Register related event listeners.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 39](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

int

 

The ID of course.

 
 `userId`

 

int

 

The ID of the current logged user.

 

 

#### (inner) toggleCategory(toggleElement, courseId, userId, storeCollapsedState)

 

**Description:
 :** 

- 

Method that handles the grade category toggle action.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 146](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleElement`

 

object

 

The category toggle node that was clicked.

 
 `courseId`

 

int

 

The ID of course.

 
 `userId`

 

int

 

The ID of the current logged user.

 
 `storeCollapsedState`

 

boolean

 

Whether to store (local storage) the state of collapsed grade categories.

 

 

#### (inner) toggleWeightInput(weightOverrideCheckbox)

 

**Description:
 :** 

- 

Toggle the weight input field based on its checkbox.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 71](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `weightOverrideCheckbox`

 

object

 

The weight override checkbox element.

 

 

#### (inner) toggleWeightInput(bulkMoveSelect)

 

**Description:
 :** 

- 

Submit the bulk move form.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 84](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulkMoveSelect`

 

object

 

The bulk move select element.

 

 

#### (inner) updateCollapsedCategoriesStoredState(category, courseId, userId, isCollapsing)

 

**Description:
 :** 

- 

Method that updates the locally stored state of collapsed grade categories based on a performed toggle action on a
given grade category.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 123](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `category`

 

string

 

The category to be added or removed from the collapsed grade categories local storage.

 
 `courseId`

 

int

 

The ID of course.

 
 `userId`

 

int

 

The ID of the current logged user.

 
 `isCollapsing`

 

boolean

 

Whether the category is being collapsed or not.

 

 

#### (inner) updateParentCategoryRowspans(toggleElement, num)

 

**Description:
 :** 

- 

Method that updates the rowspan value of all 'parent' category rows of a given category node.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_index.js](grade_amd_src_edittree_index.js.md), [line 210](grade_amd_src_edittree_index.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleElement`

 

object

 

The category toggle node that was clicked.

 
 `num`

 

int

 

The number we want to add or subtract from the rowspan value of the 'parent' category row elements.
