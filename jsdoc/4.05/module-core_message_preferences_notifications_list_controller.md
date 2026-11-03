# core_message/preferences_notifications_list_controller - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_message_preferences_notifications_list_controller.html

# core_message/preferences_notifications_list_controller

 

 

 

**Description:
 :** 

- 

Controls the preferences for the list of notification types on the
message preference page

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 16](message_amd_src_preferences_notifications_list_controller.js.md)

 

**Copyright:
 :** 

- 2016 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the preferences for the list of notification types on the
message preference page

 

 

 

 

### Methods

 

#### (inner) isDisabled() → {bool}

 

**Description:
 :** 

- 

Check if the preferences are all disabled.

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 62](message_amd_src_preferences_notifications_list_controller.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event listeners for the PreferencesController.

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 132](message_amd_src_preferences_notifications_list_controller.js.md)

 

#### (inner) setDisabled()

 

**Description:
 :** 

- 

Disable all of the preferences.

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 72](message_amd_src_preferences_notifications_list_controller.js.md)

 

#### (inner) setEnabled()

 

**Description:
 :** 

- 

Enable all of the preferences.

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 82](message_amd_src_preferences_notifications_list_controller.js.md)

 

#### (inner) toggleDisableAllStatus() → {Promise}

 

**Description:
 :** 

- 

Update the disable all notifications user property in the DOM and
send a request to update on the server.

 

**Source:
 :** 

- 
 [message/amd/src/preferences_notifications_list_controller.js](message_amd_src_preferences_notifications_list_controller.js.md), [line 92](message_amd_src_preferences_notifications_list_controller.js.md)

##### Returns:

**
 Type

 :** 

Promise
