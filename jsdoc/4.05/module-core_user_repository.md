# core_user/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_user_repository.html

# core_user/repository

 

 

 

**Description:
 :** 

- 

Module to handle AJAX interactions.

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 16](user_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2020 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module to handle AJAX interactions.

 

 

 

 

### Members

 

#### (static, constant) getUserPreference

 

**Description:
 :** 

- 

Get single user preference

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 80](user_amd_src_repository.js.md)

Get single user preference

 

#### (static, constant) getUserPreferences

 

**Description:
 :** 

- 

Get multiple user preferences

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 90](user_amd_src_repository.js.md)

Get multiple user preferences

 

#### (static, constant) setUserPreference

 

**Description:
 :** 

- 

Set single user preference

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 109](user_amd_src_repository.js.md)

Set single user preference

 

#### (static, constant) setUserPreferences

 

**Description:
 :** 

- 

Set multiple user preferences

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 129](user_amd_src_repository.js.md)

Set multiple user preferences

 

#### (static, constant) submitUserEnrolmentForm

 

**Description:
 :** 

- 

Submit the user enrolment form with the specified form data.

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 166](user_amd_src_repository.js.md)

Submit the user enrolment form with the specified form data.

 

#### (static, constant) unenrolUser

 

**Description:
 :** 

- 

Unenrol the user with the specified user enrolmentid ID.

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 151](user_amd_src_repository.js.md)

Unenrol the user with the specified user enrolmentid ID.

 

 

### Methods

 

#### (inner) addLegacySavedProperty(response, preferences) → {Promise.<Proxy>}

 

**Description:
 :** 

- 

Turn the response object into a Proxy object that will log a warning if the saved property is accessed.

 

**Source:
 :** 

- 
 [user/amd/src/repository.js](user_amd_src_repository.js.md), [line 47](user_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `response`

 

Object

 

 

 
 `preferences`

 

Object

 

The preferences that might be in the response

 

##### Returns:

**
 Type

 :** 

Promise.<Proxy>
