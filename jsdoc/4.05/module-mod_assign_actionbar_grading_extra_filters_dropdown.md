# mod_assign/actionbar/grading/extra_filters_dropdown - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_actionbar_grading_extra_filters_dropdown.html

# mod_assign/actionbar/grading/extra_filters_dropdown

 

 

 

**Description:
 :** 

- 

Module for the extra filters dropdown on the submissions page.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 20](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

 

**Copyright:
 :** 

- 2024 Mihail Geshoski 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module for the extra filters dropdown on the submissions page.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 120](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

Initialize module.

 

#### (inner, constant) The :Object

 

**Description:
 :** 

- 

object containing the relevant selectors.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 28](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

object containing the relevant selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) registerEventListeners(extraFiltersDropdown)

 

**Description:
 :** 

- 

Register event listeners for the extra filters dropdown.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 43](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `extraFiltersDropdown`

 

DropdownDialog

 

The dropdown dialog instance.

 

 

#### (async, inner) restoreAppliedMarkerFilter(extraFiltersDropdown)

 

**Description:
 :** 

- 

Restores the currently applied marker filter to its stored preference value.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 93](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `extraFiltersDropdown`

 

DropdownDialog

 

The dropdown dialog instance.

 

 

#### (async, inner) restoreAppliedSuspendedParticipantsFilter(extraFiltersDropdown)

 

**Description:
 :** 

- 

Restores the currently suspended participants filter to its stored preference value.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 105](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `extraFiltersDropdown`

 

DropdownDialog

 

The dropdown dialog instance.

 

 

#### (async, inner) restoreAppliedWorkflowFilter(extraFiltersDropdown)

 

**Description:
 :** 

- 

Restores the currently applied workflow filter to its stored preference value.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/actionbar/grading/extra_filters_dropdown.js](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md), [line 81](mod_assign_amd_src_actionbar_grading_extra_filters_dropdown.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `extraFiltersDropdown`

 

DropdownDialog

 

The dropdown dialog instance.
