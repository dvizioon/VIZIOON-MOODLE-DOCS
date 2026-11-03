# mod_assign/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_repository.html

# mod_assign/repository

 

 

 

**Description:
 :** 

- 

A repo for the search partial in the submissions page.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/repository.js](mod_assign_amd_src_repository.js.md), [line 16](mod_assign_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2024 Ilya Tregubov 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A repo for the search partial in the submissions page.

 

 

 

 

### Methods

 

#### (inner) userFetch(assignid, groupid) → {object}

 

**Description:
 :** 

- 

Given a course ID, we want to fetch the learners within this assignment.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/repository.js](mod_assign_amd_src_repository.js.md), [line 26](mod_assign_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `assignid`

 

int

 

ID of the assignment.

 
 `groupid`

 

int

 

ID of the selected group.

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
