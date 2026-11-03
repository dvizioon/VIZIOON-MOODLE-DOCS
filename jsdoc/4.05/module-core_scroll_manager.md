# core/scroll_manager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_scroll_manager.html

# core/scroll_manager

 

 

 

**Description:
 :** 

- 

Scroll manager is a class that help with saving the scroll positing when you
click on an action icon, and then when the page is reloaded after processing
the action, it scrolls you to exactly where you were. This is much nicer for
the user.

To use this in your code, you need to ensure that:

  - The button that triggers the action has to have a click event handler that
calls saveScrollPos()

  - After doing the processing, the redirect() function will add 'mdlscrollto'
parameter into the redirect url automatically.

  - Finally, on the page that is reloaded (which should be the same as the one
the user started on) you need to call scrollToSavedPosition()
on page load.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 16](lib_amd_src_scroll_manager.js.md)

 

**Copyright:
 :** 

- 2021 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Scroll manager is a class that help with saving the scroll positing when you
click on an action icon, and then when the page is reloaded after processing
the action, it scrolls you to exactly where you were. This is much nicer for
the user.

To use this in your code, you need to ensure that:

- The button that triggers the action has to have a click event handler that
calls saveScrollPos()

- After doing the processing, the redirect() function will add 'mdlscrollto'
parameter into the redirect url automatically.

- Finally, on the page that is reloaded (which should be the same as the one
the user started on) you need to call scrollToSavedPosition()
on page load.

 

 

 

 

### Members

 

#### (static, constant) initLinksScrollPos

 

**Description:
 :** 

- 

Init event handlers for all links with data-save-scroll=true.
Handle to add mdlscrollto parameter to link using js when we click on the link.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 149](lib_amd_src_scroll_manager.js.md)

Init event handlers for all links with data-save-scroll=true.
Handle to add mdlscrollto parameter to link using js when we click on the link.

 

#### (static, constant) saveScrollPos

 

**Description:
 :** 

- 

In the form that contains the element, set the value of the form field with
name mdlscrollto to the current scroll position. If there is no element with
that name, it creates a hidden form field with that name within the form.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 112](lib_amd_src_scroll_manager.js.md)

In the form that contains the element, set the value of the form field with
name mdlscrollto to the current scroll position. If there is no element with
that name, it creates a hidden form field with that name within the form.

 

#### (static, constant) saveScrollPositionToForm

 

**Description:
 :** 

- 

Save the position to form.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 140](lib_amd_src_scroll_manager.js.md)

Save the position to form.

 

#### (static, constant) scrollToSavedPosition

 

**Description:
 :** 

- 

If there is a parameter like mdlscrollto=123 in the URL, scroll to that saved position.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 166](lib_amd_src_scroll_manager.js.md)

If there is a parameter like mdlscrollto=123 in the URL, scroll to that saved position.

 

#### (static, constant) watchScrollButtonSaves

 

**Description:
 :** 

- 

Init event handlers for all links with data-savescrollposition=true.
Set the value to the closest form.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 126](lib_amd_src_scroll_manager.js.md)

Init event handlers for all links with data-savescrollposition=true.
Set the value to the closest form.

 

#### (inner) scrollingElement

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 37](lib_amd_src_scroll_manager.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `scrollingElement`

 

HTMLElement

 

the current scrolling element.

 

 

 

### Methods

 

#### (inner) getScrollPos() → {Number}

 

**Description:
 :** 

- 

Get current scroll position.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 79](lib_amd_src_scroll_manager.js.md)

##### Returns:

Scroll position.

**
 Type

 :** 

Number

 

#### (inner) getScrollPositionElement(form) → {HTMLInputElement}

 

**Description:
 :** 

- 

Get the scroll position for this form.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 91](lib_amd_src_scroll_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

HTMLFormElement

 

 

 

##### Returns:

**
 Type

 :** 

HTMLInputElement

 

#### (inner) getScrollingElement() → {HTMLElement}

 

**Description:
 :** 

- 

Get the scrolling element.

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 61](lib_amd_src_scroll_manager.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### (inner) isScrollable(element) → {boolean}

 

**Description:
 :** 

- 

Is the element scrollable?

 

**Source:
 :** 

- 
 [lib/amd/src/scroll_manager.js](lib_amd_src_scroll_manager.js.md), [line 45](lib_amd_src_scroll_manager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

Element.

 

##### Returns:

**
 Type

 :** 

boolean
