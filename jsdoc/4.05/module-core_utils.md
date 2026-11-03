# core/utils - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_utils.html

# core/utils

 

 

 

**Description:
 :** 

- 

Utility functions.

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 16](lib_amd_src_utils.js.md)

 

**Copyright:
 :** 

- 2019 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Utility functions.

 

 

 

 

### Members

 

#### (static, constant) getNormalisedComponent

 

**Description:
 :** 

- 

Normalise the provided component such that '', 'moodle', and 'core' are treated consistently.

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 142](lib_amd_src_utils.js.md)

Normalise the provided component such that '', 'moodle', and 'core' are treated consistently.

 

#### (static, constant) wrapPromiseInWhenable

 

**Description:
 :** 

- 

Wrap a Native Promise in a jQuery Whenable for b/c.

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 158](lib_amd_src_utils.js.md)

Wrap a Native Promise in a jQuery Whenable for b/c.

 

#### (inner, constant) debounceMap

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 79](lib_amd_src_utils.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `debounceMap`

 

Map

 

A map of functions to their debounced pending promises.

 

 

 

### Methods

 

#### (static) debounce(func, wait, optionsopt) → {function}

 

**Description:
 :** 

- 

Create a wrapper function to debounce the execution of the given
function. Each attempt to execute the function will reset the cooldown
period.

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 94](lib_amd_src_utils.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `func`

 

function

 

 

 

The function to debounce

 
 `wait`

 

Number

 

 

 

The number of milliseconds to wait after the final attempt to execute

 
 `options`

 

Object

 

 

 <optional>  

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `pending`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

Whether to wrap the debounced method in a pending promise

 
 `cancel`

 

boolean

 

 

 <optional>  

 

 

 `false`

 

Whether to add a cancel method to the debounced function

 

 

 

##### Returns:

**
 Type

 :** 

function

 

#### (static) throttle(func, wait) → {function}

 

**Description:
 :** 

- 

Create a wrapper function to throttle the execution of the given

function to at most once every specified period.

If the function is attempted to be executed while it's in cooldown
(during the wait period) then it'll immediately execute again as
soon as the cooldown is over.

 

**Source:
 :** 

- 
 [lib/amd/src/utils.js](lib_amd_src_utils.js.md), [line 41](lib_amd_src_utils.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `func`

 

function

 

The function to throttle

 
 `wait`

 

Number

 

The number of milliseconds to wait between executions

 

##### Returns:

**
 Type

 :** 

function
