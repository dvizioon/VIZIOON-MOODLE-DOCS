# core/event_dispatcher - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_event_dispatcher.html

# core/event_dispatcher

 

 

 

**Description:
 :** 

- 

An Event dispatcher used to dispatch Native JS CustomEvent objects with custom default properties.

 

**Source:
 :** 

- 
 [lib/amd/src/event_dispatcher.js](lib_amd_src_event_dispatcher.js.md), [line 15](lib_amd_src_event_dispatcher.js.md)

 

**Since:
 :** 

- 4.0

 

**Copyright:
 :** 

- 2021 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

An Event dispatcher used to dispatch Native JS CustomEvent objects with custom default properties.

 

 

 

 

### Methods

 

#### (inner) dispatchEvent(eventName, detail, container, options) → {CustomEvent}

 

**Description:
 :** 

- 

Dispatch an event as a CustomEvent on the specified container.
By default events are bubbled, and cancelable.

The eventName should typically by sourced using a constant. See the supplied examples.

Note: This function uses native events. Any additional details are passed to the function in event.detail.

This function mimics the behaviour of EventTarget.dispatchEvent but bubbles by default.

 

**Source:
 :** 

- 
 [lib/amd/src/event_dispatcher.js](lib_amd_src_event_dispatcher.js.md), [line 24](lib_amd_src_event_dispatcher.js.md)

##### Example

 

Using a native CustomEvent to indicate that some example data was displayed.

 

```js
// mod/example/amd/src/events.js

import {dispatchEvent} from 'core/event_dispatcher';

export const eventTypes = {
    exampleDataDisplayed: 'mod_example/exampleDataDisplayed',
};

export const notifyExampleDisplayed = someArgument => dispatchEvent(eventTypes.exampleDataDisplayed, {
    someArgument,
}, document, {
    cancelable: false,
});
```

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventName`

 

String

 

The name of the event

 
 `detail`

 

Object

 

Any additional details to pass into the eveent

 
 `container`

 

HTMLElement

 

The point at which to dispatch the event

 
 `options`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `bubbles`

 

Boolean

 

Whether to bubble up the DOM

 
 `cancelable`

 

Boolean

 

Whether preventDefault() can be called

 
 `composed`

 

Boolean

 

Whether the event can bubble across the ShadowDOM bounadry

 

 

 

##### Returns:

**
 Type

 :** 

CustomEvent
