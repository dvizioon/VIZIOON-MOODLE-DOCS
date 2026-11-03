# core/icon_system - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_icon_system.html

# core/icon_system

 

 

 

**Description:
 :** 

- 

Icon System base module.

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 16](lib_amd_src_icon_system.js.md)

 

**Copyright:
 :** 

- 2017 Damyon Wiese

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Icon System base module.

 

 

 

### Classes

 

**[core/icon_system](module-core_icon_system-core_icon_system.md)
 :** 

 

 

 

### Methods

 

#### (async, static) instance() → {Promise.<IconSystem>}

 

**Description:
 :** 

- 

Factory method to fetch the Icon System currently in use.

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 47](lib_amd_src_icon_system.js.md)

##### Returns:

**
 Type

 :** 

Promise.<IconSystem>

 

#### (inner) getTemplateName() → {string}

 

**Description:
 :** 

- 

Get the name of the template.

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 96](lib_amd_src_icon_system.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) renderIcon(key, component, title, template) → {string}

 

**Description:
 :** 

- 

Render an icon.

The key, component and title come from either the pix mustache helper tag, or the call to templates.renderIcon.
The template is the pre-loaded template string matching the template from getTemplateName() in this class.
This function must return a string (not a promise) because it is used during the internal rendering of the mustache
template (which is unfortunately synchronous). To render the mustache template in this function call
core/mustache.render() directly and do not use any partials, blocks or helper functions in the template.

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 75](lib_amd_src_icon_system.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

 

 
 `component`

 

string

 

 

 
 `title`

 

string

 

 

 
 `template`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

string
