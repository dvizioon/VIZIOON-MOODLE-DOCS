# module:core/modal_cancel - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_modal_cancel.html

# module:core/modal_cancel

 

## 

 module:core/modal_cancel

 

 

 

 

#### new (require("core/modal_cancel"))()

 

**Source:
 :** 

- 
 [lib/amd/src/modal_cancel.js](lib_amd_src_modal_cancel.js.md), [line 31](lib_amd_src_modal_cancel.js.md)

 

 

### Extends

- [module:core/modal](module-core_modal.md)

 

 

### Members

 

#### root

 

**Description:
 :** 

- 

Getter method for .root element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 97](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#root](module-core_modal.md)

Getter method for .root element.

 

 

### Methods

 

#### configure(param0)

 

**Description:
 :** 

- 

Configure the modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 245](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#configure](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param0`

 

ModalConfig

 

The configuration options

 

 

#### getActionSelector(action) → {DOMString}

 

**Description:
 :** 

- 

Get the Selector for an action.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1184](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#getActionSelector](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `action`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

DOMString

 

#### getAttachmentPoint() → {jQuery}

 

**Description:
 :** 

- 

Gets the jQuery wrapped node that the Modal should be attached to.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 855](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#getAttachmentPoint](module-core_modal.md)

##### Returns:

**
 Type

 :** 

jQuery

 

#### setBodyContent(promise) → {Promise}

 

**Description:
 :** 

- 

Alternative to setBody() that can be used from non-Jquery modules

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 611](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setBodyContent](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `promise`

 

Promise

 

promise that returns {html, js} object

 

##### Returns:

**
 Type

 :** 

Promise

 

#### setButtonDisabled(action, disabled)

 

**Description:
 :** 

- 

Set the a button enabled or disabled.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1212](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setButtonDisabled](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `action`

 

DOMString

 

The action of the button

 
 `disabled`

 

Boolean

 

the new disabled value

 

 

#### setButtonText(action, value) → {Promise}

 

**Description:
 :** 

- 

Set the title text of a button.

This method is overloaded to take either a string value for the button title or a jQuery promise that is resolved with
text most commonly from a Str.get_string call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1168](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setButtonText](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `action`

 

DOMString

 

The action of the button

 
 `value`

 

String
|

object

 

The button text, or a promise which will resolve to it

 

##### Returns:

**
 Type

 :** 

Promise

 

#### setRemoveOnClose(remove)

 

**Description:
 :** 

- 

Set the flag to remove the modal from the DOM on close.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1193](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setRemoveOnClose](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `remove`

 

Boolean

 

 

 

 

#### setReturnElement(element)

 

**Description:
 :** 

- 

Set the return element for the modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1202](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setReturnElement](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element
|

jQuery

 

Element to focus when the modal is closed

 

 

#### setTemplateJS(js)

 

**Description:
 :** 

- 

Set the template JS for this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1229](lib_amd_src_modal.js.md)

 

**Overrides:
 :** 

- 
 [module:core/modal#setTemplateJS](module-core_modal.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `js`

 

String

 

The JavaScript to run when the modal is attached to the DOM.
