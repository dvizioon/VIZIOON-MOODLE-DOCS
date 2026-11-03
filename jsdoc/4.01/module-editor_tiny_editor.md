# editor_tiny/editor - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-editor_tiny_editor.html

# editor_tiny/editor

 

 

 

**Description:
 :** 

- 

TinyMCE Editor Manager.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 16](lib_editor_tiny_amd_src_editor.js.md)

 

**Copyright:
 :** 

- 2022 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

TinyMCE Editor Manager.

 

 

 

 

### Members

 

#### (static, constant) configureDefaultEditor

 

**Description:
 :** 

- 

Set the default editor configuration.

This configuration is used when an editor is initialised without any configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 582](lib_editor_tiny_amd_src_editor.js.md)

Set the default editor configuration.

This configuration is used when an editor is initialised without any configuration.

 

#### (static, constant) getAllInstances

 

**Description:
 :** 

- 

Get a list of all Editors in a Map, keyed by the DOM Node that the Editor is associated with.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 105](lib_editor_tiny_amd_src_editor.js.md)

Get a list of all Editors in a Map, keyed by the DOM Node that the Editor is associated with.

 

#### (static, constant) getDefaultConfiguration

 

**Description:
 :** 

- 

Get the default configuration provided by TinyMCE.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 140](lib_editor_tiny_amd_src_defaults.js.md)

Get the default configuration provided by TinyMCE.

 

#### (static, constant) getDefaultMenu

 

**Description:
 :** 

- 

The upstream defaults for the TinyMCE Menu.

This value is defined in the TinyMCE documentation, but not exported anywhere useful.
https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 34](lib_editor_tiny_amd_src_defaults.js.md)

The upstream defaults for the TinyMCE Menu.

This value is defined in the TinyMCE documentation, but not exported anywhere useful.
https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

#### (static, constant) getDefaultQuickbarsImageToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_image_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 133](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_image_toolbar

 

#### (static, constant) getDefaultQuickbarsInsertToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_insert_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 122](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_insert_toolbar

 

#### (static, constant) getDefaultQuickbarsSelectionToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_selection_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 111](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_selection_toolbar

 

#### (static, constant) getDefaultToolbar

 

**Description:
 :** 

- 

The default toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 56](lib_editor_tiny_amd_src_defaults.js.md)

The default toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

#### (static, constant) getInstanceForElementId

 

**Description:
 :** 

- 

Get the TinyMCE instance for the specified Node ID.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 113](lib_editor_tiny_amd_src_editor.js.md)

Get the TinyMCE instance for the specified Node ID.

 

#### (static, constant) setupForElementId

 

**Description:
 :** 

- 

Set up TinyMCE for the selector at the specified HTML Node id.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 138](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the selector at the specified HTML Node id.

 

#### (static, constant) setupForTarget

 

**Description:
 :** 

- 

Set up TinyMCE for the HTML Element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 497](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the HTML Element.

 

#### (inner) defaultOptions :Object

 

**Description:
 :** 

- 

The default editor configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 42](lib_editor_tiny_amd_src_editor.js.md)

The default editor configuration.

##### Type:

- 

Object

 

 

#### (inner, constant) instanceMap :Map

 

**Description:
 :** 

- 

Storage for the TinyMCE instances on the page.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 36](lib_editor_tiny_amd_src_editor.js.md)

Storage for the TinyMCE instances on the page.

##### Type:

- 

Map

 

 

 

### Methods

 

#### (inner) adjustEditorSize(editor, target)

 

**Description:
 :** 

- 

Adjust the editor size base on the target element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 245](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

TinyMCE editor

 
 `target`

 

Node

 

Target element

 

 

#### (inner) fetchLanguage(language) → {object}

 

**Description:
 :** 

- 

Fetch the language data for the specified language.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 96](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `language`

 

string

 

The language identifier

 

##### Returns:

**
 Type

 :** 

object

 

#### (inner) fixDialoguePositionIfOpen(params)

 

**Description:
 :** 

- 

Fix the dialogue window positioning issue of TinyMCE editor in Safari browsers.

When using TinyMCE editor in Safari browsers, a problem may occur where the dialogue
windows (such as modal dialogs) overlap with page drawers due to a specific behavior
in Safari's rendering. This function addresses the issue by adjusting the CSS overflow
property of the page drawers, ensuring they do not obscure the dialogue windows.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 228](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `browser`

 

object

 

Browser environment.

 
 `fsplugin`

 

object

 

Fullscreen plugin.

 
 `open`

 

Boolean

 

True if the dialogue window opens, otherwise false.

 

 

 

 

#### (inner) fixMenuPositionIfInFullsreen(params)

 

**Description:
 :** 

- 

Fix the Tiny menu position if the editor is in fullscreen mode on the Boost theme.

The boost theme makes the TinyMCE editor rendered in a scrollable container,
scrolling the editor’s container will cause TinyMCE UI elements to be detached from the anchor.
Therefore, to keep the tinyMCE menu in the correct position,
adjustments must be made on the page drawers style.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 203](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `open`

 

Boolean

 

True if editor in fullscreen mode, otherwise false.

 

 

 

 

#### (inner) getEditorConfiguration(target, tinyMCE, options, pluginValues) → {object}

 

**Description:
 :** 

- 

Fetch the TinyMCE configuration for this editor instance.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 432](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 
 `tinyMCE`

 

TinyMCE

 

The TinyMCE API

 
 `options`

 

Object

 

The editor plugin configuration

 
 `pluginValues`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `pluginConfig`

 

object

 

The list of plugin configuration

 
 `pluginNames`

 

object

 

The list of plugins to load

 

 

 

##### Returns:

The TinyMCE Configuration

**
 Type

 :** 

object

 

#### (inner) getPlugins(options) → {object}

 

**Description:
 :** 

- 

Get the list of plugins to load for the specified configuration.

If the specified configuration does not include a plugin configuration, then return the default configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 165](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `options`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `plugins`

 

array

 

 

 <optional>  

 

 

 `null`

 

The plugin list

 

 

 

##### Returns:

**
 Type

 :** 

object

 

#### (inner) getStandardConfig(target, tinyMCE, options, plugins) → {object}

 

**Description:
 :** 

- 

Get the standard configuration for the specified options.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 270](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Node

 

 

 
 `tinyMCE`

 

tinyMCE

 

 

 
 `options`

 

object

 

 

 
 `plugins`

 

Array

 

 

 

##### Returns:

**
 Type

 :** 

object

 

#### (async, inner) importPluginList(pluginList) → {Array.<Promise>}

 

**Description:
 :** 

- 

Require the modules for the named set of TinyMCE plugins.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 50](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pluginList`

 

Array.<string>

 

The list of plugins

 

##### Returns:

A matching set of Promises relating to the requested plugins

**
 Type

 :** 

Array.<Promise>

 

#### (async, inner) initialisePage()

 

**Description:
 :** 

- 

Initialise the page with standard TinyMCE requirements.

Currently this includes the language taken from the HTML lang property.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 148](lib_editor_tiny_amd_src_editor.js.md)

 

#### (inner) nestMenu(editor)

 

**Description:
 :** 

- 

Nest the dropdown menu inside the parent DOM.

The TinyMCE menu has a significant issue with the Overflow style,
and the Boost theme heavily uses Overflow for drawer navigation.
Moving the menu container into the parent editor container makes it work correctly.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 186](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

object

 

 

 

 

 

 

 

**Description:
 :** 

- 

TinyMCE Editor Upstream defaults.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 18](lib_editor_tiny_amd_src_defaults.js.md)

 

**Copyright:
 :** 

- 2022 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

TinyMCE Editor Upstream defaults.

 

 

 

 

### Members

 

#### (static, constant) configureDefaultEditor

 

**Description:
 :** 

- 

Set the default editor configuration.

This configuration is used when an editor is initialised without any configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 582](lib_editor_tiny_amd_src_editor.js.md)

Set the default editor configuration.

This configuration is used when an editor is initialised without any configuration.

 

#### (static, constant) getAllInstances

 

**Description:
 :** 

- 

Get a list of all Editors in a Map, keyed by the DOM Node that the Editor is associated with.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 105](lib_editor_tiny_amd_src_editor.js.md)

Get a list of all Editors in a Map, keyed by the DOM Node that the Editor is associated with.

 

#### (static, constant) getDefaultConfiguration

 

**Description:
 :** 

- 

Get the default configuration provided by TinyMCE.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 140](lib_editor_tiny_amd_src_defaults.js.md)

Get the default configuration provided by TinyMCE.

 

#### (static, constant) getDefaultMenu

 

**Description:
 :** 

- 

The upstream defaults for the TinyMCE Menu.

This value is defined in the TinyMCE documentation, but not exported anywhere useful.
https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 34](lib_editor_tiny_amd_src_defaults.js.md)

The upstream defaults for the TinyMCE Menu.

This value is defined in the TinyMCE documentation, but not exported anywhere useful.
https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

#### (static, constant) getDefaultQuickbarsImageToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_image_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 133](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_image_toolbar

 

#### (static, constant) getDefaultQuickbarsInsertToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_insert_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 122](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_insert_toolbar

 

#### (static, constant) getDefaultQuickbarsSelectionToolbar

 

**Description:
 :** 

- 

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_selection_toolbar

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 111](lib_editor_tiny_amd_src_defaults.js.md)

The default quickbars_insert_toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/quickbars/#quickbars_selection_toolbar

 

#### (static, constant) getDefaultToolbar

 

**Description:
 :** 

- 

The default toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/defaults.js](lib_editor_tiny_amd_src_defaults.js.md), [line 56](lib_editor_tiny_amd_src_defaults.js.md)

The default toolbar configuration to use.

This is based upon the default value used if no toolbar is specified.

https://www.tiny.cloud/docs/tinymce/6/menus-configuration-options/#menu

 

#### (static, constant) getInstanceForElementId

 

**Description:
 :** 

- 

Get the TinyMCE instance for the specified Node ID.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 113](lib_editor_tiny_amd_src_editor.js.md)

Get the TinyMCE instance for the specified Node ID.

 

#### (static, constant) setupForElementId

 

**Description:
 :** 

- 

Set up TinyMCE for the selector at the specified HTML Node id.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 138](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the selector at the specified HTML Node id.

 

#### (static, constant) setupForTarget

 

**Description:
 :** 

- 

Set up TinyMCE for the HTML Element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 497](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the HTML Element.

 

#### (inner) defaultOptions :Object

 

**Description:
 :** 

- 

The default editor configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 42](lib_editor_tiny_amd_src_editor.js.md)

The default editor configuration.

##### Type:

- 

Object

 

 

#### (inner, constant) instanceMap :Map

 

**Description:
 :** 

- 

Storage for the TinyMCE instances on the page.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 36](lib_editor_tiny_amd_src_editor.js.md)

Storage for the TinyMCE instances on the page.

##### Type:

- 

Map

 

 

 

### Methods

 

#### (inner) adjustEditorSize(editor, target)

 

**Description:
 :** 

- 

Adjust the editor size base on the target element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 245](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

TinyMCE editor

 
 `target`

 

Node

 

Target element

 

 

#### (inner) fetchLanguage(language) → {object}

 

**Description:
 :** 

- 

Fetch the language data for the specified language.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 96](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `language`

 

string

 

The language identifier

 

##### Returns:

**
 Type

 :** 

object

 

#### (inner) fixDialoguePositionIfOpen(params)

 

**Description:
 :** 

- 

Fix the dialogue window positioning issue of TinyMCE editor in Safari browsers.

When using TinyMCE editor in Safari browsers, a problem may occur where the dialogue
windows (such as modal dialogs) overlap with page drawers due to a specific behavior
in Safari's rendering. This function addresses the issue by adjusting the CSS overflow
property of the page drawers, ensuring they do not obscure the dialogue windows.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 228](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `browser`

 

object

 

Browser environment.

 
 `fsplugin`

 

object

 

Fullscreen plugin.

 
 `open`

 

Boolean

 

True if the dialogue window opens, otherwise false.

 

 

 

 

#### (inner) fixMenuPositionIfInFullsreen(params)

 

**Description:
 :** 

- 

Fix the Tiny menu position if the editor is in fullscreen mode on the Boost theme.

The boost theme makes the TinyMCE editor rendered in a scrollable container,
scrolling the editor’s container will cause TinyMCE UI elements to be detached from the anchor.
Therefore, to keep the tinyMCE menu in the correct position,
adjustments must be made on the page drawers style.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 203](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `params`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `open`

 

Boolean

 

True if editor in fullscreen mode, otherwise false.

 

 

 

 

#### (inner) getEditorConfiguration(target, tinyMCE, options, pluginValues) → {object}

 

**Description:
 :** 

- 

Fetch the TinyMCE configuration for this editor instance.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 432](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 
 `tinyMCE`

 

TinyMCE

 

The TinyMCE API

 
 `options`

 

Object

 

The editor plugin configuration

 
 `pluginValues`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `pluginConfig`

 

object

 

The list of plugin configuration

 
 `pluginNames`

 

object

 

The list of plugins to load

 

 

 

##### Returns:

The TinyMCE Configuration

**
 Type

 :** 

object

 

#### (inner) getPlugins(options) → {object}

 

**Description:
 :** 

- 

Get the list of plugins to load for the specified configuration.

If the specified configuration does not include a plugin configuration, then return the default configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 165](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `options`

 

object

 

 

###### Properties

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `plugins`

 

array

 

 

 <optional>  

 

 

 `null`

 

The plugin list

 

 

 

##### Returns:

**
 Type

 :** 

object

 

#### (inner) getStandardConfig(target, tinyMCE, options, plugins) → {object}

 

**Description:
 :** 

- 

Get the standard configuration for the specified options.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 270](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Node

 

 

 
 `tinyMCE`

 

tinyMCE

 

 

 
 `options`

 

object

 

 

 
 `plugins`

 

Array

 

 

 

##### Returns:

**
 Type

 :** 

object

 

#### (async, inner) importPluginList(pluginList) → {Array.<Promise>}

 

**Description:
 :** 

- 

Require the modules for the named set of TinyMCE plugins.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 50](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pluginList`

 

Array.<string>

 

The list of plugins

 

##### Returns:

A matching set of Promises relating to the requested plugins

**
 Type

 :** 

Array.<Promise>

 

#### (async, inner) initialisePage()

 

**Description:
 :** 

- 

Initialise the page with standard TinyMCE requirements.

Currently this includes the language taken from the HTML lang property.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 148](lib_editor_tiny_amd_src_editor.js.md)

 

#### (inner) nestMenu(editor)

 

**Description:
 :** 

- 

Nest the dropdown menu inside the parent DOM.

The TinyMCE menu has a significant issue with the Overflow style,
and the Boost theme heavily uses Overflow for drawer navigation.
Moving the menu container into the parent editor container makes it work correctly.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 186](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

object
