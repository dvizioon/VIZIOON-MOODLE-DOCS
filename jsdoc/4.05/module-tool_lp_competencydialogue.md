# tool_lp/competencydialogue - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_competencydialogue.html

# tool_lp/competencydialogue

 

 

 

**Description:
 :** 

- 

Display Competency in dialogue box.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 16](admin_tool_lp_amd_src_competencydialogue.js.md)

 

**Copyright:
 :** 

- 2015 Issam Taboubi 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Display Competency in dialogue box.

 

 

 

 

### Methods

 

#### (static) init()

 

**Description:
 :** 

- 

Initialise the competency dialogue module.

Only the first call matters.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 162](admin_tool_lp_amd_src_competencydialogue.js.md)

 

#### (inner) clickEventHandler(e)

 

**Description:
 :** 

- 

The action on the click event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 109](admin_tool_lp_amd_src_competencydialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

event click

 

 

#### (inner) getCompetencyDataPromise(competencyid, options) → {Promise}

 

**Description:
 :** 

- 

Get a promise on data competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 131](admin_tool_lp_amd_src_competencydialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competencyid`

 

Number

 

 

 
 `options`

 

Object

 

 

 

##### Returns:

return promise on data request

**
 Type

 :** 

Promise

 

#### (inner) showDialogue(competencyid, options)

 

**Description:
 :** 

- 

Display a dialogue box by competencyid.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 58](admin_tool_lp_amd_src_competencydialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competencyid`

 

Number

 

The competency ID.

 
 `options`

 

Object

 

The options.

 

 

#### (inner) showDialogueFromData(dataSource)

 

**Description:
 :** 

- 

Display a dialogue box from data.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 85](admin_tool_lp_amd_src_competencydialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dataSource`

 

Object

 

data to be used to display dialogue box

 

 

#### (inner) triggerCompetencyViewedEvent(competencyId)

 

**Description:
 :** 

- 

Log the competency viewed event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencydialogue.js](admin_tool_lp_amd_src_competencydialogue.js.md), [line 45](admin_tool_lp_amd_src_competencydialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competencyId`

 

Number

 

The competency ID.
