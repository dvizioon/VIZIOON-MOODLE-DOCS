# core/sessionstorage - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_sessionstorage.html

# core/sessionstorage

 

 

 

**Description:
 :** 

- 

Simple API for set/get to sessionstorage, with cacherev expiration.

Session storage will only persist for as long as the browser window
stays open.

See:
https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage

 

**Source:
 :** 

- 
 [lib/amd/src/sessionstorage.js](lib_amd_src_sessionstorage.js.md), [line 16](lib_amd_src_sessionstorage.js.md)

 

**Copyright:
 :** 

- 2017 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Simple API for set/get to sessionstorage, with cacherev expiration.

Session storage will only persist for as long as the browser window
stays open.

See:
https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage

 

 

 

 

### Members

 

#### (inner) StorageWrapper :Object

 

**Description:
 :** 

- 

Wraps browsers sessionStorage object

 

**Source:
 :** 

- 
 [lib/amd/src/sessionstorage.js](lib_amd_src_sessionstorage.js.md), [line 32](lib_amd_src_sessionstorage.js.md)

Wraps browsers sessionStorage object

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) get(key) → {boolean|string}

 

**Description:
 :** 

- 

Get a value from session storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/sessionstorage.js](lib_amd_src_sessionstorage.js.md), [line 36](lib_amd_src_sessionstorage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

The cache key to check.

 

##### Returns:

False if the value is not in the cache, or some other error - a string otherwise.

**
 Type

 :** 

boolean
|

string

 

#### (inner) set(key, value) → {boolean}

 

**Description:
 :** 

- 

Set a value to session storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/sessionstorage.js](lib_amd_src_sessionstorage.js.md), [line 47](lib_amd_src_sessionstorage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

The cache key to set.

 
 `value`

 

string

 

The value to set.

 

##### Returns:

False if the value can't be saved in the cache, or some other error - true otherwise.

**
 Type

 :** 

boolean
