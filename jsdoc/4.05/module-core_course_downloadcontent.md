# core_course/downloadcontent - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_downloadcontent.html

# core_course/downloadcontent

 

 

 

**Description:
 :** 

- 

Functions related to downloading course content.

 

**Source:
 :** 

- 
 [course/amd/src/downloadcontent.js](course_amd_src_downloadcontent.js.md), [line 16](course_amd_src_downloadcontent.js.md)

 

**Copyright:
 :** 

- 2020 Michael Hawkins 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Functions related to downloading course content.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Set up listener to trigger the download course content modal.

 

**Source:
 :** 

- 
 [course/amd/src/downloadcontent.js](course_amd_src_downloadcontent.js.md), [line 36](course_amd_src_downloadcontent.js.md)

Set up listener to trigger the download course content modal.

 

 

### Methods

 

#### (inner) displayDownloadConfirmation(downloadModalTrigger) → {void}

 

**Description:
 :** 

- 

Display the download course content modal.

 

**Source:
 :** 

- 
 [course/amd/src/downloadcontent.js](course_amd_src_downloadcontent.js.md), [line 50](course_amd_src_downloadcontent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `downloadModalTrigger`

 

Object

 

The DOM element that triggered the download modal.

 

##### Returns:

**
 Type

 :** 

void

 

#### (inner) downloadContent(e, downloadModalTrigger, modal) → {void}

 

**Description:
 :** 

- 

Trigger downloading of course content.

 

**Source:
 :** 

- 
 [course/amd/src/downloadcontent.js](course_amd_src_downloadcontent.js.md), [line 95](course_amd_src_downloadcontent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event triggering the download.

 
 `downloadModalTrigger`

 

Object

 

The DOM element that triggered the download modal.

 
 `modal`

 

Object

 

The modal object.

 

##### Returns:

**
 Type

 :** 

void
