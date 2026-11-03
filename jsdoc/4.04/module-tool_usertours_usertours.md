# tool_usertours/usertours - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_usertours_usertours.html

# tool_usertours/usertours

 

 

 

**Description:
 :** 

- 

User tour control library.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 1](admin_tool_usertours_amd_src_usertours.js.md)

 

**Copyright:
 :** 

- 2016 Andrew Nicols 

 

User tour control library.

 

 

 

 

### Methods

 

#### (inner) addResetLink()

 

**Description:
 :** 

- 

Add a reset link to the page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 138](admin_tool_usertours_amd_src_usertours.js.md)

 

#### (inner) fetchTour(tourId)

 

**Description:
 :** 

- 

Fetch the configuration specified tour, and start the tour when it has been fetched.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 96](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tourId`

 

Number

 

The ID of the tour to start.

 

 

#### (inner) findMatchingTour(tourDetails, filters) → {null|object}

 

**Description:
 :** 

- 

Find the first matching tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 27](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tourDetails`

 

Array.<object>

 

 

 
 `filters`

 

Array.<object>

 

 

 

##### Returns:

**
 Type

 :** 

null
|

object

 

#### (inner) init(tourDetails, filters)

 

**Description:
 :** 

- 

Initialise the user tour for the current page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 37](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tourDetails`

 

Array

 

The matching tours for this page.

 
 `filters`

 

Array

 

The names of all client side filters.

 

 

#### (inner) markStepShown(e)

 

**Description:
 :** 

- 

Mark the specified step as being shownd by the user.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 215](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) markTourComplete(e)

 

**Description:
 :** 

- 

Mark the specified tour as being completed by the user.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 231](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

##### Listens to Events:

- [event:tool_usertours/stepRendered](module-tool_usertours_events.md)

 

#### (inner) resetTourState(tourId) → {Promise}

 

**Description:
 :** 

- 

Reset the state, and restart the the tour on the current page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 251](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tourId`

 

Number

 

The ID of the tour to start.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) startBootstrapTour(tourId, template, tourConfig) → {Object}

 

**Description:
 :** 

- 

Start the specified tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/usertours.js](admin_tool_usertours_amd_src_usertours.js.md), [line 159](admin_tool_usertours_amd_src_usertours.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tourId`

 

Number

 

The ID of the tour to start.

 
 `template`

 

String

 

The template to use.

 
 `tourConfig`

 

Object

 

The tour configuration.

 

##### Returns:

**
 Type

 :** 

Object
