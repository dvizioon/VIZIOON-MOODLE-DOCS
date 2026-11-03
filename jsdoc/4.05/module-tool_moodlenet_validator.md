# tool_moodlenet/validator - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_moodlenet_validator.html

# tool_moodlenet/validator

 

 

 

**Description:
 :** 

- 

Our validator that splits the user's input then fires off to a webservice

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/validator.js](admin_tool_moodlenet_amd_src_validator.js.md), [line 16](admin_tool_moodlenet_amd_src_validator.js.md)

 

**Copyright:
 :** 

- 2020 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Our validator that splits the user's input then fires off to a webservice

 

 

 

 

### Methods

 

#### (inner) validation(inputElement) → {Promise}

 

**Description:
 :** 

- 

Handle form validation

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/validator.js](admin_tool_moodlenet_amd_src_validator.js.md), [line 24](admin_tool_moodlenet_amd_src_validator.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `inputElement`

 

HTMLElement

 

The element the user entered text into.

 

##### Returns:

Was the users' entry a valid profile URL?

**
 Type

 :** 

Promise
