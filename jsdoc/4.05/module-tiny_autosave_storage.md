# tiny_autosave/storage - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_autosave_storage.html

# tiny_autosave/storage

 

 

 

**Description:
 :** 

- 

Storage helper for the Moodle Tiny Autosave plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/autosave/amd/src/storage.js](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md), [line 16](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md)

 

**Copyright:
 :** 

- 2022 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Storage helper for the Moodle Tiny Autosave plugin.

 

 

 

 

### Members

 

#### (static, constant) removeAutosaveSession

 

**Description:
 :** 

- 

Delete the draft for the current editor.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/autosave/amd/src/storage.js](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md), [line 81](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md)

Delete the draft for the current editor.

 

#### (static, constant) restoreDraft

 

**Description:
 :** 

- 

Attempt to restore a draft into the editor

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/autosave/amd/src/storage.js](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md), [line 41](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md)

Attempt to restore a draft into the editor

 

#### (static, constant) saveDraft

 

**Description:
 :** 

- 

Save the current content of the editor as a draft.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/autosave/amd/src/storage.js](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md), [line 64](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md)

Save the current content of the editor as a draft.

 

#### (inner, constant) saveDebounceMap

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/autosave/amd/src/storage.js](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md), [line 34](lib_editor_tiny_plugins_autosave_amd_src_storage.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `A`

 

Map

 

map of debounced draft saves
