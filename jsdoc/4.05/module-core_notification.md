# core/notification - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_notification.html

# core/notification

 

 

 

**Description:
 :** 

- 

Notification manager for in-page notifications in Moodle.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 16](lib_amd_src_notification.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Notification manager for in-page notifications in Moodle.

 

 

 

 

### Members

 

#### (static, constant) deleteCancelPromise

 

**Description:
 :** 

- 

Add all of the supplied notifications.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 326](lib_amd_src_notification.js.md)

Add all of the supplied notifications.

 

#### (static, constant) saveCancelPromise

 

**Description:
 :** 

- 

Add all of the supplied notifications.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 310](lib_amd_src_notification.js.md)

Add all of the supplied notifications.

 

 

### Methods

 

#### (static) addNotification(notification) → {Promise}

 

**Description:
 :** 

- 

Add a notification to the page.

Note: This does not cause the notification to be added to the session.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 123](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notification`

 

Notification

 

The notification to add.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) alert(title, message, cancelText) → {Promise}

 

**Description:
 :** 

- 

Alert dialogue.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 179](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `title`

 

String
|

Promise

 

 

 
 `message`

 

String
|

Promise

 

 

 
 `cancelText`

 

String
|

Promise

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) confirm(title, question, saveLabel, noLabel, saveCallback, cancelCallback) → {Promise}

 

**Description:
 :** 

- 

The confirm has now been replaced with a save and cancel dialogue.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 209](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `title`

 

String
|

Promise

 

 

 
 `question`

 

String
|

Promise

 

 

 
 `saveLabel`

 

String
|

Promise

 

 

 
 `noLabel`

 

String
|

Promise

 

 

 
 `saveCallback`

 

String
|

Promise

 

 

 
 `cancelCallback`

 

String
|

Promise

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) deleteCancel(title, question, deleteLabel, deleteCallback, cancelCallback, options) → {Promise}

 

**Description:
 :** 

- 

The Delete and Cancel dialogue helper.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 269](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `title`

 

String
|

Promise

 

 

 
 `question`

 

String
|

Promise

 

 

 
 `deleteLabel`

 

String
|

Promise

 

 

 
 `deleteCallback`

 

String
|

Promise

 

 

 
 `cancelCallback`

 

String
|

Promise

 

 

 
 `options`

 

Object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `triggerElement`

 

HTMLElement

 

 

 <optional>  

 

 

 `null`

 

The element that triggered the modal (will receive the focus after hidden)

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) exception(ex)

 

**Description:
 :** 

- 

Wrap M.core.exception.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 338](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `ex`

 

Error

 

 

 

 

#### (static) fetchNotifications() → {Promise}

 

**Description:
 :** 

- 

Poll the server for any new notifications.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 84](lib_amd_src_notification.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) init(contextId, notificationList)

 

**Description:
 :** 

- 

Initialise the page for the suppled context, and displaying the supplied notifications.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 390](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

Number

 

 

 
 `notificationList`

 

Array.<Notification>

 

 

 

 

#### (static) saveCancel(title, question, saveLabel, saveCallback, cancelCallback, options) → {Promise}

 

**Description:
 :** 

- 

The Save and Cancel dialogue helper.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 225](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `title`

 

String
|

Promise

 

 

 
 `question`

 

String
|

Promise

 

 

 
 `saveLabel`

 

String
|

Promise

 

 

 
 `saveCallback`

 

String
|

Promise

 

 

 
 `cancelCallback`

 

String
|

Promise

 

 

 
 `options`

 

Object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `triggerElement`

 

HTMLElement

 

 

 <optional>  

 

 

 `null`

 

The element that triggered the modal (will receive the focus after hidden)

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) addNotifications(notifications) → {Promise}

 

**Description:
 :** 

- 

Add all of the supplied notifications.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 103](lib_amd_src_notification.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notifications`

 

Array.<Notification>

 

The list of notificaitons

 

##### Returns:

**
 Type

 :** 

Promise

 

 

### Type Definitions

 

#### Notification

 

**Description:
 :** 

- 

A notification object displayed to a user.

 

**Source:
 :** 

- 
 [lib/amd/src/notification.js](lib_amd_src_notification.js.md), [line 68](lib_amd_src_notification.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `message`

 

string

 

The body of the notification

 
 `type`

 

string

 

The type of notification to add (error, warning, info, success).

 
 `closebutton`

 

Boolean

 

Whether to show the close button.

 
 `announce`

 

Boolean

 

Whether to announce to screen readers.

 

A notification object displayed to a user.

##### Type:

- 

Object
