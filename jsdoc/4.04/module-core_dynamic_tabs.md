# core/dynamic_tabs - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_dynamic_tabs.html

# core/dynamic_tabs

 

 

 

**Description:
 :** 

- 

Dynamic Tabs UI element with AJAX loading of tabs content

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 16](lib_amd_src_dynamic_tabs.js.md)

 

**Copyright:
 :** 

- 2021 David Matamoros  based on code from Marina Glancy

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Dynamic Tabs UI element with AJAX loading of tabs content

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialises the tabs view on the page (only one tabs view per page is supported)

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 48](lib_amd_src_dynamic_tabs.js.md)

Initialises the tabs view on the page (only one tabs view per page is supported)

 

 

### Methods

 

#### (inner) getActiveTabName() → {String|null}

 

**Description:
 :** 

- 

Returns id/name of the currently active tab

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 112](lib_amd_src_dynamic_tabs.js.md)

##### Returns:

**
 Type

 :** 

String
|

null

 

#### (inner) getFirstTabName() → {String|null}

 

**Description:
 :** 

- 

Returns the id/name of the first tab

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 122](lib_amd_src_dynamic_tabs.js.md)

##### Returns:

**
 Type

 :** 

String
|

null

 

#### (inner) getTab(tabName) → {HTMLElement}

 

**Description:
 :** 

- 

Return the tab given the tab name

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 164](lib_amd_src_dynamic_tabs.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tabName`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) getTabPane(tabName) → {HTMLElement}

 

**Description:
 :** 

- 

Return the tab pane given the tab name

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 174](lib_amd_src_dynamic_tabs.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tabName`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) loadTab(tabName)

 

**Description:
 :** 

- 

Loads contents of a tab using an AJAX request

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 132](lib_amd_src_dynamic_tabs.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tabName`

 

String

 

 

 

 

#### (inner) openTab(tabName) → {Boolean}

 

**Description:
 :** 

- 

Open the tab on page load. If this script loads before theme_boost/tab we need to open tab ourselves

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 184](lib_amd_src_dynamic_tabs.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tabName`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### (inner) openTabFromHash() → {Boolean}

 

**Description:
 :** 

- 

If there is a location hash that is the same as the tab name - open this tab.

 

**Source:
 :** 

- 
 [lib/amd/src/dynamic_tabs.js](lib_amd_src_dynamic_tabs.js.md), [line 201](lib_amd_src_dynamic_tabs.js.md)

##### Returns:

**
 Type

 :** 

Boolean
