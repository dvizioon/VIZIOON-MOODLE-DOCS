# core_contentbank/sort - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_contentbank_sort.html

# core_contentbank/sort

 

 

 

**Description:
 :** 

- 

Content bank UI actions.

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 16](contentbank_amd_src_sort.js.md)

 

**Copyright:
 :** 

- 2020 Bas Brands 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Content bank UI actions.

 

 

 

 

### Methods

 

#### (inner) init()

 

**Description:
 :** 

- 

Set up the contentbank views.

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 30](contentbank_amd_src_sort.js.md)

 

#### (inner) registerListenerEvents(contentBank)

 

**Description:
 :** 

- 

Register contentbank related event listeners.

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 42](contentbank_amd_src_sort.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contentBank`

 

HTMLElement

 

The DOM node of the content bank

 

 

#### (inner) setViewListPreference(viewList) → {Promise}

 

**Description:
 :** 

- 

Set the contentbank user preference in list view

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 164](contentbank_amd_src_sort.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `viewList`

 

Bool

 

view ContentBank as list.

 

##### Returns:

Repository promise.

**
 Type

 :** 

Promise

 

#### (inner) updateButtonTitle(button, ascending) → {Promise}

 

**Description:
 :** 

- 

Update the button title.

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 220](contentbank_amd_src_sort.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `button`

 

HTMLElement

 

Button to update

 
 `ascending`

 

Bool

 

Sort direction

 

##### Returns:

string promise

**
 Type

 :** 

Promise

 

#### (inner) updateSortButtons(contentBank, sortButton) → {Bool}

 

**Description:
 :** 

- 

Update the sort button view.

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 175](contentbank_amd_src_sort.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contentBank`

 

HTMLElement

 

The DOM node of the contentbank button

 
 `sortButton`

 

HTMLElement

 

The DOM node of the sort button

 

##### Returns:

sort ascending

**
 Type

 :** 

Bool

 

#### (inner) updateSortOrder(fileArea, itemList, attribute, ascending)

 

**Description:
 :** 

- 

Update the sort order of the itemlist and update the DOM

 

**Source:
 :** 

- 
 [contentbank/amd/src/sort.js](contentbank_amd_src_sort.js.md), [line 243](contentbank_amd_src_sort.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `fileArea`

 

HTMLElement

 

the Dom container for the itemlist

 
 `itemList`

 

Array

 

Nodelist of Dom elements

 
 `attribute`

 

String

 

the attribut to sort on

 
 `ascending`

 

Bool

 

Sort Ascending
