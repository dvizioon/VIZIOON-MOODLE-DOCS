# tool_templatelibrary/search - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_templatelibrary_search.html

# tool_templatelibrary/search

 

 

 

**Description:
 :** 

- 

This module adds ajax search functions to the template library page.

 

**Source:
 :** 

- 
 [admin/tool/templatelibrary/amd/src/search.js](admin_tool_templatelibrary_amd_src_search.js.md), [line 16](admin_tool_templatelibrary_amd_src_search.js.md)

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module adds ajax search functions to the template library page.

 

 

 

 

### Methods

 

#### (inner) queueRefresh(callback, delay)

 

**Description:
 :** 

- 

Call the specified function after a delay. If this function is called again before the function is executed,
the function will only be executed once.

 

**Source:
 :** 

- 
 [admin/tool/templatelibrary/amd/src/search.js](admin_tool_templatelibrary_amd_src_search.js.md), [line 66](admin_tool_templatelibrary_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `callback`

 

function

 

 

 
 `delay`

 

Number

 

The time in milliseconds to delay.

 

 

#### (inner) refreshSearch(themename)

 

**Description:
 :** 

- 

Get the current values for the form inputs and refresh the list of matching templates.

 

**Source:
 :** 

- 
 [admin/tool/templatelibrary/amd/src/search.js](admin_tool_templatelibrary_amd_src_search.js.md), [line 39](admin_tool_templatelibrary_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `themename`

 

String

 

The naeme of the theme.

 

 

#### (inner) reloadListTemplate(templateList)

 

**Description:
 :** 

- 

The ajax call has returned with a new list of templates.

 

**Source:
 :** 

- 
 [admin/tool/templatelibrary/amd/src/search.js](admin_tool_templatelibrary_amd_src_search.js.md), [line 26](admin_tool_templatelibrary_amd_src_search.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateList`

 

Array.<String>

 

List of template ids.
