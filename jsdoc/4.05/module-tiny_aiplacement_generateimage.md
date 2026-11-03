# tiny_aiplacement/generateimage - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_generateimage.html

# tiny_aiplacement/generateimage

 

 

 

**Description:
 :** 

- 

Tiny AI generate images.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 16](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

 

**Copyright:
 :** 

- 2024 Matt Porritt 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny AI generate images.

 

 

 

 

### Methods

 

#### (async) displayGeneratedImage(root)

 

**Description:
 :** 

- 

Display the generated image in the modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 155](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The root element of the modal.

 

 

#### getDisplayArgs(root)

 

**Description:
 :** 

- 

Get the display args for the image.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 186](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The root element of the modal.

 

 

#### getSelectedRadioValue(radioName, defaultValue)

 

**Description:
 :** 

- 

Get the value of the selected radio button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 209](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `radioName`

 

String

 

 

 

The name of the radio button group.

 
 `defaultValue`

 

String

 

 

 `null`

 

The default value of the radio button.

 

 

#### handleContentModalClick(e, root)

 

**Description:
 :** 

- 

Handle click events within the image modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 55](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

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
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 135](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

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

 

 

#### (async) handleInsert()

 

**Description:
 :** 

- 

Handle the insert action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 122](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

 

#### (async) handleSubmit(root, submitBtn)

 

**Description:
 :** 

- 

Handle the submit action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 93](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

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
 [lib/editor/tiny/plugins/aiplacement/amd/src/generateimage.js](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md), [line 78](lib_editor_tiny_plugins_aiplacement_amd_src_generateimage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The root element of the modal.
