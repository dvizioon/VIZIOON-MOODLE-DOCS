# core_courseformat/local/courseeditor/fileuploader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_courseformat_local_courseeditor_fileuploader.html

# core_courseformat/local/courseeditor/fileuploader

 

 

 

**Description:
 :** 

- 

The course file uploader.

This module is used to upload files directly into the course.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 16](course_format_amd_src_local_courseeditor_fileuploader.js.md)

 

**Copyright:
 :** 

- 2022 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

The course file uploader.

This module is used to upload files directly into the course.

 

 

 

 

### Members

 

#### (static, constant) uploadFilesToCourse

 

**Description:
 :** 

- 

Upload a file to the course.

This method will show any necesary modal to handle the request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 541](course_format_amd_src_local_courseeditor_fileuploader.js.md)

Upload a file to the course.

This method will show any necesary modal to handle the request.

 

#### (inner) allHandlers :Array.<[Handler](Handler.md)>|null

 

**Description:
 :** 

- 

all the available handlers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 213](course_format_amd_src_local_courseeditor_fileuploader.js.md)

all the available handlers.

##### Type:

- 

Array.<[Handler](Handler.md)>
|

null

 

 

#### (inner) courseUpdates :Map

 

**Description:
 :** 

- 

the pending course sections updates.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 53](course_format_amd_src_local_courseeditor_fileuploader.js.md)

the pending course sections updates.

##### Type:

- 

Map

 

 

#### (inner) errors :Object

 

**Description:
 :** 

- 

the error messages.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 55](course_format_amd_src_local_courseeditor_fileuploader.js.md)

the error messages.

##### Type:

- 

Object

 

 

#### (inner) handlerManagers :Object

 

**Description:
 :** 

- 

the courseId indexed loaded handler managers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 51](course_format_amd_src_local_courseeditor_fileuploader.js.md)

the courseId indexed loaded handler managers.

##### Type:

- 

Object

 

 

#### (inner) lastHandlers :Object

 

**Description:
 :** 

- 

the last handlers selected per each file extension.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 210](course_format_amd_src_local_courseeditor_fileuploader.js.md)

the last handlers selected per each file extension.

##### Type:

- 

Object

 

 

#### (inner) uploadQueue :[ProcessQueue](ProcessQueue.md)

 

**Description:
 :** 

- 

the internal uploadQueue instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 49](course_format_amd_src_local_courseeditor_fileuploader.js.md)

the internal uploadQueue instance.

##### Type:

- 

[ProcessQueue](ProcessQueue.md)

 

 

 

### Methods

 

#### (inner) addRefreshSection(courseId, sectionId)

 

**Description:
 :** 

- 

Add a section to refresh.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 433](course_format_amd_src_local_courseeditor_fileuploader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

number

 

the course id

 
 `sectionId`

 

number

 

the seciton id

 

 

#### (async, inner) loadCourseHandlerManager(courseId) → {Promise.<HandlerManager>}

 

**Description:
 :** 

- 

Load and return the course handler manager instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 468](course_format_amd_src_local_courseeditor_fileuploader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

the course Id to load

 

##### Returns:

promise of the the loaded handleManager

**
 Type

 :** 

Promise.<HandlerManager>

 

#### (async, inner) loadErrorStrings(courseId)

 

**Description:
 :** 

- 

Load all the erros messages at once in the module "errors" variable.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 482](course_format_amd_src_local_courseeditor_fileuploader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

the course id

 

 

 

### Type Definitions

 

#### Handler

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/fileuploader.js](course_format_amd_src_local_courseeditor_fileuploader.js.md), [line 26](course_format_amd_src_local_courseeditor_fileuploader.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `extension`

 

String

 

the handled extension or * for any

 
 `message`

 

String

 

the handler message

 
 `module`

 

String

 

the module name

 

##### Type:

- 

Object
