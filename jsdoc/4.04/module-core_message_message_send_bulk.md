# core_message/message_send_bulk - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_message_message_send_bulk.html

# core_message/message_send_bulk

 

 

 

**Description:
 :** 

- 

Send bulk message to the given user ids.

 

**Source:
 :** 

- 
 [message/amd/src/message_send_bulk.js](message_amd_src_message_send_bulk.js.md), [line 16](message_amd_src_message_send_bulk.js.md)

 

**Copyright:
 :** 

- 2019 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Send bulk message to the given user ids.

 

 

 

 

### Methods

 

#### (inner) sendMessage(messageText, users) → {Promise}

 

**Description:
 :** 

- 

Send a message to these users.

 

**Source:
 :** 

- 
 [message/amd/src/message_send_bulk.js](message_amd_src_message_send_bulk.js.md), [line 76](message_amd_src_message_send_bulk.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `messageText`

 

String

 

 

 
 `users`

 

Array.<Number>

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) showModal(users, callback) → {Promise}

 

**Description:
 :** 

- 

Show the send message popup.

 

**Source:
 :** 

- 
 [message/amd/src/message_send_bulk.js](message_amd_src_message_send_bulk.js.md), [line 30](message_amd_src_message_send_bulk.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `users`

 

Array.<int>

 

 

 
 `callback`

 

function

 

A callback to apply after the form is closed.

 

##### Returns:

**
 Type

 :** 

Promise
