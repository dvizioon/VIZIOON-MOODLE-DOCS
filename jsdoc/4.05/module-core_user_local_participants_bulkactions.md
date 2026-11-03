# core_user/local/participants/bulkactions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_user_local_participants_bulkactions.html

# core_user/local/participants/bulkactions

 

 

 

**Description:
 :** 

- 

Bulk actions for lists of participants.

 

**Source:
 :** 

- 
 [user/amd/src/local/participants/bulkactions.js](user_amd_src_local_participants_bulkactions.js.md), [line 16](user_amd_src_local_participants_bulkactions.js.md)

 

**Copyright:
 :** 

- 2020 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Bulk actions for lists of participants.

 

 

 

 

### Members

 

#### (static, constant) showAddNote

 

**Description:
 :** 

- 

Show the add note popup

 

**Source:
 :** 

- 
 [user/amd/src/local/participants/bulkactions.js](user_amd_src_local_participants_bulkactions.js.md), [line 41](user_amd_src_local_participants_bulkactions.js.md)

Show the add note popup

 

#### (static, constant) showSendMessage

 

**Description:
 :** 

- 

Show the send message popup.

 

**Source:
 :** 

- 
 [user/amd/src/local/participants/bulkactions.js](user_amd_src_local_participants_bulkactions.js.md), [line 128](user_amd_src_local_participants_bulkactions.js.md)

Show the send message popup.

 

 

### Methods

 

#### (inner) submitAddNote(courseid, users, modal) → {Promise}

 

**Description:
 :** 

- 

Add a note to this list of users.

 

**Source:
 :** 

- 
 [user/amd/src/local/participants/bulkactions.js](user_amd_src_local_participants_bulkactions.js.md), [line 97](user_amd_src_local_participants_bulkactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseid`

 

Number

 

 

 
 `users`

 

Array.<Number>

 

 

 
 `modal`

 

Modal

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) submitSendMessage(modal, users, text) → {Promise}

 

**Description:
 :** 

- 

Send a message to these users.

 

**Source:
 :** 

- 
 [user/amd/src/local/participants/bulkactions.js](user_amd_src_local_participants_bulkactions.js.md), [line 174](user_amd_src_local_participants_bulkactions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Modal

 

 

 
 `users`

 

Array.<Number>

 

 

 
 `text`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise
