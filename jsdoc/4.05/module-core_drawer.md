# core/drawer - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_drawer.html

# core/drawer

 

 

 

**Description:
 :** 

- 

Controls the drawer.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 16](lib_amd_src_drawer.js.md)

 

**Copyright:
 :** 

- 2019 Jun Pataleta 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the drawer.

 

 

 

 

### Methods

 

#### (inner) getDrawerRoot(contentRoot) → {*|jQuery}

 

**Description:
 :** 

- 

Find the root element of the drawer based on the using the drawer content root's ID.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 119](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contentRoot`

 

Object

 

The drawer content's root element.

 

##### Returns:

**
 Type

 :** 

*
|

jQuery

 

#### (inner) hide(root)

 

**Description:
 :** 

- 

Hide the drawer.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 49](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The drawer container.

 

 

#### (inner) isVisible(root) → {boolean}

 

**Description:
 :** 

- 

Check if the drawer is visible.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 65](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The drawer container.

 

##### Returns:

**
 Type

 :** 

boolean

 

#### (inner) registerToggles(root, toggleElements)

 

**Description:
 :** 

- 

Add event listeners to toggle the drawer.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 89](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The drawer container.

 
 `toggleElements`

 

Object

 

The toggle elements.

 

 

#### (inner) show(root)

 

**Description:
 :** 

- 

Show the drawer.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 33](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The drawer container.

 

 

#### (inner) toggle(root)

 

**Description:
 :** 

- 

Toggle the drawer visibility.

 

**Source:
 :** 

- 
 [lib/amd/src/drawer.js](lib_amd_src_drawer.js.md), [line 75](lib_amd_src_drawer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The drawer container.
