# core/emoji/auto_complete - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_emoji_auto_complete.html

# core/emoji/auto_complete

 

 

 

**Description:
 :** 

- 

Emoji auto complete.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 16](lib_amd_src_emoji_auto_complete.js.md)

 

**Copyright:
 :** 

- 2019 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Emoji auto complete.

 

 

 

 

### Methods

 

#### (inner) addRecentEmoji(unified, shortName)

 

**Description:
 :** 

- 

Add an emoji data to the set of recent emojis. The new set of recent emojis are
saved in local storage.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 56](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `unified`

 

String

 

The char chodes for the emoji

 
 `shortName`

 

String

 

The emoji short name

 

 

#### (inner) getActiveEmojiSuggestion(root) → {Element|null}

 

**Description:
 :** 

- 

Get the currently active emoji button element in the list of suggestions.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 185](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The emoji auto complete container element

 

##### Returns:

**
 Type

 :** 

Element
|

null

 

#### (inner) getEmojiTextFromShortName(shortName) → {String|null}

 

**Description:
 :** 

- 

Get the actual emoji string from the short name.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 76](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `shortName`

 

String

 

Emoji short name

 

##### Returns:

**
 Type

 :** 

String
|

null

 

#### (inner) getRecentEmojis() → {Array}

 

**Description:
 :** 

- 

Get the list of recent emojis data from local storage.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 44](lib_amd_src_emoji_auto_complete.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) getShortNameFromText(text) → {String}

 

**Description:
 :** 

- 

Remove the colon characters from the given text.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 177](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The text to process

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getWordFromPosition(text, position) → {String}

 

**Description:
 :** 

- 

Get the current word at the given position (index) within the text.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 136](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The text to process

 
 `position`

 

Number

 

The position (index) within the text to match the word

 

##### Returns:

**
 Type

 :** 

String

 

#### (inner) isCompleteShortName(text) → {Bool}

 

**Description:
 :** 

- 

Check if the given text is a full short name, i.e. has leading and trialing colon
characters.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 160](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The text to process

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (inner) isPartialShortName(text) → {Bool}

 

**Description:
 :** 

- 

Check if the given text is a partial short name, i.e. has a leading colon but no
trailing colon.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 169](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `text`

 

String

 

The text to process

 

##### Returns:

**
 Type

 :** 

Bool

 

#### (async, inner) render(root, shortNames)

 

**Description:
 :** 

- 

Render the auto complete list for the given short names.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 93](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The root container for the emoji auto complete

 
 `shortNames`

 

Array

 

The list of short names for emoji suggestions to show

 

 

#### (inner) searchEmojis(searchTerm, limit) → {Array}

 

**Description:
 :** 

- 

Get the list of emoji short names that include the given search term. If
the search term is an empty string then the list of recently used emojis
will be returned.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 118](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchTerm`

 

String

 

Text to match on

 
 `limit`

 

Number

 

Maximum number of results to return

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) selectEmojiElement(element, selectCallback)

 

**Description:
 :** 

- 

Trigger the select callback for the given emoji button element.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 227](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

The emoji button element

 
 `selectCallback`

 

function

 

The callback for when the user selects an emoji

 

 

#### (inner) selectNextEmojiSuggestion(root)

 

**Description:
 :** 

- 

Make the next sibling to the current active emoji active.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 210](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The emoji auto complete container element

 

 

#### (inner) selectPreviousEmojiSuggestion(root)

 

**Description:
 :** 

- 

Make the previous sibling of the current active emoji active.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 194](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The emoji auto complete container element
