# message_popup/notification_area_control_area - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-message_popup_notification_area_control_area.html

# message_popup/notification_area_control_area

 

 

 

**Description:
 :** 

- 

Controls the notification area on the notification page.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 16](message_output_popup_amd_src_notification_area_control_area.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the notification area on the notification page.

 

 

 

 

### Methods

 

#### (inner) getCacheNotification(id) → {object}

 

**Description:
 :** 

- 

Retrieve a notification from the cache.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 213](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

The id for the notification you wish to retrieve

 

##### Returns:

A notification (as returned by a webservice)

**
 Type

 :** 

object

 

#### (inner) getContainer() → {object}

 

**Description:
 :** 

- 

Get the container element (which the control area is within).

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 70](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getContent() → {object}

 

**Description:
 :** 

- 

Get the control area content element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 90](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getLimit() → {int}

 

**Description:
 :** 

- 

Get the limit value for the paginated loading of the
notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 111](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getNotificationElement(id) → {object|null}

 

**Description:
 :** 

- 

Find the notification element in the control area for the given id.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 224](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

The notification id

 

##### Returns:

jQuery element or null

**
 Type

 :** 

object
|

null

 

#### (inner) getOffset() → {int}

 

**Description:
 :** 

- 

Get the offset value for paginated loading of the
notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 100](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getRoot() → {object}

 

**Description:
 :** 

- 

Get the root element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 60](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getUserId() → {int}

 

**Description:
 :** 

- 

Get the user id.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 80](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) hasDoneInitialLoad() → {bool}

 

**Description:
 :** 

- 

Check if the first load of notifications has been triggered.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 173](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

true if first notification loaded, false otherwise

**
 Type

 :** 

bool

 

#### (inner) hasLoadedAllContent() → {bool}

 

**Description:
 :** 

- 

Check if all of the notifications have been loaded.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 183](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) incrementOffset()

 

**Description:
 :** 

- 

Increment the offset by the limit amount.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 144](message_output_popup_amd_src_notification_area_control_area.js.md)

 

#### (inner) loadMoreNotifications() → {object}

 

**Description:
 :** 

- 

Load notifications from the server and render them.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 340](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) markNotificationAsRead(notificationElement) → {object}

 

**Description:
 :** 

- 

Send a request to mark the notification as read in the server and remove the unread
status from the element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 284](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notificationElement`

 

object

 

The jQuery notification element

 

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Create the event listeners for the control area.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 386](message_output_popup_amd_src_notification_area_control_area.js.md)

 

#### (inner) renderNotifications(notifications) → {object}

 

**Description:
 :** 

- 

Render the notification data with the appropriate template and add it to the DOM.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 299](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notifications`

 

array

 

Array of notification data

 

##### Returns:

jQuery promise that is resolved when all notifications have been
rendered and added to the DOM

**
 Type

 :** 

object

 

#### (inner) scrollNotificationIntoView(notificationElement)

 

**Description:
 :** 

- 

Scroll the notification element into view within the control area, if it
isn't already visible.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 236](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notificationElement`

 

object

 

The jQuery notification element

 

 

#### (inner) setCacheNotification(notification)

 

**Description:
 :** 

- 

Save a notification in the cache.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 203](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notification`

 

object

 

A notification returned by a webservice

 

 

#### (inner) setLimit(value)

 

**Description:
 :** 

- 

Set the limit value for the paginated loading of the
notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 133](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

int

 

The new limit value

 

 

#### (inner) setLoadedAllContent(val)

 

**Description:
 :** 

- 

Set the state of the loaded all content property.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 193](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `val`

 

bool

 

True if all content is loaded, false otherwise

 

 

#### (inner) setOffset(value)

 

**Description:
 :** 

- 

Set the offset value for the paginated loading of the
notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 122](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

int

 

The new offset value

 

 

#### (inner) showNotification(notificationElement)

 

**Description:
 :** 

- 

Show the full notification for the given notification element. The notification
context is retrieved from the cache and send as data with an event to be
rendered in the content area.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 258](message_output_popup_amd_src_notification_area_control_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notificationElement`

 

int
|

object

 

The notification id or jQuery notification element

 

 

#### (inner) startLoading()

 

**Description:
 :** 

- 

Flag the control area as loading.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 153](message_output_popup_amd_src_notification_area_control_area.js.md)

 

#### (inner) stopLoading()

 

**Description:
 :** 

- 

Remove the loading flag from the control area.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_control_area.js](message_output_popup_amd_src_notification_area_control_area.js.md), [line 163](message_output_popup_amd_src_notification_area_control_area.js.md)
