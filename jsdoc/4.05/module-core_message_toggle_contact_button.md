# core_message/toggle_contact_button - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_message_toggle_contact_button.html

# core_message/toggle_contact_button

 

 

 

**Description:
 :** 

- 

Module to add/remove contact using ajax.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 16](message_amd_src_toggle_contact_button.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module to add/remove contact using ajax.

 

 

 

 

### Methods

 

#### (inner) addContact(element)

 

**Description:
 :** 

- 

Send a request to the server to add the current user as
a contact. The contents of the button are changed to the
remove contact button upon success.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 135](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

 

#### (inner) enhance(element)

 

**Description:
 :** 

- 

Enhances the given element with a loading gif and event handles to make
ajax requests to add or remove a contact where appropriate.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 198](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

 

#### (inner) getUserId(element) → {int}

 

**Description:
 :** 

- 

Get the id for the user being viewed.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 66](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getUserId(element) → {int}

 

**Description:
 :** 

- 

Get the id for the logged in user.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 77](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getUserId(element) → {int}

 

**Description:
 :** 

- 

Check whether a text label should be displayed or not.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 88](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

int

 

#### (inner) isContact(element) → {bool}

 

**Description:
 :** 

- 

Check the state of the element, if the current user is a contact or not.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 26](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isLoading(element) → {bool}

 

**Description:
 :** 

- 

Check if this element is currently loading.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 99](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isRequested(element) → {bool}

 

**Description:
 :** 

- 

Check the state of the element, if the current user has sent a contact request or not.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 37](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) removeContact(element)

 

**Description:
 :** 

- 

Send a request to the server to remove the current user as
a contact. The contents of the button are changed to the
add contact button upon success.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 167](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

 

#### (inner) sendRequest(element, request) → {object}

 

**Description:
 :** 

- 

Sends an ajax request to the server and handles the element state
while the request is being performed.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 110](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 
 `request`

 

object

 

Request hash to send

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) setContactRequested(element)

 

**Description:
 :** 

- 

Record that the user has sent a contact request.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 46](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button

 

 

#### (inner) setNotContact(element)

 

**Description:
 :** 

- 

Record that the user is not a contact.

 

**Source:
 :** 

- 
 [message/amd/src/toggle_contact_button.js](message_amd_src_toggle_contact_button.js.md), [line 56](message_amd_src_toggle_contact_button.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

jQuery object for the button
