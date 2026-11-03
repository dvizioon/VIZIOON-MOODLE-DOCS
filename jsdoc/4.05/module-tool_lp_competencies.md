# tool_lp/competencies - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_competencies.html

# tool_lp/competencies

 

 

 

**Description:
 :** 

- 

Handle add/remove competency links.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 16](admin_tool_lp_amd_src_competencies.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle add/remove competency links.

 

 

 

### Classes

 

**[tool_lp/competencies](module-tool_lp_competencies-tool_lp_competencies.md)
 :** 

 

 

 

### Methods

 

#### (inner) deleteHandler(deleteid)

 

**Description:
 :** 

- 

Show a confirm dialogue before deleting a competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 254](admin_tool_lp_amd_src_competencies.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `deleteid`

 

int

 

The id of record to delete.

 

 

#### (inner) doDelete(deleteid)

 

**Description:
 :** 

- 

Delete the link between competency and course, template or plan. Reload the page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 203](admin_tool_lp_amd_src_competencies.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `deleteid`

 

int

 

The id of record to delete.

 

 

#### (inner) handleDrop(drag, drop)

 

**Description:
 :** 

- 

Handle a drop from a drag/drop operation.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 76](admin_tool_lp_amd_src_competencies.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `drag`

 

DOMNode

 

The dragged node.

 
 `drop`

 

DOMNode

 

The dropped on node.

 

 

#### (inner) pickCompetency() → {Promise}

 

**Description:
 :** 

- 

Pick a competency

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 117](admin_tool_lp_amd_src_competencies.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) registerDragDrop()

 

**Description:
 :** 

- 

Initialise the drag/drop code.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 52](admin_tool_lp_amd_src_competencies.js.md)

 

#### (inner) registerEvents()

 

**Description:
 :** 

- 

Register the javascript event handlers for this page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencies.js](admin_tool_lp_amd_src_competencies.js.md), [line 300](admin_tool_lp_amd_src_competencies.js.md)
