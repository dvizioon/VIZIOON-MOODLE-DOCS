# tool_usertours/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_usertours_events.html

# tool_usertours/events

 

 

 

**Description:
 :** 

- 

Javascript events for the `tool_usertours` subsystem.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 16](admin_tool_usertours_amd_src_events.js.md)

 

**Copyright:
 :** 

- 2021 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript events for the `tool_usertours` subsystem.

 

### Example

 

Example of listening to a step rendering event and cancelling it.

 

```js
import {eventTypes as userTourEvents} from 'tool_usertours/events';

document.addEventListener(userTourEvents.stepRender, e => {
    console.log(e.detail.tour); // The Tour instance
    e.preventDefault();
});
```

 

 

 

 

### Members

 

#### (static, constant) eventTypes

 

**Description:
 :** 

- 

Events for the component.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 46](admin_tool_usertours_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `eventTypes`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `stepRender`

 

String

 

See [event:tool_usertours/stepRender](module-tool_usertours_events.md)

 
 `stepRendered`

 

String

 

See [event:tool_usertours/stepRendered](module-tool_usertours_events.md)

 
 `tourStart`

 

String

 

See [event:tool_usertours/tourStart](module-tool_usertours_events.md)

 
 `tourStarted`

 

String

 

See [event:tool_usertours/tourStarted](module-tool_usertours_events.md)

 
 `tourEnd`

 

String

 

See [event:tool_usertours/tourEnd](module-tool_usertours_events.md)

 
 `tourEnded`

 

String

 

See [event:tool_usertours/tourEnded](module-tool_usertours_events.md)

 
 `stepHide`

 

String

 

See [event:tool_usertours/stepHide](module-tool_usertours_events.md)

 
 `stepHidden`

 

String

 

See [event:tool_usertours/stepHidden](module-tool_usertours_events.md)

 

 

 

Events for the component.

 

 

### Events

 

#### tool_usertours/stepHidden

 

**Description:
 :** 

- 

An event triggered after a step has been hidden.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 128](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/stepHide

 

**Description:
 :** 

- 

An event triggered before a step is hidden.

This event is cancellable.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 116](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/stepRender

 

**Description:
 :** 

- 

An event triggered before a user tour step is rendered.

This event is cancellable.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 47](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 
 `stepConfig`

 

object

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/stepRendered

 

**Description:
 :** 

- 

An event triggered after a user tour step has been rendered.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 60](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 
 `stepConfig`

 

object

 

 

 

 

 

##### Type:

- 

CustomEvent

 

##### Listeners of This Event:

- [module:tool_usertours/usertours~markTourComplete](module-tool_usertours_usertours.md)

 

#### tool_usertours/tourEnd

 

**Description:
 :** 

- 

An event triggered before a tour ends.

This event is cancellable.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 94](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/tourEnded

 

**Description:
 :** 

- 

An event triggered after a tour has ended.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 106](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/tourStart

 

**Description:
 :** 

- 

An event triggered before a user tour starts.

This event is cancellable.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 71](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 
 `startAt`

 

Number

 

 

 

 

 

##### Type:

- 

CustomEvent

 

 

#### tool_usertours/tourStarted

 

**Description:
 :** 

- 

An event triggered after a user tour has started.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/events.js](admin_tool_usertours_amd_src_events.js.md), [line 84](admin_tool_usertours_amd_src_events.js.md)

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

 

 

 
 `tour`

 

tool_usertours/tour

 

 

 

 

 

##### Type:

- 

CustomEvent
