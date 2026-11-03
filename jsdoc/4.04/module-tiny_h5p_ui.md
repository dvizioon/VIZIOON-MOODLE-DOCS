# tiny_h5p/ui - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tiny_h5p_ui.html

# tiny_h5p/ui

 

 

 

**Description:
 :** 

- 

Tiny H5P Content configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/h5p/amd/src/ui.js](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md), [line 16](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md)

 

**Copyright:
 :** 

- 2022 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny H5P Content configuration.

 

 

 

 

### Methods

 

#### (inner) getTemplateContext(editor, data) → {object}

 

**Description:
 :** 

- 

Get the template context for the dialogue.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/h5p/amd/src/ui.js](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md), [line 50](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

Editor

 

 

 
 `data`

 

object

 

 

 

##### Returns:

data

**
 Type

 :** 

object

 

#### (inner) getUrlFromSubmission(form, submittedUrl) → {URL|null}

 

**Description:
 :** 

- 

Get the URL from the submitted form.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/h5p/amd/src/ui.js](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md), [line 75](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

FormNode

 

 

 
 `submittedUrl`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

URL
|

null

 

#### (inner) isValidUrl(url) → {boolean}

 

**Description:
 :** 

- 

Verify if this could be a h5p URL.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/h5p/amd/src/ui.js](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md), [line 107](lib_editor_tiny_plugins_h5p_amd_src_ui.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `url`

 

string

 

Url to verify

 

##### Returns:

whether this is a valid URL.

**
 Type

 :** 

boolean
