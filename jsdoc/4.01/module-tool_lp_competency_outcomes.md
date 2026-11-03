# tool_lp/competency_outcomes - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_competency_outcomes.html

# tool_lp/competency_outcomes

 

 

 

**Description:
 :** 

- 

Competency rule config.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_outcomes.js](admin_tool_lp_amd_src_competency_outcomes.js.md), [line 16](admin_tool_lp_amd_src_competency_outcomes.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Competency rule config.

 

 

 

 

### Methods

 

#### (inner) getAll() → {Object}

 

**Description:
 :** 

- 

Get all the outcomes.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_outcomes.js](admin_tool_lp_amd_src_competency_outcomes.js.md), [line 40](admin_tool_lp_amd_src_competency_outcomes.js.md)

##### Returns:

Indexed by outcome code, contains code and name.

**
 Type

 :** 

Object

 

#### (inner) getString(id) → {Promise}

 

**Description:
 :** 

- 

Get the string for an outcome.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competency_outcomes.js](admin_tool_lp_amd_src_competency_outcomes.js.md), [line 63](admin_tool_lp_amd_src_competency_outcomes.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The outcome code.

 

##### Returns:

Resolved with the string.

**
 Type

 :** 

Promise
