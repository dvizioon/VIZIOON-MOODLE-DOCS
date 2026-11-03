# mod_quiz/add_random_question - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_quiz_add_random_question.html

# mod_quiz/add_random_question

 

 

 

**Description:
 :** 

- 

Initialise the add random question modal on the quiz page.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_random_question.js](mod_quiz_amd_src_add_random_question.js.md), [line 16](mod_quiz_amd_src_add_random_question.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Initialise the add random question modal on the quiz page.

 

 

 

 

### Methods

 

#### (inner) init(contextId, category, returnUrl, cmid, showNewCategory)

 

**Description:
 :** 

- 

Create the add random question modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/add_random_question.js](mod_quiz_amd_src_add_random_question.js.md), [line 43](mod_quiz_amd_src_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `contextId`

 

int

 

Current context id.

 
 `category`

 

string

 

Category id and category context id comma separated.

 
 `returnUrl`

 

string

 

URL to return to after form submission.

 
 `cmid`

 

int

 

Current course module id.

 
 `showNewCategory`

 

boolean

 

Display the New category tab when selecting random questions.
