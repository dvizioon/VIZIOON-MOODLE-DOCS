# core/moremenu - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_moremenu.html

# core/moremenu

 

 

 

**Description:
 :** 

- 

Moves wrapping navigation items into a more menu.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 16](lib_amd_src_moremenu.js.md)

 

**Author:
 :** 

- [Bas Brands](mailto:bas@moodle.com)

 

 

**Copyright:
 :** 

- 2021 Moodle

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Moves wrapping navigation items into a more menu.

 

 

 

 

### Members

 

#### (inner, constant) Selectors

 

**Description:
 :** 

- 

Moremenu selectors.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 30](lib_amd_src_moremenu.js.md)

Moremenu selectors.

 

 

### Methods

 

#### (inner) autoCollapse(menu)

 

**Description:
 :** 

- 

Auto Collapse navigation items that wrap into a dropdown menu.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 57](lib_amd_src_moremenu.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `menu`

 

HTMLElement

 

The navbar container.

 

 

#### (inner) moveIntoMoreDropdown(menu, navNode, prepend)

 

**Description:
 :** 

- 

Move a node into the "more" dropdown menu.

This method forces a given navigation node to be added and displayed within the "more" dropdown menu.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 122](lib_amd_src_moremenu.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `menu`

 

HTMLElement

 

 

 

The navbar moremenu.

 
 `navNode`

 

HTMLElement

 

 

 

The navigation node.

 
 `prepend`

 

boolean

 

 

 `false`

 

Whether to prepend or append the node to the content in the more dropdown menu.

 

 

#### (inner) moveOutOfMoreDropdown(menu, navNode)

 

**Description:
 :** 

- 

Move a node out of the "more" dropdown menu.

This method forces a given node from the "more" dropdown menu to be displayed in the main section of the menu.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 162](lib_amd_src_moremenu.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `menu`

 

HTMLElement

 

The navbar moremenu.

 
 `navNode`

 

HTMLElement

 

The navigation node.
