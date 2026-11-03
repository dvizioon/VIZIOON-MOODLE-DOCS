# qbank_preview/preview - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-qbank_preview_preview.html

# qbank_preview/preview

 

 

 

**Description:
 :** 

- 

Javascript for preview.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 16](question_bank_previewquestion_amd_src_preview.js.md)

 

**Author:
 :** 

- [Safat Shahin](mailto:safatshahin@catalyst-au.net)

 

 

**Copyright:
 :** 

- 2021 Catalyst IT Australia Pty Ltd

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript for preview.

 

 

 

 

### Methods

 

#### (inner) autocompleteOff(form)

 

**Description:
 :** 

- 

Set the autocomplete off.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 69](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

object

 

The form element.

 

 

#### (inner) init(redirect, url)

 

**Description:
 :** 

- 

Set up the actions.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 27](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `redirect`

 

bool

 

Redirect.

 
 `url`

 

string

 

url to redirect.

 

 

#### (inner) preventRepeatSubmission(form)

 

**Description:
 :** 

- 

Event handler to stop a question form being submitted more than once.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 79](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

object

 

The form element.

 

 

#### (inner) removeClass(classname, form)

 

**Description:
 :** 

- 

Removes a class inside an element.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 94](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `classname`

 

string

 

Class name.

 
 `form`

 

object

 

The form element.

 

 

#### (inner) scrollToSavedPos(form)

 

**Description:
 :** 

- 

If there is a parameter like scrollpos=123 in the URL, scroll to that saved position.
(Note: Moodle 4.0 and above do NOT support Internet Explorer 11 and below.)

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 105](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

object

 

The form element.

 

 

#### (inner) setupQuestionForm(formElement)

 

**Description:
 :** 

- 

Set up the form element to be displayed.

 

**Source:
 :** 

- 
 [question/bank/previewquestion/amd/src/preview.js](question_bank_previewquestion_amd_src_preview.js.md), [line 49](question_bank_previewquestion_amd_src_preview.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formElement`

 

string

 

The form element.
