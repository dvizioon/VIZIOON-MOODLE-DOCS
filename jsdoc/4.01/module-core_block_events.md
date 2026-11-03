# core_block/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_block_events.html

# core_block/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `core_block` subsystem.

 

**Source:
 :** 

- 
 [blocks/amd/src/events.js](blocks_amd_src_events.js.md), [line 15](blocks_amd_src_events.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `core_block` subsystem.

 

### Example

 

Example of listening to a block event.

 

```js
import {eventTypes as blockEventTypes} from 'core_block/events';

document.addEventListener(blockEventTypes.blockContentUpdated, e => {
    window.console.log(e.target); // The HTMLElement relating to the block whose content was updated.
    window.console.log(e.detail.instanceId); // The instanceId of the block that was updated.
});
```

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for `core_block`.

 

**Source:
 :** 

- 
 [blocks/amd/src/events.js](blocks_amd_src_events.js.md), [line 40](blocks_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `blockContentUpdated`

 

String

 

See [event:blockContentUpdated](module-core_block_events.md)

 

Events for `core_block`.

 

 

### Methods

 

#### (inner) notifyBlockContentUpdated(element) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that the content of a block was updated.

 

**Source:
 :** 

- 
 [blocks/amd/src/events.js](blocks_amd_src_events.js.md), [line 53](blocks_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The HTMLElement containing the updated block.

 

##### Fires:

- [event:blockContentUpdated](module-core_block_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### blockContentUpdated

 

**Description:
 :** 

- 

An event triggered when the content of a block has changed.

 

**Source:
 :** 

- 
 [blocks/amd/src/events.js](blocks_amd_src_events.js.md), [line 41](blocks_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The block element that was updated

 
 `detail`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `instanceId`

 

number

 

The block instance id

 

 

 

##### Type:

- 

CustomEvent
