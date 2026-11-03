# core_ai/helper - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_ai_helper.html

# core_ai/helper

 

 

 

**Description:
 :** 

- 

The helper module or AI Subsystem.

 

**Source:
 :** 

- 
 [ai/amd/src/helper.js](ai_amd_src_helper.js.md), [line 16](ai_amd_src_helper.js.md)

 

**Copyright:
 :** 

- 2024 Huong Nguyen 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

The helper module or AI Subsystem.

 

 

 

 

### Methods

 

#### (static) replaceLineBreaks(text) → {String}

 

**Description:
 :** 

- 

Replace double line breaks with   
 and with 

 for paragraphs.
This is to handle the difference in response from the AI to what is expected by the editor.

 

**Source:
 :** 

- 
 [ai/amd/src/helper.js](ai_amd_src_helper.js.md), [line 31](ai_amd_src_helper.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The text to replace.

 

##### Returns:

**
 Type

 :** 

String
