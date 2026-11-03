# mod_forum/grades/expandconversation - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_forum_grades_expandconversation.html

# mod_forum/grades/expandconversation

 

 

 

**Description:
 :** 

- 

This module handles the creation of a Modal that shows the user's post in context of the entire discussion.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/expandconversation.js](mod_forum_amd_src_grades_expandconversation.js.md), [line 16](mod_forum_amd_src_grades_expandconversation.js.md)

 

**Copyright:
 :** 

- 2019 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module handles the creation of a Modal that shows the user's post in context of the entire discussion.

 

 

 

 

### Members

 

#### (static, constant) registerEventListeners

 

**Description:
 :** 

- 

Register event listeners for the expand conversations button.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/expandconversation.js](mod_forum_amd_src_grades_expandconversation.js.md), [line 111](mod_forum_amd_src_grades_expandconversation.js.md)

Register event listeners for the expand conversations button.

 

 

### Methods

 

#### (inner) findGradableNode(node) → {HTMLElement}

 

**Description:
 :** 

- 

Find the Node containing the gradable details from the provided node by searching up the tree.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/expandconversation.js](mod_forum_amd_src_grades_expandconversation.js.md), [line 36](mod_forum_amd_src_grades_expandconversation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (async, inner) showPostInContext(rootNode, param)

 

**Description:
 :** 

- 

Show the post in context in a modal.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/grades/expandconversation.js](mod_forum_amd_src_grades_expandconversation.js.md), [line 45](mod_forum_amd_src_grades_expandconversation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rootNode`

 

HTMLElement

 

The button that has been clicked

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `focusOnClose`

 

bool

 

 

 <optional>  

 

 

 `null`
