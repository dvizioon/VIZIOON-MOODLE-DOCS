# mod_assign/grading_form_change_checker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_assign_grading_form_change_checker.html

# mod_assign/grading_form_change_checker

 

 

 

**Description:
 :** 

- 

Simple method to check for changes to a form between two points in time.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_form_change_checker.js](mod_assign_amd_src_grading_form_change_checker.js.md), [line 16](mod_assign_amd_src_grading_form_change_checker.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2016 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Simple method to check for changes to a form between two points in time.

 

 

 

 

### Methods

 

#### (inner) checkFormForChanges(selector) → {Boolean}

 

**Description:
 :** 

- 

Compare the current values in the form to the previously saved state.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_form_change_checker.js](mod_assign_amd_src_grading_form_change_checker.js.md), [line 39](mod_assign_amd_src_grading_form_change_checker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

The selector for the form element.

 

##### Returns:

True if there are changes to the form data.

**
 Type

 :** 

Boolean

 

#### (inner) saveFormState(selector)

 

**Description:
 :** 

- 

Save the values in the form to a data attribute so they can be compared later for changes.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_form_change_checker.js](mod_assign_amd_src_grading_form_change_checker.js.md), [line 27](mod_assign_amd_src_grading_form_change_checker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

The selector for the form element.
