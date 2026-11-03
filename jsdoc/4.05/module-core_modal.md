# module:core/modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_modal.html

# module:core/modal

 

## 

 module:core/modal

 

 

 

 

#### new (require("core/modal"))(root)

 

**Description:
 :** 

- 

Constructor for the Modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 114](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The HTMLElement at the root of the Modal content

 

 

 

 

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

Getter method for .root element.

 

#### root

 

**Description:
 :** 

- 

Setter method for .root element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 105](lib_amd_src_modal.js.md)

Setter method for .root element.

 

#### (inner) A :Number

 

**Description:
 :** 

- 

counter that gets incremented for each modal created.
This can be used to generate unique values for the modals.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 87](lib_amd_src_modal.js.md)

counter that gets incremented for each modal created.
This can be used to generate unique values for the modals.

##### Type:

- 

Number

 

 

#### (inner) Module :Promise

 

**Description:
 :** 

- 

singleton for the backdrop to be reused by all Modal instances

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 84](lib_amd_src_modal.js.md)

singleton for the backdrop to be reused by all Modal instances

##### Type:

- 

Promise

 

 

#### (inner) The :string

 

**Description:
 :** 

- 

type of modal

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 78](lib_amd_src_modal.js.md)

type of modal

##### Type:

- 

string

 

 

#### (inner) The :string

 

**Description:
 :** 

- 

template to use for this modal

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 81](lib_amd_src_modal.js.md)

template to use for this modal

##### Type:

- 

string

 

 

 

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

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `js`

 

String

 

The JavaScript to run when the modal is attached to the DOM.

 

 

#### (protected, static) _getTemplateName(modalConfig) → {string}

 

**Description:
 :** 

- 

A helper to get the template name for this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 218](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalConfig`

 

ModalConfig

 

 

 

##### Returns:

**
 Type

 :** 

string

 

#### (static) registerModalType()

 

**Description:
 :** 

- 

Register a modal with the legacy modal registry.

This is provided to allow backwards-compatibility with existing code that uses the legacy modal registry.
It is not necessary to register modals for code only present in Moodle 4.3 and later.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 169](lib_amd_src_modal.js.md)

 

#### (inner) accessibilityHide()

 

**Description:
 :** 

- 

Restores the aria visibility on the DOM elements changed when displaying
the dialogue popup and makes the dialogue aria hidden to allow screen
readers to navigate the main page correctly when the dialogue is closed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 990](lib_amd_src_modal.js.md)

 

#### (inner) accessibilityShow()

 

**Description:
 :** 

- 

Sets the appropriate aria attributes on this dialogue and the other
elements in the DOM to ensure that screen readers are able to navigate
the dialogue popup correctly.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 975](lib_amd_src_modal.js.md)

 

#### (inner) asyncSet(value, setFunction) → {Promise}

 

**Description:
 :** 

- 

Set or resolve and set the value using the function.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1132](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The string or jQuery promise.

 
 `setFunction`

 

function

 

The setter

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) attachToDOM()

 

**Description:
 :** 

- 

Attach the modal to the correct part of the page.

If it hasn't already been added it runs any
javascript that has been cached until now.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 291](lib_amd_src_modal.js.md)

 

#### (inner) calculateZIndex() → {int}

 

**Description:
 :** 

- 

Determine the highest z-index value currently on the page.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 790](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) countOtherVisibleModals() → {int}

 

**Description:
 :** 

- 

Count the number of other visible modals (not including this one).

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 328](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) destroy()

 

**Description:
 :** 

- 

Remove this modal from the DOM.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 962](lib_amd_src_modal.js.md)

 

#### (inner) getBackdrop() → {object}

 

**Description:
 :** 

- 

Get the modal backdrop.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 348](lib_amd_src_modal.js.md)

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### (inner) getBody() → {object}

 

**Description:
 :** 

- 

Get the modal body element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 394](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getBodyPromise() → {object}

 

**Description:
 :** 

- 

Get a promise resolving to the body region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 424](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getFooter() → {object}

 

**Description:
 :** 

- 

Get the modal footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 404](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getFooterPromise() → {object}

 

**Description:
 :** 

- 

Get a promise resolving to the footer region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 434](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getModal() → {object}

 

**Description:
 :** 

- 

Get the modal element of this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 374](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getModalCount() → {int}

 

**Description:
 :** 

- 

Get the unique modal count.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 444](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getRoot() → {object}

 

**Description:
 :** 

- 

Get the root element of this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 364](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getTitle() → {object}

 

**Description:
 :** 

- 

Get the modal title element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 384](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### (inner) getTitlePromise() → {Promise}

 

**Description:
 :** 

- 

Get a promise resolving to the title region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 414](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) hasFocus() → {bool}

 

**Description:
 :** 

- 

Check if this modal has focus.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 829](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hasFooterContent() → {bool}

 

**Description:
 :** 

- 

Check if the footer has any content in it.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 678](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hasTransitions() → {bool}

 

**Description:
 :** 

- 

Check if this modal has CSS transitions applied.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 840](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) hide()

 

**Description:
 :** 

- 

Hide this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 918](lib_amd_src_modal.js.md)

 

#### (inner) hideFooter()

 

**Description:
 :** 

- 

Hide the footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 688](lib_amd_src_modal.js.md)

 

#### (inner) hideIfNotForm()

 

**Description:
 :** 

- 

Hide this modal if it does not contain a form.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 906](lib_amd_src_modal.js.md)

 

#### (inner) isLarge() → {bool}

 

**Description:
 :** 

- 

Check if the modal is a large modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 731](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isSmall() → {bool}

 

**Description:
 :** 

- 

Check if the modal is a small modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 764](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isVerticallyCentered() → {bool}

 

**Description:
 :** 

- 

Check if the modal is vertically centered.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 741](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) isVisible() → {bool}

 

**Description:
 :** 

- 

Check if this modal is visible.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 819](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### (inner) registerCloseOnCancel()

 

**Description:
 :** 

- 

Register a listener to close the dialogue when the cancel button is pressed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1062](lib_amd_src_modal.js.md)

 

#### (inner) registerCloseOnDelete()

 

**Description:
 :** 

- 

Register a listener to close the dialogue when the delete button is pressed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1109](lib_amd_src_modal.js.md)

 

#### (inner) registerCloseOnSave()

 

**Description:
 :** 

- 

Register a listener to close the dialogue when the save button is pressed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1085](lib_amd_src_modal.js.md)

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 1005](lib_amd_src_modal.js.md)

 

#### (inner) setBody(value)

 

**Description:
 :** 

- 

Set the modal body element.

This method is overloaded to take either a string value for the body or a jQuery promise that is resolved with
HTML and Javascript most commonly from a Templates.render call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 475](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The body string or jQuery promise which resolves to the body.

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

 

#### (inner) setFooter(value)

 

**Description:
 :** 

- 

Set the modal footer element. The footer element is made visible, if it
isn't already.

This method is overloaded to take either a string
value for the body or a jQuery promise that is resolved with HTML and Javascript
most commonly from a Templates.render call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 623](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The footer string or jQuery promise

 

 

#### (inner) setLarge()

 

**Description:
 :** 

- 

Mark the modal as a large modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 706](lib_amd_src_modal.js.md)

 

#### (inner) setScrollable(value)

 

**Description:
 :** 

- 

Set this modal to be scrollable or not.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 774](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

bool

 

Whether the modal is scrollable or not

 

 

#### (inner) setSmall()

 

**Description:
 :** 

- 

Mark the modal as a small modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 751](lib_amd_src_modal.js.md)

 

#### (inner) setTitle(value)

 

**Description:
 :** 

- 

Set the modal title element.

This method is overloaded to take either a string value for the title or a jQuery promise that is resolved with
HTML most commonly from a Str.get_string call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 454](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The title string or jQuery promise which resolves to the title.

 

 

#### (inner) setVerticallyCentered()

 

**Description:
 :** 

- 

Mark the modal as a centered modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 719](lib_amd_src_modal.js.md)

 

#### (inner) show() → {Promise}

 

**Description:
 :** 

- 

Display this modal. The modal will be attached to the DOM if it hasn't
already been.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 859](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) showFooter()

 

**Description:
 :** 

- 

Show the footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 697](lib_amd_src_modal.js.md)

 

 

### Type Definitions

 

#### ModalConfig

 

**Description:
 :** 

- 

A configuration to provide to the modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 39](lib_amd_src_modal.js.md)

##### Properties:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `type`

 

string

 

 

 <optional>  

 

 

 

The type of modal to create.

 
 `title`

 

string
|

Promise.<string>

 

 

 <optional>  

 

 

 

The title of the modal.

 
 `body`

 

string
|

Promise.<string>

 

 

 <optional>  

 

 

 

The body of the modal.

 
 `footer`

 

string
|

Promise.<string>

 

 

 <optional>  

 

 

 

The footer of the modal.

 
 `show`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

Whether to show the modal immediately.

 
 `scrollable`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether the modal should be scrollable.

 
 `removeOnClose`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether the modal should be removed from the DOM when it is closed.

 
 `returnElement`

 

Element
|

jQuery

 

 

 <optional>  

 

 

 

The element to focus when closing the modal.

 
 `large`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

Whether the modal should be a large modal.

 
 `isVerticallyCentered`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

Whether the modal should be vertically centered.

 
 `buttons`

 

object

 

 

 <optional>  

 

 

 `{}`

 

The buttons to display in the footer as a key => title pair.

 

A configuration to provide to the modal.

##### Type:

- 

Object
