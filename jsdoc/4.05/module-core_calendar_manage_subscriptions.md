# core_calendar/manage_subscriptions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_calendar_manage_subscriptions.html

# core_calendar/manage_subscriptions

 

 

 

**Description:
 :** 

- 

A module to handle Delete/Update operations of the manage subscription page.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 16](calendar_amd_src_manage_subscriptions.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A module to handle Delete/Update operations of the manage subscription page.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialises.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 139](calendar_amd_src_manage_subscriptions.js.md)

Initialises.

 

 

### Methods

 

#### (inner) createModal(element, messageCode) → {promise}

 

**Description:
 :** 

- 

Create modal.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 71](calendar_amd_src_manage_subscriptions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 
 `messageCode`

 

string

 

Message code.

 

##### Returns:

Promise for modal

**
 Type

 :** 

promise

 

#### (inner) getSubscriptionId(element) → {Number}

 

**Description:
 :** 

- 

Get subscription id for given element.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 40](calendar_amd_src_manage_subscriptions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

update/delete link

 

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getSubscriptionName(element) → {String}

 

**Description:
 :** 

- 

Get subscription name for given element.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 50](calendar_amd_src_manage_subscriptions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

update/delete link

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getSubscriptionRow(subscriptionId) → {Element}

 

**Description:
 :** 

- 

Get subscription table row for subscription id.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 60](calendar_amd_src_manage_subscriptions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `subscriptionId`

 

string

 

Subscription id

 

##### Returns:

**
 Type

 :** 

Element

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events for update/delete links.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 105](calendar_amd_src_manage_subscriptions.js.md)

 

#### (async, inner) responseHandlerForDelete(element, data) → {Promise}

 

**Description:
 :** 

- 

Response handler for delete action.

 

**Source:
 :** 

- 
 [calendar/amd/src/manage_subscriptions.js](calendar_amd_src_manage_subscriptions.js.md), [line 95](calendar_amd_src_manage_subscriptions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 
 `data`

 

Object

 

 

 

##### Returns:

**
 Type

 :** 

Promise
