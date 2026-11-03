# tool_lp/competencyactions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_competencyactions.html

# tool_lp/competencyactions

 

 

 

**Description:
 :** 

- 

Handle selection changes and actions on the competency tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 16](admin_tool_lp_amd_src_competencyactions.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle selection changes and actions on the competency tree.

 

 

 

 

### Members

 

#### (inner) Picker :Object

 

**Description:
 :** 

- 

instance.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 51](admin_tool_lp_amd_src_competencyactions.js.md)

instance.

##### Type:

- 

Object

 

 

#### (inner) Rule :Object

 

**Description:
 :** 

- 

config instance.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 53](admin_tool_lp_amd_src_competencyactions.js.md)

config instance.

##### Type:

- 

Object

 

 

#### (inner) Taxonomy :Object

 

**Description:
 :** 

- 

constants indexed per level.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 57](admin_tool_lp_amd_src_competencyactions.js.md)

constants indexed per level.

##### Type:

- 

Object

 

 

#### (inner) The :Object

 

**Description:
 :** 

- 

competency we're picking a relation to.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 55](admin_tool_lp_amd_src_competencyactions.js.md)

competency we're picking a relation to.

##### Type:

- 

Object

 

 

#### (inner) The :Array

 

**Description:
 :** 

- 

rules modules. Values are object containing type, namd and amd.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 59](admin_tool_lp_amd_src_competencyactions.js.md)

rules modules. Values are object containing type, namd and amd.

##### Type:

- 

Array

 

 

#### (inner) moveSource :Node

 

**Description:
 :** 

- 

The start of a drag operation

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 45](admin_tool_lp_amd_src_competencyactions.js.md)

The start of a drag operation

##### Type:

- 

Node

 

 

#### (inner) moveTarget :Node

 

**Description:
 :** 

- 

The end of a drag operation

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 47](admin_tool_lp_amd_src_competencyactions.js.md)

The end of a drag operation

##### Type:

- 

Node

 

 

#### (inner) pageContextId :Number

 

**Description:
 :** 

- 

The page context ID.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 49](admin_tool_lp_amd_src_competencyactions.js.md)

The page context ID.

##### Type:

- 

Number

 

 

#### (inner) the :Number

 

**Description:
 :** 

- 

selected competency ID.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 61](admin_tool_lp_amd_src_competencyactions.js.md)

selected competency ID.

##### Type:

- 

Number

 

 

#### (inner) treeModel :Object

 

**Description:
 :** 

- 

This is an object representing the nodes in the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 43](admin_tool_lp_amd_src_competencyactions.js.md)

This is an object representing the nodes in the tree.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) addCompetencyChildren(parent, competencies)

 

**Description:
 :** 

- 

Turn a flat list of competencies into a tree structure (recursive).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 202](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `parent`

 

Object

 

The current parent node in the tree

 
 `competencies`

 

Array.<Object>

 

The flat list of competencies

 

 

#### (inner) addHandler()

 

**Description:
 :** 

- 

Respond to choosing the "Add" menu item for the selected node in the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 64](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) allowDrop(e)

 

**Description:
 :** 

- 

HTML5 implementation of drag/drop (there is an accesible alternative in the menus).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 554](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) confirmMove()

 

**Description:
 :** 

- 

Confirms a competency move.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 123](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) deleteCompetencyHandler()

 

**Description:
 :** 

- 

Show a confirm dialogue before deleting a competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 517](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) deleteRelatedHandler(e)

 

**Description:
 :** 

- 

Deletes a related competency without confirmation.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 598](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event that triggered the action.

 

 

#### (inner) doDelete()

 

**Description:
 :** 

- 

Delete a competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 486](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) doMove()

 

**Description:
 :** 

- 

A source and destination has been chosen - so time to complete a move.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 106](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) dragEnter(e)

 

**Description:
 :** 

- 

HTML5 implementation of drag/drop (there is an accesible alternative in the menus).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 564](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) dragLeave(e)

 

**Description:
 :** 

- 

HTML5 implementation of drag/drop (there is an accesible alternative in the menus).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 574](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) dragStart(e)

 

**Description:
 :** 

- 

HTML5 implementation of drag/drop (there is an accesible alternative in the menus).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 545](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) dropOver(e)

 

**Description:
 :** 

- 

HTML5 implementation of drag/drop (there is an accesible alternative in the menus).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 584](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) editHandler()

 

**Description:
 :** 

- 

Edit the selected competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 293](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) getTaxonomyAtLevel(level) → {String}

 

**Description:
 :** 

- 

Return the taxonomy constant for a level.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 653](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `level`

 

Number

 

The level.

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) init(model, pagectxid, taxonomies, rulesMods)

 

**Description:
 :** 

- 

Initialise this page (attach event handlers etc).

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 821](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `model`

 

Object

 

The tree model provides some useful functions for loading and searching competencies.

 
 `pagectxid`

 

Number

 

The page context ID.

 
 `taxonomies`

 

Object

 

Constants indexed by level.

 
 `rulesMods`

 

Object

 

The modules of the rules.

 

 

#### (inner) initMovePopup(popup)

 

**Description:
 :** 

- 

A move competency popup was opened - initialise the aria tree in it.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 178](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `popup`

 

dialogue

 

The tool_lp/dialogue that was created.

 

 

#### (inner) moveDownHandler()

 

**Description:
 :** 

- 

Move a competency "down". This only affects the sort order within the same branch of the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 361](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) moveHandler(e)

 

**Description:
 :** 

- 

A node was chosen and "Move" was selected from the menu. Open a popup to select the target.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 222](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) moveUpHandler()

 

**Description:
 :** 

- 

Move a competency "up". This only affects the sort order within the same branch of the tree.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 343](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) parseTaxonomies(taxonomiesstr) → {Array}

 

**Description:
 :** 

- 

Return the string "Selected ".

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 804](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `taxonomiesstr`

 

String

 

Comma separated list of taxonomies.

 

##### Returns:

of level => taxonomystr

**
 Type

 :** 

Array

 

#### (inner) relateCompetenciesHandler()

 

**Description:
 :** 

- 

Open a competencies popup to relate competencies.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 407](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) reloadPage(context)

 

**Description:
 :** 

- 

Re-render the page with the latest data.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 311](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `context`

 

Object

 

 

 

 

#### (inner) seeCoursesHandler()

 

**Description:
 :** 

- 

Open a dialogue to show all the courses using the selected competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 379](admin_tool_lp_amd_src_competencyactions.js.md)

 

#### (inner) selectionChanged(evt, params) → {Boolean}

 

**Description:
 :** 

- 

Handler when a node in the aria tree is selected.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 749](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `evt`

 

Event

 

The event that triggered the selection change.

 
 `params`

 

Object

 

The parameters for the event. Contains a list of selected nodes.

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) strAddTaxonomy(level) → {String}

 

**Description:
 :** 

- 

Return the string "Add ".

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 727](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `level`

 

Number

 

The level.

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) strSelectedTaxonomy(level) → {String}

 

**Description:
 :** 

- 

Return the string "Selected ".

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 738](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `level`

 

Number

 

The level.

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) triggerCompetencyViewedEvent(competency)

 

**Description:
 :** 

- 

Log the competency viewed event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 636](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `competency`

 

Object

 

The competency.

 

 

#### (inner) updateSearchHandler(e)

 

**Description:
 :** 

- 

Perform a search and render the page with the new search results.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 325](admin_tool_lp_amd_src_competencyactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) updatedRelatedCompetencies()

 

**Description:
 :** 

- 

Updates the competencies list (with relations) and add listeners.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/competencyactions.js](admin_tool_lp_amd_src_competencyactions.js.md), [line 624](admin_tool_lp_amd_src_competencyactions.js.md)
