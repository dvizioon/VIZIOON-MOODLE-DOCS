# core/moodlenet/send_resource - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_moodlenet_send_resource.html

# core/moodlenet/send_resource

 

 

 

**Description:
 :** 

- 

A module to handle Share operations of the MoodleNet.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 16](lib_amd_src_moodlenet_send_resource.js.md)

 

**Since:
 :** 

- 4.2

 

**Copyright:
 :** 

- 2023 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A module to handle Share operations of the MoodleNet.

 

 

 

 

### Members

 

#### (static, constant) handleModal

 

**Description:
 :** 

- 

Handle modal.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 156](lib_amd_src_moodlenet_send_resource.js.md)

Handle modal.

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 215](lib_amd_src_moodlenet_send_resource.js.md)

Initialize.

 

#### (static, constant) sendToMoodleNet

 

**Description:
 :** 

- 

Handle send to MoodleNet.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 57](lib_amd_src_moodlenet_send_resource.js.md)

Handle send to MoodleNet.

 

 

### Methods

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 190](lib_amd_src_moodlenet_send_resource.js.md)

 

#### (async, inner) renderModal(data, selectedActivities)

 

**Description:
 :** 

- 

Render the modal to send resource to MoodleNet.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 114](lib_amd_src_moodlenet_send_resource.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `data`

 

object

 

The data of the resource to be shared.

 
 `selectedActivities`

 

array

 

Selected activities.

 

 

#### (inner) responseFromMoodleNet(status, resourceUrl)

 

**Description:
 :** 

- 

Handle response from MoodleNet.

 

**Source:
 :** 

- 
 [lib/amd/src/moodlenet/send_resource.js](lib_amd_src_moodlenet_send_resource.js.md), [line 91](lib_amd_src_moodlenet_send_resource.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `status`

 

boolean

 

Response status. True if successful.

 
 `resourceUrl`

 

String

 

Resource URL.
