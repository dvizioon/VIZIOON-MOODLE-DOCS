# core_message/message_preferences - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_message_message_preferences.html

# core_message/message_preferences

 

 

 

**Description:
 :** 

- 

Controls the message preference page.

 

**Source:
 :** 

- 
 [message/amd/src/message_preferences.js](message_amd_src_message_preferences.js.md), [line 16](message_amd_src_message_preferences.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the message preference page.

 

 

 

 

### Methods

 

#### (inner) preferencesDisabled() → {bool}

 

**Description:
 :** 

- 

Check if the preferences have been disabled on this page.

 

**Source:
 :** 

- 
 [message/amd/src/message_preferences.js](message_amd_src_message_preferences.js.md), [line 46](message_amd_src_message_preferences.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Create all of the event listeners for the message preferences page.

 

**Source:
 :** 

- 
 [message/amd/src/message_preferences.js](message_amd_src_message_preferences.js.md), [line 93](message_amd_src_message_preferences.js.md)

 

#### (inner) saveContactablePrivacySetting() → {Promise}

 

**Description:
 :** 

- 

Update the contactable privacy user preference in the DOM and
send a request to update on the server.

 

**Source:
 :** 

- 
 [message/amd/src/message_preferences.js](message_amd_src_message_preferences.js.md), [line 56](message_amd_src_message_preferences.js.md)

##### Returns:

**
 Type

 :** 

Promise
