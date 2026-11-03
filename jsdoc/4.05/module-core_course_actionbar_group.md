# module:core_course/actionbar/group - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_actionbar_group.html

# module:core_course/actionbar/group

 

## 

 module:core_course/actionbar/group

 

 

 

 

#### new (require("core_course/actionbar/group"))(baseUrl, cmid)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/group.js](course_amd_src_actionbar_group.js.md), [line 35](course_amd_src_actionbar_group.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `baseUrl`

 

string

 

 

 

The base URL for the page.

 
 `cmid`

 

int
|

null

 

 

 `null`

 

ID of the course module initiating the group search (optional).

 

 

 

 

### Methods

 

#### selectOneLink(groupID) → {string}

 

**Description:
 :** 

- 

Build up the link that is dedicated to a particular result.

 

**Source:
 :** 

- 
 [course/amd/src/actionbar/group.js](course_amd_src_actionbar_group.js.md), [line 57](course_amd_src_actionbar_group.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `groupID`

 

Number

 

The ID of the group selected.

 

##### Returns:

**
 Type

 :** 

string
