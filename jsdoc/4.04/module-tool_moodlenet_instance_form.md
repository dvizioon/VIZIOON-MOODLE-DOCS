# tool_moodlenet/instance_form - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_moodlenet_instance_form.html

# tool_moodlenet/instance_form

 

 

 

**Description:
 :** 

- 

Our basic form manager for when a user either enters
their profile url or just wants to browse.

This file is a mishmash of JS functions we need for both the standalone (M3.7, M3.8)
plugin & Moodle 3.9 functions. The 3.9 Functions have a base understanding that certain
things exist i.e. directory structures for templates. When this feature goes 3.9+ only
The goal is that we can quickly gut all AMD modules into bare JS files and use ES6 guidelines.
Till then this will have to do.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/instance_form.js](admin_tool_moodlenet_amd_src_instance_form.js.md), [line 16](admin_tool_moodlenet_amd_src_instance_form.js.md)

 

**Copyright:
 :** 

- 2020 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Our basic form manager for when a user either enters
their profile url or just wants to browse.

This file is a mishmash of JS functions we need for both the standalone (M3.7, M3.8)
plugin & Moodle 3.9 functions. The 3.9 Functions have a base understanding that certain
things exist i.e. directory structures for templates. When this feature goes 3.9+ only
The goal is that we can quickly gut all AMD modules into bare JS files and use ES6 guidelines.
Till then this will have to do.

 

 

 

 

### Methods

 

#### (inner) chooserNavigateFromMnet(carousel, modal, footerData)

 

**Description:
 :** 

- 

Given a user no longer wishes to see the MoodleNet profile url form transition them from there.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/instance_form.js](admin_tool_moodlenet_amd_src_instance_form.js.md), [line 127](admin_tool_moodlenet_amd_src_instance_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `carousel`

 

jQuery

 

Our carousel instance to manage

 
 `modal`

 

jQuery

 

Our modal instance to manage

 
 `footerData`

 

Object

 

Our footer object to render out

 

 

#### (inner) chooserNavigateToMnet(showMoodleNet, footerData, carousel, modal)

 

**Description:
 :** 

- 

Given a user wishes to see the MoodleNet profile url form transition them there.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/instance_form.js](admin_tool_moodlenet_amd_src_instance_form.js.md), [line 86](admin_tool_moodlenet_amd_src_instance_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `showMoodleNet`

 

HTMLElement

 

The chooser's area for ment

 
 `footerData`

 

Object

 

Our footer object to render out

 
 `carousel`

 

jQuery

 

Our carousel instance to manage

 
 `modal`

 

jQuery

 

Our modal instance to manage

 

 

#### (inner) registerListenerEvents(page)

 

**Description:
 :** 

- 

Add the event listeners to our form.

 

**Source:
 :** 

- 
 [admin/tool/moodlenet/amd/src/instance_form.js](admin_tool_moodlenet_amd_src_instance_form.js.md), [line 44](admin_tool_moodlenet_amd_src_instance_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `page`

 

HTMLElement

 

The whole page element for our form area
