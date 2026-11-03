# module:core_form/dynamicform - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_form_dynamicform.html

# module:core_form/dynamicform

 

## 

 module:core_form/dynamicform

 

 

 

 

#### new (require("core_form/dynamicform"))(container, formClass)

 

**Description:
 :** 

- 

Constructor

Creates an instance

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 94](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Element

 

the parent element for the form

 
 `formClass`

 

string

 

full name of the php class that extends \core_form\modal , must be in autoloaded location

 

 

 

### Classes

 

**[core_form/dynamicform](module-core_form_dynamicform-core_form_dynamicform.md)
 :** 

 

 

 

### Members

 

#### events :Object

 

**Description:
 :** 

- 

Various events that can be observed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 58](lib_form_amd_src_dynamicform.js.md)

Various events that can be observed.

##### Type:

- 

Object

 

 

 

### Methods

 

#### addEventListener(…args)

 

**Description:
 :** 

- 

Add listener for an event

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 174](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `args`

 

array

 

 

 <repeatable>  

 

 

 

 

#### disableButtons()

 

**Description:
 :** 

- 

Disable buttons during form submission

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 324](lib_form_amd_src_dynamicform.js.md)

 

#### enableButtons()

 

**Description:
 :** 

- 

Enable buttons after form submission (on validation error)

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 332](lib_form_amd_src_dynamicform.js.md)

 

#### getFormNode() → {HTMLFormElement}

 

**Description:
 :** 

- 

Get the form node from the Dialogue.

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 260](lib_form_amd_src_dynamicform.js.md)

##### Returns:

**
 Type

 :** 

HTMLFormElement

 

#### load(args) → {Promise}

 

**Description:
 :** 

- 

Loads the form via AJAX and shows it inside a given container

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 139](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `args`

 

Object

 

 

 `null`

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### notifyResetFormChanges()

 

**Description:
 :** 

- 

Notifies listeners that form dirty state should be reset.

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 269](lib_form_amd_src_dynamicform.js.md)

##### Fires:

- event:formSubmittedByJavascript

 

#### onSubmitSuccess(response)

 

**Description:
 :** 

- 

On form submit

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 203](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `response`

 

*

 

Response received from the form's "process" method

 

 

#### processCancelButton()

 

**Description:
 :** 

- 

Click on a "cancel" button

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 277](lib_form_amd_src_dynamicform.js.md)

 

#### (async) submitFormAjax()

 

**Description:
 :** 

- 

Submit the form via AJAX call to the core_form_dynamic_form WS

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 340](lib_form_amd_src_dynamicform.js.md)

 

#### updateForm(param) → {Promise}

 

**Description:
 :** 

- 

Update form contents

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 296](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `html`

 

string

 

 

 
 `js`

 

string

 

 

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### validateElements() → {Boolean}

 

**Description:
 :** 

- 

Validate form elements

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 305](lib_form_amd_src_dynamicform.js.md)

##### Fires:

- event:formSubmittedByJavascript

##### Returns:

Whether client-side validation has passed, false if there are errors

**
 Type

 :** 

Boolean

 

#### (inner) submitButtonPressed(button)

 

**Description:
 :** 

- 

Click on a "submit" button that is marked in the form as registerNoSubmitButton()

 

**Source:
 :** 

- 
 [lib/form/amd/src/dynamicform.js](lib_form_amd_src_dynamicform.js.md), [line 231](lib_form_amd_src_dynamicform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `button`

 

Element

 

that was pressed

 

##### Fires:

- event:formSubmittedByJavascript
