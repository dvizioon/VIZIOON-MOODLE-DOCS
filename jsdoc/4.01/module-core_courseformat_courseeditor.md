# core_courseformat/courseeditor - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_courseformat_courseeditor.html

# core_courseformat/courseeditor

 

 

 

**Description:
 :** 

- 

Generic reactive module used in the course editor.

 

**Source:
 :** 

- 
 [course/format/amd/src/courseeditor.js](course_format_amd_src_courseeditor.js.md), [line 16](course_format_amd_src_courseeditor.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Generic reactive module used in the course editor.

 

 

 

 

### Members

 

#### (static, constant) getCourseEditor

 

**Description:
 :** 

- 

Get a specific course editor reactive instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/courseeditor.js](course_format_amd_src_courseeditor.js.md), [line 83](course_format_amd_src_courseeditor.js.md)

Get a specific course editor reactive instance.

 

#### (static, constant) getCurrentCourseEditor

 

**Description:
 :** 

- 

Get the current course reactive instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/courseeditor.js](course_format_amd_src_courseeditor.js.md), [line 108](course_format_amd_src_courseeditor.js.md)

Get the current course reactive instance.

 

#### (static, constant) setViewFormat

 

**Description:
 :** 

- 

Setup the current view settings

The backend cache state revision is a combination of the course->cacherev, the
user course preferences and completion state. The backend updates that number
everytime some change in the course affects the user course state.

 

**Source:
 :** 

- 
 [course/format/amd/src/courseeditor.js](course_format_amd_src_courseeditor.js.md), [line 67](course_format_amd_src_courseeditor.js.md)

Setup the current view settings

The backend cache state revision is a combination of the course->cacherev, the
user course preferences and completion state. The backend updates that number
everytime some change in the course affects the user course state.

 

 

### Methods

 

#### (inner) dispatchStateChangedEvent(detail, target)

 

**Description:
 :** 

- 

Trigger a state changed event.

This function will be moved to core_course/events module
when the file is migrated to the new JS events structure proposed in MDL-70990.

 

**Source:
 :** 

- 
 [course/format/amd/src/courseeditor.js](course_format_amd_src_courseeditor.js.md), [line 34](course_format_amd_src_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

the full state

 
 `target`

 

object

 

the custom event target (document if none provided)
