# block_starredcourses/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-block_starredcourses_repository.html

# block_starredcourses/repository

 

 

 

**Description:
 :** 

- 

A javascript module to retrieve user's starred courses.

 

**Source:
 :** 

- 
 [blocks/starredcourses/amd/src/repository.js](blocks_starredcourses_amd_src_repository.js.md), [line 16](blocks_starredcourses_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2018 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to retrieve user's starred courses.

 

 

 

 

### Methods

 

#### (inner) getStarredCourses(args) → {promise}

 

**Description:
 :** 

- 

Retrieve a list of starred courses.

Valid args are:
int limit number of records to retrieve
int offset the offset of records to retrieve

 

**Source:
 :** 

- 
 [blocks/starredcourses/amd/src/repository.js](blocks_starredcourses_amd_src_repository.js.md), [line 25](blocks_starredcourses_amd_src_repository.js.md)

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
