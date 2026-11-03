# module:core/pending - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_pending.html

# module:core/pending

 

## 

 module:core/pending

 

 

A helper used to register any long-running operations that are in-progress and that Behat must wait for it to complete.

This is useful in cases where the user interface may be updated and take some time to change - for example where
applying a transition.

This data is used by Behat, but may also be consumed by other location too.

By informing Behat that an action is about to happen, and then that it is complete, allows
Behat to wait for that completion and avoid random failures in automated testing.

Note: It is recommended that a descriptive key be used to aid in debugging where possible, but this is optional.

 

 

 

 

## Constructor

#### new (require("core/pending"))(pendingKeyopt) → {Promise}

 

**Description:
 :** 

- 

Request a new pendingPromise for later resolution.

When the action you are performing is complete, simply call resolve on the returned Promise.

 

**Source:
 :** 

- 
 [lib/amd/src/pending.js](lib_amd_src_pending.js.md), [line 38](lib_amd_src_pending.js.md)

##### Example

 

```js
import Pending from 'core/pending';
import {getString} from 'core/str';

const stringPromise = new Pending('mod_myexample/setup');
const myString = getString('ok')
    .then(okay => {
        window.console.log(okay);
    })
    .then(okay => stringPromise.resolve(okay));
```

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `pendingKey`

 

String

 

 

 <optional>  

 

 

 `'pendingPromise'`

 

An identifier to help in debugging

 

##### Returns:

A Native Promise

**
 Type

 :** 

Promise

 

 

 

### Methods

 

#### (static) Promise(fn, pendingKeyopt) → {Promise}

 

**Description:
 :** 

- 

Create a new Pending Promise with the same interface as a native Promise.

 

**Source:
 :** 

- 
 [lib/amd/src/pending.js](lib_amd_src_pending.js.md), [line 111](lib_amd_src_pending.js.md)

 

**Since:
 :** 

- Moodle 4.2

##### Example

 

```js
// Use the Pending class in the same way that you would a Native Promise.
import Pending from 'core/pending';
import {getString} from 'core/str';

export const init => {
    Pending.Promise((resolve, reject) => {
        getString('ok')
            .then(okay => {
                window.console.log(okay);
                return okay;
            })
            .then(resolve)
            .catch(reject);
    }, 'mod_myexample/setup:init');
};
```

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `fn`

 

Callable

 

 

 

 

 

A callable which takes the resolve and reject arguments as in a Native Promise constructor.

 
 `pendingKey`

 

String

 

 

 <optional>  

 

 

 `'pendingPromise'`

 

An identifier to help in debugging

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) request(pendingKey) → {Promise}

 

**Description:
 :** 

- 

Create a new Pending Promise statically.

 

**Source:
 :** 

- 
 [lib/amd/src/pending.js](lib_amd_src_pending.js.md), [line 47](lib_amd_src_pending.js.md)

 

**Deprecated::** 

- since Moodle 4.2

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pendingKey`

 

String

 

An identifier to help in debugging

 

##### Returns:

A Native Promise

**
 Type

 :** 

Promise
