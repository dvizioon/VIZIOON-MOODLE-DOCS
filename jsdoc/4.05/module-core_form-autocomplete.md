# core/form-autocomplete - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_form-autocomplete.html

# core/form-autocomplete

 

 

 

**Description:
 :** 

- 

Autocomplete wrapper for select2 library.

 

**Source:
 :** 

- 
 [lib/amd/src/form-autocomplete.js](lib_amd_src_form-autocomplete.js.md), [line 16](lib_amd_src_form-autocomplete.js.md)

 

**Since:
 :** 

- 3.0

 

**Copyright:
 :** 

- 2015 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Autocomplete wrapper for select2 library.

 

 

 

 

### Members

 

#### (inner) KEYS :Object

 

**Description:
 :** 

- 

List of keycode constants.

 

**Source:
 :** 

- 
 [lib/amd/src/form-autocomplete.js](lib_amd_src_form-autocomplete.js.md), [line 46](lib_amd_src_form-autocomplete.js.md)

List of keycode constants.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) enhance() → {Promise}

 

**Description:
 :** 

- 

We need to use jQuery here as some calling code uses .done() and .fail() rather than native .then() and .catch()

 

**Source:
 :** 

- 
 [lib/amd/src/form-autocomplete.js](lib_amd_src_form-autocomplete.js.md), [line 1316](lib_amd_src_form-autocomplete.js.md)

##### Returns:

A jQuery promise

**
 Type

 :** 

Promise

 

#### (inner) enhanceField(selector, tags, ajax, placeholder, caseSensitive, showSuggestions, noSelectionString, closeSuggestionsOnSelect, templateOverrides) → {Promise}

 

**Description:
 :** 

- 

Turn a boring select box into an auto-complete beast.

 

**Source:
 :** 

- 
 [lib/amd/src/form-autocomplete.js](lib_amd_src_form-autocomplete.js.md), [line 1106](lib_amd_src_form-autocomplete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

string

 

The selector that identifies the select box.

 
 `tags`

 

boolean

 

Whether to allow support for tags (can define new entries).

 
 `ajax`

 

string

 

Name of an AMD module to handle ajax requests. If specified, the AMD
module must expose 2 functions "transport" and "processResults".
These are modeled on Select2 see: https://select2.github.io/options.html#ajax

 
 `placeholder`

 

String
|

Promise.<string>

 

The text to display before a selection is made.

 
 `caseSensitive`

 

Boolean

 

If search has to be made case sensitive.

 
 `showSuggestions`

 

Boolean

 

If suggestions should be shown

 
 `noSelectionString`

 

String
|

Promise.<string>

 

Text to display when there is no selection

 
 `closeSuggestionsOnSelect`

 

Boolean

 

Whether to close the suggestions immediately after making a selection.

 
 `templateOverrides`

 

Object

 

A set of templates to use instead of the standard templates

 

##### Returns:

**
 Type

 :** 

Promise
