# tool_behat/steps - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_behat_steps.html

# tool_behat/steps

 

 

 

**Description:
 :** 

- 

Enhancements for the step definitions page.

 

**Source:
 :** 

- 
 [admin/tool/behat/amd/src/steps.js](admin_tool_behat_amd_src_steps.js.md), [line 20](admin_tool_behat_amd_src_steps.js.md)

 

**Author:
 :** 

- [Mark Johnson](mailto:mark.johnson@catalyst-eu.net)

 

 

**Copyright:
 :** 

- 2022 Catalyst IT EU

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Enhancements for the step definitions page.

 

 

 

 

### Methods

 

#### (inner) getGeneratorEntities(entityType) → {Promise}

 

**Description:
 :** 

- 

Call the get_entity_generator web service function

Takes the name of an entity generator and returns an object containing a list of the required fields.

 

**Source:
 :** 

- 
 [admin/tool/behat/amd/src/steps.js](admin_tool_behat_amd_src_steps.js.md), [line 37](admin_tool_behat_amd_src_steps.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entityType`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) getRequiredFieldsContent(entityData) → {Promise}

 

**Description:
 :** 

- 

Render HTML for required fields

Takes the entity data returned from getGeneratorEntities and renders the HTML to display the required fields.

 

**Source:
 :** 

- 
 [admin/tool/behat/amd/src/steps.js](admin_tool_behat_amd_src_steps.js.md), [line 50](admin_tool_behat_amd_src_steps.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entityData`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise
