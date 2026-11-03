# core/str - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_str.html

# core/str

 

 

 

**Description:
 :** 

- 

Fetch and return language strings.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 16](lib_amd_src_str.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Fetch and return language strings.

 

 

 

 

### Members

 

#### (static, constant) getString

 

**Description:
 :** 

- 

Return a Promise that resolves to a string.

If the string has previously been cached, then the Promise will be resolved immediately, otherwise it will be fetched
from the server and resolved when available.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 88](lib_amd_src_str.js.md)

Return a Promise that resolves to a string.

If the string has previously been cached, then the Promise will be resolved immediately, otherwise it will be fetched
from the server and resolved when available.

##### Example

 

Fetching a string

 

```js
import {getString} from 'core/str';

getString('cannotfindteacher', 'error')
.then((str) => window.console.log(str)); // Cannot find teacher
```

 

#### (static, constant) getStrings

 

**Description:
 :** 

- 

Make a batch request to load a set of strings.

Any missing string will be fetched from the server.
The Promise will only be resolved once all strings are available, or an attempt has been made to fetch them.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 123](lib_amd_src_str.js.md)

Make a batch request to load a set of strings.

Any missing string will be fetched from the server.
The Promise will only be resolved once all strings are available, or an attempt has been made to fetch them.

##### Example

 

Fetching a set of strings

 

```js
import {getStrings} from 'core/str';
getStrings([
    {
        key: 'cannotfindteacher',
        component: 'error',
    },
    {
        key: 'yes',
        component: 'core',
    },
    {
        key: 'no',
        component: 'core',
    },
])
.then((cannotFindTeacher, yes, no) => {
    window.console.log(cannotFindTeacher); // Cannot find teacher
    window.console.log(yes); // Yes
    window.console.log(no); // No
});
```

 

#### (static, constant) get_string

 

**Description:
 :** 

- 

Return a Promise that resolves to a string.

If the string has previously been cached, then the Promise will be resolved immediately, otherwise it will be fetched
from the server and resolved when available.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 64](lib_amd_src_str.js.md)

Return a Promise that resolves to a string.

If the string has previously been cached, then the Promise will be resolved immediately, otherwise it will be fetched
from the server and resolved when available.

##### Example

 

Fetching a string

 

```js
import {getString} from 'core/str';
get_string('cannotfindteacher', 'error')
.then((str) => window.console.log(str)); // Cannot find teacher
```

 

#### (static, constant) get_strings

 

**Description:
 :** 

- 

Make a batch request to load a set of strings.

Any missing string will be fetched from the server.
The Promise will only be resolved once all strings are available, or an attempt has been made to fetch them.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 242](lib_amd_src_str.js.md)

Make a batch request to load a set of strings.

Any missing string will be fetched from the server.
The Promise will only be resolved once all strings are available, or an attempt has been made to fetch them.

##### Example

 

Fetching a set of strings

 

```js
import {getStrings} from 'core/str';
get_strings([
    {
        key: 'cannotfindteacher',
        component: 'error',
    },
    {
        key: 'yes',
        component: 'core',
    },
    {
        key: 'no',
        component: 'core',
    },
])
.then((cannotFindTeacher, yes, no) => {
    window.console.log(cannotFindTeacher); // Cannot find teacher
    window.console.log(yes); // Yes
    window.console.log(no); // No
});
```

 

 

### Methods

 

#### (protected, inner) cache_strings(strings)

 

**Description:
 :** 

- 

Add a list of strings to the caches.

This function should typically only be called from core APIs to pre-cache values.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 249](lib_amd_src_str.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `strings`

 

Array.<Object>

 

List of strings to fetch

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `key`

 

string

 

 

 

 

 

The string identifer to fetch

 
 `value`

 

string

 

 

 

 

 

The string value

 
 `component`

 

string

 

 

 <optional>  

 

 

 `'core'`

 

The componet to fetch from

 
 `lang`

 

string

 

 

 <optional>  

 

 

 `Config.language`

 

The language to fetch a string for. Defaults to current page language.

 

 

 

 

#### (inner) getRequestedStrings(requests) → {Array.<Promise>}

 

**Description:
 :** 

- 

Internal function to perform the string requests.

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 131](lib_amd_src_str.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `requests`

 

Array.<StringRequest>

 

List of strings to fetch

 

##### Returns:

**
 Type

 :** 

Array.<Promise>

 

 

### Type Definitions

 

#### StringRequest

 

**Source:
 :** 

- 
 [lib/amd/src/str.js](lib_amd_src_str.js.md), [line 30](lib_amd_src_str.js.md)

##### Type:

- 

object
