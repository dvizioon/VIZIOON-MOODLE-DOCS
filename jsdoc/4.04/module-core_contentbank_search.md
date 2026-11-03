# core_contentbank/search - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_contentbank_search.html

# core_contentbank/search

 

 

 

**Description:
 :** 

- 

Search methods for finding contents in the content bank.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 16](contentbank_amd_src_search.js.md)

 

**Copyright:
 :** 

- 2020 Sara Arjona 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Search methods for finding contents in the content bank.

 

 

 

 

### Methods

 

#### (inner) filterContents(body, searchTerm) → {Array}

 

**Description:
 :** 

- 

Return the list of contents which have a name that matches the given search term.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 110](contentbank_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `body`

 

HTMLElement

 

The root element for the contentbank.

 
 `searchTerm`

 

String

 

The search term to match.

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) highlight(text, highlightText) → {String}

 

**Description:
 :** 

- 

Highlight a given string in a text.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 137](contentbank_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The whole text.

 
 `highlightText`

 

String

 

The piece of text to highlight.

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) init()

 

**Description:
 :** 

- 

Set up the search.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 30](contentbank_amd_src_search.js.md)

 

#### (inner) registerListenerEvents(root)

 

**Description:
 :** 

- 

Register contentbank search related event listeners.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 44](contentbank_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element for the contentbank.

 

 

#### (inner) toggleSearchResultsView(body, searchQuery)

 

**Description:
 :** 

- 

Toggle (display/hide) the search results depending on the value of the search query.

 

**Source:
 :** 

- 
 [contentbank/amd/src/search.js](contentbank_amd_src_search.js.md), [line 74](contentbank_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `body`

 

HTMLElement

 

The root element for the contentbank.

 
 `searchQuery`

 

String

 

The search query.
