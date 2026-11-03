# mod_forum/discussion_nested_v2 - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_forum_discussion_nested_v2.html

# mod_forum/discussion_nested_v2

 

 

 

**Description:
 :** 

- 

Module for viewing a discussion in nested v2 view.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 16](mod_forum_amd_src_discussion_nested_v2.js.md)

 

**Copyright:
 :** 

- 2019 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module for viewing a discussion in nested v2 view.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialise the javascript for the discussion in nested v2 display mode.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 405](mod_forum_amd_src_discussion_nested_v2.js.md)

Initialise the javascript for the discussion in nested v2 display mode.

 

#### (inner) showInPageReplyForm

 

**Description:
 :** 

- 

Variable to hold the showInPageReplyForm function after it's built.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 222](mod_forum_amd_src_discussion_nested_v2.js.md)

Variable to hold the showInPageReplyForm function after it's built.

 

 

### Methods

 

#### (inner) buildShowInPageReplyFormFunction(additionalTemplateContext) → {function}

 

**Description:
 :** 

- 

Build the showInPageReplyForm function with the given additional template context.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 230](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `additionalTemplateContext`

 

Object

 

Additional render context for the in page reply template.

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getHideRepliesButton(replyVisibilityToggleContainer) → {Object}

 

**Description:
 :** 

- 

Get the hide replies button element from the replies visibility toggle container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 157](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `replyVisibilityToggleContainer`

 

Object

 

jQuery element for the toggle container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getInPageReplyContainer(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the in page reply container element from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 86](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getInPageReplyCreateButton(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the in page reply create (reply) button element from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 106](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getInPageReplyForm(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the in page reply form element from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 96](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getParentPostContainers(element) → {Object}

 

**Description:
 :** 

- 

Get the parent post container elements from the given element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 66](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

jQuery element to search from

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getPostContainer(element) → {Object}

 

**Description:
 :** 

- 

Get the closest post container element from the given element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 45](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

jQuery element to search from

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getPostContainerById(element, id) → {Object}

 

**Description:
 :** 

- 

Get the closest post container element from the given element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 56](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

jQuery element to search from

 
 `id`

 

Number

 

Id of the post to find.

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getPostContentContainer(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the post content container element from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 76](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getRepliesContainer(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the replies container element from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 127](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getRepliesVisibilityToggleContainer(postContainer) → {Object}

 

**Description:
 :** 

- 

Get the replies visibility toggle container (show/hide replies button container) element
from the post container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 117](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) getShowRepliesButton(replyVisibilityToggleContainer) → {Object}

 

**Description:
 :** 

- 

Get the show replies button element from the replies visibility toggle container element.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 147](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `replyVisibilityToggleContainer`

 

Object

 

jQuery element for the toggle container

 

##### Returns:

jQuery element

**
 Type

 :** 

Object

 

#### (inner) hasInPageReplyForm(inPageReplyContainer) → {Bool}

 

**Description:
 :** 

- 

Check if the in page reply container contains the in page reply form.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 306](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `inPageReplyContainer`

 

Object

 

jQuery element for the in page reply container

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) hasReplies(postContainer) → {Bool}

 

**Description:
 :** 

- 

Check if the post has any replies.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 137](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) hideInPageReplyForm(postContainer, postIdToSee)

 

**Description:
 :** 

- 

Hide the in page reply form in the given in page reply container. The form
display will be animated.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 279](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `postContainer`

 

Object

 

 

 

jQuery element for the post container

 
 `postIdToSee`

 

Number
|

null

 

 

 `null`

 

Id of the post to scroll into view (if any)

 

 

#### (inner) hideReplies(postContainer)

 

**Description:
 :** 

- 

Hide the post replies.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 206](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

 

#### (inner) incrementTotalReplyCount(postContainer)

 

**Description:
 :** 

- 

Increment the total reply count in the show/hide replies buttons for the post.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 341](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

 

#### (inner) registerEventListeners(root)

 

**Description:
 :** 

- 

Create all of the event listeners for the discussion.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 353](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

jQuery element for the discussion container

 

 

#### (inner) renderInPageReplyTemplate(additionalTemplateContext, button, postContainer) → {Object}

 

**Description:
 :** 

- 

Render the template to generate the in page reply form HTML.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 318](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `additionalTemplateContext`

 

Object

 

Additional render context for the in page reply template

 
 `button`

 

Object

 

jQuery element for the reply button that was clicked

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

jQuery promise

**
 Type

 :** 

Object

 

#### (inner) repliesVisible(postContainer) → {Bool}

 

**Description:
 :** 

- 

Check if the replies are visible.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 167](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `postContainer`

 

Object

 

jQuery element for the post container

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) showReplies(postContainer, postIdToSee)

 

**Description:
 :** 

- 

Show the post replies.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/discussion_nested_v2.js](mod_forum_amd_src_discussion_nested_v2.js.md), [line 178](mod_forum_amd_src_discussion_nested_v2.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `postContainer`

 

Object

 

 

 

jQuery element for the post container

 
 `postIdToSee`

 

Number
|

null

 

 

 `null`

 

Id of the post to scroll into view (if any)
