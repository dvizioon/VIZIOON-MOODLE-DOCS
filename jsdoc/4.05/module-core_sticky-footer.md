# core/sticky-footer - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_sticky-footer.html

# core/sticky-footer

 

 

 

**Description:
 :** 

- 

Sticky footer wrapper module.

Themes are responsible for implementing the sticky footer. However,
modules can interact with the sticky footer using this module.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 16](lib_amd_src_sticky-footer.js.md)

 

**Copyright:
 :** 

- 2023 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Sticky footer wrapper module.

Themes are responsible for implementing the sticky footer. However,
modules can interact with the sticky footer using this module.

 

 

 

 

### Members

 

#### (static, constant) disableStickyFooter

 

**Description:
 :** 

- 

Disable sticky footer in the page.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 63](lib_amd_src_sticky-footer.js.md)

Disable sticky footer in the page.

 

#### (static, constant) enableStickyFooter

 

**Description:
 :** 

- 

Enable sticky footer in the page.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 50](lib_amd_src_sticky-footer.js.md)

Enable sticky footer in the page.

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize the module if the theme does not implement its own init.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 90](lib_amd_src_sticky-footer.js.md)

Initialize the module if the theme does not implement its own init.

 

#### (static, constant) registerManager

 

**Description:
 :** 

- 

Register the theme sticky footer methods.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 80](lib_amd_src_sticky-footer.js.md)

Register the theme sticky footer methods.

 

 

### Methods

 

#### (inner) notifyStickyFooterStateChange(enabled)

 

**Description:
 :** 

- 

Dispatch an event to notify that the state (enabled/disabled) of the sticky footer has changed.

 

**Source:
 :** 

- 
 [lib/amd/src/sticky-footer.js](lib_amd_src_sticky-footer.js.md), [line 109](lib_amd_src_sticky-footer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `enabled`

 

boolean

 

Whether the sticky footer has been enabled or disabled.
