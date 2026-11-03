# core/local/aria/focuslock - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_aria_focuslock.html

# core/local/aria/focuslock

 

 

 

**Description:
 :** 

- 

Tab locking system.

This is based on code and examples provided in the ARIA specification.
https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/dialog.html

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 16](lib_amd_src_local_aria_focuslock.js.md)

 

**Copyright:
 :** 

- 2019 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tab locking system.

This is based on code and examples provided in the ARIA specification.
https://www.w3.org/TR/wai-aria-practices/examples/dialog-modal/dialog.html

 

 

 

 

### Methods

 

#### (static) trapFocus(newLockRegion)

 

**Description:
 :** 

- 

Start trapping the focus and lock it to the specified newLockRegion.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 314](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newLockRegion`

 

HTMLElement

 

The container to lock focus to

 

 

#### (static) untrapFocus()

 

**Description:
 :** 

- 

Stop trapping the focus.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 349](lib_amd_src_local_aria_focuslock.js.md)

 

#### (inner) addLockRegionToStack(newLockRegion)

 

**Description:
 :** 

- 

Add a new lock region to the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 250](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newLockRegion`

 

HTMLElement

 

 

 

 

#### (inner) attemptFocus(focusTarget) → {Bool}

 

**Description:
 :** 

- 

Attempt to focus the supplied focusTarget.

Note: This example is a heavily inspired by the WCAG example.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 214](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `focusTarget`

 

HTMLElement

 

 

 

##### Returns:

Whether focus was successful o rnot.

**
 Type

 :** 

Bool

 

#### (inner) focusFirstDescendant() → {Bool}

 

**Description:
 :** 

- 

Focus the first descendant of the current lock region.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 134](lib_amd_src_local_aria_focuslock.js.md)

##### Returns:

Whether a node was focused

**
 Type

 :** 

Bool

 

#### (inner) focusLastDescendant() → {Bool}

 

**Description:
 :** 

- 

Focus the last descendant of the current lock region.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 156](lib_amd_src_local_aria_focuslock.js.md)

##### Returns:

Whether a node was focused

**
 Type

 :** 

Bool

 

#### (inner) getCurrentLockRegion() → {HTMLElement}

 

**Description:
 :** 

- 

Get the current lock region from the top of the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 240](lib_amd_src_local_aria_focuslock.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) hasTrappedRegionsInStack() → {Bool}

 

**Description:
 :** 

- 

Whether any region is left in the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 304](lib_amd_src_local_aria_focuslock.js.md)

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) isFocusable(focusTarget) → {Bool}

 

**Description:
 :** 

- 

Check whether the supplied focusTarget is actually focusable.
There are cases where a normally focusable element can reject focus.

Note: This example is a wholesale copy of the WCAG example.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 182](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `focusTarget`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) keyDownHandler(event)

 

**Description:
 :** 

- 

Catch event for any keydown during focus lock.

This is used to detect situations when the user would be tabbing out to the browser UI. In that
case, no 'focus' event is generated, so we need to trap it before it happens via the keydown
event.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 97](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

KeyboardEvent

 

 

 

 

#### (inner) lockHandler(eventopt)

 

**Description:
 :** 

- 

The lock handler.

This is the item that does a majority of the work.
The overall logic from this comes from the examles in the WCAG guidelines.

The general idea is that if the focus is not held within by an Element within the lock region, then we replace focus
on the first element in the lock region. If the first element is the element previously selected prior to the
user-initiated focus change, then instead jump to the last element in the lock region.

This gives us a solution which supports focus locking of any kind, which loops in both directions, and which
prevents the lock from escaping the modal entirely.

If no event is supplied then this function can be used to focus the first element in the lock region, or the
last element if the first element is already focused.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 55](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `event`

 

Event

 

 

 <optional>  

 

The event from the focus change

 

 

#### (inner) removeLastLockRegionFromStack()

 

**Description:
 :** 

- 

Remove the top lock region from the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 282](lib_amd_src_local_aria_focuslock.js.md)
