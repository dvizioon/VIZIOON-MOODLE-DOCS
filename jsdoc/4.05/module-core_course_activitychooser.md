# core_course/activitychooser - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_activitychooser.html

# core_course/activitychooser

 

 

 

**Description:
 :** 

- 

A type of dialogue used as for choosing modules in a course.

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 16](course_amd_src_activitychooser.js.md)

 

**Copyright:
 :** 

- 2020 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A type of dialogue used as for choosing modules in a course.

 

 

 

 

### Methods

 

#### (inner) buildModal(body, footer) → {Object}

 

**Description:
 :** 

- 

Given an object we want to build a modal ready to show

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 306](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `body`

 

Promise

 

 

 
 `footer`

 

String
|

Boolean

 

Either a footer to add or nothing

 

##### Returns:

The modal ready to display immediately and render body in later.

**
 Type

 :** 

Object

 

#### (inner) init(courseId, chooserConfig)

 

**Description:
 :** 

- 

Set up the activity chooser.

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 49](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

Course ID to use later on in fetchModules()

 
 `chooserConfig`

 

Object

 

Any PHP config settings that we may need to reference

 

 

#### (inner) nullFavouriteDomManager(favouriteTabNav, modalBody)

 

**Description:
 :** 

- 

A small helper function to handle the case where there are no more favourites
and we need to mess a bit with the available tabs in the chooser

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 326](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `favouriteTabNav`

 

HTMLElement

 

Dom node of the favourite tab nav

 
 `modalBody`

 

HTMLElement

 

Our current modals' body

 

 

#### (inner) partiallyAppliedFavouriteManager(moduleData, sectionnum) → {function}

 

**Description:
 :** 

- 

Export a curried function where the builtModules has been applied.
We have our array of modules so we can rerender the favourites area and have all of the items sorted.

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 364](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `moduleData`

 

Array

 

This is our raw WS data that we need to manipulate

 
 `sectionnum`

 

Number

 

We need this to add the sectionnum to the URL's in the faves area after rerender

 

##### Returns:

partially applied function so we can manipulate DOM nodes easily & update our internal array

**
 Type

 :** 

function

 

#### (inner) registerListenerEvents(courseId, chooserConfig)

 

**Description:
 :** 

- 

Once a selection has been made make the modal & module information and pass it along

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 64](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

 

 
 `chooserConfig`

 

Object

 

Any PHP config settings that we may need to reference

 

 

#### (inner) sectionMapper(webServiceData, num, sectionreturnnum, beforemod) → {Array}

 

**Description:
 :** 

- 

Given the web service data and an ID we want to make a deep copy
of the WS data then add on the section num to the addoption URL

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 200](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `webServiceData`

 

Object

 

Our original data from the Web service call

 
 `num`

 

Number

 

The number of the section we need to append to the links

 
 `sectionreturnnum`

 

Number
|

null

 

The number of the section return we need to append to the links

 
 `beforemod`

 

Number
|

null

 

The ID of the cm we need to append to the links

 

##### Returns:

[modules] with URL's built

**
 Type

 :** 

Array

 

#### (inner) templateDataBuilder(data, chooserConfig) → {Object}

 

**Description:
 :** 

- 

Given an array of modules we want to figure out where & how to place them into our template object

 

**Source:
 :** 

- 
 [course/amd/src/activitychooser.js](course_amd_src_activitychooser.js.md), [line 223](course_amd_src_activitychooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `data`

 

Array

 

our modules to manipulate into a Templatable object

 
 `chooserConfig`

 

Object

 

Any PHP config settings that we may need to reference

 

##### Returns:

Our built object ready to render out

**
 Type

 :** 

Object
