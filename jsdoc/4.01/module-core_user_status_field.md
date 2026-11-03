# core_user/status_field - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_user_status_field.html

# core_user/status_field

 

 

 

**Description:
 :** 

- 

AMD module for the user enrolment status field in the course participants page.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 16](user_amd_src_status_field.js.md)

 

**Copyright:
 :** 

- 2017 Jun Pataleta

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

AMD module for the user enrolment status field in the course participants page.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialise the statu field handler.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 363](user_amd_src_status_field.js.md)

Initialise the statu field handler.

 

 

### Methods

 

#### (inner) getBody(contextId, ueid, formdata) → {Promise}

 

**Description:
 :** 

- 

Get the body fragment.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 346](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `contextId`

 

Number

 

 

 

 

 
 `ueid`

 

Number

 

 

 

The user enrolment id

 
 `formdata`

 

Object

 

 

 `null`

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) getDynamicTableFromLink(link) → {HTMLElement}

 

**Description:
 :** 

- 

Get the dynamic table from the specified link.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 48](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) getStatusContainer(link) → {HTMLElement}

 

**Description:
 :** 

- 

Get the status container from the specified link.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 56](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) getUserEnrolmentIdFromLink(link) → {Number}

 

**Description:
 :** 

- 

Get user enrolment id from the specified link

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 64](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) registerEventListeners(contextId, uniqueId)

 

**Description:
 :** 

- 

Register all event listeners for the status fields.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 72](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

Number

 

 

 
 `uniqueId`

 

Number

 

 

 

 

#### (inner) showEditDialogue(link, getBody)

 

**Description:
 :** 

- 

Show the edit dialogue.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 110](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 
 `getBody`

 

function

 

Function to get the body for the specified user enrolment

 

 

#### (inner) showStatusDetails(link)

 

**Description:
 :** 

- 

Show the user details dialogue.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 215](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 

 

#### (inner) showUnenrolConfirmation(link)

 

**Description:
 :** 

- 

Show and handle the unenrolment confirmation dialogue.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 149](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `link`

 

HTMLElement

 

 

 

 

#### (inner) submitEditFormAjax(clickedLink, getBody, modal, userEnrolmentId, userData)

 

**Description:
 :** 

- 

Submit the edit dialogue.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 267](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clickedLink`

 

HTMLElement

 

 

 
 `getBody`

 

function

 

 

 
 `modal`

 

Object

 

 

 
 `userEnrolmentId`

 

Number

 

 

 
 `userData`

 

Object

 

 

 

 

#### (inner) submitUnenrolFormAjax(clickedLink, modal, args, userData)

 

**Description:
 :** 

- 

Submit the unenrolment form.

 

**Source:
 :** 

- 
 [user/amd/src/status_field.js](user_amd_src_status_field.js.md), [line 308](user_amd_src_status_field.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clickedLink`

 

HTMLElement

 

 

 
 `modal`

 

Object

 

 

 
 `args`

 

Object

 

 

 
 `userData`

 

Object
