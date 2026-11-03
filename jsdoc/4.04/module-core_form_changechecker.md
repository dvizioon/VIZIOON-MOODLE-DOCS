# core_form/changechecker - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_form_changechecker.html

# core_form/changechecker

 

 

 

**Description:
 :** 

- 

This module provides change detection to forms, allowing a browser to warn the user before navigating away if changes
have been made.

Two flags are stored for each form:

  - a 'dirty' flag; and

  - a 'submitted' flag.

When the page is unloaded each watched form is checked. If the 'dirty' flag is set for any form, and the 'submitted'
flag is not set for any form, then a warning is shown.

The 'dirty' flag is set when any form element is modified within a watched form.
The flag can also be set programatically. This may be required for custom form elements.

It is not possible to customise the warning message in any modern browser.

Please note that some browsers have controls on when these alerts may or may not be shown.
See [https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload](https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload) for browser-specific
notes and references.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 16](lib_form_amd_src_changechecker.js.md)

 

**Copyright:
 :** 

- 2021 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module provides change detection to forms, allowing a browser to warn the user before navigating away if changes
have been made.

Two flags are stored for each form:

- a 'dirty' flag; and

- a 'submitted' flag.

When the page is unloaded each watched form is checked. If the 'dirty' flag is set for any form, and the 'submitted'
flag is not set for any form, then a warning is shown.

The 'dirty' flag is set when any form element is modified within a watched form.
The flag can also be set programatically. This may be required for custom form elements.

It is not possible to customise the warning message in any modern browser.

Please note that some browsers have controls on when these alerts may or may not be shown.
See [https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload](https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload) for browser-specific
notes and references.

 

### Examples

 

Usage where the FormElement is already held

 

```js
import {watchForm} from 'core_form/changechecker';

// Fetch the form element somehow.
watchForm(formElement);
```

Usage from the child of a form - i.e. an input, button, div, etc.

 

```js
import {watchForm} from 'core_form/changechecker';

// Watch the form by using a child of it.
watchForm(document.querySelector('input[data-foo="bar"]'););
```

Usage from within a template

 

```js
<form id="mod_example-entry-{{uniqid}}" ...>
  <!--

  -->
</form>
{{#js}}
require(['core_form/changechecker'], function(changeChecker) {
    watchFormById('mod_example-entry-{{uniqid}}');
});
{{/js}}
```

 

 

 

 

### Methods

 

#### (static) disableAllChecks()

 

**Description:
 :** 

- 

Actively disable the form change checker.

Please note that it cannot be re-enabled once disabled.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 220](lib_form_amd_src_changechecker.js.md)

 

#### (static) isAnyWatchedFormDirty() → {Bool}

 

**Description:
 :** 

- 

Check whether any watched from is dirty.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 230](lib_form_amd_src_changechecker.js.md)

##### Returns:

**
 Type

 :** 

Bool

 

#### (static) markAllFormsAsDirty()

 

**Description:
 :** 

- 

Mark all forms as dirty.

This function is only for backwards-compliance with the old YUI module and should not be used in any other situation.
It will be removed in Moodle 4.4.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 188](lib_form_amd_src_changechecker.js.md)

 

#### (static) markAllFormsSubmitted()

 

**Description:
 :** 

- 

Mark all forms as submitted.

This function is only for backwards-compliance with the old YUI module and should not be used in any other situation.
It will be removed in Moodle 4.4.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 367](lib_form_amd_src_changechecker.js.md)

 

#### (static) markFormAsDirty(formNode)

 

**Description:
 :** 

- 

Mark a specific form as dirty.

This behaviour may be required for custom form elements which are not caught by the standard change listeners.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 202](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formNode`

 

HTMLElement

 

 

 

 

#### (static) markFormAsDirtyById(formId)

 

**Description:
 :** 

- 

Mark the form matching the specified ID as dirty.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 511](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formId`

 

String

 

 

 

 

#### (static) markFormChangedFromNode(changedNode)

 

**Description:
 :** 

- 

Mark a form as changed.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 322](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `changedNode`

 

HTMLElement

 

An element in the form which was changed

 

 

#### (static) markFormSubmitted(formNode)

 

**Description:
 :** 

- 

Mark a form as submitted.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 349](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formNode`

 

HTMLElement

 

An element in the form to mark as submitted

 

 

#### (static) resetAllFormDirtyStates()

 

**Description:
 :** 

- 

Reset the 'dirty' flag for all watched forms.

If a form was previously marked as 'dirty', then this flag will be cleared and when the page is unloaded no warning
will be shown.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 156](lib_form_amd_src_changechecker.js.md)

 

#### (static) resetFormDirtyState(formNode)

 

**Description:
 :** 

- 

Reset the 'dirty' flag of the specified form.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 169](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formNode`

 

HTMLElement

 

 

 

 

#### (static) resetFormDirtyStateById(formId)

 

**Description:
 :** 

- 

Reset the dirty state of the form matching the specified ID..

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 501](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formId`

 

String

 

 

 

 

#### (protected, static) startWatching()

 

**Description:
 :** 

- 

Start watching for form changes.

This function is called on module load, and should not normally be called.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 416](lib_form_amd_src_changechecker.js.md)

 

#### (static) unWatchForm(formNode)

 

**Description:
 :** 

- 

Stop watching the specified form for changes.

If the form was not watched, then no change is made.

A child of the form may be passed instead.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 144](lib_form_amd_src_changechecker.js.md)

##### Example

 

Stop watching a form for changes

 

```js
import {unWatchForm} from 'core_form/changechecker';

// ...
document.addEventListener('click', e => {
    if (e.target.closest('[data-action="changePage"]')) {
        unWatchForm(e.target);
    }
});
```

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formNode`

 

HTMLElement

 

 

 

 

#### (static) watchForm(formNode)

 

**Description:
 :** 

- 

Watch the specified form for changes.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 108](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formNode`

 

HTMLElement

 

 

 

 

#### (static) watchFormById(formId)

 

**Description:
 :** 

- 

Watch the form matching the specified ID for changes.

 

**Source:
 :** 

- 
 [lib/form/amd/src/changechecker.js](lib_form_amd_src_changechecker.js.md), [line 491](lib_form_amd_src_changechecker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formId`

 

String
