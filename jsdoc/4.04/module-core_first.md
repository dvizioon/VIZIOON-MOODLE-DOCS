# core/first - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_first.html

# core/first

 

 

 

**Description:
 :** 

- 

This is an empty module, that is required before all other modules.
Because every module is returned from a request for any other module, this
forces the loading of all modules with a single request.

This function also sets up the listeners for ajax requests so we can tell
if any requests are still in progress.

 

**Source:
 :** 

- 
 [lib/amd/src/first.js](lib_amd_src_first.js.md), [line 16](lib_amd_src_first.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This is an empty module, that is required before all other modules.
Because every module is returned from a request for any other module, this
forces the loading of all modules with a single request.

This function also sets up the listeners for ajax requests so we can tell
if any requests are still in progress.
