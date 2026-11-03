# module:core/bulkactions/bulk_actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_bulkactions_bulk_actions.html

# module:core/bulkactions/bulk_actions

 

## 

 module:core/bulkactions/bulk_actions

 

 

 

 

#### new (require("core/bulkactions/bulk_actions"))(maxButtons) → {void}

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 61](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `maxButtons`

 

int
|

null

 

 

 `null`

 

Sets the maximum number of action buttons to display. If exceeded, additional actions
are shown in a dropdown menu.

 

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

 

 

#### maxButtons

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 52](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `maxButtons`

 

int

 

Sets the maximum number of action buttons to display. If exceeded, additional actions
are shown in a dropdown menu.

 

 

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

 

#### (inner) deselectItem(selectedItem) → {void}

 

**Description:
 :** 

- 

Defines the action for deselecting a selected item.

The base bulk actions class supports deselecting all selected items but does not have knowledge of the type of the
selected element. Therefore, each subclass must explicitly define the action of resetting the attributes that
indicate a selected state.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 119](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectedItem`

 

HTMLElement

 

The selected element.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) disableBulkActionsMode() → {void}

 

**Description:
 :** 

- 

Disables the bulk action mode.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 185](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

void

 

#### (inner) enableBulkActionsMode() → {Promise.<void>}

 

**Description:
 :** 

- 

Enables the bulk action mode.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 144](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (inner) getBulkActions() → {Array}

 

**Description:
 :** 

- 

Returns the array of the relevant bulk action objects.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 87](lib_amd_src_bulkactions_bulk_actions.js.md)

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
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 97](lib_amd_src_bulkactions_bulk_actions.js.md)

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
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 134](lib_amd_src_bulkactions_bulk_actions.js.md)

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
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 107](lib_amd_src_bulkactions_bulk_actions.js.md)

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

 

#### (inner) renderBulkActions() → {Promise.<string>}

 

**Description:
 :** 

- 

Renders the bulk actions content.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 201](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

Promise.<string>

 

#### (inner) updateBulkItemSelection() → {void}

 

**Description:
 :** 

- 

Updates the selected items count in the bulk actions content.

 

**Source:
 :** 

- 
 [lib/amd/src/bulkactions/bulk_actions.js](lib_amd_src_bulkactions_bulk_actions.js.md), [line 241](lib_amd_src_bulkactions_bulk_actions.js.md)

##### Returns:

**
 Type

 :** 

void
