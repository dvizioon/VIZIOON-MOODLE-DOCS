# tiny_link/link - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tiny_link_link.html

# tiny_link/link

 

 

 

**Description:
 :** 

- 

Link helper for Tiny Link plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 16](lib_editor_tiny_plugins_link_amd_src_link.js.md)

 

**Copyright:
 :** 

- 2023 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Link helper for Tiny Link plugin.

 

 

 

 

### Members

 

#### (static, constant) getCurrentLinkData

 

**Description:
 :** 

- 

Get current link data.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 120](lib_editor_tiny_plugins_link_amd_src_link.js.md)

Get current link data.

 

#### (static, constant) setLink

 

**Description:
 :** 

- 

Handle insertion of a new link, or update of an existing one.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 34](lib_editor_tiny_plugins_link_amd_src_link.js.md)

Handle insertion of a new link, or update of an existing one.

 

#### (static, constant) toggleActiveState

 

**Description:
 :** 

- 

Change the active state of button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 233](lib_editor_tiny_plugins_link_amd_src_link.js.md)

Change the active state of button.

 

#### (static, constant) unSetLink

 

**Description:
 :** 

- 

Handle unlink of a link

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 57](lib_editor_tiny_plugins_link_amd_src_link.js.md)

Handle unlink of a link

 

 

### Methods

 

#### (inner) getAnchorElement(editor, selectedElm) → {Element}

 

**Description:
 :** 

- 

Get anchor element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 177](lib_editor_tiny_plugins_link_amd_src_link.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `selectedElm`

 

Element

 

 

 

##### Returns:

**
 Type

 :** 

Element

 

#### (inner) getSelectedLink(editor) → {Element}

 

**Description:
 :** 

- 

Get selected link.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 166](lib_editor_tiny_plugins_link_amd_src_link.js.md)

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

Element

 

#### (inner) getTextSelection(editor) → {string}

 

**Description:
 :** 

- 

Get only the selected text.
In some cases, window.getSelection() is not run as expected. We should only get the text value
For ex: Some text here
window.getSelection() will return XYZSome text here

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 191](lib_editor_tiny_plugins_link_amd_src_link.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 

##### Returns:

Selected text

**
 Type

 :** 

string

 

#### (inner) isInAnchor(editor, selectedElm) → {boolean}

 

**Description:
 :** 

- 

Check the current selected element is an anchor or not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 213](lib_editor_tiny_plugins_link_amd_src_link.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `selectedElm`

 

Element

 

 

 

##### Returns:

**
 Type

 :** 

boolean

 

#### (async, inner) setLinkOnSelection(currentForm, editor, url)

 

**Description:
 :** 

- 

Final step setting the anchor on the selection.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 86](lib_editor_tiny_plugins_link_amd_src_link.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentForm`

 

Element

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `url`

 

String

 

URL the link will point to.

 

 

#### (inner) toggleState(editor, toggler) → {function}

 

**Description:
 :** 

- 

Change state of button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/link/amd/src/link.js](lib_editor_tiny_plugins_link_amd_src_link.js.md), [line 222](lib_editor_tiny_plugins_link_amd_src_link.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `toggler`

 

function

 

 

 

##### Returns:

**
 Type

 :** 

function
