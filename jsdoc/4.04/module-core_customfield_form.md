# core_customfield/form - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_customfield_form.html

# core_customfield/form

 

 

 

**Description:
 :** 

- 

Custom Field interaction management for Moodle.

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 16](customfield_amd_src_form.js.md)

 

**Copyright:
 :** 

- 2018 Toni Barbera

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Custom Field interaction management for Moodle.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialise the custom fields manager.

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 285](customfield_amd_src_form.js.md)

Initialise the custom fields manager.

 

 

### Methods

 

#### (inner) confirmDelete(id, type, component, area, itemid)

 

**Description:
 :** 

- 

Display confirmation dialogue

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 46](customfield_amd_src_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

 

 
 `type`

 

String

 

 

 
 `component`

 

String

 

 

 
 `area`

 

String

 

 

 
 `itemid`

 

Number

 

 

 

 

#### (inner) createNewCategory(component, area, itemid)

 

**Description:
 :** 

- 

Creates a new custom fields category with default name and updates the list

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 83](customfield_amd_src_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

String

 

 

 
 `area`

 

String

 

 

 
 `itemid`

 

Number

 

 

 

 

#### (inner) createNewField(element, component, area, itemid)

 

**Description:
 :** 

- 

Create new custom field

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 104](customfield_amd_src_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 
 `component`

 

String

 

 

 
 `area`

 

String

 

 

 
 `itemid`

 

Number

 

 

 

 

#### (inner) editField(element, component, area, itemid)

 

**Description:
 :** 

- 

Edit custom field

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 145](customfield_amd_src_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

 

 
 `component`

 

String

 

 

 
 `area`

 

String

 

 

 
 `itemid`

 

Number

 

 

 

 

#### (inner) getCategoryNameFor(nodeElement) → {String}

 

**Description:
 :** 

- 

Fetch the category name from an inplace editable, given a child node of that field.

 

**Source:
 :** 

- 
 [customfield/amd/src/form.js](customfield_amd_src_form.js.md), [line 182](customfield_amd_src_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `nodeElement`

 

NodeElement

 

 

 

##### Returns:

**
 Type

 :** 

String
