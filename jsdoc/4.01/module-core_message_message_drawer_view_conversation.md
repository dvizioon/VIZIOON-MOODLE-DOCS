# core_message/message_drawer_view_conversation - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_message_message_drawer_view_conversation.html

# core_message/message_drawer_view_conversation

 

 

 

**Description:
 :** 

- 

Controls the conversation page in the message drawer.

This function handles all of the user actions that the user can take
when interacting with the conversation page.

It maintains a view state which is a data representation of the view
and only operates on that data.

The view state is immutable and should never be modified directly. Instead
all changes to the view state should be done using the StateManager which
will generate a new version of the view state with the requested changes.

After any changes to the view state the module will call the render function
to ask the renderer to update the UI.

General rules for this module:
1.) Never modify viewState directly. All changes should be via the StateManager.
2.) Call render() with the new state when you want to update the UI
3.) Never modify the UI directly in this module. This module is only concerned
with the data in the view state.

The general flow for a user interaction will be something like:
User interaction: User clicks "confirm block" button to block the other user
1.) This module is hears the click
2.) This module sends a request to the server to block the user
3.) The server responds with the new user profile
4.) This module generates a new state using the StateManager with the updated
user profile.
5.) This module asks the Patcher to generate a patch from the current state and
the newly generated state. This patch tells the renderer what has changed
between the states.
6.) This module gives the Renderer the generated patch. The renderer updates
the UI with changes according to the patch.

 

**Source:
 :** 

- 
 [message/amd/src/message_drawer_view_conversation.js](message_amd_src_message_drawer_view_conversation.js.md), [line 16](message_amd_src_message_drawer_view_conversation.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Controls the conversation page in the message drawer.

This function handles all of the user actions that the user can take
when interacting with the conversation page.

It maintains a view state which is a data representation of the view
and only operates on that data.

The view state is immutable and should never be modified directly. Instead
all changes to the view state should be done using the StateManager which
will generate a new version of the view state with the requested changes.

After any changes to the view state the module will call the render function
to ask the renderer to update the UI.

General rules for this module:
1.) Never modify viewState directly. All changes should be via the StateManager.
2.) Call render() with the new state when you want to update the UI
3.) Never modify the UI directly in this module. This module is only concerned
with the data in the view state.

The general flow for a user interaction will be something like:
User interaction: User clicks "confirm block" button to block the other user
1.) This module is hears the click
2.) This module sends a request to the server to block the user
3.) The server responds with the new user profile
4.) This module generates a new state using the StateManager with the updated
user profile.
5.) This module asks the Patcher to generate a patch from the current state and
the newly generated state. This patch tells the renderer what has changed
between the states.
6.) This module gives the Renderer the generated patch. The renderer updates
the UI with changes according to the patch.
