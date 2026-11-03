# module:core/local/templates/renderer - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_local_templates_renderer.html

# module:core/local/templates/renderer

 

## 

 module:core/local/templates/renderer

 

 

 

 

#### new (require("core/local/templates/renderer"))()

 

**Description:
 :** 

- 

Constructor

Each call to templates.render gets it's own instance of this class.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 98](lib_amd_src_local_templates_renderer.js.md)

 

 

 

### Members

 

#### (inner) disallowedNestedHelpers :Array

 

**Description:
 :** 

- 

List of helpers that can't be called within other helpers

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 68](lib_amd_src_local_templates_renderer.js.md)

List of helpers that can't be called within other helpers

##### Type:

- 

Array

 

 

#### (inner) iconSystem :Object

 

**Description:
 :** 

- 

Object extending core/iconsystem

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 65](lib_amd_src_local_templates_renderer.js.md)

Object extending core/iconsystem

##### Type:

- 

Object

 

 

#### (inner) isLoadingTemplates :Bool

 

**Description:
 :** 

- 

Whether templates are currently being loaded

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 62](lib_amd_src_local_templates_renderer.js.md)

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
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 59](lib_amd_src_local_templates_renderer.js.md)

List of templates to be loaded

##### Type:

- 

Array.<Object>

 

 

#### (inner) requiredDates :Array.<object>

 

**Description:
 :** 

- 

Collection of dates found during the rendering of one template

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 47](lib_amd_src_local_templates_renderer.js.md)

Collection of dates found during the rendering of one template

##### Type:

- 

Array.<object>

 

 

#### (inner) requiredJS :Array.<string>

 

**Description:
 :** 

- 

Collection of js blocks found during the rendering of one template

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 50](lib_amd_src_local_templates_renderer.js.md)

Collection of js blocks found during the rendering of one template

##### Type:

- 

Array.<string>

 

 

#### (inner) requiredStrings :Array.<string>

 

**Description:
 :** 

- 

Collection of strings found during the rendering of one template

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 44](lib_amd_src_local_templates_renderer.js.md)

Collection of strings found during the rendering of one template

##### Type:

- 

Array.<string>

 

 

#### (inner) templateCache :Array.<String>

 

**Description:
 :** 

- 

Cache of already loaded template strings

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 73](lib_amd_src_local_templates_renderer.js.md)

Cache of already loaded template strings

##### Type:

- 

Array.<String>

 

 

#### (inner) themeName :String

 

**Description:
 :** 

- 

for the current render

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 53](lib_amd_src_local_templates_renderer.js.md)

for the current render

##### Type:

- 

String

 

 

#### (inner) uniqInstances :Number

 

**Description:
 :** 

- 

Count of times this constructor has been called.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 56](lib_amd_src_local_templates_renderer.js.md)

Count of times this constructor has been called.

##### Type:

- 

Number

 

 

 

### Methods

 

#### addHelperFunction(helperFunction, context) → {function}

 

**Description:
 :** 

- 

Return a helper function to be added to the context for rendering the a
template.

This will parse the provided text before giving it to the helper function
in order to remove any disallowed nested helpers to prevent one helper
from calling another.

In particular to prevent the JS helper from being called from within another
helper because it can lead to security issues when the JS portion is user
provided.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 385](lib_amd_src_local_templates_renderer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `helperFunction`

 

function

 

The helper function to add

 
 `context`

 

object

 

The template context for the helper function

 

##### Returns:

To be set in the context

**
 Type

 :** 

function

 

#### (async) processRenderedContent(renderedContent) → {Promise.<object.<string, string>>}

 

**Description:
 :** 

- 

Process the rendered content, treating any strings and applying and helper strings, dates, etc.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 574](lib_amd_src_local_templates_renderer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `renderedContent`

 

string

 

 

 

##### Returns:

The rendered HTML and JS.

**
 Type

 :** 

Promise.<object.<string, string>>

 

#### (async) setupIconSystem()

 

**Description:
 :** 

- 

Helper to set up the icon system.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 154](lib_amd_src_local_templates_renderer.js.md)

 

#### treatDatesInContent(content, dates) → {String}

 

**Description:
 :** 

- 

Treat strings in content.

The purpose of this method is to replace the date placeholders found in the
content with the their respective translated dates.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 522](lib_amd_src_local_templates_renderer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `content`

 

String

 

The content in which string placeholders are to be found.

 
 `dates`

 

Array

 

The dates to replace with.

 

##### Returns:

The treated content.

**
 Type

 :** 

String

 

#### treatStringsInContent(content, stringMap) → {String}

 

**Description:
 :** 

- 

Treat strings in content.

The purpose of this method is to replace the placeholders found in a string
with the their respective translated strings.

Previously we were relying on String.replace() but the complexity increased with
the numbers of strings to replace. Now we manually walk the string and stop at each
placeholder we find, only then we replace it. Most of the time we will
replace all the placeholders in a single run, at times we will need a few
more runs when placeholders are replaced with strings that contain placeholders
themselves.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 476](lib_amd_src_local_templates_renderer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `content`

 

String

 

The content in which string placeholders are to be found.

 
 `stringMap`

 

Map

 

The strings to replace with.

 

##### Returns:

The treated content.

**
 Type

 :** 

String

 

#### (static) getLoader() → {Loader}

 

**Description:
 :** 

- 

Get the Loader used to fetch templates.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 119](lib_amd_src_local_templates_renderer.js.md)

##### Returns:

**
 Type

 :** 

Loader

 

#### (static) setLoader(loader)

 

**Description:
 :** 

- 

Set the template loader to use for all Template renderers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 110](lib_amd_src_local_templates_renderer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `loader`

 

Loader
