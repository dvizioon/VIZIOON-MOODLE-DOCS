# core/log - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_log.html

# core/log

 

 

 

**Description:
 :** 

- 

This is an empty module, that is required before all other modules.
Because every module is returned from a request for any other module, this
forces the loading of all modules with a single request.

 

**Source:
 :** 

- 
 [lib/amd/src/log.js](lib_amd_src_log.js.md), [line 16](lib_amd_src_log.js.md)

 

**Copyright:
 :** 

- 2015 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This is an empty module, that is required before all other modules.
Because every module is returned from a request for any other module, this
forces the loading of all modules with a single request.

 

 

 

 

### Methods

 

#### (inner) setConfig(config)

 

**Description:
 :** 

- 

Set default config settings.

 

**Source:
 :** 

- 
 [lib/amd/src/log.js](lib_amd_src_log.js.md), [line 39](lib_amd_src_log.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

Object

 

including the level to use.
