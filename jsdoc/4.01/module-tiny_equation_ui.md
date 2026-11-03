# tiny_equation/ui - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tiny_equation_ui.html

# tiny_equation/ui

 

 

 

**Description:
 :** 

- 

Tiny Equation UI.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 16](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

 

**Copyright:
 :** 

- 2022 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny Equation UI.

 

 

 

 

### Members

 

#### (static, constant) handleAction

 

**Description:
 :** 

- 

Handle action

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 42](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

Handle action

 

 

### Methods

 

#### (async, inner) displayDialogue(editor) → {Promise.<void>}

 

**Description:
 :** 

- 

Display the equation editor

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 51](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

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

 

#### (inner) getTemplateContext(editor, data) → {Object}

 

**Description:
 :** 

- 

Get template context.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 126](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `data`

 

Object

 

 

 

##### Returns:

**
 Type

 :** 

Object

 

#### (inner) groupNavigation(e)

 

**Description:
 :** 

- 

Callback handling the keyboard navigation in the groups of the library.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 234](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

 

#### (inner) notifyFilter(element)

 

**Description:
 :** 

- 

Notify the filters about the modified nodes

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 226](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

 

 

 

#### (inner) selectLibraryItem(libraryItem, contextId)

 

**Description:
 :** 

- 

Handle select library item.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 143](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `libraryItem`

 

Object

 

 

 
 `contextId`

 

number

 

 

 

 

#### (inner) updatePreview(contextId)

 

**Description:
 :** 

- 

Update the preview section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/equation/amd/src/ui.js](lib_editor_tiny_plugins_equation_amd_src_ui.js.md), [line 176](lib_editor_tiny_plugins_equation_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

number
