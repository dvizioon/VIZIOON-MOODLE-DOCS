# tool_lp/competencypicker_user_plans - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_lp_competencypicker_user_plans.html

# tool_lp/competencypicker_user_plans

 

 

 

**Description:
 :** 

- 

Competency picker from user plans.

To handle 'save' events use: picker.on('save').

This will receive a object with either a single 'competencyId', or an array in 'competencyIds'
depending on the value of multiSelect.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 16](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency picker from user plans.

To handle 'save' events use: picker.on('save').

This will receive a object with either a single 'competencyId', or an array in 'competencyIds'
depending on the value of multiSelect.

 

 

 

### Classes

 

**[tool_lp/competencypicker_user_plans](module-tool_lp_competencypicker_user_plans-tool_lp_competencypicker_user_plans.md)
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
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 68](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

 

#### (inner) _fetchCompetencies(planId, searchText) → {Promise}

 

**Description:
 :** 

- 

Fetch the competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 87](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `planId`

 

Number

 

The planId.

 
 `searchText`

 

String

 

Limit the competencies to those matching the text.

 

##### Returns:

The promise object.

**
 Type

 :** 

Promise

 

#### (inner) _getPlan(id) → {Object|undefined}

 

**Description:
 :** 

- 

Convenience method to get a plan object.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 122](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The plan ID.

 

##### Returns:

The plan.

**
 Type

 :** 

Object
|

undefined

 

#### (inner) _loadCompetencies() → {Promise}

 

**Description:
 :** 

- 

Load the competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 140](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) _loadPlans() → {Promise}

 

**Description:
 :** 

- 

Load the plans.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 150](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

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
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 186](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

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
 [admin/tool/lp/amd/src/competencypicker_user_plans.js](admin_tool_lp_amd_src_competencypicker_user_plans.js.md), [line 209](admin_tool_lp_amd_src_competencypicker_user_plans.js.md)

##### Returns:

**
 Type

 :** 

Promise
