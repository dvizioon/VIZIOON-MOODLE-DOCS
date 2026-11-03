# tool_lp/Competencydialogue - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_Competencydialogue.html

# tool_lp/Competencydialogue

 

 

 

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
