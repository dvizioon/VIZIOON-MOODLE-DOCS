# core/comboboxsearch/search_combobox - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_comboboxsearch_search_combobox.html

# core/comboboxsearch/search_combobox

 

 

 

**Description:
 :** 

- 

The class that manages the state of the search within a combobox.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 22](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

The class that manages the state of the search within a combobox.

 

 

 

 

### Methods

 

#### changeHandler(e)

 

**Description:
 :** 

- 

The handler for when a user changes the value of the component (selects an option from the dropdown).

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 384](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 359](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

The triggering event that we are working with.

 

 

#### closeSearch(clear)

 

**Description:
 :** 

- 

When called, close the dropdown and reset the input field attributes.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 236](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `clear`

 

Boolean

 

 

 `false`

 

Conditionality clear the input box.

 

 

#### componentSelector()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 128](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### dropdownSelector()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 135](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### fetchDataset()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 99](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### filterDataset(dataset)

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 107](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dataset`

 

Array

 

 

 

 

#### filterMatchDataset()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 114](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### (async) filterrenderpipe() → {Promise.<void>}

 

**Description:
 :** 

- 

Update any changeable nodes, filter and then render the result.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 330](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (async) getDataset() → {Promise.<null>}

 

**Description:
 :** 

- 

Return the dataset that we will be searching upon.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 152](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

Promise.<null>

 

#### getDatasetSize() → {number}

 

**Description:
 :** 

- 

Return the size of the dataset.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 165](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

number

 

#### getHTMLElements() → {object}

 

**Description:
 :** 

- 

Return an object containing a handfull of dom nodes that we sometimes need the value of.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 220](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

object

 

#### getMatchedResults() → {Array}

 

**Description:
 :** 

- 

Return the results of the filter upon the dataset.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 174](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### getPreppedSearchTerm() → {string}

 

**Description:
 :** 

- 

Get the transformed search value.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 201](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### getSearchTerm() → {string}

 

**Description:
 :** 

- 

Get the value that the user entered.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 192](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### registerChangeHandlers()

 

**Description:
 :** 

- 

Register change event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 294](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### registerClickHandlers()

 

**Description:
 :** 

- 

Register clickable event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 286](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### registerInputHandlers()

 

**Description:
 :** 

- 

Register input event listener for the text input area.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 302](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### (async) renderAndShow() → {Promise.<void>}

 

**Description:
 :** 

- 

A combo method to take the matching fields and render out the results.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 343](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### renderDropdown()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 121](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### searchResultsVisible() → {Boolean}

 

**Description:
 :** 

- 

Check whether search results are currently visible.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 252](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### setMatchedResults(result)

 

**Description:
 :** 

- 

Given a filter has been run across the dataset, store the matched results.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 183](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `result`

 

Array

 

 

 

 

#### setSearchTerms(result)

 

**Description:
 :** 

- 

When a user searches for something, set our variable to manage it.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 210](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `result`

 

string

 

 

 

 

#### toggleDropdown(on)

 

**Description:
 :** 

- 

When called, update the dropdown fields.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 263](lib_amd_src_comboboxsearch_search_combobox.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `on`

 

Boolean

 

 

 `false`

 

Flag to toggle hiding or showing values.

 

 

#### triggerSelector()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 143](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

**Deprecated::** 

- since Moodle 4.4

 

#### (async) updateLiveRegion()

 

**Description:
 :** 

- 

Updates the screen reader live region with the result count.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 391](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### updateNodes()

 

**Description:
 :** 

- 

These class members change when a new result set is rendered. So update for fresh data.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 274](lib_amd_src_comboboxsearch_search_combobox.js.md)
