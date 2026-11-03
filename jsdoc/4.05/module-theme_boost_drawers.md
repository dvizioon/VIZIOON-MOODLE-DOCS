# module:theme_boost/drawers - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-theme_boost_drawers.html

# module:theme_boost/drawers

 

## 

 module:theme_boost/drawers

 

 

The Drawers class is used to control on-screen drawer elements.

It handles opening, and closing of drawer elements, as well as more detailed behaviours such as closing a drawer when
another drawer is opened, and supports closing a drawer when the screen is resized.

Drawers are instantiated on page load, and can also be toggled lazily when toggling any drawer toggle, open button,
or close button.

A range of show and hide events are also dispatched as detailed in the class
[eventTypes](module-theme_boost_drawers.md) object.

 

 

 

 

## Constructor

#### new (require("theme_boost/drawers"))()

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 263](theme_boost_amd_src_drawers.js.md)

##### Examples

 

Standard usage

 

```js
// The module just needs to be included to add drawer support.
import 'theme_boost/drawers';
```

Manually open or close any drawer

 

```js
import Drawers from 'theme_boost/drawers';

const myDrawer = Drawers.getDrawerInstanceForNode(document.querySelector('.myDrawerNode');
myDrawer.closeDrawer();
```

Listen to the before show event and cancel it

 

```js
import Drawers from 'theme_boost/drawers';

document.addEventListener(Drawers.eventTypes.drawerShow, e => {
    // The drawer which will be shown.
    window.console.log(e.target);

    // The instance of the Drawers class for this drawer.
    window.console.log(e.detail.drawerInstance);

    // Prevent this drawer from being shown.
    e.preventDefault();
});
```

Listen to the shown event

 

```js
document.addEventListener(Drawers.eventTypes.drawerShown, e => {
    // The drawer which was shown.
    window.console.log(e.target);

    // The instance of the Drawers class for this drawer.
    window.console.log(e.detail.drawerInstance);
});
```

 

 

 

### Members

 

#### closeOnResize

 

**Description:
 :** 

- 

Whether the drawer should close when the window is resized

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 323](theme_boost_amd_src_drawers.js.md)

Whether the drawer should close when the window is resized

 

#### drawerNode

 

**Description:
 :** 

- 

The underlying HTMLElement which is controlled.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 267](theme_boost_amd_src_drawers.js.md)

The underlying HTMLElement which is controlled.

 

#### eventTypes

 

**Description:
 :** 

- 

The list of event types.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 336](theme_boost_amd_src_drawers.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `drawerShow`

 

String

 

See [event:theme_boost/drawers:show](module-theme_boost_drawers.md)

 
 `drawerShown`

 

String

 

See [event:theme_boost/drawers:shown](module-theme_boost_drawers.md)

 
 `drawerHide`

 

String

 

See [event:theme_boost/drawers:hide](module-theme_boost_drawers.md)

 
 `drawerHidden`

 

String

 

See [event:theme_boost/drawers:hidden](module-theme_boost_drawers.md)

 

The list of event types.

 

#### isOpen

 

**Description:
 :** 

- 

Whether the drawer is open.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 314](theme_boost_amd_src_drawers.js.md)

Whether the drawer is open.

 

#### (inner, constant) THRESHOLD :Number

 

**Description:
 :** 

- 

Pixel thresshold to auto-hide drawers.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 61](theme_boost_amd_src_drawers.js.md)

Pixel thresshold to auto-hide drawers.

##### Type:

- 

Number

 

 

#### (inner) boundingRect :DOMRect

 

**Description:
 :** 

- 

The drawer page bounding box dimensions.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 269](theme_boost_amd_src_drawers.js.md)

The drawer page bounding box dimensions.

##### Type:

- 

DOMRect

 

 

 

### Methods

 

#### closeDrawer(args)

 

**Description:
 :** 

- 

Close the drawer.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 499](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `focusOnOpenButton`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether to alter page focus when opening the drawer

 
 `updatePreferences`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether to update the user prewference

 

 

 

 

#### displace(scrollPosition)

 

**Description:
 :** 

- 

Displaces the drawer outsite the page.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 580](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `scrollPosition`

 

Number

 

the page current scroll position

 

 

#### openDrawer(args)

 

**Description:
 :** 

- 

Open the drawer.

By default, openDrawer sets the page focus to the close drawer button. However, when a drawer is open at page
load, this represents an accessibility problem as the initial focus changes without any user interaction. The
focusOnCloseButton parameter can be set to false to prevent this behaviour.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 420](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `focusOnCloseButton`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether to alter page focus when opening the drawer

 
 `setUserPref`

 

boolean

 

 

 <optional>  

 

 

 `true`

 

Whether to store the opened drawer state as a user preference

 

 

 

 

#### preventOverlap(currentFocus)

 

**Description:
 :** 

- 

Prevent drawer from overlapping an element.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 615](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentFocus`

 

HTMLElement

 

 

 

 

#### toggleVisibility()

 

**Description:
 :** 

- 

Toggle visibility of the drawer.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 567](theme_boost_amd_src_drawers.js.md)

 

#### (static) closeAllDrawers()

 

**Description:
 :** 

- 

Close all drawers.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 657](theme_boost_amd_src_drawers.js.md)

 

#### (static) closeOtherDrawers(comparisonInstance)

 

**Description:
 :** 

- 

Close all drawers except for the specified drawer.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 668](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `comparisonInstance`

 

[module:theme_boost/drawers](module-theme_boost_drawers.md)

 

 

 

 

#### (static) displaceDrawers(displace)

 

**Description:
 :** 

- 

Prevent drawer from covering the content when the page content covers the full page.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 699](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `displace`

 

Number

 

 

 

 

#### (static) getDrawerInstanceForNode(drawerNode) → {[module:theme_boost/drawers](module-theme_boost_drawers.md)}

 

**Description:
 :** 

- 

Get the drawer instance for the specified node

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 381](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `drawerNode`

 

HTMLElement

 

 

 

##### Returns:

**
 Type

 :** 

[module:theme_boost/drawers](module-theme_boost_drawers.md)

 

#### (static) preventCoveringFocusedElement()

 

**Description:
 :** 

- 

Prevent drawers from covering the focused element.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 681](theme_boost_amd_src_drawers.js.md)

 

#### (inner) focusLastUsedToggle(target)

 

**Description:
 :** 

- 

Set the focus to the last used button to open this drawer.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 725](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

string

 

The drawer target.

 

 

#### (inner) setLastUsedToggle(toggleButton)

 

**Description:
 :** 

- 

Set the last used attribute for the last used toggle button for a drawer.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 711](theme_boost_amd_src_drawers.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleButton`

 

object

 

The clicked button.

 

 

 

### Events

 

#### theme_boost/drawers:hidden

 

**Description:
 :** 

- 

An event triggered after a drawer is hidden.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 364](theme_boost_amd_src_drawers.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The drawer that was be hidden.

 

##### Type:

- 

CustomEvent

 

 

#### theme_boost/drawers:hide

 

**Description:
 :** 

- 

An event triggered before a drawer is hidden.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 355](theme_boost_amd_src_drawers.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The drawer that will be hidden.

 

##### Type:

- 

CustomEvent

 

 

#### theme_boost/drawers:show

 

**Description:
 :** 

- 

An event triggered before a drawer is shown.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 337](theme_boost_amd_src_drawers.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The drawer that will be opened.

 

##### Type:

- 

CustomEvent

 

 

#### theme_boost/drawers:shown

 

**Description:
 :** 

- 

An event triggered after a drawer is shown.

 

**Source:
 :** 

- 
 [theme/boost/amd/src/drawers.js](theme_boost_amd_src_drawers.js.md), [line 346](theme_boost_amd_src_drawers.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

The drawer that was be opened.

 

##### Type:

- 

CustomEvent
