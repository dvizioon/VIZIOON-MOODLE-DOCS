# mod_assign/grading_review_panel - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_grading_review_panel.html

# mod_assign/grading_review_panel

 

 

 

**Description:
 :** 

- 

Javascript controller for the "Review" panel at the left of the page.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 16](mod_assign_amd_src_grading_review_panel.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2016 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript controller for the "Review" panel at the left of the page.

 

 

 

### Classes

 

**[mod_assign/grading_review_panel](module-mod_assign_grading_review_panel-mod_assign_grading_review_panel.md)
 :** 

 

 

 

### Methods

 

#### (inner) collapsePanel()

 

**Description:
 :** 

- 

Hide the review panel.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 102](mod_assign_amd_src_grading_review_panel.js.md)

 

#### (inner) expandPanel()

 

**Description:
 :** 

- 

Show the review panel.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 112](mod_assign_amd_src_grading_review_panel.js.md)

 

#### (inner) getPanelContentElement() → {jQuery}

 

**Description:
 :** 

- 

Get the review panel content element.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 79](mod_assign_amd_src_grading_review_panel.js.md)

##### Returns:

**
 Type

 :** 

jQuery

 

#### (inner) getPanelElement() → {jQuery}

 

**Description:
 :** 

- 

Get the review panel element.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 69](mod_assign_amd_src_grading_review_panel.js.md)

##### Returns:

**
 Type

 :** 

jQuery

 

#### (inner) getReviewPanel(pluginname) → {DOMNode}

 

**Description:
 :** 

- 

It is first come first served to get ownership of the grading review panel.
There can be only one.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 39](mod_assign_amd_src_grading_review_panel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pluginname`

 

String

 

the first plugin to ask for the panel gets it.

 

##### Returns:

or false

**
 Type

 :** 

DOMNode

 

#### (inner) getTogglePanelButton() → {jQuery}

 

**Description:
 :** 

- 

Get the toggle review panel button.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 59](mod_assign_amd_src_grading_review_panel.js.md)

##### Returns:

**
 Type

 :** 

jQuery

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the review panel.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 122](mod_assign_amd_src_grading_review_panel.js.md)

 

#### (inner) togglePanel()

 

**Description:
 :** 

- 

Show/Hide the review panel.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/grading_review_panel.js](mod_assign_amd_src_grading_review_panel.js.md), [line 89](mod_assign_amd_src_grading_review_panel.js.md)
