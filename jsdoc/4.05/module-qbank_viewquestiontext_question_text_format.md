# qbank_viewquestiontext/question_text_format - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-qbank_viewquestiontext_question_text_format.html

# qbank_viewquestiontext/question_text_format

 

 

 

**Description:
 :** 

- 

Javascript for question_text_format question bank control.

 

**Source:
 :** 

- 
 [question/bank/viewquestiontext/amd/src/question_text_format.js](question_bank_viewquestiontext_amd_src_question_text_format.js.md), [line 16](question_bank_viewquestiontext_amd_src_question_text_format.js.md)

 

**Author:
 :** 

- [Mark Johnson](mailto:mark.johnson@catalyst-eu.net)

 

 

**Copyright:
 :** 

- 2023 Catalyst IT Europe Ltd.

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript for question_text_format question bank control.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialise question text format widget.

Find the uiRoot element and attach a change listener to the question text format selector.

 

**Source:
 :** 

- 
 [question/bank/viewquestiontext/amd/src/question_text_format.js](question_bank_viewquestiontext_amd_src_question_text_format.js.md), [line 61](question_bank_viewquestiontext_amd_src_question_text_format.js.md)

Initialise question text format widget.

Find the uiRoot element and attach a change listener to the question text format selector.

 

 

### Methods

 

#### (async, inner) handleFormatChange(e) → {Promise.<void>}

 

**Description:
 :** 

- 

Save the selected format via a web service call, and refresh the UI.

 

**Source:
 :** 

- 
 [question/bank/viewquestiontext/amd/src/question_text_format.js](question_bank_viewquestiontext_amd_src_question_text_format.js.md), [line 42](question_bank_viewquestiontext_amd_src_question_text_format.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

Select field change event.

 

##### Returns:

**
 Type

 :** 

Promise.<void>
