# core/prefetch - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_prefetch.html

# core/prefetch

 

 

 

**Description:
 :** 

- 

Prefetch module to help lazily load content for use on the current page.

 

**Source:
 :** 

- 
 [lib/amd/src/prefetch.js](lib_amd_src_prefetch.js.md), [line 16](lib_amd_src_prefetch.js.md)

 

**Copyright:
 :** 

- 2020 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Prefetch module to help lazily load content for use on the current page.

 

### Example

 

Pre-fetching a set of strings to use later

 

```js
import prefetch from 'core/prefetch';

// A single string prefetch.
prefetch.prefetchString('error', 'cannotfindteacher');

// Prefetch multiple strings in the same component.
prefetch.prefetchStrings('core', [
    'yes',
    'no',
]);

// Use the strings.
import {get_string as getString, get_strings as getStrings} from 'core/str';
getString('cannotfindteacher', 'error')
.then(str => {
    window.console.log(str); // Cannot find teacher
})
.catch();
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
})
.catch();
```

 

 

 

 

### Methods

 

#### (static) prefetchString(component, key)

 

**Description:
 :** 

- 

Add a single string to the prefetch queue.

 

**Source:
 :** 

- 
 [lib/amd/src/prefetch.js](lib_amd_src_prefetch.js.md), [line 202](lib_amd_src_prefetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

String

 

The component that the string belongs to

 
 `key`

 

String

 

The string identifier

 

 

#### (static) prefetchStrings(component, keys)

 

**Description:
 :** 

- 

Add a set of strings from the same component to the prefetch queue.

 

**Source:
 :** 

- 
 [lib/amd/src/prefetch.js](lib_amd_src_prefetch.js.md), [line 185](lib_amd_src_prefetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

String

 

The component that all of the strings belongs to

 
 `keys`

 

Array.<String>

 

An array of string identifiers.

 

 

#### (static) prefetchTemplate(templateName)

 

**Description:
 :** 

- 

Add a single template to the prefetch queue.

 

**Source:
 :** 

- 
 [lib/amd/src/prefetch.js](lib_amd_src_prefetch.js.md), [line 174](lib_amd_src_prefetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateName`

 

String

 

The template names to fetch

 

 

#### (static) prefetchTemplates(templatesNames)

 

**Description:
 :** 

- 

Add a set of templates to the prefetch queue.

 

**Source:
 :** 

- 
 [lib/amd/src/prefetch.js](lib_amd_src_prefetch.js.md), [line 162](lib_amd_src_prefetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templatesNames`

 

Array

 

A list of the template names to fetch
