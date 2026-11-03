# tool_lp/competencytree - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_competencytree.html

# tool_lp/competencytree

 

 

 

**Description:
 :** 

- 

Handle selection changes on the competency tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 16](admin_tool_lp_amd_src_competencytree.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle selection changes on the competency tree.

 

 

 

 

### Members

 

#### (inner) competencies :Array.<Object>

 

**Description:
 :** 

- 

Cached list of competencies

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 27](admin_tool_lp_amd_src_competencytree.js.md)

Cached list of competencies

##### Type:

- 

Array.<Object>

 

 

#### (inner) competencyFrameworkId :Number

 

**Description:
 :** 

- 

The current framework id

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 30](admin_tool_lp_amd_src_competencytree.js.md)

The current framework id

##### Type:

- 

Number

 

 

#### (inner) competencyFrameworkShortName :String

 

**Description:
 :** 

- 

The current framework short name

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 33](admin_tool_lp_amd_src_competencytree.js.md)

The current framework short name

##### Type:

- 

String

 

 

#### (inner) competencyFramworkCanManage :Boolean

 

**Description:
 :** 

- 

Can manage the competencies framework

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 42](admin_tool_lp_amd_src_competencytree.js.md)

Can manage the competencies framework

##### Type:

- 

Boolean

 

 

#### (inner) currentNodeId :String

 

**Description:
 :** 

- 

The data-id of the current node in the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 39](admin_tool_lp_amd_src_competencytree.js.md)

The data-id of the current node in the tree.

##### Type:

- 

String

 

 

#### (inner) treeSelector :String

 

**Description:
 :** 

- 

The selector for the root of the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 36](admin_tool_lp_amd_src_competencytree.js.md)

The selector for the root of the tree.

##### Type:

- 

String

 

 

 

### Methods

 

#### (static) getCompetency(id) → {Object}

 

**Description:
 :** 

- 

Get a competency by id

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 204](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency id

 

##### Returns:

**
 Type

 :** 

Object

 

#### (static) getCompetencyFrameworkId() → {Number}

 

**Description:
 :** 

- 

Get the competency framework id this model was initiliased with.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 194](admin_tool_lp_amd_src_competencytree.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (static) getCompetencyLevel(id) → {Number}

 

**Description:
 :** 

- 

Get the competency level.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 214](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency ID.

 

##### Returns:

**
 Type

 :** 

Number

 

#### (static) hasRule(id) → {Boolean}

 

**Description:
 :** 

- 

Does the competency have a rule?

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 237](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency ID.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (static) init(id, shortname, search, selector, canmanage, competencyid)

 

**Description:
 :** 

- 

Initialise the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 145](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency framework id.

 
 `shortname`

 

String

 

The framework shortname

 
 `search`

 

String

 

The current search string

 
 `selector`

 

String

 

The selector for the tree div

 
 `canmanage`

 

Boolean

 

Can manage the competencies

 
 `competencyid`

 

Number

 

The id of the competency to show first

 

 

#### (static) listCompetencies() → {Array.<Object>}

 

**Description:
 :** 

- 

Get all competencies for this framework.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 260](admin_tool_lp_amd_src_competencytree.js.md)

##### Returns:

**
 Type

 :** 

Array.<Object>

 

#### (static) on(eventname, handler)

 

**Description:
 :** 

- 

Add an event handler for custom events emitted by the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 164](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventname`

 

String

 

The name of the event - only "selectionchanged" for now

 
 `handler`

 

function

 

The handler for the event.

 

 

#### (inner) getChildren(id) → {Array}

 

**Description:
 :** 

- 

Get the children of a competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 172](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency ID.

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) hasChildren(id) → {Boolean}

 

**Description:
 :** 

- 

Whether a competency has children.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 220](admin_tool_lp_amd_src_competencytree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The competency ID.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) reloadCompetencies() → {Promise}

 

**Description:
 :** 

- 

Reload all the page competencies framework competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencytree.js](admin_tool_lp_amd_src_competencytree.js.md), [line 246](admin_tool_lp_amd_src_competencytree.js.md)

##### Returns:

**
 Type

 :** 

Promise
