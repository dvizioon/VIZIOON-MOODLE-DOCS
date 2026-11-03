# module:core_message/notification_processor_settings - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_message_notification_processor_settings.html

# module:core_message/notification_processor_settings

 

## 

 module:core_message/notification_processor_settings

 

 

 

 

#### new (require("core_message/notification_processor_settings"))(root)

 

**Description:
 :** 

- 

Constructor for the Modal.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 50](message_amd_src_notification_processor_settings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root jQuery element for the modal.

 

 

 

 

### Methods

 

#### (inner) disableButtons()

 

**Description:
 :** 

- 

Disable the buttons in the footer.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 149](message_amd_src_notification_processor_settings.js.md)

 

#### (inner) enableButtons()

 

**Description:
 :** 

- 

Enable the buttons in the footer.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 159](message_amd_src_notification_processor_settings.js.md)

 

#### (inner) getContextId() → {Number|null}

 

**Description:
 :** 

- 

Retrieve the current context id, if any.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 129](message_amd_src_notification_processor_settings.js.md)

##### Returns:

The notification context id

**
 Type

 :** 

Number
|

null

 

#### (inner) getElement() → {object|null}

 

**Description:
 :** 

- 

Retrieve the current element, if any.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 90](message_amd_src_notification_processor_settings.js.md)

##### Returns:

The notification node element.

**
 Type

 :** 

object
|

null

 

#### (inner) getForm() → {object}

 

**Description:
 :** 

- 

Get the form element from the modal.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 139](message_amd_src_notification_processor_settings.js.md)

##### Returns:

**
 Type

 :** 

object

 

#### (inner) getName() → {string|null}

 

**Description:
 :** 

- 

Retrieve the current name, if any.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 110](message_amd_src_notification_processor_settings.js.md)

##### Returns:

The notification name.

**
 Type

 :** 

string
|

null

 

#### (inner) getUserId() → {int|null}

 

**Description:
 :** 

- 

Retrieve the current userid, if any.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 70](message_amd_src_notification_processor_settings.js.md)

##### Returns:

The notification userid

**
 Type

 :** 

int
|

null

 

#### (inner) hide()

 

**Description:
 :** 

- 

Clear the notification from the modal when it's closed so
that it is loaded fresh next time it's displayed.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 232](message_amd_src_notification_processor_settings.js.md)

 

#### (inner) loadAllContent() → {object}

 

**Description:
 :** 

- 

Load both the title and body content.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 210](message_amd_src_notification_processor_settings.js.md)

##### Returns:

promise

**
 Type

 :** 

object

 

#### (inner) loadBodyContent() → {object}

 

**Description:
 :** 

- 

Load the body for the modal to the appropriate value
depending on message outputs.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 183](message_amd_src_notification_processor_settings.js.md)

##### Returns:

A promise resolved with the fragment html and js from

**
 Type

 :** 

object

 

#### (inner) loadTitleContent() → {object}

 

**Description:
 :** 

- 

Load the title for the modal to the appropriate value
depending on message outputs.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 169](message_amd_src_notification_processor_settings.js.md)

##### Returns:

A promise resolved with the new title text.

**
 Type

 :** 

object

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 281](message_amd_src_notification_processor_settings.js.md)

 

#### (inner) setContextId(id)

 

**Description:
 :** 

- 

Set the context id to the given value.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 119](message_amd_src_notification_processor_settings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

The notification context id

 

 

#### (inner) setElement(element)

 

**Description:
 :** 

- 

Set the object to the given value.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 80](message_amd_src_notification_processor_settings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

The notification node element.

 

 

#### (inner) setName(name)

 

**Description:
 :** 

- 

Set the name to the given value.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 100](message_amd_src_notification_processor_settings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

string

 

The notification name.

 

 

#### (inner) setUserId(id)

 

**Description:
 :** 

- 

Set the userid to the given value.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 60](message_amd_src_notification_processor_settings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

The notification userid

 

 

#### (inner) show()

 

**Description:
 :** 

- 

Load the modal content before showing it. This
is to allow us to re-use the same modal for creating and
editing different message outputs within the page.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 220](message_amd_src_notification_processor_settings.js.md)

 

#### (inner) updateConfiguredStatus() → {Promise|boolean}

 

**Description:
 :** 

- 

Checks if the processor has been configured. If so then remove the unconfigured
status from the interface.

 

**Source:
 :** 

- 
 [message/amd/src/notification_processor_settings.js](message_amd_src_notification_processor_settings.js.md), [line 245](message_amd_src_notification_processor_settings.js.md)

##### Returns:

**
 Type

 :** 

Promise
|

boolean
