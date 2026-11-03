# mod_lti/coursecategory - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_lti_coursecategory.html

# mod_lti/coursecategory

 

 

 

**Description:
 :** 

- 

Select course categories for LTI tool.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/coursecategory.js](mod_lti_amd_src_coursecategory.js.md), [line 16](mod_lti_amd_src_coursecategory.js.md)

 

**Since:
 :** 

- 4.3

 

**Copyright:
 :** 

- 2023 Jackson D'souza 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Select course categories for LTI tool.

 

 

 

 

### Methods

 

#### (static) init(selectedcategories)

 

**Description:
 :** 

- 

Initialise this module.
Loop through checkbox form elements starting with #cat-{N} and set it to checked
if {N} is found in the Selected category(s) list. Show / Hide the parent UL element.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/coursecategory.js](mod_lti_amd_src_coursecategory.js.md), [line 91](mod_lti_amd_src_coursecategory.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectedcategories`

 

string

 

Selected category(s).
