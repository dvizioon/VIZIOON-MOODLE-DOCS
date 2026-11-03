# tool_lp/competency_rule_points - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_competency_rule_points.html

# tool_lp/competency_rule_points

 

 

 

**Description:
 :** 

- 

Competency rule points module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 16](admin_tool_lp_amd_src_competency_rule_points.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency rule points module.

 

 

 

 

### Methods

 

#### (protected, inner) _getCompetenciesConfig() → {Array}

 

**Description:
 :** 

- 

Gathers the input provided by the user for competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 59](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Returns:

Containing id, points and required.

**
 Type

 :** 

Array

 

#### (protected, inner) _getRequiredPoints() → {Number}

 

**Description:
 :** 

- 

Fetches the required points set by the user.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 85](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getConfig() → {String}

 

**Description:
 :** 

- 

The config established by this rule.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 44](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getType() → {String}

 

**Description:
 :** 

- 

Return the type of the module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 96](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) injectTemplate(container) → {Promise}

 

**Description:
 :** 

- 

Callback to inject the template.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 106](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Node

 

Node to inject in.

 

##### Returns:

Resolved when done.

**
 Type

 :** 

Promise

 

#### (inner) isValid() → {Boolean}

 

**Description:
 :** 

- 

Whether or not the current config is valid.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule_points.js](admin_tool_lp_amd_src_competency_rule_points.js.md), [line 173](admin_tool_lp_amd_src_competency_rule_points.js.md)

##### Returns:

**
 Type

 :** 

Boolean
