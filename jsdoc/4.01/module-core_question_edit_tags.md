# core_question/edit_tags - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_question_edit_tags.html

# core_question/edit_tags

 

 

 

**Description:
 :** 

- 

A javascript module to handle question tags editing.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 16](question_amd_src_edit_tags.js.md)

 

**Deprecated::** 

- since Moodle 4.0

 

**Copyright:
 :** 

- 2018 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

**To Do:
 :** 

- Final deprecation on Moodle 4.4 MDL-72438

 

 

A javascript module to handle question tags editing.

 

 

 

 

### Methods

 

#### (inner) disableSaveButton(root)

 

**Description:
 :** 

- 

Disable the save button in the footer.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 58](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element.

 

 

#### (inner) enableSaveButton(root)

 

**Description:
 :** 

- 

Enable the save button in the footer.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 48](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element.

 

 

#### (inner) getFormData(modal) → {string}

 

**Description:
 :** 

- 

Get the serialised form data.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 68](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

object

 

The modal object.

 

##### Returns:

serialised form data

**
 Type

 :** 

string

 

#### (inner) save(modal, root) → {object}

 

**Description:
 :** 

- 

Send the form data to the server to save question tags.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 242](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

object

 

The modal object.

 
 `root`

 

object

 

The container element.

 

##### Returns:

A promise

**
 Type

 :** 

object

 

#### (inner) startLoading(root)

 

**Description:
 :** 

- 

Set the element state to loading.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 79](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element

 

 

#### (inner) stopLoading(root)

 

**Description:
 :** 

- 

Remove the loading state from the element.

 

**Source:
 :** 

- 
 [question/amd/src/edit_tags.js](question_amd_src_edit_tags.js.md), [line 91](question_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element
