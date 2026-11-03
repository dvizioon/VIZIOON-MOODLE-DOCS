# block_myoverview/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-block_myoverview_repository.html

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

 

#### (static, constant) CARDLIST_REQUIRED_FIELDS :Array.<string>

 

**Description:
 :** 

- 

These course fields are the only ones needed to be included in the results for the card and list views.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 71](blocks_myoverview_amd_src_repository.js.md)

These course fields are the only ones needed to be included in the results for the card and list views.

##### Type:

- 

Array.<string>

 

 

#### (static, constant) SUMMARY_REQUIRED_FIELDS :Array.<string>

 

**Description:
 :** 

- 

These course fields are the only ones needed to be included in the results for the card and list views.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 86](blocks_myoverview_amd_src_repository.js.md)

These course fields are the only ones needed to be included in the results for the card and list views.

##### Type:

- 

Array.<string>

 

 

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
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 57](blocks_myoverview_amd_src_repository.js.md)

Set the favourite state on a list of courses.

Valid args are:
Array courses list of course id numbers.

 

 

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
 [blocks/myoverview/amd/src/repository.js](blocks_myoverview_amd_src_repository.js.md), [line 26](blocks_myoverview_amd_src_repository.js.md)

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
