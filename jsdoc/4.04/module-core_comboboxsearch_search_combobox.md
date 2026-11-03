# core/comboboxsearch/search_combobox - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_comboboxsearch_search_combobox.html

# core/comboboxsearch/search_combobox

 

 

 

**Description:
 :** 

- 

The class that manages the state of the search within a combobox.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 20](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 380](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 355](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 234](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 126](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### dropdownSelector()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 133](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### fetchDataset()

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 97](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### filterDataset(dataset)

 

**Description:
 :** 

- 

Stub out a required function.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 105](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 112](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### (async) filterrenderpipe() → {Promise.<void>}

 

**Description:
 :** 

- 

Update any changeable nodes, filter and then render the result.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 328](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 150](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 163](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 218](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 172](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 199](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 190](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 292](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### registerClickHandlers()

 

**Description:
 :** 

- 

Register clickable event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 284](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### registerInputHandlers()

 

**Description:
 :** 

- 

Register input event listener for the text input area.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 300](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### (async) renderAndShow() → {Promise.<void>}

 

**Description:
 :** 

- 

A combo method to take the matching fields and render out the results.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 340](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 119](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

#### searchResultsVisible() → {Boolean}

 

**Description:
 :** 

- 

Check whether search results are currently visible.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 250](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 181](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 208](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 261](lib_amd_src_comboboxsearch_search_combobox.js.md)

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
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 141](lib_amd_src_comboboxsearch_search_combobox.js.md)

 

**Deprecated::** 

- since Moodle 4.4

 

#### updateNodes()

 

**Description:
 :** 

- 

These class members change when a new result set is rendered. So update for fresh data.

 

**Source:
 :** 

- 
 [lib/amd/src/comboboxsearch/search_combobox.js](lib_amd_src_comboboxsearch_search_combobox.js.md), [line 272](lib_amd_src_comboboxsearch_search_combobox.js.md)
