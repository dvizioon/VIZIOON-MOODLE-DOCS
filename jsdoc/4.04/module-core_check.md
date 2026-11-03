# core/check - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_check.html

# core/check

 

 

 

**Description:
 :** 

- 

Check API webservice repository

 

**Source:
 :** 

- 
 [lib/amd/src/check/repository.js](lib_amd_src_check_repository.js.md), [line 16](lib_amd_src_check_repository.js.md)

 

**Author:
 :** 

- [Matthew Hilton](mailto:matthewhilton@catalyst-au.net)

 

 

**Copyright:
 :** 

- Catalyst IT, 2023

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Check API webservice repository

 

 

 

 

### Members

 

#### (static, constant) getCheckResult

 

**Description:
 :** 

- 

Call check_get_result webservice function

 

**Source:
 :** 

- 
 [lib/amd/src/check/repository.js](lib_amd_src_check_repository.js.md), [line 34](lib_amd_src_check_repository.js.md)

Call check_get_result webservice function

 

 

### Methods

 

#### (inner) getAndRender(domSelector, adminTreeId, settingName, includeDetails)

 

**Description:
 :** 

- 

Get the result of a check and replace a given DOM element with the result.

 

**Source:
 :** 

- 
 [lib/amd/src/check/check_result.js](lib_amd_src_check_check_result.js.md), [line 29](lib_amd_src_check_check_result.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `domSelector`

 

String

 

A CSS selector for a dom element to replace the the HTML for.

 
 `adminTreeId`

 

String

 

Id of the admin_setting that called this webservice. Used to retrieve the check registered to it.

 
 `settingName`

 

String

 

Name of setting (used to find the parent node in the admin tree)

 
 `includeDetails`

 

Boolean

 

If true, details will be included in the check.
By default only the status and the summary is returned.

 

 

 

 

 

**Description:
 :** 

- 

Check API result functions

 

**Source:
 :** 

- 
 [lib/amd/src/check/check_result.js](lib_amd_src_check_check_result.js.md), [line 16](lib_amd_src_check_check_result.js.md)

 

**Author:
 :** 

- [Matthew Hilton](mailto:matthewhilton@catalyst-au.net)

 

 

**Copyright:
 :** 

- Catalyst IT, 2023

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Check API result functions

 

 

 

 

### Members

 

#### (static, constant) getCheckResult

 

**Description:
 :** 

- 

Call check_get_result webservice function

 

**Source:
 :** 

- 
 [lib/amd/src/check/repository.js](lib_amd_src_check_repository.js.md), [line 34](lib_amd_src_check_repository.js.md)

Call check_get_result webservice function

 

 

### Methods

 

#### (inner) getAndRender(domSelector, adminTreeId, settingName, includeDetails)

 

**Description:
 :** 

- 

Get the result of a check and replace a given DOM element with the result.

 

**Source:
 :** 

- 
 [lib/amd/src/check/check_result.js](lib_amd_src_check_check_result.js.md), [line 29](lib_amd_src_check_check_result.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `domSelector`

 

String

 

A CSS selector for a dom element to replace the the HTML for.

 
 `adminTreeId`

 

String

 

Id of the admin_setting that called this webservice. Used to retrieve the check registered to it.

 
 `settingName`

 

String

 

Name of setting (used to find the parent node in the admin tree)

 
 `includeDetails`

 

Boolean

 

If true, details will be included in the check.
By default only the status and the summary is returned.
