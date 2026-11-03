# tool_lp/dragdrop-reorder - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_lp_dragdrop-reorder.html

# tool_lp/dragdrop-reorder

 

 

 

**Description:
 :** 

- 

Drag and drop reorder via HTML5.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/dragdrop-reorder.js](admin_tool_lp_amd_src_dragdrop-reorder.js.md), [line 16](admin_tool_lp_amd_src_dragdrop-reorder.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Drag and drop reorder via HTML5.

 

 

 

 

### Methods

 

#### (static) dragdrop(group, dragHandleText, sameNodeText, parentNodeText, sameNodeClass, parentNodeClass, dragHandleInsertClass, callback)

 

**Description:
 :** 

- 

Create an instance of M.tool_lp.dragdrop

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/dragdrop-reorder.js](admin_tool_lp_amd_src_dragdrop-reorder.js.md), [line 58](admin_tool_lp_amd_src_dragdrop-reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `group`

 

String

 

Unique string to identify this interaction.

 
 `dragHandleText`

 

String

 

Alt text for the drag handle.

 
 `sameNodeText`

 

String

 

Used in keyboard drag drop for the list of items target.

 
 `parentNodeText`

 

String

 

Used in keyboard drag drop for the parent target.

 
 `sameNodeClass`

 

String

 

class used to find the each of the list of items.

 
 `parentNodeClass`

 

String

 

class used to find the container for the list of items.

 
 `dragHandleInsertClass`

 

String

 

class used to find the location to insert the drag handles.

 
 `callback`

 

function

 

Drop hit handler.
