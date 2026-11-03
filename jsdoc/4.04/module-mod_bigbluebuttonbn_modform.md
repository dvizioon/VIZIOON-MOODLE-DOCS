# mod_bigbluebuttonbn/modform - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_bigbluebuttonbn_modform.html

# mod_bigbluebuttonbn/modform

 

 

 

**Description:
 :** 

- 

JS for the mod_form page on mod_bigbluebuttonbn plugin.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 16](mod_bigbluebuttonbn_amd_src_modform.js.md)

 

**Copyright:
 :** 

- 2021 Blindside Networks Inc

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JS for the mod_form page on mod_bigbluebuttonbn plugin.

 

 

 

 

### Members

 

#### (inner, constant) ELEMENT_SELECTOR

 

**Description:
 :** 

- 

Get all selectors in one place.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 32](mod_bigbluebuttonbn_amd_src_modform.js.md)

Get all selectors in one place.

 

 

### Methods

 

#### (inner) applyInstanceTypeProfile(profileType, isFeatureEnabled)

 

**Description:
 :** 

- 

Show or hide form element depending on the selected profile

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 90](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `profileType`

 

string

 

 

 
 `isFeatureEnabled`

 

function

 

 

 

 

#### (inner) getParticipantList() → {any}

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 261](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Returns:

**
 Type

 :** 

any

 

#### (inner) init(info)

 

**Description:
 :** 

- 

Initialise the moodle form code.

This will help hide or show items depending on the selection of the instance type.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 42](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `info`

 

object

 

 

 

 

#### (inner) participantAddFromCurrentSelection()

 

**Description:
 :** 

- 

Add participant from the currently selected options

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 319](mod_bigbluebuttonbn_amd_src_modform.js.md)

 

#### (async, inner) participantAddToForm(selectionTypeValue, selectionValue, selectedRole, canRemove) → {Promise.<void>}

 

**Description:
 :** 

- 

Add rows to the participant list depending on the current selection.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 204](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectionTypeValue`

 

string

 

 

 
 `selectionValue`

 

string

 

 

 
 `selectedRole`

 

string

 

 

 
 `canRemove`

 

boolean

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (inner) participantListInit()

 

**Description:
 :** 

- 

Init the participant list

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 180](mod_bigbluebuttonbn_amd_src_modform.js.md)

 

#### (inner) participantListRoleUpdate(type, id)

 

**Description:
 :** 

- 

Role update

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 302](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

string

 

 

 
 `id`

 

string

 

 

 

 

#### (inner) participantListUpdate(list)

 

**Description:
 :** 

- 

Update the related form element with the list value.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 252](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `list`

 

object

 

 

 

 

#### (inner) participantRemove(selectionTypeValue, selectionValue)

 

**Description:
 :** 

- 

Remove participant both in the table/form and in the form element.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 275](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectionTypeValue`

 

string

 

 

 
 `selectionValue`

 

string

 

 

 

 

#### (inner) updateSelectionFromType(currentTypeSelect)

 

**Description:
 :** 

- 

Update selectable options when changing types

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/modform.js](mod_bigbluebuttonbn_amd_src_modform.js.md), [line 346](mod_bigbluebuttonbn_amd_src_modform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentTypeSelect`

 

HTMLNode
