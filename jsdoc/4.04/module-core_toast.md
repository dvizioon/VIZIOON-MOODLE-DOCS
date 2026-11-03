# core/toast - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_toast.html

# core/toast

 

 

 

**Description:
 :** 

- 

A system for displaying small snackbar notifications to users which disappear shortly after they are shown.

 

**Source:
 :** 

- 
 [lib/amd/src/toast.js](lib_amd_src_toast.js.md), [line 16](lib_amd_src_toast.js.md)

 

**Copyright:
 :** 

- 2019 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A system for displaying small snackbar notifications to users which disappear shortly after they are shown.

 

 

 

 

### Members

 

#### (static, constant) removeToastRegion

 

**Description:
 :** 

- 

Remove a parent region.

This is useful in cases such as where a dialog is to be removed and the toast region should be moved back to the body.

 

**Source:
 :** 

- 
 [lib/amd/src/toast.js](lib_amd_src_toast.js.md), [line 121](lib_amd_src_toast.js.md)

Remove a parent region.

This is useful in cases such as where a dialog is to be removed and the toast region should be moved back to the body.

 

 

### Methods

 

#### (static) add(message, configuration)

 

**Description:
 :** 

- 

Add a new toast or snackbar notification to the page.

 

**Source:
 :** 

- 
 [lib/amd/src/toast.js](lib_amd_src_toast.js.md), [line 77](lib_amd_src_toast.js.md)

##### Example

 

```js
import {add as addToast} from 'core/toast';
import {getString} from 'core/str';

addToast('Example string', {
    type: 'warning',
    autohide: false,
    closeButton: true,
});

addToast(getString('example', 'mod_myexample'), {
    type: 'warning',
    autohide: false,
    closeButton: true,
});
```

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `message`

 

String
|

Promise.<string>

 

 

 
 `configuration`

 

Object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `title`

 

String

 

 

 <optional>  

 

 

 

 

 
 `subtitle`

 

String

 

 

 <optional>  

 

 

 

 

 
 `type`

 

String

 

 

 <optional>  

 

 

 `info`

 

Optional type of the toast notification ('success', 'info', 'warning' or 'danger')

 
 `autohide`

 

Boolean

 

 

 <optional>  

 

 

 `true`

 

 

 
 `closeButton`

 

Boolean

 

 

 <optional>  

 

 

 `false`

 

 

 
 `delay`

 

Number

 

 

 <optional>  

 

 

 `4000`

 

 

 

 

 

 

#### (static) addToastRegion(parent)

 

**Description:
 :** 

- 

Add a new region to place toasts in, taking in a parent element.

 

**Source:
 :** 

- 
 [lib/amd/src/toast.js](lib_amd_src_toast.js.md), [line 35](lib_amd_src_toast.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `parent`

 

HTMLElement
