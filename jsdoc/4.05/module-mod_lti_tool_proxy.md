# mod_lti/tool_proxy - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_lti_tool_proxy.html

# mod_lti/tool_proxy

 

 

 

**Description:
 :** 

- 

Provides an interface for a tool proxy in the Moodle server.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_proxy.js](mod_lti_amd_src_tool_proxy.js.md), [line 16](mod_lti_amd_src_tool_proxy.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2015 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Provides an interface for a tool proxy in the Moodle server.

 

 

 

 

### Methods

 

#### (inner) create(args) → {Promise}

 

**Description:
 :** 

- 

Create a tool proxy in Moodle.

The promise will fail if the proxy cannot be created, so you must handle the fail result.

See mod/lti/classes/external.php create_tool_proxy_parameters

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_proxy.js](mod_lti_amd_src_tool_proxy.js.md), [line 73](mod_lti_amd_src_tool_proxy.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Tool proxy properties

 

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

Delete a tool proxy from Moodle.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_proxy.js](mod_lti_amd_src_tool_proxy.js.md), [line 50](mod_lti_amd_src_tool_proxy.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Integer

 

Tool proxy ID

 

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
 [mod/lti/amd/src/tool_proxy.js](mod_lti_amd_src_tool_proxy.js.md), [line 26](mod_lti_amd_src_tool_proxy.js.md)

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
