# enrol_manual/quickenrolment - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-enrol_manual_quickenrolment.html

# enrol_manual/quickenrolment

 

 

 

**Description:
 :** 

- 

Quick enrolment AMD module.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 16](enrol_manual_amd_src_quickenrolment.js.md)

 

**Copyright:
 :** 

- 2016 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Quick enrolment AMD module.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Set up quick enrolment for the manual enrolment plugin.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 191](enrol_manual_amd_src_quickenrolment.js.md)

Set up quick enrolment for the manual enrolment plugin.

 

 

### Methods

 

#### (inner) getBodyForContext(contextId) → {Promise}

 

**Description:
 :** 

- 

Get the content of the body for the specified context.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 48](enrol_manual_amd_src_quickenrolment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

Number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) getDynamicTableForElement(element) → {HTMLElement}

 

**Description:
 :** 

- 

Get the dynamic table for the button.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 58](enrol_manual_amd_src_quickenrolment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) registerEventListeners(contextId)

 

**Description:
 :** 

- 

Register the event listeners for this contextid.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 69](enrol_manual_amd_src_quickenrolment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

Number

 

 

 

 

#### (inner) showModal(dynamicTable, contextId) → {Promise}

 

**Description:
 :** 

- 

Display the modal for this contextId.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 88](enrol_manual_amd_src_quickenrolment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dynamicTable`

 

HTMLElement

 

The table to beb refreshed when changes are made

 
 `contextId`

 

Number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) submitFormAjax(dynamicTable, modal)

 

**Description:
 :** 

- 

Submit the form via ajax.

 

**Source:
 :** 

- 
 [enrol/manual/amd/src/quickenrolment.js](enrol_manual_amd_src_quickenrolment.js.md), [line 144](enrol_manual_amd_src_quickenrolment.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dynamicTable`

 

HTMLElement

 

 

 
 `modal`

 

Object
