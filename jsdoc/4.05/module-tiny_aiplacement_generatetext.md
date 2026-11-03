# tiny_aiplacement/generatetext - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_generatetext.html

# tiny_aiplacement/generatetext

 

 

 

**Description:
 :** 

- 

Tiny AI generate text.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 16](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

 

**Copyright:
 :** 

- 2024 Matt Porritt 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny AI generate text.

 

 

 

 

### Methods

 

#### (async) displayGeneratedText(root)

 

**Description:
 :** 

- 

Display the generated text in the modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 178](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The root element of the modal.

 

 

#### getRequestArgs(root)

 

**Description:
 :** 

- 

Get the request args for the generated text.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 205](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element of the modal.

 

 

#### handleContentModalClick(e, root)

 

**Description:
 :** 

- 

Handle click events within the text modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 53](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The click event object.

 
 `root`

 

HTMLElement

 

The root element of the modal.

 

 

#### (async) handleGenerationError(root, submitBtn, errorMessage)

 

**Description:
 :** 

- 

Handle a generation error.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 158](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

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

 
 `errorMessage`

 

String

 

The error message to display.

 

 

#### (async) handleInsert(root, submitBtn)

 

**Description:
 :** 

- 

Handle the insert action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 122](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element of the modal.

 
 `submitBtn`

 

HTMLElement

 

The submit button element.

 

 

#### (async) handleSubmit(root, submitBtn)

 

**Description:
 :** 

- 

Handle the submit action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 91](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

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

 

 

#### setupPromptArea(root)

 

**Description:
 :** 

- 

Set up the prompt area in the modal, adding necessary event listeners.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generatetext.js](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md), [line 76](lib_editor_tiny_plugins_aiplacement_amd_src_generatetext.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The root element of the modal.
