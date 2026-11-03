# core_form/filetypes - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_form_filetypes.html

# core_form/filetypes

 

 

 

**Description:
 :** 

- 

This module allows to enhance the form elements MoodleQuickForm_filetypes

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 16](lib_form_amd_src_filetypes.js.md)

 

**Since:
 :** 

- 3.3

 

**Copyright:
 :** 

- 2017 David Mudrak 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module allows to enhance the form elements MoodleQuickForm_filetypes

 

 

 

 

### Methods

 

#### (inner) prepareBrowserModal() → {Promise}

 

**Description:
 :** 

- 

Create and set the modal for displaying the browser (this.browserModal).

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 85](lib_form_amd_src_filetypes.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) prepareBrowserTree() → {Promise}

 

**Description:
 :** 

- 

Create and set the tree in the browser modal's body.

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 114](lib_form_amd_src_filetypes.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) prepareBrowserTrigger() → {Promise}

 

**Description:
 :** 

- 

Create and set the browser trigger widget (this.browserTrigger).

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 71](lib_form_amd_src_filetypes.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) saveBrowserModal()

 

**Description:
 :** 

- 

Update the associated input field with selected file types.

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 220](lib_form_amd_src_filetypes.js.md)

 

#### (inner) toggleCheckbox(key)

 

**Description:
 :** 

- 

Change the checked status of the given file type (group or extension).

 

**Source:
 :** 

- 
 [lib/form/amd/src/filetypes.js](lib_form_amd_src_filetypes.js.md), [line 207](lib_form_amd_src_filetypes.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

String
