# mod_assign/participants_selector - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_assign_participants_selector.html

# mod_assign/participants_selector

 

 

 

**Description:
 :** 

- 

Custom auto-complete adapter to load users from the assignment list_participants webservice.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/participant_selector.js](mod_assign_amd_src_participant_selector.js.md), [line 16](mod_assign_amd_src_participant_selector.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Custom auto-complete adapter to load users from the assignment list_participants webservice.

 

 

 

 

### Methods

 

#### (inner) processResults(selector, data) → {Array}

 

**Description:
 :** 

- 

Process the results returned from transport (convert to value + label)

 

**Source:
 :** 

- 
 [mod/assign/amd/src/participant_selector.js](mod_assign_amd_src_participant_selector.js.md), [line 29](mod_assign_amd_src_participant_selector.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

 

 
 `data`

 

Array

 

 

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) transport(selector, query, success, failure)

 

**Description:
 :** 

- 

Fetch results based on the current query. This also renders each result from a template before returning them.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/participant_selector.js](mod_assign_amd_src_participant_selector.js.md), [line 41](mod_assign_amd_src_participant_selector.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

String

 

Selector for the original select element

 
 `query`

 

String

 

Current search string

 
 `success`

 

function

 

Success handler

 
 `failure`

 

function

 

Failure handler
