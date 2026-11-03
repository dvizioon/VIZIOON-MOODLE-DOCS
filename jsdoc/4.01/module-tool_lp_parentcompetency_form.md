# tool_lp/parentcompetency_form - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_lp_parentcompetency_form.html

# tool_lp/parentcompetency_form

 

 

 

**Description:
 :** 

- 

Handle selecting parent competency in competency form.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 16](admin_tool_lp_amd_src_parentcompetency_form.js.md)

 

**Copyright:
 :** 

- 2015 Issam Taboubi 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle selecting parent competency in competency form.

 

 

 

 

### Members

 

#### (inner) The :String

 

**Description:
 :** 

- 

parent competency button selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 49](admin_tool_lp_amd_src_parentcompetency_form.js.md)

parent competency button selector.

##### Type:

- 

String

 

 

#### (inner) The :String

 

**Description:
 :** 

- 

hidden input field selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 51](admin_tool_lp_amd_src_parentcompetency_form.js.md)

hidden input field selector.

##### Type:

- 

String

 

 

#### (inner) The :String

 

**Description:
 :** 

- 

static element displaying the parent competency.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 53](admin_tool_lp_amd_src_parentcompetency_form.js.md)

static element displaying the parent competency.

##### Type:

- 

String

 

 

#### (inner) The :Number

 

**Description:
 :** 

- 

competency framework ID.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 55](admin_tool_lp_amd_src_parentcompetency_form.js.md)

competency framework ID.

##### Type:

- 

Number

 

 

#### (inner) The :Number

 

**Description:
 :** 

- 

page context ID.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 57](admin_tool_lp_amd_src_parentcompetency_form.js.md)

page context ID.

##### Type:

- 

Number

 

 

 

### Methods

 

#### (inner) init(buttonSelector, inputSelector, staticElementSelector, frameworkId, pageContextId)

 

**Description:
 :** 

- 

Main initialisation.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 129](admin_tool_lp_amd_src_parentcompetency_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `buttonSelector`

 

String

 

The parent competency button selector.

 
 `inputSelector`

 

String

 

The hidden input field selector.

 
 `staticElementSelector`

 

String

 

The static element displaying the parent competency.

 
 `frameworkId`

 

Number

 

The competency framework ID.

 
 `pageContextId`

 

Number

 

The page context ID.

 

 

#### (inner) registerEvents()

 

**Description:
 :** 

- 

Register the events of parent competency button click.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 88](admin_tool_lp_amd_src_parentcompetency_form.js.md)

 

#### (inner) setParent(data)

 

**Description:
 :** 

- 

Set the parent competency in the competency form.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/parentcompetency_form.js](admin_tool_lp_amd_src_parentcompetency_form.js.md), [line 60](admin_tool_lp_amd_src_parentcompetency_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `data`

 

Object

 

Data containing selected competency.
