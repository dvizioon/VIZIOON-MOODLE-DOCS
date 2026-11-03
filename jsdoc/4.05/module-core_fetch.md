# core/fetch - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_fetch.html

# core/fetch

 

 

 

**Description:
 :** 

- 

The core/fetch module allows you to make web service requests to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 16](lib_amd_src_fetch.js.md)

 

**Copyright:
 :** 

- Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

The core/fetch module allows you to make web service requests to the Moodle API.

 

### Example

 

Perform a single GET request

 

```js
import Fetch from 'core/fetch';

const result = Fetch.performGet('mod_example', 'animals', { params: { type: 'mammal' } });

result.then((response) => {
   // Do something with the Response object.
})
.catch((error) => {
    // Handle the error
});
```

 

 

 

### Classes

 

**[Fetch](module-core_fetch-Fetch.md)
 :[RequestWrapper](module-core_fetch-RequestWrapper.md)
 :** 

 

 

 

### Methods

 

#### (static) performDelete(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 271](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `params`

 

object

 

 

 <optional>  

 

 

 `{}`

 

The parameters to pass to the API

 
 `body`

 

string
|

Object
|

FormData

 

 

 <optional>  

 

 

 `null`

 

The HTTP method to use

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (static) performGet(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 155](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `params`

 

object

 

 

 <optional>  

 

 

 `{}`

 

The parameters to pass to the API

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (static) performHead(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 178](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `params`

 

object

 

 

 <optional>  

 

 

 `{}`

 

The parameters to pass to the API

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (static) performPatch(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a PATCH request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 247](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `body`

 

string
|

Object
|

FormData

 

The HTTP method to use

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (static) performPost(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 201](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `body`

 

string
|

Object
|

FormData

 

The HTTP method to use

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (static) performPut(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 224](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `body`

 

string
|

Object
|

FormData

 

The HTTP method to use

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>

 

#### (async, static) request(component, action, params) → {Promise.<Response>}

 

**Description:
 :** 

- 

Make a single request to the Moodle API.

 

**Source:
 :** 

- 
 [lib/amd/src/fetch.js](lib_amd_src_fetch.js.md), [line 122](lib_amd_src_fetch.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

The frankenstyle component name

 
 `action`

 

string

 

The component action to perform

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `params`

 

object

 

 

 <optional>  

 

 

 `{}`

 

The parameters to pass to the API

 
 `body`

 

string
|

Object
|

FormData

 

 

 <optional>  

 

 

 `null`

 

The HTTP method to use

 
 `method`

 

string

 

 

 <optional>  

 

 

 `"GET"`

 

The HTTP method to use

 

 

 

##### Returns:

A promise that resolves to the Response object for the request

**
 Type

 :** 

Promise.<Response>
