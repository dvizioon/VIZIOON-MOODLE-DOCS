# core/bulkactions/bulk_action - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_bulkactions_bulk_action.html

# core/bulkactions/bulk_action

 

 

 

**Description:
 :** 

- 

Base class for defining a bulk action.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 16](lib_amd_src_bulkactions_bulk_action.js.md)

 

**Copyright:
 :** 

- 2023 Mihail Geshoski 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Base class for defining a bulk action.

 

 

 

 

### Members

 

#### selectedItems

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 27](lib_amd_src_bulkactions_bulk_action.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `selectedItems`

 

array

 

The array of selected item elements.

 

 

 

### Methods

 

#### (inner) getBulkActionTriggerSelector() → {string}

 

**Description:
 :** 

- 

Defines the selector of the element that triggers the bulk action.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 57](lib_amd_src_bulkactions_bulk_action.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) registerListenerEvents(containerElement) → {void}

 

**Description:
 :** 

- 

Registers the listener events for the bulk actions.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 29](lib_amd_src_bulkactions_bulk_action.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `containerElement`

 

HTMLElement

 

The container element for the bulk actions.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) renderBulkActionTrigger() → {Promise}

 

**Description:
 :** 

- 

Renders the bulk action trigger element.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 76](lib_amd_src_bulkactions_bulk_action.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) setSelectedItems(selectedItems) → {void}

 

**Description:
 :** 

- 

Setter method for the selectedItems property.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 46](lib_amd_src_bulkactions_bulk_action.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectedItems`

 

Array

 

The array of selected item elements..

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) triggerBulkAction()

 

**Description:
 :** 

- 

Defines the behavior once the bulk action is triggered.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_action.js](lib_amd_src_bulkactions_bulk_action.js.md), [line 67](lib_amd_src_bulkactions_bulk_action.js.md)
