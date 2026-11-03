# tool_lp/actionselector - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_actionselector.html

# tool_lp/actionselector

 

 

 

**Description:
 :** 

- 

Action selector.

To handle 'save' events use: actionselector.on('save')
This will receive the information to display in popup.
The actions have the format [{'text': sometext, 'value' : somevalue}].

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 16](admin_tool_lp_amd_src_actionselector.js.md)

 

**Copyright:
 :** 

- 2016 Serge Gauthier - 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Action selector.

To handle 'save' events use: actionselector.on('save')
This will receive the information to display in popup.
The actions have the format [{'text': sometext, 'value' : somevalue}].

 

 

 

### Classes

 

**[tool_lp/actionselector](module-tool_lp_actionselector-tool_lp_actionselector.md)
 :** 

 

 

 

### Methods

 

#### (inner) _afterRender()

 

**Description:
 :** 

- 

Hook to executed after the view is rendered.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 76](admin_tool_lp_amd_src_actionselector.js.md)

 

#### (inner) _find(selector) → {JQuery}

 

**Description:
 :** 

- 

Find a node in the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 140](admin_tool_lp_amd_src_actionselector.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

 

 

##### Returns:

The node

**
 Type

 :** 

JQuery

 

#### (inner) _refresh() → {Promise}

 

**Description:
 :** 

- 

Refresh the view.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 151](admin_tool_lp_amd_src_actionselector.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _render() → {Promise}

 

**Description:
 :** 

- 

Render the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 166](admin_tool_lp_amd_src_actionselector.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _reset()

 

**Description:
 :** 

- 

Reset the dialogue properties.

This does not reset everything, just enough to reset the UI.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 184](admin_tool_lp_amd_src_actionselector.js.md)

 

#### (inner) close()

 

**Description:
 :** 

- 

Close the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 111](admin_tool_lp_amd_src_actionselector.js.md)

 

#### (inner) display() → {Promise}

 

**Description:
 :** 

- 

Opens the action selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/actionselector.js](admin_tool_lp_amd_src_actionselector.js.md), [line 122](admin_tool_lp_amd_src_actionselector.js.md)

##### Returns:

**
 Type

 :** 

Promise
