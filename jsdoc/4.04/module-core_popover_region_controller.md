# core/popover_region_controller - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_popover_region_controller.html

# core/popover_region_controller

 

 

 

**Description:
 :** 

- 

Controls the popover region element.

See template: core/popover_region

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 16](lib_amd_src_popover_region_controller.js.md)

 

**Since:
 :** 

- 3.2

 

**Copyright:
 :** 

- 2015 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the popover region element.

See template: core/popover_region

 

 

 

 

### Methods

 

#### (inner) closeMenu()

 

**Description:
 :** 

- 

Hide the popover.

Note: This triggers the menuClosed event.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 115](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) contentItemHasFocus() → {bool}

 

**Description:
 :** 

- 

Check if a content item has focus.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 215](lib_amd_src_popover_region_controller.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) focusContentItem(item)

 

**Description:
 :** 

- 

Focus the given content item or the first focusable element within
the content item.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 243](lib_amd_src_popover_region_controller.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

object

 

The content item jQuery element

 

 

#### (inner) focusFirstContentItem()

 

**Description:
 :** 

- 

Set focus on the first content item in the list.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 258](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) focusLastContentItem()

 

**Description:
 :** 

- 

Set focus on the last content item in the list.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 267](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) focusMenuToggle()

 

**Description:
 :** 

- 

Sets the focus on the menu toggle.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 206](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) focusNextContentItem()

 

**Description:
 :** 

- 

Set focus on the content item after the item that currently has focus
in the list.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 276](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) focusPreviousContentItem()

 

**Description:
 :** 

- 

Set focus on the content item preceding the item that currently has focus
in the list.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 290](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) getContent() → {jQuery}

 

**Description:
 :** 

- 

Return the content element.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 82](lib_amd_src_popover_region_controller.js.md)

##### Returns:

object

**
 Type

 :** 

jQuery

 

#### (inner) getContentContainer() → {jQuery}

 

**Description:
 :** 

- 

Return the container element for the content element.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 72](lib_amd_src_popover_region_controller.js.md)

##### Returns:

object

**
 Type

 :** 

jQuery

 

#### (inner) getContentItemWithFocus() → {jQuery}

 

**Description:
 :** 

- 

Return the currently focused content item.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 225](lib_amd_src_popover_region_controller.js.md)

##### Returns:

object

**
 Type

 :** 

jQuery

 

#### (inner) isMenuOpen() → {bool}

 

**Description:
 :** 

- 

Checks if the popover is displayed.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 92](lib_amd_src_popover_region_controller.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) openMenu()

 

**Description:
 :** 

- 

Show the popover.

Note: This triggers the menuOpened event.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 136](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) registerBaseEventListeners()

 

**Description:
 :** 

- 

Register the minimal amount of listeners for the popover to function.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 304](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) registerListNavigationEventListeners()

 

**Description:
 :** 

- 

Set up the event listeners for keyboard navigating a list of content items.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 343](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) startLoading()

 

**Description:
 :** 

- 

Set the loading state on this popover.

Note: This triggers the startLoading event.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 178](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) stopLoading()

 

**Description:
 :** 

- 

Undo the loading state on this popover.

Note: This triggers the stopLoading event.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 192](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) toggleMenu()

 

**Description:
 :** 

- 

Toggle the visibility of the popover.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 102](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) updateButtonAriaLabel()

 

**Description:
 :** 

- 

Set the appropriate aria label on the popover toggle.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 161](lib_amd_src_popover_region_controller.js.md)

 

#### (inner) updateFocusItemTabIndex()

 

**Description:
 :** 

- 

Set the appropriate tabindex attribute on the popover toggle.

 

**Source:
 :** 

- 
 [lib/amd/src/popover_region_controller.js](lib_amd_src_popover_region_controller.js.md), [line 398](lib_amd_src_popover_region_controller.js.md)
