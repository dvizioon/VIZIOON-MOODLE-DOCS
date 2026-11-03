# core/storagewrapper - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_storagewrapper.html

# core/storagewrapper

 

 

 

**Description:
 :** 

- 

Wrap an instance of the browser's local or session storage to handle
cache expiry, key namespacing and other helpful things.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 16](lib_amd_src_storagewrapper.js.md)

 

**Copyright:
 :** 

- 2017 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Wrap an instance of the browser's local or session storage to handle
cache expiry, key namespacing and other helpful things.

 

 

 

 

### Methods

 

#### (inner) clean()

 

**Description:
 :** 

- 

Clean local storage.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 165](lib_amd_src_storagewrapper.js.md)

 

#### (inner) detectSupport() → {boolean}

 

**Description:
 :** 

- 

Check if the browser supports the type of storage.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 41](lib_amd_src_storagewrapper.js.md)

##### Returns:

True if the browser supports storage.

**
 Type

 :** 

boolean

 

#### (inner) get(key) → {boolean|string}

 

**Description:
 :** 

- 

Get a value from local storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 127](lib_amd_src_storagewrapper.js.md)

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

 

#### (inner) hashString(source) → {Number}

 

**Description:
 :** 

- 

Hash a string, used to make shorter key prefixes.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 103](lib_amd_src_storagewrapper.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

String

 

The string to hash

 

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) prefixKey(key) → {string}

 

**Description:
 :** 

- 

Add a unique prefix to all keys so multiple moodle sites do not share caches.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 70](lib_amd_src_storagewrapper.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

The cache key to prefix.

 

##### Returns:

The new key

**
 Type

 :** 

string

 

#### (inner) set(key, value) → {boolean}

 

**Description:
 :** 

- 

Set a value to local storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 143](lib_amd_src_storagewrapper.js.md)

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

 

#### (inner) validateCache()

 

**Description:
 :** 

- 

Check the current jsrev version and clear the cache if it has been bumped.

 

**Source:
 :** 

- 
 [lib/amd/src/storagewrapper.js](lib_amd_src_storagewrapper.js.md), [line 81](lib_amd_src_storagewrapper.js.md)
