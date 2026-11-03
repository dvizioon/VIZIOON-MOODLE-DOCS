# tool_lp/form_competency_element - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_form_competency_element.html

# tool_lp/form_competency_element

 

 

 

**Description:
 :** 

- 

Badge select competency actions

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/form_competency_element.js](admin_tool_lp_amd_src_form_competency_element.js.md), [line 16](admin_tool_lp_amd_src_form_competency_element.js.md)

 

**Copyright:
 :** 

- 2019 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Badge select competency actions

 

 

 

 

### Methods

 

#### (inner) init(contextId)

 

**Description:
 :** 

- 

Listen for clicks on the competency picker and push the changes to the form element.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/form_competency_element.js](admin_tool_lp_amd_src_form_competency_element.js.md), [line 124](admin_tool_lp_amd_src_form_competency_element.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

Integer

 

 

 

 

#### (inner) pickCompetenciesHandler()

 

**Description:
 :** 

- 

Open a competencies popup to relate competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/form_competency_element.js](admin_tool_lp_amd_src_form_competency_element.js.md), [line 95](admin_tool_lp_amd_src_form_competency_element.js.md)

 

#### (inner) renderCompetencies() → {boolean}

 

**Description:
 :** 

- 

Re-render the list of selected competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/form_competency_element.js](admin_tool_lp_amd_src_form_competency_element.js.md), [line 30](admin_tool_lp_amd_src_form_competency_element.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### (inner) unpickCompetenciesHandler(e) → {boolean}

 

**Description:
 :** 

- 

Deselect a competency

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/form_competency_element.js](admin_tool_lp_amd_src_form_competency_element.js.md), [line 71](admin_tool_lp_amd_src_form_competency_element.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

##### Returns:

**
 Type

 :** 

boolean
