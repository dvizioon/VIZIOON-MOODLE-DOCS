# tiny_aiplacement/textmark - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_textmark.html

# tiny_aiplacement/textmark

 

 

 

**Description:
 :** 

- 

Tiny AI Mark Changed text.

This module marks text that was returned by the AI service
and that has been changed by a human prior to being inserted.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/textmark.js](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md), [line 16](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md)

 

**Copyright:
 :** 

- 2023 Matt Porritt 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny AI Mark Changed text.

This module marks text that was returned by the AI service
and that has been changed by a human prior to being inserted.

 

 

 

 

### Methods

 

#### (static) findDifferences(originalText, editedText) → {Array.<Object>}

 

**Description:
 :** 

- 

Finds the differences between the original and edited text using the LCS algorithm.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/textmark.js](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md), [line 76](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `originalText`

 

string

 

The original text.

 
 `editedText`

 

string

 

The edited text.

 

##### Returns:

An array of difference objects with start, end, and text properties.

**
 Type

 :** 

Array.<Object>

 

#### (static) longestCommonSubsequence(a, b) → {string}

 

**Description:
 :** 

- 

Finds the longest common subsequence of two strings.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/textmark.js](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md), [line 35](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `a`

 

string

 

The first string.

 
 `b`

 

string

 

The second string.

 

##### Returns:

The longest common subsequence.

**
 Type

 :** 

string

 

#### (async, static) wrapEditedSections(originalText, editedText) → {Promise.<string>}

 

**Description:
 :** 

- 

Wraps the edited sections of the text in span tags with a 'user-edited' class.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/textmark.js](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md), [line 133](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `originalText`

 

string

 

The original text.

 
 `editedText`

 

string

 

The edited text.

 

##### Returns:

A promise that resolves with the edited text, where edited sections are wrapped in span tags.

**
 Type

 :** 

Promise.<string>

 

#### (async, static) wrapInSpan(editedSection) → {Promise.<string>}

 

**Description:
 :** 

- 

Wraps the given edited section in a span tag with a 'user-edited' class.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/textmark.js](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md), [line 115](lib_editor_tiny_plugins_aiplacement_amd_src_textmark.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editedSection`

 

string

 

The edited section of the text.

 

##### Returns:

A promise that resolves with the wrapped edited section.

**
 Type

 :** 

Promise.<string>
