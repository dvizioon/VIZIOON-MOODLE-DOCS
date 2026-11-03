# tool_lp/scaleconfig - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_scaleconfig.html

# tool_lp/scaleconfig

 

 

 

**Description:
 :** 

- 

Handle opening a dialogue to configure scale data.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 16](admin_tool_lp_amd_src_scaleconfig.js.md)

 

**Copyright:
 :** 

- 2015 Adrian Greeve 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handle opening a dialogue to configure scale data.

 

 

 

 

### Members

 

#### (inner) Reference :Dialogue

 

**Description:
 :** 

- 

to the popup.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 55](admin_tool_lp_amd_src_scaleconfig.js.md)

to the popup.

##### Type:

- 

Dialogue

 

 

#### (inner) The :String

 

**Description:
 :** 

- 

select box selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 43](admin_tool_lp_amd_src_scaleconfig.js.md)

select box selector.

##### Type:

- 

String

 

 

#### (inner) The :String

 

**Description:
 :** 

- 

hidden field selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 45](admin_tool_lp_amd_src_scaleconfig.js.md)

hidden field selector.

##### Type:

- 

String

 

 

#### (inner) The :String

 

**Description:
 :** 

- 

trigger selector.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 47](admin_tool_lp_amd_src_scaleconfig.js.md)

trigger selector.

##### Type:

- 

String

 

 

#### (inner) scaleid :Number

 

**Description:
 :** 

- 

Current scale ID.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 53](admin_tool_lp_amd_src_scaleconfig.js.md)

Current scale ID.

##### Type:

- 

Number

 

 

#### (inner) scalevalues :Array

 

**Description:
 :** 

- 

ID and name of the scales.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 49](admin_tool_lp_amd_src_scaleconfig.js.md)

ID and name of the scales.

##### Type:

- 

Array

 

 

#### (inner) {Number)

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 51](admin_tool_lp_amd_src_scaleconfig.js.md)

 

 

### Methods

 

#### (inner) getScaleValues(scaleid) → {Promise}

 

**Description:
 :** 

- 

Get the scale values for the selected scale.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 181](admin_tool_lp_amd_src_scaleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `scaleid`

 

Number

 

The scale ID of the selected scale.

 

##### Returns:

A deffered object with the scale values.

**
 Type

 :** 

Promise

 

#### (inner) init(selectSelector, inputSelector, triggerSelector) → {ScaleConfig}

 

**Description:
 :** 

- 

Main initialisation.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 213](admin_tool_lp_amd_src_scaleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectSelector`

 

String

 

The select box selector.

 
 `inputSelector`

 

String

 

The hidden input field selector.

 
 `triggerSelector`

 

String

 

The trigger selector.

 

##### Returns:

A new instance of ScaleConfig.

**
 Type

 :** 

ScaleConfig

 

#### (inner) initScaleConfig(popup)

 

**Description:
 :** 

- 

Initialises the scale configuration dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 112](admin_tool_lp_amd_src_scaleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `popup`

 

Dialogue

 

Dialogue object to initialise.

 

 

#### (inner) retrieveOriginalScaleConfig() → {Object|String}

 

**Description:
 :** 

- 

Gets the original scale configuration if it was set.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 92](admin_tool_lp_amd_src_scaleconfig.js.md)

##### Returns:

scale configuration or empty string.

**
 Type

 :** 

Object
|

String

 

#### (inner) scaleChangeHandler(e)

 

**Description:
 :** 

- 

Triggered when a scale is selected.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 195](admin_tool_lp_amd_src_scaleconfig.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) setScaleConfig()

 

**Description:
 :** 

- 

Set the scale configuration back into a JSON string in the hidden element.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 145](admin_tool_lp_amd_src_scaleconfig.js.md)

 

#### (inner) showConfig()

 

**Description:
 :** 

- 

Displays the scale configuration dialogue.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/scaleconfig.js](admin_tool_lp_amd_src_scaleconfig.js.md), [line 58](admin_tool_lp_amd_src_scaleconfig.js.md)
