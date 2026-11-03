# core/templates - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_templates.html

# core/templates

 

 

 

**Description:
 :** 

- 

Template renderer for Moodle. Load and render Moodle templates with Mustache.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 16](lib_amd_src_templates.js.md)

 

**Since:
 :** 

- 2.9

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Template renderer for Moodle. Load and render Moodle templates with Mustache.

 

 

 

 

### Members

 

#### (inner) cachePartialPromises :Array.<Promise>

 

**Description:
 :** 

- 

Cache of already loaded template partial promises

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 69](lib_amd_src_templates.js.md)

Cache of already loaded template partial promises

##### Type:

- 

Array.<Promise>

 

 

#### (inner) disallowedNestedHelpers :Array

 

**Description:
 :** 

- 

List of helpers that can't be called within other helpers

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 81](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 72](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 78](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 75](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 306](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 309](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 303](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 63](lib_amd_src_templates.js.md)

Cache of already loaded template strings

##### Type:

- 

Array.<String>

 

 

#### (inner) templatePromises :Array.<Promise>

 

**Description:
 :** 

- 

Cache of already loaded template promises

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 66](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 312](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 60](lib_amd_src_templates.js.md)

Count of times this constructor has been called.

##### Type:

- 

Number

 

 

 

### Methods

 

#### (inner) appendNodeContents(element, html, js) → {Array}

 

**Description:
 :** 

- 

Append some HTML to a node and trigger events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1313](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

jQuery
|

String

 

Element or selector to append HTML to

 
 `html`

 

String

 

HTML to append

 
 `js`

 

String

 

Javascript to run after we append the html

 

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) getTemplate(templateNames, themeName) → {Promise}

 

**Description:
 :** 

- 

Prefetch a set of templates without rendering them.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1199](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateNames`

 

Array

 

The list of templates to fetch

 
 `themeName`

 

String

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) prependNodeContents(element, html, js) → {Array}

 

**Description:
 :** 

- 

Prepend some HTML to a node and trigger events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1300](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

jQuery
|

String

 

Element or selector to prepend HTML to

 
 `html`

 

String

 

HTML to prepend

 
 `js`

 

String

 

Javascript to run after we prepend the html

 

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) renderIcon(key, component, title) → {Promise}

 

**Description:
 :** 

- 

Every call to renderIcon creates a new instance of the class and calls renderIcon on it. This
means each render call has it's own class variables.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1245](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

Icon key.

 
 `component`

 

string

 

Icon component

 
 `title`

 

string

 

Icon title

 

##### Returns:

JQuery promise object resolved when the pix has been rendered.

**
 Type

 :** 

Promise

 

#### (inner) replaceNode(element, newHTML, newJS) → {Array}

 

**Description:
 :** 

- 

Insert a node in the page with some new HTML and run the JS.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1287](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

JQuery

 

Element or selector to replace.

 
 `newHTML`

 

String

 

HTML to insert / replace.

 
 `newJS`

 

String

 

Javascript to run after the insertion.

 

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) replaceNodeContents(element, newHTML, newJS) → {Array}

 

**Description:
 :** 

- 

Replace a node in the page with some new HTML and run the JS.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1274](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

JQuery

 

Element or selector to replace.

 
 `newHTML`

 

String

 

HTML to insert / replace.

 
 `newJS`

 

String

 

Javascript to run after the insertion.

 

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) runTemplateJS(source)

 

**Description:
 :** 

- 

Execute a block of JS returned from a template.
Call this AFTER adding the template HTML into the DOM so the nodes can be found.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 935](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

string

 

A block of javascript.

 

 

#### (inner) runTemplateJS(source)

 

**Description:
 :** 

- 

Execute a block of JS returned from a template.
Call this AFTER adding the template HTML into the DOM so the nodes can be found.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 1265](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

string

 

A block of javascript.
