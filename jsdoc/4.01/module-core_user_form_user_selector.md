# core_user/form_user_selector - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_user_form_user_selector.html

# core_user/form_user_selector

 

 

 

**Description:
 :** 

- 

Provides the required functionality for an autocomplete element to select a user.

 

**Source:
 :** 

- 
 [user/amd/src/form_user_selector.js](user_amd_src_form_user_selector.js.md), [line 16](user_amd_src_form_user_selector.js.md)

 

**Copyright:
 :** 

- 2020 David Mudrák 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Provides the required functionality for an autocomplete element to select a user.

 

 

 

 

### Methods

 

#### (static) processResults(selector, results) → {Array}

 

**Description:
 :** 

- 

Process the results for auto complete elements.

 

**Source:
 :** 

- 
 [user/amd/src/form_user_selector.js](user_amd_src_form_user_selector.js.md), [line 78](user_amd_src_form_user_selector.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

The selector of the auto complete element.

 
 `results`

 

Array

 

An array or results returned by {@see transport()}.

 

##### Returns:

New array of the selector options.

**
 Type

 :** 

Array

 

#### (static) transport(selector, query, callback, failure)

 

**Description:
 :** 

- 

Load the list of users matching the query and render the selector labels for them.

 

**Source:
 :** 

- 
 [user/amd/src/form_user_selector.js](user_amd_src_form_user_selector.js.md), [line 36](user_amd_src_form_user_selector.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

The selector of the auto complete element.

 
 `query`

 

String

 

The query string.

 
 `callback`

 

function

 

A callback function receiving an array of results.

 
 `failure`

 

function

 

A function to call in case of failure, receiving the error message.
