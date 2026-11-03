# core/url - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_url.html

# core/url

 

 

 

**Description:
 :** 

- 

URL utility functions.

 

**Source:
 :** 

- 
 [lib/amd/src/url.js](lib_amd_src_url.js.md), [line 16](lib_amd_src_url.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

URL utility functions.

 

 

 

 

### Methods

 

#### (inner) fileUrl(relativeScript, slashArg) → {string}

 

**Description:
 :** 

- 

Construct a file url

 

**Source:
 :** 

- 
 [lib/amd/src/url.js](lib_amd_src_url.js.md), [line 29](lib_amd_src_url.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `relativeScript`

 

string

 

 

 
 `slashArg`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

string

 

#### (inner) imageUrl(imagename, component) → {string}

 

**Description:
 :** 

- 

Wrapper for image_url function.

 

**Source:
 :** 

- 
 [lib/amd/src/url.js](lib_amd_src_url.js.md), [line 97](lib_amd_src_url.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `imagename`

 

string

 

The image name (e.g. t/edit).

 
 `component`

 

string

 

The component (e.g. mod_feedback).

 

##### Returns:

**
 Type

 :** 

string

 

#### (inner) relativeUrl(relativePath, params, includeSessKey) → {string}

 

**Description:
 :** 

- 

Take a path relative to the moodle basedir and do some fixing (see class moodle_url in php).

 

**Source:
 :** 

- 
 [lib/amd/src/url.js](lib_amd_src_url.js.md), [line 53](lib_amd_src_url.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `relativePath`

 

string

 

The path relative to the moodle basedir.

 
 `params`

 

object

 

The query parameters for the URL.

 
 `includeSessKey`

 

bool

 

Add the session key to the query params.

 

##### Returns:

**
 Type

 :** 

string
