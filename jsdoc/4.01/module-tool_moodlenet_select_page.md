# tool_moodlenet/select_page - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tool_moodlenet_select_page.html

# tool_moodlenet/select_page

 

 

 

**Description:
 :** 

- 

When returning to Moodle let the user select which course to add the resource to.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 16](admin_tool_moodlenet_amd_src_select_page.js.md)

 

**Copyright:
 :** 

- 2020 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

When returning to Moodle let the user select which course to add the resource to.

 

 

 

 

### Members

 

#### (inner) The :string

 

**Description:
 :** 

- 

id corresponding to the import.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 35](admin_tool_moodlenet_amd_src_select_page.js.md)

id corresponding to the import.

##### Type:

- 

string

 

 

 

### Methods

 

#### (inner) addCourses(page)

 

**Description:
 :** 

- 

Fetch the courses to show the user. We use the same WS structure & template as the search for consistency.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 152](admin_tool_moodlenet_amd_src_select_page.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `page`

 

HTMLElement

 

The whole page element for our course page

 

 

#### (inner) debounce(func, wait, immediate) → {function}

 

**Description:
 :** 

- 

Define our own debounce function as Moodle 3.7 does not have it.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 163](admin_tool_moodlenet_amd_src_select_page.js.md)

 

**Copyright:
 :** 

- 2009-2020 Jeremy Ashkenas, DocumentCloud and Investigative Reporters & Editors

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `func`

 

function

 

The function we want to keep calling

 
 `wait`

 

number

 

Our timeout

 
 `immediate`

 

boolean

 

Do we want to apply the function immediately

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) init(importIdString)

 

**Description:
 :** 

- 

Set up the page.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 40](admin_tool_moodlenet_amd_src_select_page.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `importIdString`

 

string

 

the string ID of the import.

 

 

#### (inner) registerListenerEvents(page)

 

**Description:
 :** 

- 

Add the event listeners to our page.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 132](admin_tool_moodlenet_amd_src_select_page.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `page`

 

HTMLElement

 

The whole page element for our page

 

 

#### (inner) searchCourses(inputValue, page, areaReplace)

 

**Description:
 :** 

- 

For a given input, the page & what to replace fetch courses and manage icons too.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/select_page.js](admin_tool_moodlenet_amd_src_select_page.js.md), [line 94](admin_tool_moodlenet_amd_src_select_page.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `inputValue`

 

string

 

What to search for

 
 `page`

 

HTMLElement

 

The whole page element for our page

 
 `areaReplace`

 

HTMLElement

 

The Element to replace the contents of
