# core/togglesensitive - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_togglesensitive.html

# core/togglesensitive

 

 

 

**Description:
 :** 

- 

JS module for toggling the sensitive input visibility (e.g. passwords, keys).

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 16](lib_amd_src_togglesensitive.js.md)

 

**Copyright:
 :** 

- 2023 David Woloszyn 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JS module for toggling the sensitive input visibility (e.g. passwords, keys).

 

 

 

 

### Methods

 

#### (inner) handleButtonInteraction(event)

 

**Description:
 :** 

- 

Handle events trigger by interacting with the toggle button.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 101](lib_amd_src_togglesensitive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

The button event.

 

 

#### (inner) handleScreenResizing()

 

**Description:
 :** 

- 

Handle events trigger by resizing the screen.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 117](lib_amd_src_togglesensitive.js.md)

 

#### (inner) init(elementId, isSmallScreensOnly)

 

**Description:
 :** 

- 

Entrypoint of the js.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 44](lib_amd_src_togglesensitive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

Form button element.

 
 `isSmallScreensOnly`

 

boolean

 

Is this for small screens only?

 

 

#### (inner) registerListenerEvents()

 

**Description:
 :** 

- 

Register event listeners.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 87](lib_amd_src_togglesensitive.js.md)

 

#### (inner) renderSensitiveToggle(sensitiveInput)

 

**Description:
 :** 

- 

Render the new input html with toggle button and update the incoming html.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 66](lib_amd_src_togglesensitive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sensitiveInput`

 

HTMLElement

 

HTML element for the sensitive input.

 

 

#### (inner) toggleSensitiveVisibility(sensitiveInput, toggleButton, force)

 

**Description:
 :** 

- 

Toggle the sensitive input visibility and its associated icon.

 

**Source:
 :** 

- 
 [lib/amd/src/togglesensitive.js](lib_amd_src_togglesensitive.js.md), [line 134](lib_amd_src_togglesensitive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sensitiveInput`

 

HTMLInputElement

 

The sensitive input element.

 
 `toggleButton`

 

HTMLElement

 

The toggle button.

 
 `force`

 

boolean

 

Force the input back to password type.
