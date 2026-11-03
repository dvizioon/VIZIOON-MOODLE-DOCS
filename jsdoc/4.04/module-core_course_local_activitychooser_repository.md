# core_course/local/activitychooser/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_course_local_activitychooser_repository.html

# core_course/local/activitychooser/repository

 

 

 

**Description:
 :** 

- 

A javascript module to handle user AJAX actions.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 16](course_amd_src_local_activitychooser_repository.js.md)

 

**Copyright:
 :** 

- 2019 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle user AJAX actions.

 

 

 

 

### Methods

 

#### (inner) activityModules(courseid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 25](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the modules for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) favouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 42](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) fetchFooterData(courseid, sectionid) → {object}

 

**Description:
 :** 

- 

Fetch all the information on modules we'll need in the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 82](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

What course to fetch the data for

 
 `sectionid`

 

Number

 

What section to fetch the data for

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) unfavouriteModule(modName, modID) → {object}

 

**Description:
 :** 

- 

Given a module name, module ID & the current course we want to specify that the module
is no longer a users' favourite.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/repository.js](course_amd_src_local_activitychooser_repository.js.md), [line 62](course_amd_src_local_activitychooser_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modName`

 

String

 

Frankenstyle name of the component to add favourite

 
 `modID`

 

int

 

ID of the module. Mainly for LTI cases where they have same / similar names

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
