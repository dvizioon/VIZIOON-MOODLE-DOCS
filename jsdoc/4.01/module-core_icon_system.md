# core/icon_system - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_icon_system.html

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

 

#### (inner) getTemplateName() → {String}

 

**Description:
 :** 

- 

getTemplateName

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 66](lib_amd_src_icon_system.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) init() → {Promise}

 

**Description:
 :** 

- 

Initialise the icon system.

 

**Source:
 :** 

- 
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 36](lib_amd_src_icon_system.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) renderIcon(key, component, title, template) → {String}

 

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
 [lib/amd/src/icon_system.js](lib_amd_src_icon_system.js.md), [line 46](lib_amd_src_icon_system.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

String

 

 

 
 `component`

 

String

 

 

 
 `title`

 

String

 

 

 
 `template`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

String
