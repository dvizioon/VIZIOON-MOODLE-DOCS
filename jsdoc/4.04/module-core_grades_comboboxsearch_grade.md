# core_grades/comboboxsearch/grade - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_grades_comboboxsearch_grade.html

# core_grades/comboboxsearch/grade

 

 

 

**Description:
 :** 

- 

Allow the user to search for grades within the grade area.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 16](grade_amd_src_comboboxsearch_grade.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for grades within the grade area.

 

 

 

 

### Methods

 

#### changeHandler(e)

 

**Description:
 :** 

- 

The handler for when a user changes the value of the component (selects an option from the dropdown).

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 214](grade_amd_src_comboboxsearch_grade.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The change event.

 

 

#### (async) clickHandler(e)

 

**Description:
 :** 

- 

The handler for when a user interacts with the component.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 196](grade_amd_src_comboboxsearch_grade.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

The triggering event that we are working with.

 

 

#### componentSelector() → {string}

 

**Description:
 :** 

- 

The overall div that contains the searching widget.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 88](grade_amd_src_comboboxsearch_grade.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### dropdownSelector() → {string}

 

**Description:
 :** 

- 

The dropdown div that contains the searching widget result space.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 97](grade_amd_src_comboboxsearch_grade.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (async) fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 134](grade_amd_src_comboboxsearch_grade.js.md)

##### Returns:

**
 Type

 :** 

Promise.<*>

 

#### (async) filterDataset(filterableData) → {Array}

 

**Description:
 :** 

- 

Dictate to the search component how and what we want to match upon.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 144](grade_amd_src_comboboxsearch_grade.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterableData`

 

Array

 

 

 

##### Returns:

The users that match the given criteria.

**
 Type

 :** 

Array

 

#### filterMatchDataset()

 

**Description:
 :** 

- 

Given we have a subset of the dataset, set the field that we matched upon to inform the end user.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 160](grade_amd_src_comboboxsearch_grade.js.md)

 

#### registerInputEvents()

 

**Description:
 :** 

- 

Handle any keyboard inputs.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 174](grade_amd_src_comboboxsearch_grade.js.md)

 

#### registerInputHandlers()

 

**Description:
 :** 

- 

Override the input event listener for the text input area.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 221](grade_amd_src_comboboxsearch_grade.js.md)

 

#### (async) renderDefault()

 

**Description:
 :** 

- 

Build the content then replace the node by default we want our form to exist.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 119](grade_amd_src_comboboxsearch_grade.js.md)

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 104](grade_amd_src_comboboxsearch_grade.js.md)

 

#### selectOneLink(gradeID)

 

**Description:
 :** 

- 

Build up the view all link that is dedicated to a particular result.
We will call this function when a user interacts with the combobox to redirect them to show their results in the page.

 

**Source:
 :** 

- 
 [grade/amd/src/comboboxsearch/grade.js](grade_amd_src_comboboxsearch_grade.js.md), [line 242](grade_amd_src_comboboxsearch_grade.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `gradeID`

 

Number

 

The ID of the grade item selected.
