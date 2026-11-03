# core_badges/actions - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_badges_actions.html

# core_badges/actions

 

 

 

**Description:
 :** 

- 

Various actions on badges - enabling, disabling, etc.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 16](badges_amd_src_actions.js.md)

 

**Copyright:
 :** 

- 2024 Sara Arjona 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Various actions on badges - enabling, disabling, etc.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 38](badges_amd_src_actions.js.md)

Initialize module.

 

 

### Methods

 

#### (async, inner) disableBadge(badgeId, badgeName, reportElement)

 

**Description:
 :** 

- 

Disable the badge.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 153](badges_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `badgeId`

 

Number

 

The id of the badge to disable.

 
 `badgeName`

 

String

 

The name of the badge to enable.

 
 `reportElement`

 

HTMLElement

 

the report element.

 

 

#### (async, inner) enableBadge(badgeId, badgeName, reportElement)

 

**Description:
 :** 

- 

Enable the badge.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 100](badges_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `badgeId`

 

Number

 

The id of the badge to enable.

 
 `badgeName`

 

String

 

The name of the badge to enable.

 
 `reportElement`

 

HTMLElement

 

the report element.

 

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register events for delete preset option in action menu.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 57](badges_amd_src_actions.js.md)

 

#### (inner) showDisableResultToast(badgeName, result)

 

**Description:
 :** 

- 

Show the result of disabling a badge.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 182](badges_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `badgeName`

 

String

 

The name of the badge to disable.

 
 `result`

 

Object

 

The result of disabling a badge.

 

 

#### (inner) showEnableResultToast(badgeName, result)

 

**Description:
 :** 

- 

Show the result of enabling a badge.

 

**Source:
 :** 

- 
 [badges/amd/src/actions.js](badges_amd_src_actions.js.md), [line 132](badges_amd_src_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `badgeName`

 

String

 

The name of the badge to enable.

 
 `result`

 

Object

 

The result of enabling a badge.
