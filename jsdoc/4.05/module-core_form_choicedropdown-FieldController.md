# FieldController - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_form_choicedropdown-FieldController.html

# FieldController

 

## 
 [core_form/choicedropdown](module-core_form_choicedropdown.md)~

 
 FieldController

 

 

 

 

#### new FieldController(elementId)

 

**Description:
 :** 

- 

Class constructor.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 46](lib_form_amd_src_choicedropdown.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementId`

 

String

 

Form element id

 

 

 

 

### Methods

 

#### addEventListeners()

 

**Description:
 :** 

- 

Add form element event listener.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 56](lib_form_amd_src_choicedropdown.js.md)

 

#### disableInteractiveDialog()

 

**Description:
 :** 

- 

Disable the choice dialog and convert it into a regular select field.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 120](lib_form_amd_src_choicedropdown.js.md)

 

#### hasForceDialog() → {Boolean}

 

**Description:
 :** 

- 

Check if the field has a force dialog attribute.
// *
The force dialog is a setting to force the javascript control even in
behat test.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 134](lib_form_amd_src_choicedropdown.js.md)

##### Returns:

if the dialog modal should be forced or not

**
 Type

 :** 

Boolean

 

#### isDisabled() → {Boolean}

 

**Description:
 :** 

- 

Check if the field is disabled.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 89](lib_form_amd_src_choicedropdown.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### (async) updateDropdown()

 

**Description:
 :** 

- 

Update selected option preview in form.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 96](lib_form_amd_src_choicedropdown.js.md)

 

#### (async) updateSelect()

 

**Description:
 :** 

- 

Update selected option preview in form.

 

**Source:
 :** 

- 
 [lib/form/amd/src/choicedropdown.js](lib_form_amd_src_choicedropdown.js.md), [line 107](lib_form_amd_src_choicedropdown.js.md)
