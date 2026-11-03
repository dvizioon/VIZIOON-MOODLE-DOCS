# module:tiny_aiplacement/generatebase - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_generatebase.html

# module:tiny_aiplacement/generatebase

 

## 

 module:tiny_aiplacement/generatebase

 

 

 

 

#### new (require("tiny_aiplacement/generatebase"))(editor)

 

**Description:
 :** 

- 

Class constructor.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 43](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE.editor

 

The tinyMCE editor instance.

 

 

 

 

### Methods

 

#### (async) addContentEventListeners(modal)

 

**Description:
 :** 

- 

Add event listeners for the text modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 94](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Modal

 

 

 

 

#### (async) displayContentModal()

 

**Description:
 :** 

- 

Display the modal when the AI button is clicked.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 54](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

 

#### (async) displayLoading(root, submitBtn, removeClass)

 

**Description:
 :** 

- 

Display the loading state in the modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 128](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `root`

 

HTMLElement

 

 

 

The root element of the modal.

 
 `submitBtn`

 

HTMLElement

 

 

 

The submit button element.

 
 `removeClass`

 

String
|

null

 

 

 `null`

 

The class to be removed from the loading spinner div, if any.

 

 

#### (async) hideLoading(root, submitBtn)

 

**Description:
 :** 

- 

Hide the loading action in the modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 159](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element of the modal.

 
 `submitBtn`

 

Object

 

The submit button element.

 

 

#### hideLoadingSpinner(root)

 

**Description:
 :** 

- 

Hide the loading spinner.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 115](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element of the modal.

 

 

#### (async) setupModal() → {TextModal}

 

**Description:
 :** 

- 

Set up the base text generation modal with default body content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatebase.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md), [line 77](lib_editor_tiny_plugins_aiplacement_amd_src_generatebase.js.md)

##### Returns:

The image modal object.

**
 Type

 :** 

TextModal
