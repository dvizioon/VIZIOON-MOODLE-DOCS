# tool_lp/competencyruleconfig - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_competencyruleconfig.html

# tool_lp/competencyruleconfig

 

 

 

**Description:
 :** 

- 

Competency rule config.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 16](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency rule config.

 

 

 

 

### Methods

 

#### (protected, inner) _afterChange()

 

**Description:
 :** 

- 

After change.

Triggered when a change occured.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 68](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (protected, inner) _afterRender()

 

**Description:
 :** 

- 

After render hook.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 102](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (protected, inner) _afterRuleConfigChange(e, rule)

 

**Description:
 :** 

- 

After change in rule's config.

Triggered when a change occured in a specific rule config.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 84](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 
 `rule`

 

Rule

 

 

 

 

#### (protected, inner) _find(selector) → {JQuery}

 

**Description:
 :** 

- 

Find a node in the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 181](admin_tool_lp_amd_src_competencyruleconfig.js.md)

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

 

#### (protected, inner) _getApplicableOutcomesOptions() → {Array}

 

**Description:
 :** 

- 

Get the applicable outcome options.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 193](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (protected, inner) _getApplicableRulesOptions() → {Array}

 

**Description:
 :** 

- 

Get the applicable rules options.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 215](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (protected, inner) _getConfig() → {Object}

 

**Description:
 :** 

- 

Get the full config for the competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 240](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

Contains rule, ruleoutcome and ruleconfig.

**
 Type

 :** 

Object

 

#### (protected, inner) _getOutcome() → {String}

 

**Description:
 :** 

- 

Get the selected outcome code.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 256](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (protected, inner) _getRule() → {null|Rule}

 

**Description:
 :** 

- 

Get the selected rule.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 267](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

null
|

Rule

 

#### (protected, inner) _getRuleName(type) → {String}

 

**Description:
 :** 

- 

Return the name of a rule.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 288](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

String

 

The type of a rule.

 

##### Returns:

**
 Type

 :** 

String

 

#### (protected, inner) _initOutcomes() → {Promise}

 

**Description:
 :** 

- 

Initialise the outcomes.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 308](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (protected, inner) _initRules() → {Promise}

 

**Description:
 :** 

- 

Initialise the rules.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 323](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (protected, inner) _isValid() → {Boolean}

 

**Description:
 :** 

- 

Whether or not the current config is valid.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 349](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (protected, inner) _preRender() → {Promise}

 

**Description:
 :** 

- 

Hook to executed before render.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 380](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (protected, inner) _render() → {Promise}

 

**Description:
 :** 

- 

Render the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 403](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (protected, inner) _setUp()

 

**Description:
 :** 

- 

Set up the instance.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 446](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (protected, inner) _switchedOutcome()

 

**Description:
 :** 

- 

Called when the user switches outcome.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 483](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (protected, inner) _switchedRule()

 

**Description:
 :** 

- 

Called when the user switches rule.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 507](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (protected, inner) _trigger(type, data)

 

**Description:
 :** 

- 

Trigger an event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 533](admin_tool_lp_amd_src_competencyruleconfig.js.md)

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

 

 

#### (inner) canBeConfigured() → {Boolean}

 

**Description:
 :** 

- 

Whether the current competency can be configured.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 129](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) close()

 

**Description:
 :** 

- 

Close the dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 146](admin_tool_lp_amd_src_competencyruleconfig.js.md)

 

#### (inner) display() → {Promise}

 

**Description:
 :** 

- 

Opens the picker.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 156](admin_tool_lp_amd_src_competencyruleconfig.js.md)

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
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 369](admin_tool_lp_amd_src_competencyruleconfig.js.md)

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

 

 

#### (protected, inner) ready() → {Promise}

 

**Description:
 :** 

- 

Returns a promise that is resolved when the module is ready.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 392](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) setTargetCompetencyId(competencyId)

 

**Description:
 :** 

- 

Set the target competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyruleconfig.js](admin_tool_lp_amd_src_competencyruleconfig.js.md), [line 432](admin_tool_lp_amd_src_competencyruleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competencyId`

 

Number

 

The target competency Id.
