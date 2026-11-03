# module:core_group/comboboxsearch/group - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_group_comboboxsearch_group.html

# module:core_group/comboboxsearch/group

 

## 

 module:core_group/comboboxsearch/group

 

 

 

 

#### new (require("core_group/comboboxsearch/group"))(cmid)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 40](group_amd_src_comboboxsearch_group.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `cmid`

 

int
|

null

 

 

 `null`

 

ID of the course module initiating the group search (optional).

 

 

 

 

### Methods

 

#### changeHandler(e)

 

**Description:
 :** 

- 

The handler for when a user changes the value of the component (selects an option from the dropdown).

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 206](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 188](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 100](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 109](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 145](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 155](group_amd_src_comboboxsearch_group.js.md)

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
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 171](group_amd_src_comboboxsearch_group.js.md)

 

#### registerInputHandlers()

 

**Description:
 :** 

- 

Override the input event listener for the text input area.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 213](group_amd_src_comboboxsearch_group.js.md)

 

#### (async) renderDefault()

 

**Description:
 :** 

- 

Build the content then replace the node by default we want our form to exist.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 131](group_amd_src_comboboxsearch_group.js.md)

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 116](group_amd_src_comboboxsearch_group.js.md)

 

#### selectOneLink(groupID)

 

**Description:
 :** 

- 

Build up the view all link that is dedicated to a particular result.
We will call this function when a user interacts with the combobox to redirect them to show their results in the page.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/group.js](group_amd_src_comboboxsearch_group.js.md), [line 236](group_amd_src_comboboxsearch_group.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `groupID`

 

Number

 

The ID of the group selected.
