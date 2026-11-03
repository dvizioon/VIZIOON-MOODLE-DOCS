# core/menu_navigation - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_menu_navigation.html

# core/menu_navigation

 

 

 

**Description:
 :** 

- 

Keyboard initialization for a given html node.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 16](lib_amd_src_menu_navigation.js.md)

 

**Author:
 :** 

- Mathew May <mathew.solutions>

 

 

**Copyright:
 :** 

- 2021 Moodle

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Keyboard initialization for a given html node.

 

 

 

 

### Methods

 

#### (inner) clickErrorHandler(item, fallback) → {HTMLElement}

 

**Description:
 :** 

- 

Small helper function to check if a given node is null or not.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 40](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

HTMLElement
|

null

 

The node that we want to compare.

 
 `fallback`

 

HTMLElement

 

Either the first node or final node that can be focused on.

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) clickListenerEvents(e)

 

**Description:
 :** 

- 

Defined click event handling so we can remove listeners on nodes on resize etc.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 164](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

event

 

The triggering element and key presses etc.

 

 

#### (inner) findUsableLastNode(elementRoot) → {HTMLElement}

 

**Description:
 :** 

- 

We need to look within the menu to find a last node we can add focus to.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 242](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementRoot`

 

HTMLElement

 

Menu to find a final child node within.

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) keyboardListenerEvents(e)

 

**Description:
 :** 

- 

Defined keyboard event handling so we can remove listeners on nodes on resize etc.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 92](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

event

 

The triggering element and key presses etc.

 

 

#### (inner) menuItemHelper(src)

 

**Description:
 :** 

- 

Control classes etc of the selected dropdown item and its' parent 

**:** 

  - [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 53](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `src`

 

HTMLElement

 

The node within the dropdown the user selected.

 

 

#### (inner) setFocusHomeEnd(node)

 

**Description:
 :** 

  - 

Focus on either the start or end of a nav list.

 

**Source:
 :** 

  - 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 232](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

HTMLElement

 

The element to focus on.

 

 

#### (inner) setFocusNext(currentNode, firstNode)

 

**Description:
 :** 

  - 

Handle the focusing to the next element in the dropdown.

 

**Source:
 :** 

  - 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 189](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentNode`

 

HTMLElement
|

null

 

The node that we want to take action on.

 
 `firstNode`

 

HTMLElement

 

The backup node to focus as a last resort.

 

 

#### (inner) setFocusPrev(currentNode, lastNode)

 

**Description:
 :** 

  - 

Handle the focusing to the previous element in the dropdown.

 

**Source:
 :** 

  - 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 211](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentNode`

 

HTMLElement
|

null

 

The node that we want to take action on.

 
 `lastNode`

 

HTMLElement

 

The backup node to focus as a last resort.
