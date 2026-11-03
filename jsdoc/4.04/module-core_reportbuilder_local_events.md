# core_reportbuilder/local/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_reportbuilder_local_events.html

# core_reportbuilder/local/events

 

 

 

**Description:
 :** 

- 

Report builder events

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/events.js](reportbuilder_amd_src_local_events.js.md), [line 16](reportbuilder_amd_src_local_events.js.md)

 

**Copyright:
 :** 

- 2021 Paul Holden 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Report builder events

 

 

 

 

### Events

 

#### tableReload

 

**Description:
 :** 

- 

Trigger table reloading

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/events.js](reportbuilder_amd_src_local_events.js.md), [line 31](reportbuilder_amd_src_local_events.js.md)

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

 

 

 
 `preservePagination`

 

Boolean

 

Whether current pagination should be preserved (default false)

 
 `preserveTriggerElement`

 

String

 

Element selector that should be focused after table reload (default null)

 

 

 

##### Type:

- 

CustomEvent

 

##### Example

 

Triggering table reload

 

```js
import {dispatchEvent} from 'core/event_dispatcher';
import * as reportEvents from 'core_reportbuilder/local/events';

dispatchEvent(reportEvents.tableReload, {}, document.querySelector(...));
```
