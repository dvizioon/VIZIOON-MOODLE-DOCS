# core_form/submit - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_form_submit.html

# core_form/submit

 

 

 

**Description:
 :** 

- 

Submit button JavaScript. All submit buttons will be automatically disabled once the form is
submitted, unless that submission results in an error/cancelling the submit.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 16](lib_form_amd_src_submit.js.md)

 

**Since:
 :** 

- 3.8

 

**Copyright:
 :** 

- 2019 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Submit button JavaScript. All submit buttons will be automatically disabled once the form is
submitted, unless that submission results in an error/cancelling the submit.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialises submit buttons.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 113](lib_form_amd_src_submit.js.md)

Initialises submit buttons.

 

#### (inner) cookieListener

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 29](lib_form_amd_src_submit.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `ID`

 

number

 

for setInterval used when polling for download cookie

 

 

#### (inner, constant) cookieListeningButtons

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 32](lib_form_amd_src_submit.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `Array`

 

Array

 

of buttons that need re-enabling if we get a download cookie

 

 

#### (inner) currentUploadCount

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 35](lib_form_amd_src_submit.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `Number`

 

number

 

of files uploading.

 

 

#### (inner) uploadListenersRegistered

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 41](lib_form_amd_src_submit.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `Is`

 

Boolean

 

upload listeners registered?

 

 

#### (inner, constant) uploadListeningButtons

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 38](lib_form_amd_src_submit.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `Array`

 

Array

 

of buttons that need re-enabling if we get a upload process.

 

 

 

### Methods

 

#### (inner) checkUploadCount()

 

**Description:
 :** 

- 

Enable submit buttons when all files are uploaded.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 94](lib_form_amd_src_submit.js.md)

 

#### (inner) clearDownloadCookie()

 

**Description:
 :** 

- 

Clears the download cookie if there is one.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 87](lib_form_amd_src_submit.js.md)

 

#### (inner) getCookieName() → {string}

 

**Description:
 :** 

- 

Gets a unique name for the download cookie.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 80](lib_form_amd_src_submit.js.md)

##### Returns:

Cookie name

**
 Type

 :** 

string

 

#### (inner) listenForDownloadCookie(button)

 

**Description:
 :** 

- 

Listens in case a download cookie is provided.

This function is used to detect file downloads. If there is a file download then we get a
beforeunload event, but the page is never unloaded and when the file download completes we
should re-enable the buttons. We detect this by watching for a specific cookie.

PHP function \core_form\util::form_download_complete() can be used to send this cookie.

 

**Source:
 :** 

- 
 [lib/form/amd/src/submit.js](lib_form_amd_src_submit.js.md), [line 54](lib_form_amd_src_submit.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `button`

 

HTMLElement

 

Button to re-enable
