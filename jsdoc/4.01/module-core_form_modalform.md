# module:core_form/modalform - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_form_modalform.html

# module:core_form/modalform

 

## 

 module:core_form/modalform

 

 

 

 

#### new (require("core_form/modalform"))(config)

 

**Description:
 :** 

- 

Constructor

Shows the required form inside a modal dialogue

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 99](lib_form_amd_src_modalform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

Object

 

parameters for the form and modal dialogue:

 

 

 

 

### Members

 

#### events :Object

 

**Description:
 :** 

- 

Various events that can be observed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 55](lib_form_amd_src_modalform.js.md)

Various events that can be observed.

##### Type:

- 

Object

 

 

#### (inner) list :jQuery

 

**Description:
 :** 

- 

of elements with errors

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 323](lib_form_amd_src_modalform.js.md)

of elements with errors

##### Type:

- 

jQuery

 

 

 

### Methods

 

#### addEventListener(…args)

 

**Description:
 :** 

- 

Add listener for an event

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 219](lib_form_amd_src_modalform.js.md)

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
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 338](lib_form_amd_src_modalform.js.md)

 

#### enableButtons()

 

**Description:
 :** 

- 

Enable buttons after form submission (on validation error)

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 345](lib_form_amd_src_modalform.js.md)

 

#### getFormNode() → {HTMLFormElement}

 

**Description:
 :** 

- 

Get the form node from the Dialogue.

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 286](lib_form_amd_src_modalform.js.md)

##### Returns:

**
 Type

 :** 

HTMLFormElement

 

#### notifyResetFormChanges()

 

**Description:
 :** 

- 

Notifies listeners that form dirty state should be reset.

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 270](lib_form_amd_src_modalform.js.md)

##### Fires:

- event:formSubmittedByJavascript

 

#### onSubmitError(exception)

 

**Description:
 :** 

- 

On exception during form processing. Caller may override

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 256](lib_form_amd_src_modalform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `exception`

 

Object

 

 

 

 

#### processNoSubmitButton(button)

 

**Description:
 :** 

- 

Click on a "submit" button that is marked in the form as registerNoSubmitButton()

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 296](lib_form_amd_src_modalform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `button`

 

Element

 

button that was pressed

 

##### Fires:

- event:formSubmittedByJavascript

 

#### (async) submitFormAjax()

 

**Description:
 :** 

- 

Submit the form via AJAX call to the core_form_dynamic_form WS

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 352](lib_form_amd_src_modalform.js.md)

 

#### validateElements() → {Boolean}

 

**Description:
 :** 

- 

Validate form elements

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 319](lib_form_amd_src_modalform.js.md)

##### Fires:

- event:formSubmittedByJavascript

##### Returns:

Whether client-side validation has passed, false if there are errors

**
 Type

 :** 

Boolean

 

#### (inner) setSaveButtonClasses(value)

 

**Description:
 :** 

- 

Set the classes for the 'save' button.

 

**Source:
 :** 

- 
 [lib/form/amd/src/modalform.js](lib_form_amd_src_modalform.js.md), [line 394](lib_form_amd_src_modalform.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

String

 

The 'save' button classes.
