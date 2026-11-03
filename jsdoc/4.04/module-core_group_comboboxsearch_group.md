# core_group/comboboxsearch/group - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_group_comboboxsearch_group.html

# core_group/comboboxsearch/group

 

 

 

**Description:
 :** 

- 

Allow the user to search for groups.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 16](group_amd_src_comboboxsearch_group.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for groups.

 

 

 

 

### Methods

 

#### changeHandler(e)

 

**Description:
 :** 

- 

The handler for when a user changes the value of the component (selects an option from the dropdown).

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 194](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 176](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 88](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 97](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 133](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 143](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 159](group_amd_src_comboboxsearch_group.js.md)

 

#### registerInputHandlers()

 

**Description:
 :** 

- 

Override the input event listener for the text input area.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 201](group_amd_src_comboboxsearch_group.js.md)

 

#### (async) renderDefault()

 

**Description:
 :** 

- 

Build the content then replace the node by default we want our form to exist.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 119](group_amd_src_comboboxsearch_group.js.md)

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 104](group_amd_src_comboboxsearch_group.js.md)

 

#### selectOneLink(groupID)

 

**Description:
 :** 

- 

Build up the view all link that is dedicated to a particular result.
We will call this function when a user interacts with the combobox to redirect them to show their results in the page.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 224](group_amd_src_comboboxsearch_group.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `groupID`

 

Number

 

The ID of the group selected.
