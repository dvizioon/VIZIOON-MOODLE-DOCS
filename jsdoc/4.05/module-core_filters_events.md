# core_filters/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_filters_events.html

# core_filters/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `core_filters` subsystem.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 15](filter_amd_src_events.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `core_filters` subsystem.

 

### Example

 

Example of listening to a filter event.

 

```js
import {eventTypes as filterEventTypes} from 'core_filters/events';

document.addEventListener(filterEventTypes.filterContentUpdated, e => {
    window.console.log(e.detail.nodes); // A list of the HTMLElements whose content was updated
});
```

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for the `core_filters` subsystem.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 41](filter_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `filterContentUpdated`

 

String

 

See [event:filterContentUpdated](module-core_filters_events.md)

 
 `filterContentRenderingComplete`

 

String

 

See [event:filterContentRenderingComplete](module-core_filters_events.md)

 

Events for the `core_filters` subsystem.

 

 

### Methods

 

#### (inner) notifyFilterContentRenderingComplete(nodes) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that the filter has been processed.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 81](filter_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `nodes`

 

NodeList
|

Array.<Node>

 

List of nodes that has been modified by filter

 

##### Fires:

- [event:filterContentRenderingComplete](module-core_filters_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### (inner) notifyFilterContentUpdated(nodes) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that the specified nodes were updated and should be processed by the filter system.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 65](filter_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `nodes`

 

jQuery
|

Array

 

 

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### filterContentRenderingComplete

 

**Description:
 :** 

- 

An event triggered when filter system have done rendering the content using the filter system.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 55](filter_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

 

 

##### Type:

- 

CustomEvent

 

 

#### filterContentUpdated

 

**Description:
 :** 

- 

An event triggered when page content is updated and must be processed by the filter system.

An example of this is loading user text that could have equations in it. MathJax can typeset the equations but
only if it is notified that there are new nodes in the page that need processing.

 

**Source:
 :** 

- 
 [filter/amd/src/events.js](filter_amd_src_events.js.md), [line 42](filter_amd_src_events.js.md)

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

 

 

 
 `nodes`

 

Array.<NodeElement>

 

The list of parent nodes which were updated

 

 

 

##### Type:

- 

CustomEvent

 

##### Listeners of This Event:

- [module:media_videojs/loader.setUp](module-media_videojs_loader.md)
