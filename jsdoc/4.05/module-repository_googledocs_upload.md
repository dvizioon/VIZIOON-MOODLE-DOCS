# repository_googledocs/upload - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-repository_googledocs_upload.html

# repository_googledocs/upload

 

 

 

**Description:
 :** 

- 

Upload module for Google Docs repository.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 16](repository_googledocs_amd_src_upload.js.md)

 

**Copyright:
 :** 

- 2025 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Upload module for Google Docs repository.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initializes the upload module.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 148](repository_googledocs_amd_src_upload.js.md)

Initializes the upload module.

 

 

### Methods

 

#### (inner) commitFiles(repoId, contextId, callback, files, modal)

 

**Description:
 :** 

- 

Upload files to server.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 103](repository_googledocs_amd_src_upload.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `repoId`

 

Integer

 

Repository ID

 
 `contextId`

 

Integer

 

Context ID

 
 `callback`

 

function

 

Callback function

 
 `files`

 

array

 

Files to be uploaded

 
 `modal`

 

Modal

 

Modal instance

 

 

#### (inner) initDropzone(modal)

 

**Description:
 :** 

- 

Initialize the dropzone inside the modal.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 74](repository_googledocs_amd_src_upload.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Modal

 

Modal instance

 

 

#### (inner) openUploadModal(data)

 

**Description:
 :** 

- 

Open the upload modal.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 41](repository_googledocs_amd_src_upload.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `data`

 

object

 

Data passed from the event

 

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events.

 

**Source:
 :** 

- 
 [repository/googledocs/amd/src/upload.js](repository_googledocs_amd_src_upload.js.md), [line 136](repository_googledocs_amd_src_upload.js.md)
