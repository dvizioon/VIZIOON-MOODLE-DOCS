# tiny_noautolink/noautolink - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tiny_noautolink_noautolink.html

# tiny_noautolink/noautolink

 

 

 

**Description:
 :** 

- 

Helper for Tiny noautolink plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 16](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

 

**Copyright:
 :** 

- 2023 Meirza 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Helper for Tiny noautolink plugin.

 

 

 

 

### Members

 

#### (static, constant) handleAction

 

**Description:
 :** 

- 

Handle action.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 36](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

Handle action.

 

#### (static, constant) toggleActiveState

 

**Description:
 :** 

- 

Change the active state of button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 210](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

Change the active state of button.

 

 

### Methods

 

#### (inner) getAnchorElement(editor, selectedElm) → {Element}

 

**Description:
 :** 

- 

Get anchor element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 177](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

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

 

#### (inner) getSelectedContent(editor) → {String}

 

**Description:
 :** 

- 

Return the full string based on the position of the cursor within the string.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 101](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

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

String

 

#### (inner) isInAnchor(editor, selectedElm) → {boolean}

 

**Description:
 :** 

- 

Check the current selected element is an anchor or not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 190](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

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

 

#### (inner) setNoAutoLink(editor, messages, urlString)

 

**Description:
 :** 

- 

Display notification feedback when applying the noautolink to the selected text.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 55](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `messages`

 

object

 

 

 
 `urlString`

 

String

 

 

 

 

#### (async, inner) setNoautolinkOnSelection(editor, url)

 

**Description:
 :** 

- 

Wrap the selection with the nolink class.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 142](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
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
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 199](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

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

 

#### (inner) unsetNoAutoLink(editor, messages)

 

**Description:
 :** 

- 

Display notification feedback when removing the noautolink to the selected text.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 74](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `messages`

 

object

 

 

 

 

#### (async, inner) unsetNoautolinkOnSelection(editor, url)

 

**Description:
 :** 

- 

Remove the nolink on the selection.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/noautolink/amd/src/noautolink.js](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md), [line 163](lib_editor_tiny_plugins_noautolink_amd_src_noautolink.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

 

 
 `url`

 

String

 

URL the link will point to.
