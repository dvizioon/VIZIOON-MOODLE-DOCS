# core_form/showadvanced - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_form_showadvanced.html

# core_form/showadvanced

 

 

 

**Description:
 :** 

- 

A class to help show and hide advanced form content.

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 16](lib_form_amd_src_showadvanced.js.md)

 

**Copyright:
 :** 

- 2016 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A class to help show and hide advanced form content.

 

 

 

### Classes

 

**[core_form/showadvanced](module-core_form_showadvanced-core_form_showadvanced.md)
 :** 

 

 

 

### Methods

 

#### (inner) enhanceFieldset(fieldset) → {ShowAdvanced}

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 110](lib_form_amd_src_showadvanced.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `fieldset`

 

JQuery

 

JQuery selector representing a fieldset

 

##### Returns:

**
 Type

 :** 

ShowAdvanced

 

#### (inner) enhanceForm(form) → {ShowAdvanced}

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 64](lib_form_amd_src_showadvanced.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

JQuery

 

JQuery selector representing the form

 

##### Returns:

**
 Type

 :** 

ShowAdvanced

 

#### (inner) generateId(node) → {String}

 

**Description:
 :** 

- 

Generates a uniq id for the dom element it's called on unless the element already has an id.
The id is set on the dom node before being returned.

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 93](lib_form_amd_src_showadvanced.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

JQuery

 

JQuery selector representing a single DOM Node.

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) init(formid) → {ShowAdvanced}

 

**Description:
 :** 

- 

Initialise this module.

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 217](lib_form_amd_src_showadvanced.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formid`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

ShowAdvanced

 

#### (inner) switchState(e) → {Boolean}

 

**Source:
 :** 

- 
 [lib/form/amd/src/showadvanced.js](lib_form_amd_src_showadvanced.js.md), [line 172](lib_form_amd_src_showadvanced.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

Event that triggered this action.

 

##### Returns:

**
 Type

 :** 

Boolean
