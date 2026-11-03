# core/ajax - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_ajax.html

# core/ajax

 

 

 

**Description:
 :** 

- 

Standard Ajax wrapper for Moodle. It calls the central Ajax script,
which can call any existing webservice using the current session.
In addition, it can batch multiple requests and return multiple responses.

 

**Source:
 :** 

- 
 [lib/amd/src/ajax.js](lib_amd_src_ajax.js.md), [line 16](lib_amd_src_ajax.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Standard Ajax wrapper for Moodle. It calls the central Ajax script,
which can call any existing webservice using the current session.
In addition, it can batch multiple requests and return multiple responses.

 

 

 

 

### Methods

 

#### (inner) call(requests, asyncopt, loginrequiredopt, nosessionupdateopt, timeoutopt, cachekeyopt) → {Array.<Promise>}

 

**Description:
 :** 

- 

Make a series of ajax requests and return all the responses.

 

**Source:
 :** 

- 
 [lib/amd/src/ajax.js](lib_amd_src_ajax.js.md), [line 130](lib_amd_src_ajax.js.md)

##### Examples

 

A simple example that you might find in a repository module

 

```js
import {call as fetchMany} from 'core/ajax';

export const fetchMessages = timeSince => fetchMany([{methodname: 'core_message_get_messages', args: {timeSince}}])[0];

export const fetchNotifications = timeSince => fetchMany([{
    methodname: 'core_message_get_notifications',
    args: {
        timeSince,
    }
}])[0];

export const fetchSomethingElse = (some, params, here) => fetchMany([{
    methodname: 'core_get_something_else',
    args: {
        some,
        params,
        gohere: here,
    },
}])[0];
```

An example of fetching a string using the cachekey parameter

 

```js
import {call as fetchMany} from 'core/ajax';
import * as Notification from 'core/notification';

export const performAction = (some, args) => {
    Promises.all(fetchMany([{methodname: 'core_get_string', args: {
        stringid: 'do_not_copy',
        component: 'core',
        lang: 'en',
        stringparams: [],
    }}], true, false, false, undefined, M.cfg.langrev))
    .then(([doNotCopyString]) => {
        window.console.log(doNotCopyString);
    })
    .catch(Notification.exception);
};
```

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `requests`

 

Array.<request>

 

 

 

 

 

Array of requests with each containing methodname and args properties.
done and fail callbacks can be set for each element in the array, or the
can be attached to the promises returned by this function.

 
 `async`

 

Boolean

 

 

 <optional>  

 

 

 `true`

 

If false this function will not return until the promises are resolved.

 
 `loginrequired`

 

Boolean

 

 

 <optional>  

 

 

 `true`

 

When false this function calls an endpoint which does not use the
session.
Note: This may only be used with external functions which have been marked as
`'loginrequired' => false`

 
 `nosessionupdate`

 

Boolean

 

 

 <optional>  

 

 

 `false`

 

If true, the timemodified for the session will not be updated.

 
 `timeout`

 

Number

 

 

 <optional>  

 

 

 

number of milliseconds to wait for a response. Defaults to no limit.

 
 `cachekey`

 

Number

 

 

 <optional>  

 

 

 

A cache key used to improve browser-side caching.
Typically the same `cachekey` is used for all function calls.
When the key changes, this causes the URL used to perform the fetch to change, which
prevents the existing browser cache from being used.
Note: This option is only availbale when `loginrequired` is `false`.
See [https://tracker.moodle.org/browser/MDL-65794](https://tracker.moodle.org/browser/MDL-65794) for more information.

 

##### Returns:

The Promises for each of the supplied requests.
The order of the Promise matches the order of requests exactly.

**
 Type

 :** 

Array.<Promise>

 

 

### Type Definitions

 

#### request

 

**Description:
 :** 

- 

A request to be performed.

 

**Source:
 :** 

- 
 [lib/amd/src/ajax.js](lib_amd_src_ajax.js.md), [line 28](lib_amd_src_ajax.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `methodname`

 

string

 

The remote method to be called

 
 `args`

 

object

 

The arguments to pass when fetching the remote content

 

A request to be performed.

##### Type:

- 

object
