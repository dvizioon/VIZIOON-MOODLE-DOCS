# quizaccess_seb/validate_quiz_access - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-quizaccess_seb_validate_quiz_access.html

# quizaccess_seb/validate_quiz_access

 

 

 

**Description:
 :** 

- 

Validate Safe Exam Browser access keys.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 16](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

 

**Author:
 :** 

- [Andrew Madden](mailto:andrewmadden@catalyst-au.net)

 

 

**Copyright:
 :** 

- 2021 Catalyst IT

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Validate Safe Exam Browser access keys.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize the process of fetching the keys.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 109](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

Initialize the process of fetching the keys.

 

 

### Methods

 

#### (inner) isKeyEmpty(key) → {boolean}

 

**Description:
 :** 

- 

Check if the key is not yet set.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 87](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

config key or browser exam key.

 

##### Returns:

**
 Type

 :** 

boolean

 

#### (inner) isQuizAccessValid(cmid) → {Promise}

 

**Description:
 :** 

- 

Validate keys in Moodle backend.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 67](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

[init](global.md)

 

Value of course module id of the quiz.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) reconfigureSafeExamBrowser(cmid)

 

**Description:
 :** 

- 

Reload Safe Exam Browser with current quiz configuration.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 97](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

[init](global.md)

 

Value of course module id of the quiz.

 

 

#### (inner) safeExamBrowserKeysUpdated(cmid, autoreconfigure)

 

**Description:
 :** 

- 

Once the keys are fetched, action checking access.

 

**Source:
 :** 

- 
 [mod/quiz/accessrule/seb/amd/src/validate_quiz_access.js](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md), [line 39](mod_quiz_accessrule_seb_amd_src_validate_quiz_access.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `cmid`

 

[init](global.md)

 

 

 

Value of course module id of the quiz.

 
 `autoreconfigure`

 

boolean

 

 

 `false`

 

Value of Moodle setting: quizaccess_seb/autoreconfigureseb.
