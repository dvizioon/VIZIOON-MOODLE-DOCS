# core/local/aria/aria-hidden. - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_local_aria_aria-hidden..html

# core/local/aria/aria-hidden.

 

 

 

**Description:
 :** 

- 

ARIA helpers related to the aria-hidden attribute.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/aria-hidden.js](lib_amd_src_local_aria_aria-hidden.js.md), [line 16](lib_amd_src_local_aria_aria-hidden.js.md)

 

**Copyright:
 :** 

- 2020 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

ARIA helpers related to the aria-hidden attribute.

 

 

 

 

### Methods

 

#### (static) hide(target) → {Array}

 

**Description:
 :** 

- 

Update the supplied DOM Module to be hidden.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/aria-hidden.js](lib_amd_src_local_aria_aria-hidden.js.md), [line 132](lib_amd_src_local_aria_aria-hidden.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Array

 

#### (static) hideSiblings(target) → {Array}

 

**Description:
 :** 

- 

Correctly mark all siblings of the supplied target Element as hidden.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/aria-hidden.js](lib_amd_src_local_aria_aria-hidden.js.md), [line 224](lib_amd_src_local_aria_aria-hidden.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Array

 

#### (static) unhide(target) → {Array}

 

**Description:
 :** 

- 

Reverse the effect of the hide action.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/aria-hidden.js](lib_amd_src_local_aria_aria-hidden.js.md), [line 196](lib_amd_src_local_aria_aria-hidden.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Array

 

#### (static) unhideSiblings(target) → {Array}

 

**Description:
 :** 

- 

Correctly reverse the hide action of all children of the supplied target Element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/aria/aria-hidden.js](lib_amd_src_local_aria_aria-hidden.js.md), [line 271](lib_amd_src_local_aria_aria-hidden.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

Array
