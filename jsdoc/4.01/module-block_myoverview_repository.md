# block_myoverview/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-block_myoverview_repository.html

# block_myoverview/repository

 

 

 

**Description:
 :** 

- 

A javascript module to retrieve enrolled coruses from the server.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 16](blocks_myoverview_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2018 Bas Brands 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to retrieve enrolled coruses from the server.

 

 

 

 

### Members

 

#### (static, constant) setFavouriteCourses

 

**Description:
 :** 

- 

Set the favourite state on a list of courses.

Valid args are:
Array courses list of course id numbers.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 58](blocks_myoverview_amd_src_repository.js.md)

Set the favourite state on a list of courses.

Valid args are:
Array courses list of course id numbers.

 

#### (static, constant) updateUserPreferences

 

**Description:
 :** 

- 

Update the user preferences.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 82](blocks_myoverview_amd_src_repository.js.md)

Update the user preferences.

 

 

### Methods

 

#### (inner) getEnrolledCoursesByTimeline(args) → {promise}

 

**Description:
 :** 

- 

Retrieve a list of enrolled courses.

Valid args are:
string classification future, inprogress, past
int limit number of records to retreive
int Offset offset for pagination
int sort sort by lastaccess or name

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 27](blocks_myoverview_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

The request arguments

 

##### Returns:

Resolved with an array of courses

**
 Type

 :** 

promise
