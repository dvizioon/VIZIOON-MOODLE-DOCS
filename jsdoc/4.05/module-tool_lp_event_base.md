# tool_lp/event_base - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_lp_event_base.html

# tool_lp/event_base

 

 

 

**Description:
 :** 

- 

Event base javascript module.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/event_base.js](admin_tool_lp_amd_src_event_base.js.md), [line 16](admin_tool_lp_amd_src_event_base.js.md)

 

**Copyright:
 :** 

- 2015 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Event base javascript module.

 

 

 

 

### Methods

 

#### (inner) _trigger(type, data)

 

**Description:
 :** 

- 

Trigger an event.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/event_base.js](admin_tool_lp_amd_src_event_base.js.md), [line 46](admin_tool_lp_amd_src_event_base.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

String

 

The type of event.

 
 `data`

 

Object

 

The data to pass to the listeners.

 

 

#### (inner) on(type, handler)

 

**Description:
 :** 

- 

Register an event listener.

 

**Source:
 :** 

- 
 [admin/tool/lp/amd/src/event_base.js](admin_tool_lp_amd_src_event_base.js.md), [line 35](admin_tool_lp_amd_src_event_base.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

String

 

The event type.

 
 `handler`

 

function

 

The event listener.
