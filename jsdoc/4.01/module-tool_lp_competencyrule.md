# tool_lp/competencyrule - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_competencyrule.html

# tool_lp/competencyrule

 

 

 

**Description:
 :** 

- 

Competency rule base module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 16](admin_tool_lp_amd_src_competency_rule.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency rule base module.

 

 

 

 

### Methods

 

#### (inner) _isValid() → {Boolean}

 

**Description:
 :** 

- 

Whether or not the current config is valid.

Plugins should override this.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 106](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (protected, inner) _load() → {Promise}

 

**Description:
 :** 

- 

Load the class.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 118](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (protected, inner) _trigger(type, data)

 

**Description:
 :** 

- 

Trigger an event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 150](admin_tool_lp_amd_src_competency_rule.js.md)

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

 

 

#### (protected, inner) _triggerChange()

 

**Description:
 :** 

- 

Trigger the change event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 162](admin_tool_lp_amd_src_competency_rule.js.md)

 

#### (inner) canConfig() → {Boolean}

 

**Description:
 :** 

- 

Whether or not the current competency can be configured using this rule.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 52](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) getConfig() → {String|null}

 

**Description:
 :** 

- 

The config established by this rule.

To override in subclasses when relevant.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 62](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

**
 Type

 :** 

String
|

null

 

#### (inner) getType() → {String}

 

**Description:
 :** 

- 

Return the type of the module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 74](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) init() → {Promise}

 

**Description:
 :** 

- 

The init process.

Do not override this, instead override _load.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 84](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

Revoled when the plugin is initialised.

**
 Type

 :** 

Promise

 

#### (inner) injectTemplate() → {Promise}

 

**Description:
 :** 

- 

Callback to inject the template.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 96](admin_tool_lp_amd_src_competency_rule.js.md)

##### Returns:

Resolved when done.

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
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 129](admin_tool_lp_amd_src_competency_rule.js.md)

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

 

 

#### (inner) setTargetCompetency(competency)

 

**Description:
 :** 

- 

Sets the current competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_rule.js](admin_tool_lp_amd_src_competency_rule.js.md), [line 140](admin_tool_lp_amd_src_competency_rule.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competency`

 

Competency
