# tool_analytics/model - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_analytics_model.html

# tool_analytics/model

 

 

 

**Description:
 :** 

- 

AMD module for model actions confirmation.

 

**Source:
 :** 

- 
 [admin/tool/analytics/amd/src/model.js](admin_tool_analytics_amd_src_model.js.md), [line 16](admin_tool_analytics_amd_src_model.js.md)

 

**Copyright:
 :** 

- 2017 David Monllao

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

AMD module for model actions confirmation.

 

 

 

 

### Methods

 

#### (inner) confirmAction(actionId, actionType)

 

**Description:
 :** 

- 

Displays a confirm modal window before executing the action.

 

**Source:
 :** 

- 
 [admin/tool/analytics/amd/src/model.js](admin_tool_analytics_amd_src_model.js.md), [line 80](admin_tool_analytics_amd_src_model.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actionId`

 

String

 

 

 
 `actionType`

 

String

 

 

 

 

#### (inner) selectEvaluationOptions(actionId, trainedOnlyExternally)

 

**Description:
 :** 

- 

Displays evaluation mode and time-splitting method choices.

 

**Source:
 :** 

- 
 [admin/tool/analytics/amd/src/model.js](admin_tool_analytics_amd_src_model.js.md), [line 119](admin_tool_analytics_amd_src_model.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actionId`

 

String

 

 

 
 `trainedOnlyExternally`

 

Boolean

 

 

 

 

#### (inner) selectExportOptions(actionId, isTrained)

 

**Description:
 :** 

- 

Displays export options.

We have two main options: export training data and export configuration.
The 2nd option has an extra option: include the trained algorithm weights.

 

**Source:
 :** 

- 
 [admin/tool/analytics/amd/src/model.js](admin_tool_analytics_amd_src_model.js.md), [line 169](admin_tool_analytics_amd_src_model.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actionId`

 

String

 

 

 
 `isTrained`

 

Boolean
