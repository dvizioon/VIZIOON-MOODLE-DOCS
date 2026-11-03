# module:core_group/groupPicker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_group_groupPicker.html

# module:core_group/groupPicker

 

## 

 module:core_group/groupPicker

 

 

 

 

#### new (require("core_group/groupPicker"))(elementId)

 

**Description:
 :** 

- 

Creates the group picker class and finds the corresponding DOM element.

 

**Source:
 :** 

- 
 [group/amd/src/grouppicker.js](group_amd_src_grouppicker.js.md), [line 33](group_amd_src_grouppicker.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `elementId`

 

String

 

 

 `groups`

 

The DOM element id of the  input

 

##### Throws:

 

Error if the element was not found.

 

 

 

### Classes

 

**[core_group/GroupPicker](module-core_group_groupPicker-core_group_GroupPicker.md)
 :** 

 

 

 

### Methods

 

#### getDomElement() → {HTMLElement}

 

**Description:
 :** 

- 

Returns the DOM element this class is linked to.

 

**Source:
 :** 

- 
 [group/amd/src/grouppicker.js](group_amd_src_grouppicker.js.md), [line 48](group_amd_src_grouppicker.js.md)

##### Returns:

The DOM element

**
 Type

 :** 

HTMLElement

 

#### getSelectedValues() → {Array.<Number>}

 

**Description:
 :** 

- 

Returns the selected group values.

 

**Source:
 :** 

- 
 [group/amd/src/grouppicker.js](group_amd_src_grouppicker.js.md), [line 57](group_amd_src_grouppicker.js.md)

##### Returns:

The group IDs that are currently selected.

**
 Type

 :** 

Array.<Number>
