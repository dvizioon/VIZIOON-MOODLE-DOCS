# core/templates - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_templates.html

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

 

 

 

 

### Methods

 

#### (inner) appendNodeContents(element, html, js) → {Array}

 

**Description:
 :** 

- 

Append some HTML to a node and trigger events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 277](lib_amd_src_templates.js.md)

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

 

#### (inner) domAppend(element, html, js) → {Array}

 

**Description:
 :** 

- 

Append some HTML to a node and trigger events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 126](lib_amd_src_templates.js.md)

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

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) domPrepend(element, html, js) → {Array}

 

**Description:
 :** 

- 

Prepend some HTML to a node and trigger events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 99](lib_amd_src_templates.js.md)

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

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) domReplace(element, newHTML, newJS, replaceChildNodes) → {Array}

 

**Description:
 :** 

- 

Do some DOM replacement and trigger correct events and fire javascript.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 56](lib_amd_src_templates.js.md)

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

 
 `replaceChildNodes`

 

Boolean

 

Replace only the childnodes, alternative is to replace the entire node.

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

##### Returns:

The list of new DOM Nodes

**
 Type

 :** 

Array

 

#### (inner) getTemplate(templateNames, themeNameopt) → {Promise}

 

**Description:
 :** 

- 

Prefetch a set of templates without rendering them.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 182](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `templateNames`

 

Array

 

 

 

 

 

The list of templates to fetch

 
 `themeName`

 

String

 

 

 <optional>  

 

 

 `config.themeName`

 

The name of the theme to use

 

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 266](lib_amd_src_templates.js.md)

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

 

#### (inner) render(templateName, context, themeName) → {Promise}

 

**Description:
 :** 

- 

Every call to render creates a new instance of the class and calls render on it. This
means each render call has it's own class variables.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 158](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateName`

 

string

 

should consist of the component and the name of the template like this:
core/menu (lib/templates/menu.mustache) or
tool_bananas/yellow (admin/tool/bananas/templates/yellow.mustache)

 
 `context`

 

Object

 

Could be array, string or simple value for the context of the template.

 
 `themeName`

 

string

 

Name of the current theme.

 

##### Returns:

JQuery promise object resolved when the template has been rendered.

**
 Type

 :** 

Promise

 

#### (inner) renderForPromise(templateName, context, themeName) → {Promise}

 

**Description:
 :** 

- 

Every call to render creates a new instance of the class and calls render on it. This
means each render call has it's own class variables.

This alernate to the standard .render() function returns the html and js in a single object suitable for a
native Promise.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 196](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateName`

 

string

 

should consist of the component and the name of the template like this:
core/menu (lib/templates/menu.mustache) or
tool_bananas/yellow (admin/tool/bananas/templates/yellow.mustache)

 
 `context`

 

Object

 

Could be array, string or simple value for the context of the template.

 
 `themeName`

 

string

 

Name of the current theme.

 

##### Returns:

JQuery promise object resolved when the template has been rendered.

**
 Type

 :** 

Promise

 

#### (inner) renderPix(key, component, title) → {Promise}

 

**Description:
 :** 

- 

Every call to renderIcon creates a new instance of the class and calls renderIcon on it. This
means each render call has it's own class variables.

 

**Source:
 :** 

- 
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 216](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 255](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 244](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 32](lib_amd_src_templates.js.md)

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
 [lib/amd/src/templates.js](lib_amd_src_templates.js.md), [line 235](lib_amd_src_templates.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

string

 

A block of javascript.
