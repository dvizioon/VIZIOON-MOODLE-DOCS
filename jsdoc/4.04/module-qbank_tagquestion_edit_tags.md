# qbank_tagquestion/edit_tags - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-qbank_tagquestion_edit_tags.html

# qbank_tagquestion/edit_tags

 

 

 

**Description:
 :** 

- 

A javascript module to handle question tags editing.

 

**Source:
 :** 

- 
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 16](question_bank_tagquestion_amd_src_edit_tags.js.md)

 

**Copyright:
 :** 

- 2018 Simey Lameze 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 56](question_bank_tagquestion_amd_src_edit_tags.js.md)

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 46](question_bank_tagquestion_amd_src_edit_tags.js.md)

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 66](question_bank_tagquestion_amd_src_edit_tags.js.md)

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 242](question_bank_tagquestion_amd_src_edit_tags.js.md)

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 77](question_bank_tagquestion_amd_src_edit_tags.js.md)

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
 [question/bank/tagquestion/amd/src/edit_tags.js](question_bank_tagquestion_amd_src_edit_tags.js.md), [line 89](question_bank_tagquestion_amd_src_edit_tags.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The container element
