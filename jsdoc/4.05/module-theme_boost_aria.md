# theme_boost/aria - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-theme_boost_aria.html

# theme_boost/aria

 

 

 

**Description:
 :** 

- 

Enhancements to Bootstrap components for accessibility.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 16](theme_boost_amd_src_aria.js.md)

 

**Copyright:
 :** 

- 2018 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Enhancements to Bootstrap components for accessibility.

 

 

 

 

### Methods

 

#### (inner) autoFocus()

 

**Description:
 :** 

- 

After page load, focus on any element with special autofocus attribute.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 406](theme_boost_amd_src_aria.js.md)

 

#### (inner) collapseFix()

 

**Description:
 :** 

- 

Fix keyboard interaction with Bootstrap Collapse elements.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 503](theme_boost_amd_src_aria.js.md)

 

**See:
 :** 

- [WAI-ARIA Authoring Practices 1.1 - Disclosure (Show/Hide)](https://www.w3.org/TR/wai-aria-practices-1.1/)

 

 

#### (inner) comboboxFix()

 

**Description:
 :** 

- 

A lot of Bootstrap's out of the box features don't work if dropdown items are not focusable.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 235](theme_boost_amd_src_aria.js.md)

 

#### (inner) dropdownFix()

 

**Description:
 :** 

- 

Drop downs from bootstrap don't support keyboard accessibility by default.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 31](theme_boost_amd_src_aria.js.md)

 

#### (inner) rovingFocus(elements, e, vertical, updateTabIndex)

 

**Description:
 :** 

- 

Changes the focus to the correct element based on the key that is pressed.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 425](theme_boost_amd_src_aria.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elements`

 

NodeList

 

A NodeList of focusable elements to navigate between.

 
 `e`

 

KeyboardEvent

 

The keyboard event that triggers the roving focus.

 
 `vertical`

 

boolean

 

Whether the navigation is vertical.

 
 `updateTabIndex`

 

boolean

 

Whether to update the tabIndex of the elements.

 

 

#### (inner) tabElementFix()

 

**Description:
 :** 

- 

Fix accessibility issues regarding tab elements focus and their tab order in Bootstrap navs.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 469](theme_boost_amd_src_aria.js.md)

 

#### (inner) toolbarFix()

 

**Description:
 :** 

- 

Fix accessibility issues

 

**Source:
 :** 

- 
 [theme/boost/amd/src/aria.js](theme_boost_amd_src_aria.js.md), [line 518](theme_boost_amd_src_aria.js.md)
