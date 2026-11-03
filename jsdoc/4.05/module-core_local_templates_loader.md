# core/local/templates/loader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_local_templates_loader.html

# core/local/templates/loader

 

 

 

**Description:
 :** 

- 

Template this.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 24](lib_amd_src_local_templates_loader.js.md)

 

**Since:
 :** 

- 4.3

 

**Copyright:
 :** 

- 2023 Andrew Lyons 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Template this.

 

 

 

 

### Members

 

#### (inner) cachePartialPromises :Array.<Promise>

 

**Description:
 :** 

- 

Cache of already loaded template partial promises

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 48](lib_amd_src_local_templates_loader.js.md)

Cache of already loaded template partial promises

##### Type:

- 

Array.<Promise>

 

 

#### (inner) isLoadingTemplates :Bool

 

**Description:
 :** 

- 

Whether templates are currently being loaded

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 39](lib_amd_src_local_templates_loader.js.md)

Whether templates are currently being loaded

##### Type:

- 

Bool

 

 

#### (inner) loadTemplateBuffer :Array.<Object>

 

**Description:
 :** 

- 

List of templates to be loaded

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 36](lib_amd_src_local_templates_loader.js.md)

List of templates to be loaded

##### Type:

- 

Array.<Object>

 

 

#### (inner) templateCache :Map

 

**Description:
 :** 

- 

Cache of already loaded template strings

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 42](lib_amd_src_local_templates_loader.js.md)

Cache of already loaded template strings

##### Type:

- 

Map

 

 

#### (inner) templatePromises :Array.<Promise>

 

**Description:
 :** 

- 

Cache of already loaded template promises

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 45](lib_amd_src_local_templates_loader.js.md)

Cache of already loaded template promises

##### Type:

- 

Array.<Promise>

 

 

#### (inner) themeName :String

 

**Description:
 :** 

- 

for the current render

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 33](lib_amd_src_local_templates_loader.js.md)

for the current render

##### Type:

- 

String

 

 

 

### Methods

 

#### (async, static) _cachePartials(templateName, themeName, parentage) → {promise.<string>}

 

**Description:
 :** 

- 

Cache the template partials for the specified template.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 279](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateName`

 

string

 

 

 
 `themeName`

 

string

 

 

 
 `parentage`

 

array

 

 

 

##### Returns:

**
 Type

 :** 

promise.<string>

 

#### (static) getSearchKey(theme, templateName) → {string}

 

**Description:
 :** 

- 

A helper to get the search key

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 58](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `theme`

 

string

 

 

 
 `templateName`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

string

 

#### (static) getTemplateFromCache(searchKey) → {string}

 

**Description:
 :** 

- 

Fetch a template from the cache.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 128](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchKey`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

string

 

#### (static) getTemplatePromiseFromCache(searchKey) → {Object|null}

 

**Description:
 :** 

- 

Search the various caches for a template promise for the given search key.
The search key should be in the format // e.g. boost/core/modal.

If the template is found in any of the caches it will populate the other caches with
the same data as well.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 457](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchKey`

 

String

 

The template search key in the format // e.g. boost/core/modal

 

##### Returns:

jQuery promise resolved with the template source

**
 Type

 :** 

Object
|

null

 

#### (static) hasTemplateInCache(searchKey) → {bool}

 

**Description:
 :** 

- 

Check whether a template is in the cache.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 138](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchKey`

 

string

 

 

 

##### Returns:

**
 Type

 :** 

bool

 

#### (static) processLoadTemplateBuffer()

 

**Description:
 :** 

- 

Take all of the templates waiting in the buffer and load them from the server
or from the cache.

All of the templates that need to be loaded from the server will be batched up
and sent in a single network request.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 311](lib_amd_src_local_templates_loader.js.md)

 

#### (static) setTemplateInCache(searchKey, templateSource)

 

**Description:
 :** 

- 

Store a template in the cache.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 116](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchKey`

 

string

 

 

 
 `templateSource`

 

string

 

 

 

 

#### (inner) cachePartials(templateName, themeNameopt, parentage) → {Promise}

 

**Description:
 :** 

- 

Load a template and scan it for partials. Recursively fetch the partials.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 238](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `templateName`

 

string

 

 

 

 

 

should consist of the component and the name of the template like this:
core/menu (lib/templates/menu.mustache) or
tool_bananas/yellow (admin/tool/bananas/templates/yellow.mustache)

 
 `themeName`

 

string

 

 

 <optional>  

 

 

 `config.theme`

 

 

 
 `parentage`

 

Array

 

 

 

 

 

A list of requested partials in this render chain.

 

##### Returns:

JQuery promise object resolved when all partials are in the cache.

**
 Type

 :** 

Promise

 

#### (inner) getTemplate(templateName, themeNameopt) → {Promise}

 

**Description:
 :** 

- 

Load a template.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 62](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `templateName`

 

string

 

 

 

 

 

should consist of the component and the name of the template like this:
core/menu (lib/templates/menu.mustache) or
tool_bananas/yellow (admin/tool/bananas/templates/yellow.mustache)

 
 `themeName`

 

string

 

 

 <optional>  

 

 

 `config.theme`

 

The theme to load the template from

 

##### Returns:

JQuery promise object resolved when the template has been fetched.

**
 Type

 :** 

Promise

 

#### (inner) partialHelper(name, themeNameopt) → {string}

 

**Description:
 :** 

- 

Load a partial from the cache or ajax.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 192](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `name`

 

string

 

 

 

 

 

The partial name to load.

 
 `themeName`

 

string

 

 

 <optional>  

 

 

 `config.theme`

 

The theme to load the partial from.

 

##### Returns:

**
 Type

 :** 

string

 

#### (inner) scanForPartials(templateSource) → {Array}

 

**Description:
 :** 

- 

Scan a template source for partial tags and return a list of the found partials.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/loader.js](lib_amd_src_local_templates_loader.js.md), [line 209](lib_amd_src_local_templates_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateSource`

 

string

 

source template to scan.

 

##### Returns:

List of partials.

**
 Type

 :** 

Array
