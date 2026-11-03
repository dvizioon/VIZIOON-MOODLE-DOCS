# mod_bigbluebuttonbn/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_bigbluebuttonbn_events.html

# mod_bigbluebuttonbn/events

 

 

 

**Description:
 :** 

- 

Events for the mod_bigbluebuttonbn plugin.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/events.js](mod_bigbluebuttonbn_amd_src_events.js.md), [line 16](mod_bigbluebuttonbn_amd_src_events.js.md)

 

**Copyright:
 :** 

- 2021 Blindside Networks Inc

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Events for the mod_bigbluebuttonbn plugin.

 

 

 

 

### Members

 

#### (static, constant) notifyCurrentSessionEnded

 

**Description:
 :** 

- 

Trigger the currentSessionEnded event.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/events.js](mod_bigbluebuttonbn_amd_src_events.js.md), [line 68](mod_bigbluebuttonbn_amd_src_events.js.md)

Trigger the currentSessionEnded event.

##### Fires:

- [event:mod_bigbluebuttonbn/currentSessionEnded](module-mod_bigbluebuttonbn_events.md)

 

#### (static, constant) notifySessionEnded

 

**Description:
 :** 

- 

Trigger the sessionEnded event.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/events.js](mod_bigbluebuttonbn_amd_src_events.js.md), [line 56](mod_bigbluebuttonbn_amd_src_events.js.md)

Trigger the sessionEnded event.

##### Fires:

- [event:mod_bigbluebuttonbn/sessionEnded](module-mod_bigbluebuttonbn_events.md)

 

 

### Events

 

#### mod_bigbluebuttonbn/currentSessionEnded

 

**Description:
 :** 

- 

Fired when the current session has been ended.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/events.js](mod_bigbluebuttonbn_amd_src_events.js.md), [line 38](mod_bigbluebuttonbn_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

 

 

##### Type:

- 

CustomEvent

 

 

#### mod_bigbluebuttonbn/sessionEnded

 

**Description:
 :** 

- 

Fired when a session has been ended.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/events.js](mod_bigbluebuttonbn_amd_src_events.js.md), [line 27](mod_bigbluebuttonbn_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `bbbId`

 

number

 

 

 
 `groupId`

 

number

 

 

 

 

 

##### Type:

- 

CustomEvent
