# module:core/bulkactions/bulk_actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_bulkactions_bulk_actions.html

# module:core/bulkactions/bulk_actions

 

## 

 module:core/bulkactions/bulk_actions

 

 

 

 

#### new (require("core/bulkactions/bulk_actions"))() → {void}

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 53](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

void

 

 

 

### Members

 

#### initialStickyFooterContent

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 40](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `initialStickyFooterContent`

 

string
|

null

 

The initial content of the sticky footer.

 

 

#### isBulkActionsModeEnabled

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 46](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `isBulkActionsModeEnabled`

 

boolean

 

Whether the bulk actions mode is enabled.

 

 

#### selectedItems

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 43](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `selectedItems`

 

Array

 

The array of selected item elements.

 

 

#### (inner, constant) The :Object

 

**Description:
 :** 

- 

object containing the relevant selectors.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 28](lib_amd_src_bulkactions_bulk_actions.js.md)

object containing the relevant selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) disableBulkActionsMode() → {void}

 

**Description:
 :** 

- 

Disables the bulk action mode.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 151](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

void

 

#### (inner) enableBulkActionsMode() → {Promise}

 

**Description:
 :** 

- 

Enables the bulk action mode.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 118](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) getBulkActions() → {Array}

 

**Description:
 :** 

- 

Returns the array of the relevant bulk action objects.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 76](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getSelectedItems() → {Array}

 

**Description:
 :** 

- 

Returns the array of selected items.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 86](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getStickyFooterContainer() → {HTMLElement}

 

**Description:
 :** 

- 

Returns the sticky footer container.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 108](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) registerItemSelectChangeEvent(eventHandler) → {void}

 

**Description:
 :** 

- 

Adds the listener for the item select change event.
The event handler function that is passed as a parameter should be called right after the event is triggered.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 96](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventHandler`

 

function

 

The event handler function.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) renderBulkActions() → {Promise}

 

**Description:
 :** 

- 

Renders the bulk actions content.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 167](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) updateBulkItemSelection() → {void}

 

**Description:
 :** 

- 

Updates the selected items count in the bulk actions content.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 186](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

void
