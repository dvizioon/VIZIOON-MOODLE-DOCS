# gradingform_guide/comment_chooser - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-gradingform_guide_comment_chooser.html

# gradingform_guide/comment_chooser

 

 

 

**Description:
 :** 

- 

AMD code for the frequently used comments chooser for the marking guide grading form.

 

**Source:
 :** 

- 
 [grade/grading/form/guide/amd/src/comment_chooser.js](grade_grading_form_guide_amd_src_comment_chooser.js.md), [line 16](grade_grading_form_guide_amd_src_comment_chooser.js.md)

 

**Copyright:
 :** 

- 2015 Jun Pataleta 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

AMD code for the frequently used comments chooser for the marking guide grading form.

 

 

 

 

### Methods

 

#### (static) initialise(criterionId, buttonId, remarkId, commentOptions)

 

**Description:
 :** 

- 

Initialises the module.

Basically, it performs the binding and handling of the button click event for
the 'Insert frequently used comment' button.

 

**Source:
 :** 

- 
 [grade/grading/form/guide/amd/src/comment_chooser.js](grade_grading_form_guide_amd_src_comment_chooser.js.md), [line 40](grade_grading_form_guide_amd_src_comment_chooser.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `criterionId`

 

Integer

 

The criterion ID.

 
 `buttonId`

 

String

 

The element ID of the button which the handler will be bound to.

 
 `remarkId`

 

String

 

The element ID of the remark text area where the text of the selected comment will be copied to.

 
 `commentOptions`

 

Array

 

The array of frequently used comments to be used as options.
