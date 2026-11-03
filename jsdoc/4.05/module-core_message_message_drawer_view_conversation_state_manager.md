# core_message/message_drawer_view_conversation_state_manager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_message_message_drawer_view_conversation_state_manager.html

# core_message/message_drawer_view_conversation_state_manager

 

 

 

**Description:
 :** 

- 

This module operates on the view states from the message_drawer_view_conversation module.
It exposes functions that can be used to generate new version of the state.

Important notes for this module:
1.) The existing state is always immutable. It should never be modified.
2.) All functions that operate on the state should always clone the state and
modify the cloned state before returning it.

It's important that the states remain immutable because they are diff'd in
the message_drawer_view_conversation_patcher module in order to work out what
has changed.

 

**Source:
 :** 

- 
 [message/amd/src/message_drawer_view_conversation_state_manager.js](message_amd_src_message_drawer_view_conversation_state_manager.js.md), [line 16](message_amd_src_message_drawer_view_conversation_state_manager.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module operates on the view states from the message_drawer_view_conversation module.
It exposes functions that can be used to generate new version of the state.

Important notes for this module:
1.) The existing state is always immutable. It should never be modified.
2.) All functions that operate on the state should always clone the state and
modify the cloned state before returning it.

It's important that the states remain immutable because they are diff'd in
the message_drawer_view_conversation_patcher module in order to work out what
has changed.
