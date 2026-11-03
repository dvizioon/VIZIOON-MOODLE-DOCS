# tool_lp/competencypicker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_competencypicker.html

# tool_lp/competencypicker

 

 

 

**Description:
 :** 

- 

Competency picker.

To handle 'save' events use: picker.on('save')
This will receive a object with either a single 'competencyId', or an array in 'competencyIds'
depending on the value of multiSelect.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 16](admin_tool_lp_amd_src_competencypicker.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency picker.

To handle 'save' events use: picker.on('save')
This will receive a object with either a single 'competencyId', or an array in 'competencyIds'
depending on the value of multiSelect.

 

 

 

 

### Methods

 

#### (inner) _afterRender()

 

**Description:
 :** 

- 

Hook to executed after the view is rendered.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 88](admin_tool_lp_amd_src_competencypicker.js.md)

 

#### (inner) _fetchCompetencies(frameworkId, searchText) → {Promise}

 

**Description:
 :** 

- 

Fetch the competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 223](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `frameworkId`

 

Number

 

The frameworkId.

 
 `searchText`

 

String

 

Limit the competencies to those matching the text.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _find(selector) → {JQuery}

 

**Description:
 :** 

- 

Find a node in the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 274](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

JQuery

 

#### (inner) _getFramework(fid) → {Object}

 

**Description:
 :** 

- 

Convenience method to get a framework object.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 285](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `fid`

 

Number

 

The framework ID.

 

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) _loadCompetencies() → {Promise}

 

**Description:
 :** 

- 

Load the competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 303](admin_tool_lp_amd_src_competencypicker.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _loadFrameworks() → {Promise}

 

**Description:
 :** 

- 

Load the frameworks.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 313](admin_tool_lp_amd_src_competencypicker.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _preRender() → {Promise}

 

**Description:
 :** 

- 

Hook to executed before render.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 363](admin_tool_lp_amd_src_competencypicker.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _refresh() → {Promise}

 

**Description:
 :** 

- 

Refresh the view.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 386](admin_tool_lp_amd_src_competencypicker.js.md)

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
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 401](admin_tool_lp_amd_src_competencypicker.js.md)

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
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 433](admin_tool_lp_amd_src_competencypicker.js.md)

 

#### (inner) _reset(type, data)

 

**Description:
 :** 

- 

Trigger an event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 460](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

String

 

The type of event.

 
 `data`

 

Object

 

The data to pass to the listeners.

 

 

#### (inner) _setDisallowedCompetencyIDs(ids)

 

**Description:
 :** 

- 

Set what competencies cannot be picked.

This needs to be set after reset/close.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 448](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `ids`

 

Array.<Number>

 

The IDs.

 

 

#### (inner) close()

 

**Description:
 :** 

- 

Close the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 193](admin_tool_lp_amd_src_competencypicker.js.md)

 

#### (inner) display() → {Promise}

 

**Description:
 :** 

- 

Opens the picker.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 204](admin_tool_lp_amd_src_competencypicker.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) on(type, handler)

 

**Description:
 :** 

- 

Register an event listener.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker.js](admin_tool_lp_amd_src_competencypicker.js.md), [line 352](admin_tool_lp_amd_src_competencypicker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

String

 

The event type.

 
 `handler`

 

function

 

The event listener.
