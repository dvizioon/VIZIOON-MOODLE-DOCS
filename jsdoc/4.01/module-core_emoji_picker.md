# core/emoji/picker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_emoji_picker.html

# core/emoji/picker

 

 

 

**Description:
 :** 

- 

Emoji picker.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 16](lib_amd_src_emoji_picker.js.md)

 

**Copyright:
 :** 

- 2019 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Emoji picker.

 

 

 

 

### Methods

 

#### (inner) addIndexesToRowData(rowData) → {Array}

 

**Description:
 :** 

- 

Add each row's index to it's value in the row data.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 89](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowData`

 

Array

 

List of emoji row data

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) addRecentEmoji(rowData, recentEmojiRowCount, newEmoji) → {Array}

 

**Description:
 :** 

- 

Add an emoji data to the set of recent emojis. This function will update the row
data to ensure that the recent emoji rows are correct and all of the rows are
re-indexed.

The new set of recent emojis are saved in local storage and the full set of updated
row data and new emoji row count are returned.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 307](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowData`

 

Array

 

The emoji rows data

 
 `recentEmojiRowCount`

 

Number

 

Count of the recent emoji rows

 
 `newEmoji`

 

Object

 

The emoji data for the emoji to add to the recent emoji list

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) clearSearch(emojiContainer, searchResultsContainer, searchInput)

 

**Description:
 :** 

- 

Hide the search result container and show the emojis container.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 529](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `emojiContainer`

 

Element

 

The emojis container

 
 `searchResultsContainer`

 

Element

 

The search results container

 
 `searchInput`

 

Element

 

The search input

 

 

#### (async, inner) createEmojiRow(rowIndex, emojis) → {Element}

 

**Description:
 :** 

- 

Create an emoji row element.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 139](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowIndex`

 

Number

 

Index of the row in the row data

 
 `emojis`

 

Array

 

The list of emoji data for the row

 

##### Returns:

**
 Type

 :** 

Element

 

#### (async, inner) createHeaderRow(rowIndex, name) → {Element}

 

**Description:
 :** 

- 

Create a header row element for the category name.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 120](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowIndex`

 

Number

 

Index of the row in the row data

 
 `name`

 

String

 

The category display name

 

##### Returns:

**
 Type

 :** 

Element

 

#### (inner) createRowDataForCategory(categoryName, categoryDisplayName, emojis, totalRowCount) → {Array}

 

**Description:
 :** 

- 

Create the row data for a category.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 59](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `categoryName`

 

String

 

The category name

 
 `categoryDisplayName`

 

String

 

The category display name

 
 `emojis`

 

Array

 

The emoji data

 
 `totalRowCount`

 

Number

 

The total number of rows generated so far

 

##### Returns:

**
 Type

 :** 

Array

 

#### (async, inner) createRowElement(rowData) → {Element}

 

**Description:
 :** 

- 

Create a row element from the row data.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 354](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowData`

 

Object

 

The emoji row data

 

##### Returns:

**
 Type

 :** 

Element

 

#### (inner) doRowsMatch(a, b) → {Bool}

 

**Description:
 :** 

- 

Check if the given rows match.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 378](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `a`

 

Object

 

The first row

 
 `b`

 

Object

 

The second row

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) findCategorySelectorFromElement(element) → {Element|null}

 

**Description:
 :** 

- 

Search from an element and up through it's ancestors to fine the category
selector element and return it.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 177](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

Element to begin searching from

 

##### Returns:

**
 Type

 :** 

Element
|

null

 

#### (inner) generateRenderRowsAtPositionFunction(rowContainer) → {function}

 

**Description:
 :** 

- 

Build a function to render the visible emoji rows for a given scroll
position.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 472](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowContainer`

 

Element

 

The container element for the emoji rows

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getCategoryByScrollPosition(root, position, categoryScrollPositions) → {Array}

 

**Description:
 :** 

- 

Get the category selector element and the scroll positions for the previous and
next categories for the given scroll position.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 221](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The picker root element

 
 `position`

 

Number

 

The position to get the category for

 
 `categoryScrollPositions`

 

Object

 

Set of scroll positions for all categories

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getCategoryScrollPositionsFromRowData(rowData) → {Object}

 

**Description:
 :** 

- 

Calculate the scroll position for the beginning of each category from
the row data.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 103](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowData`

 

Array

 

List of emoji row data

 

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) getHandleClick(recentEmojiRowCount, emojiContainer, searchResultsContainer, searchInput, selectCallback, renderAtPosition) → {function}

 

**Description:
 :** 

- 

Build the function to handle a user clicking something in the picker.

The function currently handles clicking on the category selector or selecting
a specific emoji.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 586](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `recentEmojiRowCount`

 

Number

 

Number of rows of recent emojis

 
 `emojiContainer`

 

Element

 

Container element for the visible of emojis

 
 `searchResultsContainer`

 

Element

 

Contaienr element for the search results

 
 `searchInput`

 

Element

 

Search input element

 
 `selectCallback`

 

function

 

Callback function to execute when a user selects an emoji

 
 `renderAtPosition`

 

function

 

Render function to display current visible emojis

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getHandleMouseEnter(emojiPreview, emojiShortName) → {function}

 

**Description:
 :** 

- 

Build function to handle mouse hovering an emoji. Shows the preview.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 543](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `emojiPreview`

 

Element

 

The emoji preview element

 
 `emojiShortName`

 

Element

 

The emoji short name element

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getHandleMouseLeave(emojiPreview, emojiShortName) → {function}

 

**Description:
 :** 

- 

Build function to handle mouse leaving an emoji. Removes the preview.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 561](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `emojiPreview`

 

Element

 

The emoji preview element

 
 `emojiShortName`

 

Element

 

The emoji short name element

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getHandleScroll(root, currentVisibleRowScrollPosition, emojiContainer, initialCategoryScrollPositions, renderAtPosition) → {function}

 

**Description:
 :** 

- 

Build the function that handles scrolling of the emoji container to display the
correct emojis.

We render the emoji rows as they are needed rather than all up front so that we
can avoid adding tends of thousands of elements to the DOM unnecessarily which
would bog down performance.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 658](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The picker root element

 
 `currentVisibleRowScrollPosition`

 

Number

 

The current scroll position of the container

 
 `emojiContainer`

 

Element

 

The emojis container element

 
 `initialCategoryScrollPositions`

 

Object

 

Scroll positions for each category

 
 `renderAtPosition`

 

function

 

Function to render the appropriate emojis for a scroll position

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getHandleSearch(searchInput, searchResultsContainer, emojiContainer) → {function}

 

**Description:
 :** 

- 

Build the function that handles search input from the user.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 719](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchInput`

 

Element

 

The search input element

 
 `searchResultsContainer`

 

Element

 

Container element to display the search results

 
 `emojiContainer`

 

Element

 

Container element for the emoji rows

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getRecentEmojis() → {Array}

 

**Description:
 :** 

- 

Get the list of recent emojis data from local storage.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 278](lib_amd_src_emoji_picker.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getRowsToRender(scrollPosition, visibleRowCount, rowData) → {Array}

 

**Description:
 :** 

- 

Calculate which rows should be visible based on the given scroll position. Adds a
buffer to amount to either side of the total number of requested rows so that
scrolling the emoji rows container is smooth.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 339](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `scrollPosition`

 

Number

 

Scroll position within the emoji container

 
 `visibleRowCount`

 

Number

 

How many rows should be visible

 
 `rowData`

 

Array

 

The emoji rows data

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) isEmojiElement(element) → {Bool}

 

**Description:
 :** 

- 

Check if the element is an emoji element.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 167](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

Element to check

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) registerEventListeners(root, emojiContainer, renderAtPosition, currentVisibleRowScrollPosition, selectCallback, categoryScrollPositions, rowData, recentEmojiRowCount)

 

**Description:
 :** 

- 

Register the emoji picker event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 767](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The picker root element

 
 `emojiContainer`

 

Element

 

Root element containing the list of visible emojis

 
 `renderAtPosition`

 

function

 

Function to render the visible emojis at a given scroll position

 
 `currentVisibleRowScrollPosition`

 

Number

 

What is the current scroll position

 
 `selectCallback`

 

function

 

Function to execute when the user picks an emoji

 
 `categoryScrollPositions`

 

Object

 

Scroll positions for where each of the emoji categories begin

 
 `rowData`

 

Array

 

Data representing each of the display rows for hte emoji container

 
 `recentEmojiRowCount`

 

Number

 

Number of rows of recent emojis

 

 

#### (async, inner) renderRows(rowContainer, currentRows, nextRows)

 

**Description:
 :** 

- 

Update the visible rows. Deletes any row elements that should no longer
be visible and creates the newly visible row elements. Any rows that haven't
changed visibility will be left untouched.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 418](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rowContainer`

 

Element

 

The container element for the emoji rows

 
 `currentRows`

 

Array

 

List of row data that matches the currently visible rows

 
 `nextRows`

 

Array

 

List of row data containing the new list of rows to be made visible

 

 

#### (inner) saveRecentEmoji(recentEmojis)

 

**Description:
 :** 

- 

Save the list of recent emojis in local storage.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 289](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `recentEmojis`

 

Array

 

List of emoji data to save

 

 

#### (inner) setCategorySelectorActive(root, element)

 

**Description:
 :** 

- 

Sets the given category selector element as active.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 200](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The root picker element

 
 `element`

 

Element

 

The category selector element to make active

 

 

#### (inner) showSearchResults(emojiContainer, searchResultsContainer)

 

**Description:
 :** 

- 

Show the search results container and hide the emoji container.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 516](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `emojiContainer`

 

Element

 

The emojis container

 
 `searchResultsContainer`

 

Element

 

The search results container
