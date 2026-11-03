# core/tablock - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_tablock.html

# core/tablock

 

 

 

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 271](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 305](lib_amd_src_local_aria_focuslock.js.md)

 

#### (inner) addLockRegionToStack(newLockRegion)

 

**Description:
 :** 

- 

Add a new lock region to the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 207](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 171](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 91](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 113](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 197](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 261](lib_amd_src_local_aria_focuslock.js.md)

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
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 139](lib_amd_src_local_aria_focuslock.js.md)

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

 

#### (inner) lockHandler(event)

 

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

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 52](lib_amd_src_local_aria_focuslock.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

The event from the focus change

 

 

#### (inner) removeLastLockRegionFromStack()

 

**Description:
 :** 

- 

Remove the top lock region from the stack.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/focuslock.js](lib_amd_src_local_aria_focuslock.js.md), [line 239](lib_amd_src_local_aria_focuslock.js.md)
