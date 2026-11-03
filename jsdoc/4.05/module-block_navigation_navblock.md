# block_navigation/navblock - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-block_navigation_navblock.html

# block_navigation/navblock

 

 

 

**Description:
 :** 

- 

Load the navigation tree javascript.

 

**Source:
 :** 

- 
 [blocks/navigation/amd/src/navblock.js](blocks_navigation_amd_src_navblock.js.md), [line 16](blocks_navigation_amd_src_navblock.js.md)

 

**Copyright:
 :** 

- 2015 John Okely 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Load the navigation tree javascript.

 

 

 

 

### Methods

 

#### (static) init(instanceId)

 

**Description:
 :** 

- 

Initialise the navblock javascript for the specified block instance.

 

**Source:
 :** 

- 
 [blocks/navigation/amd/src/navblock.js](blocks_navigation_amd_src_navblock.js.md), [line 32](blocks_navigation_amd_src_navblock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `instanceId`

 

Number

 

 

 

 

#### (inner) collapseGroup(item)

 

**Description:
 :** 

- 

The method to call whe then the navtree collapses a group

 

**Source:
 :** 

- 
 [blocks/navigation/amd/src/navblock.js](blocks_navigation_amd_src_navblock.js.md), [line 48](blocks_navigation_amd_src_navblock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

 

 

##### Fires:

- [event:blockContentUpdated](module-core_block_events.md)

 

#### (inner) finishExpandingGroup(item)

 

**Description:
 :** 

- 

The method to call when then the navtree finishes expanding a group.

 

**Source:
 :** 

- 
 [blocks/navigation/amd/src/navblock.js](blocks_navigation_amd_src_navblock.js.md), [line 36](blocks_navigation_amd_src_navblock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

Object

 

 

 

##### Fires:

- [event:blockContentUpdated](module-core_block_events.md)
