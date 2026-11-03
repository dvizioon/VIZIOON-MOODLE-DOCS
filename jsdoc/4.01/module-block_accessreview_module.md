# block_accessreview/module - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-block_accessreview_module.html

# block_accessreview/module

 

 

 

**Description:
 :** 

- 

Manager for the accessreview block.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 16](blocks_accessreview_amd_src_module.js.md)

 

**Author:
 :** 

- [Max Larkin](mailto:max@brickfieldlabs.ie)

 

 

**Copyright:
 :** 

- 2020 Brickfield Education Labs 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Manager for the accessreview block.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Setting up the access review module.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 294](blocks_accessreview_amd_src_module.js.md)

Setting up the access review module.

 

#### (inner, constant) numColours :number

 

**Description:
 :** 

- 

The number of colours used to represent the heatmap. (Indexed on 0.)

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 33](blocks_accessreview_amd_src_module.js.md)

The number of colours used to represent the heatmap. (Indexed on 0.)

##### Type:

- 

number

 

 

#### (inner) toggleState :boolean

 

**Description:
 :** 

- 

The toggle state of the heatmap.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 39](blocks_accessreview_amd_src_module.js.md)

The toggle state of the heatmap.

##### Type:

- 

boolean

 

 

 

### Methods

 

#### (inner) fetchReviewData(courseid, updatePreference) → {Array.<Promise>}

 

**Description:
 :** 

- 

Fetch the review data.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 269](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `courseid`

 

Number

 

 

 

 

 
 `updatePreference`

 

Boolean

 

 

 `false`

 

 

 

##### Returns:

**
 Type

 :** 

Array.<Promise>

 

#### (inner) getErrorTotals(sectionData, moduleData) → {Object}

 

**Description:
 :** 

- 

Parses information on the errors, generating the min, max and totals.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 207](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionData`

 

Array.<Object>

 

The error data for course sections.

 
 `moduleData`

 

Array.<Object>

 

The error data for course modules.

 

##### Returns:

An object representing the extra error information.

**
 Type

 :** 

Object

 

#### (inner) getTogglePreferenceParams(toggleState) → {Promise}

 

**Description:
 :** 

- 

Set the user preference for the toggle value.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 248](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleState`

 

Boolean

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) hideAccessMap(updatePreference)

 

**Description:
 :** 

- 

Hides or removes the templates from the HTML of the current page.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 159](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `updatePreference`

 

Boolean

 

 

 `false`

 

 

 

 

#### (inner) renderTemplate(element, errorCount, checkCount, displayFormat, minViews, viewDelta) → {Promise}

 

**Description:
 :** 

- 

Renders the HTML template onto a particular HTML element.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 51](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The element to attach the HTML to.

 
 `errorCount`

 

number

 

The number of errors on this module/section.

 
 `checkCount`

 

number

 

The number of checks triggered on this module/section.

 
 `displayFormat`

 

String

 

 

 
 `minViews`

 

Number

 

 

 
 `viewDelta`

 

Number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) showAccessMap(courseId, displayFormat, updatePreference) → {Promise}

 

**Description:
 :** 

- 

Applies the template to all sections and modules on the course page.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 116](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `courseId`

 

Number

 

 

 

 

 
 `displayFormat`

 

String

 

 

 

 

 
 `updatePreference`

 

Boolean

 

 

 `false`

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) toggleAccessMap(courseId, displayFormat)

 

**Description:
 :** 

- 

Toggles the heatmap on/off.

 

**Source:
 :** 

- 
 [blocks/accessreview/amd/src/module.js](blocks_accessreview_amd_src_module.js.md), [line 191](blocks_accessreview_amd_src_module.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

 

 
 `displayFormat`

 

String
