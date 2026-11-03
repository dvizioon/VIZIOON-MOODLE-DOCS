# core_group/comboboxsearch/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_group_comboboxsearch_repository.html

# core_group/comboboxsearch/repository

 

 

 

**Description:
 :** 

- 

A repo for the comboboxsearch group type.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/repository.js](group_amd_src_comboboxsearch_repository.js.md), [line 16](group_amd_src_comboboxsearch_repository.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A repo for the comboboxsearch group type.

 

 

 

 

### Methods

 

#### (inner) groupFetch(courseid, cmid) → {object}

 

**Description:
 :** 

- 

Given a course ID and optionally a module ID, we want to fetch the groups, so we may fetch their users.

 

**Source:
 :** 

- 
 [group/amd/src/comboboxsearch/repository.js](group_amd_src_comboboxsearch_repository.js.md), [line 26](group_amd_src_comboboxsearch_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

int

 

ID of the course to fetch the groups of.

 
 `cmid`

 

int
|

null

 

ID of the course module initiating the group search (optional).

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
