# mod_feedback/edit - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_feedback_edit.html

# mod_feedback/edit

 

 

 

**Description:
 :** 

- 

Edit items in feedback module

 

**Source:
 :** 

- 
 [mod/feedback/amd/src/edit.js](mod_feedback_amd_src_edit.js.md), [line 16](mod_feedback_amd_src_edit.js.md)

 

**Copyright:
 :** 

- 2016 Marina Glancy

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Edit items in feedback module

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialise editor and all it's modules

 

**Source:
 :** 

- 
 [mod/feedback/amd/src/edit.js](mod_feedback_amd_src_edit.js.md), [line 79](mod_feedback_amd_src_edit.js.md)

Initialise editor and all it's modules

 

 

### Methods

 

#### (async, inner) enhanceEditForm() → {Promise.<void>}

 

**Description:
 :** 

- 

Enhance the edit form by adding a move item button and an action menu to each question.

 

**Source:
 :** 

- 
 [mod/feedback/amd/src/edit.js](mod_feedback_amd_src_edit.js.md), [line 149](mod_feedback_amd_src_edit.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (inner) getItemId(id)

 

**Description:
 :** 

- 

Returns the Feedback question item id from the DOM id of an item.

 

**Source:
 :** 

- 
 [mod/feedback/amd/src/edit.js](mod_feedback_amd_src_edit.js.md), [line 52](mod_feedback_amd_src_edit.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

String

 

The dom id, f.g.: feedback_item_22

 

##### Returns:

int

 

#### (inner) getItemOrder(element)

 

**Description:
 :** 

- 

Returns the order of the items in the sortable list.

 

**Source:
 :** 

- 
 [mod/feedback/amd/src/edit.js](mod_feedback_amd_src_edit.js.md), [line 62](mod_feedback_amd_src_edit.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

The element to get the order from.

 

##### Returns:

string
