# core_user/comboboxsearch/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_user_comboboxsearch_user.html

# core_user/comboboxsearch/user

 

 

 

**Description:
 :** 

- 

Allow the user to search for learners.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 16](user_amd_src_comboboxsearch_user.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for learners.

 

 

 

 

### Methods

 

#### changeHandler(e)

 

**Description:
 :** 

- 

The handler for when a user changes the value of the component (selects an option from the dropdown).

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 193](user_amd_src_comboboxsearch_user.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The change event.

 

 

#### componentSelector() → {string}

 

**Description:
 :** 

- 

The overall div that contains the searching widget.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 75](user_amd_src_comboboxsearch_user.js.md)

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
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 84](user_amd_src_comboboxsearch_user.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 120](user_amd_src_comboboxsearch_user.js.md)

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
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 130](user_amd_src_comboboxsearch_user.js.md)

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

 

#### (async) filterMatchDataset() → {Array}

 

**Description:
 :** 

- 

Given we have a subset of the dataset, set the field that we matched upon to inform the end user.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 149](user_amd_src_comboboxsearch_user.js.md)

##### Returns:

The results with the matched fields inserted.

**
 Type

 :** 

Array

 

#### getStringMap() → {Promise.<void>}

 

**Description:
 :** 

- 

Given the set of profile fields we can possibly search, fetch their strings,
so we can report to screen readers the field that matched.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 283](user_amd_src_comboboxsearch_user.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### keyHandler(e)

 

**Description:
 :** 

- 

The handler for when a user presses a key within the component.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 208](user_amd_src_comboboxsearch_user.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

KeyboardEvent

 

The triggering event that we are working with.

 

 

#### (async) renderDefault()

 

**Description:
 :** 

- 

Build the content then replace the node by default we want our form to exist.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 108](user_amd_src_comboboxsearch_user.js.md)

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 91](user_amd_src_comboboxsearch_user.js.md)

 

#### selectAllResultsLink()

 

**Description:
 :** 

- 

Build up the view all link.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 263](user_amd_src_comboboxsearch_user.js.md)

 

#### selectOneLink(userID)

 

**Description:
 :** 

- 

Build up the view all link that is dedicated to a particular result.
We will call this function when a user interacts with the combobox to redirect them to show their results in the page.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 273](user_amd_src_comboboxsearch_user.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userID`

 

Number

 

The ID of the user selected.

 

 

#### toggleDropdown(on)

 

**Description:
 :** 

- 

When called, hide or show the users dropdown.

 

**Source:
 :** 

- 
 [user/amd/src/comboboxsearch/user.js](user_amd_src_comboboxsearch_user.js.md), [line 241](user_amd_src_comboboxsearch_user.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `on`

 

Boolean

 

 

 `false`

 

Flag to toggle hiding or showing values.
