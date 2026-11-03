# mod_lti/tool_type - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_lti_tool_type.html

# mod_lti/tool_type

 

 

 

**Description:
 :** 

- 

Provides an interface for a tool type in the Moodle server.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 16](mod_lti_amd_src_tool_type.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2015 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Provides an interface for a tool type in the Moodle server.

 

 

 

 

### Members

 

#### (inner) constants

 

**Description:
 :** 

- 

Tool type constants.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 161](mod_lti_amd_src_tool_type.js.md)

Tool type constants.

 

 

### Methods

 

#### (inner) create(args) → {Promise}

 

**Description:
 :** 

- 

Create a tool type in Moodle.

The promise will fail if the URL is not a cartridge, so you must handle the fail result.

See also:
mod/lti/classes/external.php create_tool_type_parameters()

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 51](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Tool type properties

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise

 

#### (inner) delete(id) → {Promise}

 

**Description:
 :** 

- 

Delete a tool type from Moodle.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 99](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Integer

 

Tool type ID

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise

 

#### (inner) isCartridge(url) → {Promise}

 

**Description:
 :** 

- 

Check if the given URL is a cartridge URL.

The promise will fail if the URL is unreachable, so you must handle the fail result.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 135](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `url`

 

String

 

 

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise

 

#### (inner) query(args) → {Promise}

 

**Description:
 :** 

- 

Get a list of tool types from Moodle for the given
search args.

See also:
mod/lti/classes/external.php get_tool_types_parameters()

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 26](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Search parameters

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise

 

#### (inner) query(id) → {Promise}

 

**Description:
 :** 

- 

Get a list of tool types from Moodle for the given
tool proxy id.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 122](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Integer

 

Tool type ID

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise

 

#### (inner) update(args) → {Promise}

 

**Description:
 :** 

- 

Update a tool type in Moodle.

See also:
mod/lti/classes/external.php update_tool_type_parameters()

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_type.js](mod_lti_amd_src_tool_type.js.md), [line 75](mod_lti_amd_src_tool_type.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Tool type properties

 

##### Returns:

jQuery Deferred object

**
 Type

 :** 

Promise
