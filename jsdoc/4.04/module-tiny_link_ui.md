# tiny_link/ui - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tiny_link_ui.html

# tiny_link/ui

 

 

 

**Description:
 :** 

- 

Tiny Link UI.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 16](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

 

**Copyright:
 :** 

- 2023 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny Link UI.

 

 

 

 

### Members

 

#### (static, constant) handleAction

 

**Description:
 :** 

- 

Handle action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 37](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

Handle action.

 

 

### Methods

 

#### (async, inner) displayDialogue(editor) → {Promise.<void>}

 

**Description:
 :** 

- 

Display the link dialogue.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 51](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (inner) filePickerCallback(params, currentForm, editor)

 

**Description:
 :** 

- 

Update the dialogue after a link was selected in the File Picker.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 117](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

Object

 

 

 
 `currentForm`

 

Element

 

 

 
 `editor`

 

TinyMCE

 

 

 

 

#### (inner) getTemplateContext(editor) → {Object}

 

**Description:
 :** 

- 

Get template context.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 99](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) updateTextToDisplay(currentForm)

 

**Description:
 :** 

- 

Update the text to display if the user does not provide the custom text.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/ui.js](lib_editor_tiny_plugins_link_amd_src_ui.js.md), [line 130](lib_editor_tiny_plugins_link_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentForm`

 

Element
