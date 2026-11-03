# tool_lp/menubar - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_lp_menubar.html

# tool_lp/menubar

 

 

 

**Description:
 :** 

- 

Aria menubar functionality. Enhances a simple nested list structure into a full aria widget.
Based on the open ajax example: http://oaa-accessibility.org/example/26/

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 16](admin_tool_lp_amd_src_menubar.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Aria menubar functionality. Enhances a simple nested list structure into a full aria widget.
Based on the open ajax example: http://oaa-accessibility.org/example/26/

 

 

 

 

### Methods

 

#### (inner) addAriaAttributes()

 

**Description:
 :** 

- 

Enhance the dom with aria attributes.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 777](admin_tool_lp_amd_src_menubar.js.md)

 

#### (inner) addEventListeners()

 

**Description:
 :** 

- 

Bind the event listeners to the DOM

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 90](admin_tool_lp_amd_src_menubar.js.md)

 

#### (inner) closeAll()

 

**Description:
 :** 

- 

Handy function to close all open menus anywhere on the page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 836](admin_tool_lp_amd_src_menubar.js.md)

 

#### (inner) closeAllSubMenus()

 

**Description:
 :** 

- 

Close all open submenus anywhere in the page (there should only ever be one open at a time).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 32](admin_tool_lp_amd_src_menubar.js.md)

 

#### (inner) enhance(selector, handler)

 

**Description:
 :** 

- 

Create a menu bar object for every node matching the selector.

The expected DOM structure is shown below.

 <- This is the target of the selector parameter.

  -  <- This is repeated for each top level menu.
 Text <- This is the text for the top level menu.

 <- This is a list of the entries in this top level menu.

    -  <- This is repeated for each menu entry.
 [Choice 1](someurl) <- The anchor for the menu.

 

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 800](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

The selector for the outer most menu node.

 
 `handler`

 

function

 

Javascript handler for when a menu item was chosen. If the
handler returns true (or does not exist), the
menu will look for an anchor with a link to follow.
For example, if the menu entry has a "data-action" attribute
and we want to call a javascript function when that entry is chosen,
we could pass a list of handlers like this:
{ "[data-action='add']" : callAddFunction }

 

 

#### (inner) handleClick(item, e) → {boolean}

 

**Description:
 :** 

- 

Process click events for the top menus.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 140](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the jquery object of the item firing the event

 
 `e`

 

Event

 

is the associated event object

 

##### Returns:

Returns false

**
 Type

 :** 

boolean

 

#### (inner) moveDown(item, startChr) → {Object}

 

**Description:
 :** 

- 

Member function to select the next item in a menu.
If the active item is the last in the menu, this function will loop to the
first menu item.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 644](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the active menu item

 
 `startChr`

 

String

 

is the character to attempt to match against the beginning of the
menu item titles. If found, focus moves to the next menu item beginning with that character.

 

##### Returns:

Returns the item to move to. Returns item is no move is possible

**
 Type

 :** 

Object

 

#### (inner) moveToNext(item) → {Object}

 

**Description:
 :** 

- 

Move to the next menu level.
This will be either the next root-level menu or the child of a menu parent. If
at the root level and the active item is the last in the menu, this function will loop
to the first menu item.

If the menu is a horizontal menu, the first child element of the newly selected menu will
be selected

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 409](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the active menu item

 

##### Returns:

Returns the item to move to. Returns item is no move is possible

**
 Type

 :** 

Object

 

#### (inner) moveToPrevious(item) → {Object}

 

**Description:
 :** 

- 

Member function to move to the previous menu level.
This will be either the previous root-level menu or the child of a menu parent. If
at the root level and the active item is the first in the menu, this function will loop
to the last menu item.

If the menu is a horizontal menu, the first child element of the newly selected menu will
be selected

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 528](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the active menu item

 

##### Returns:

Returns the item to move to. Returns item is no move is possible

**
 Type

 :** 

Object

 

#### (inner) moveUp(item) → {Object}

 

**Description:
 :** 

- 

Function moveUp() is a member function to select the previous item in a menu.
If the active item is the first in the menu, this function will loop to the
last menu item.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 739](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

is the active menu item

 

##### Returns:

Returns the item to move to. Returns item is no move is possible

**
 Type

 :** 

Object

 

#### (inner) openSubMenu(menu)

 

**Description:
 :** 

- 

Open a submenu, first it closes all other sub-menus and sets the open direction.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/menubar.js](admin_tool_lp_amd_src_menubar.js.md), [line 76](admin_tool_lp_amd_src_menubar.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `menu`

 

Node
