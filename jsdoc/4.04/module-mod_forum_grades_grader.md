# mod_forum/grades/grader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_forum_grades_grader.html

# mod_forum/grades/grader

 

 

 

**Description:
 :** 

- 

This module will tie together all of the different calls the gradable module will make.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 16](mod_forum_amd_src_grades_grader.js.md)

 

**Copyright:
 :** 

- 2019 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module will tie together all of the different calls the gradable module will make.

 

 

 

 

### Members

 

#### (static, constant) registerLaunchListeners

 

**Description:
 :** 

- 

Register listeners to launch the grading panel.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 183](mod_forum_amd_src_grades_grader.js.md)

Register listeners to launch the grading panel.

 

 

### Methods

 

#### (inner) discussionPostMapper(discussion) → {Array}

 

**Description:
 :** 

- 

For a discussion we need to manipulate it's posts to hide certain UI elements.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 83](mod_forum_amd_src_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `discussion`

 

Object

 

 

 

##### Returns:

name, id, posts

**
 Type

 :** 

Array

 

#### (inner) getContentForUserIdFunction(cmid, experimentalDisplayMode) → {function}

 

**Description:
 :** 

- 

Curried function with CMID set, this is then used in unified grader as a fetch a users content.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 42](mod_forum_amd_src_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

Number

 

 

 
 `experimentalDisplayMode`

 

Bool

 

 

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getGradableUsersForCourseidFunction(courseID, groupID, onlyActive) → {Array}

 

**Description:
 :** 

- 

Curried function with CMID set, this is then used in unified grader as a fetch users call.
The function curried fetches all users in a course for a given CMID.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 68](mod_forum_amd_src_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseID`

 

Number

 

 

 
 `groupID`

 

Number

 

 

 
 `onlyActive`

 

Boolean

 

Whether to fetch only the active enrolled users or all enrolled users in the course.

 

##### Returns:

Array of users for a given context.

**
 Type

 :** 

Array

 

#### (async, inner) launchViewGrading(rootNode, param)

 

**Description:
 :** 

- 

Launch the Grader.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 158](mod_forum_amd_src_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rootNode`

 

HTMLElement

 

the root HTML element describing what is to be graded

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `focusOnClose`

 

bool

 

 

 <optional>  

 

 

 `null`

 

 

 

 

 

 

#### (async, inner) launchWholeForumGrading(rootNode, param)

 

**Description:
 :** 

- 

Launch the Grader.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/grader.js](mod_forum_amd_src_grades_grader.js.md), [line 119](mod_forum_amd_src_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rootNode`

 

HTMLElement

 

the root HTML element describing what is to be graded

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `focusOnClose`

 

bool

 

 

 <optional>  

 

 

 `null`
