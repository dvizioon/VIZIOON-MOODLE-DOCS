# core_message/notification_preference - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_message_notification_preference.html

# core_message/notification_preference

 

 

 

**Description:
 :** 

- 

Controls the preference for an individual notification type on the
message preference page.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 16](message_amd_src_notification_preference.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the preference for an individual notification type on the
message preference page.

 

 

 

 

### Methods

 

#### (inner) getEnabledPreferenceKey() → {string}

 

**Description:
 :** 

- 

Get the unique key for the enabled preference.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 54](message_amd_src_notification_preference.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) getPreferenceKey() → {string}

 

**Description:
 :** 

- 

Get the unique prefix key that identifies this user preference.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 44](message_amd_src_notification_preference.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) getProcessors() → {array}

 

**Description:
 :** 

- 

Get the list of Processors available for this preference.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 64](message_amd_src_notification_preference.js.md)

##### Returns:

**
 Type

 :** 

array

 

#### (inner) isLoading() → {Boolean}

 

**Description:
 :** 

- 

Check if the preference is loading.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 96](message_amd_src_notification_preference.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) save() → {object}

 

**Description:
 :** 

- 

Persist the current state of the processors for this preference.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 106](message_amd_src_notification_preference.js.md)

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) startLoading()

 

**Description:
 :** 

- 

Flag the preference as loading.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 76](message_amd_src_notification_preference.js.md)

 

#### (inner) stopLoading()

 

**Description:
 :** 

- 

Remove the loading flag for this preference.

 

**Source:
 :** 

- 
 [message/amd/src/notification_preference.js](message_amd_src_notification_preference.js.md), [line 86](message_amd_src_notification_preference.js.md)
