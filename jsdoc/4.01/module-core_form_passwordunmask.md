# core_form/passwordunmask - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_form_passwordunmask.html

# core_form/passwordunmask

 

 

 

**Description:
 :** 

- 

Password Unmask functionality.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 16](lib_form_amd_src_passwordunmask.js.md)

 

**Since:
 :** 

- 3.2

 

**Copyright:
 :** 

- 2016 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Password Unmask functionality.

 

 

 

### Classes

 

**[core_form/passwordunmask](module-core_form_passwordunmask-core_form_passwordunmask.md)
 :** 

 

 

 

### Methods

 

#### (inner) addListeners() → {PasswordUnmask}

 

**Description:
 :** 

- 

Add the event listeners required for PasswordUnmask.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 58](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

**
 Type

 :** 

PasswordUnmask

 

#### (inner) checkFocusOut(e)

 

**Description:
 :** 

- 

Check whether focus was lost from the PasswordUnmask and turn editing off if required.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 118](lib_form_amd_src_passwordunmask.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

EventFacade

 

The EventFacade generating the suspsected Focus Out

 

 

#### (inner) getDisplayValue() → {String}

 

**Description:
 :** 

- 

Get the currently value.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 241](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) isEditing() → {Boolean}

 

**Description:
 :** 

- 

Whether the user is currently editing the field.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 154](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

True if edit mode is enabled

**
 Type

 :** 

Boolean

 

#### (inner) passwordVisible() → {Boolean}

 

**Description:
 :** 

- 

Whether the password is currently visible (unmasked).

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 144](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

True if the password is unmasked

**
 Type

 :** 

Boolean

 

#### (inner) setDisplayValue() → {PasswordUnmask}

 

**Description:
 :** 

- 

Set the currently value in the display, taking into account the current settings.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 251](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

**
 Type

 :** 

PasswordUnmask

 

#### (inner) turnEditingOff(focusOnEditLink) → {PasswordUnmask}

 

**Description:
 :** 

- 

Disable the editing functionality, optionally focusing on the edit link.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 205](lib_form_amd_src_passwordunmask.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `focusOnEditLink`

 

Boolean

 

Whether to focus on the edit link after disabling the editor

 

##### Returns:

**
 Type

 :** 

PasswordUnmask

 

#### (inner) turnEditingOn() → {PasswordUnmask}

 

**Description:
 :** 

- 

Enable the editing functionality.

 

**Source:
 :** 

- 
 [lib/form/amd/src/passwordunmask.js](lib_form_amd_src_passwordunmask.js.md), [line 164](lib_form_amd_src_passwordunmask.js.md)

##### Returns:

**
 Type

 :** 

PasswordUnmask
