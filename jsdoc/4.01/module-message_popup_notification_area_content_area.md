# message_popup/notification_area_content_area - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-message_popup_notification_area_content_area.html

# message_popup/notification_area_content_area

 

 

 

**Description:
 :** 

- 

Controls the content area of the notification area on the
notification page.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 16](message_output_popup_amd_src_notification_area_content_area.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the content area of the notification area on the
notification page.

 

 

 

 

### Methods

 

#### (inner) getContainer() → {object}

 

**Description:
 :** 

- 

Get the container element (which the content area is within).

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 70](message_output_popup_amd_src_notification_area_content_area.js.md)

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

Get the content area content element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 100](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getFooter() → {object}

 

**Description:
 :** 

- 

Get the content area footer element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 110](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getHeader() → {object}

 

**Description:
 :** 

- 

Get the content area header element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 90](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Returns:

jQuery element

**
 Type

 :** 

object

 

#### (inner) getRoot() → {object}

 

**Description:
 :** 

- 

Get the root element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 60](message_output_popup_amd_src_notification_area_content_area.js.md)

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
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 80](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) hide()

 

**Description:
 :** 

- 

Hide the content area. Typically used with responsive
styling on smaller screens.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 130](message_output_popup_amd_src_notification_area_content_area.js.md)

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Create the event listeners for the content area.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 196](message_output_popup_amd_src_notification_area_content_area.js.md)

 

#### (inner) setContentHMTL(html)

 

**Description:
 :** 

- 

Change the HTML in the content area content element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 150](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `html`

 

string

 

The HTML to be set.

 

 

#### (inner) setFooterHTML(html)

 

**Description:
 :** 

- 

Change the HTML in the content area footer element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 160](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `html`

 

string

 

The HTML to be set.

 

 

#### (inner) setHeaderHTML(html)

 

**Description:
 :** 

- 

Change the HTML in the content area header element.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 140](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `html`

 

string

 

The HTML to be set

 

 

#### (inner) show()

 

**Description:
 :** 

- 

Display the content area. Typically used with responsive
styling on smaller screens.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 120](message_output_popup_amd_src_notification_area_content_area.js.md)

 

#### (inner) showNotification(notification) → {object}

 

**Description:
 :** 

- 

Render the given notification context in the content area.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_area_content_area.js](message_output_popup_amd_src_notification_area_content_area.js.md), [line 170](message_output_popup_amd_src_notification_area_content_area.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notification`

 

object

 

The notification context (from a webservice)

 

##### Returns:

jQuery promise

**
 Type

 :** 

object
