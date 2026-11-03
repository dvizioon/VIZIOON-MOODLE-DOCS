# tool_lp/templateactions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_templateactions.html

# tool_lp/templateactions

 

 

 

**Description:
 :** 

- 

Handle actions on learning plan templates via ajax.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 16](admin_tool_lp_amd_src_templateactions.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle actions on learning plan templates via ajax.

 

 

 

 

### Members

 

#### (inner) Action :Boolean

 

**Description:
 :** 

- 

to apply to plans when deleting a template

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 33](admin_tool_lp_amd_src_templateactions.js.md)

to apply to plans when deleting a template

##### Type:

- 

Boolean

 

 

#### (inner) pagecontextid :Number

 

**Description:
 :** 

- 

The id of the context

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 27](admin_tool_lp_amd_src_templateactions.js.md)

The id of the context

##### Type:

- 

Number

 

 

#### (inner) templateid :Number

 

**Description:
 :** 

- 

The id of the template

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 30](admin_tool_lp_amd_src_templateactions.js.md)

The id of the template

##### Type:

- 

Number

 

 

 

### Methods

 

#### (inner) confirmDelete(e)

 

**Description:
 :** 

- 

Handler for "Delete learning plan template" actions.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 107](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) deleteHandler(e)

 

**Description:
 :** 

- 

Expose the event handler for the delete.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 177](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) doDelete()

 

**Description:
 :** 

- 

Delete a template and reload the page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 60](admin_tool_lp_amd_src_templateactions.js.md)

 

#### (inner) doDuplicate(e)

 

**Description:
 :** 

- 

Duplicate a template and reload the page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 82](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) duplicateHandler(e)

 

**Description:
 :** 

- 

Expose the event handler for the duplicate.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 184](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) init(contextid)

 

**Description:
 :** 

- 

Initialise the module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 191](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextid`

 

Number

 

The context id of the page.

 

 

#### (inner) reloadList(context)

 

**Description:
 :** 

- 

Callback to render the page template again and update the page.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 48](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `context`

 

Object

 

The context for the template.

 

 

#### (inner) updatePage(newhtml, newjs)

 

**Description:
 :** 

- 

Callback to replace the dom element with the rendered template.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/templateactions.js](admin_tool_lp_amd_src_templateactions.js.md), [line 36](admin_tool_lp_amd_src_templateactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newhtml`

 

String

 

The new html to insert.

 
 `newjs`

 

String

 

The new js to run.
