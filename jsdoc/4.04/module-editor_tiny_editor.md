# editor_tiny/editor - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-editor_tiny_editor.html

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 569](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 107](lib_editor_tiny_amd_src_editor.js.md)

Get a list of all Editors in a Map, keyed by the DOM Node that the Editor is associated with.

 

#### (static, constant) getInstanceForElementId

 

**Description:
 :** 

- 

Get the TinyMCE instance for the specified Node ID.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 115](lib_editor_tiny_amd_src_editor.js.md)

Get the TinyMCE instance for the specified Node ID.

 

#### (static, constant) setupForElementId

 

**Description:
 :** 

- 

Set up TinyMCE for the selector at the specified HTML Node id.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 139](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the selector at the specified HTML Node id.

 

#### (static, constant) setupForTarget

 

**Description:
 :** 

- 

Set up TinyMCE for the HTML Element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 458](lib_editor_tiny_amd_src_editor.js.md)

Set up TinyMCE for the HTML Element.

 

#### (inner) defaultOptions :Object

 

**Description:
 :** 

- 

The default editor configuration.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 44](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 38](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 191](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 98](lib_editor_tiny_amd_src_editor.js.md)

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

 

#### (inner) getEditorConfiguration(target, tinyMCE, options, pluginValues) → {object}

 

**Description:
 :** 

- 

Fetch the TinyMCE configuration for this editor instance.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 381](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 173](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 216](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 52](lib_editor_tiny_amd_src_editor.js.md)

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
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 156](lib_editor_tiny_amd_src_editor.js.md)

 

#### (inner) isModalMode(target) → {boolean}

 

**Description:
 :** 

- 

Check if the target for TinyMCE is in a modal or not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/editor.js](lib_editor_tiny_amd_src_editor.js.md), [line 447](lib_editor_tiny_amd_src_editor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

Target to check

 

##### Returns:

True if the target is in a modal form.

**
 Type

 :** 

boolean
