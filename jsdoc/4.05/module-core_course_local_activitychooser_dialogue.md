# core_course/local/activitychooser/dialogue - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_course_local_activitychooser_dialogue.html

# core_course/local/activitychooser/dialogue

 

 

 

**Description:
 :** 

- 

A type of dialogue used as for choosing options.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 16](course_amd_src_local_activitychooser_dialogue.js.md)

 

**Copyright:
 :** 

- 2019 Mihail Geshoski 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A type of dialogue used as for choosing options.

 

 

 

 

### Methods

 

#### (inner) disableFocusAllChooserOptions(sectionChooserOptions)

 

**Description:
 :** 

- 

Disable the focus of all chooser options in a specific container (section).

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 479](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionChooserOptions`

 

HTMLElement

 

The section that contains the chooser items

 

 

#### (inner) displayChooser(modalPromise, sectionModules, partialFavourite, footerData)

 

**Description:
 :** 

- 

Display the module chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 492](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalPromise`

 

Promise

 

Our created modal for the section

 
 `sectionModules`

 

Array

 

An array of all of the built module information

 
 `partialFavourite`

 

function

 

Partially applied function we need to manage favourite status

 
 `footerData`

 

Object

 

Our base footer object.

 

 

#### (inner) focusChooserOption(currentChooserOption, previousChooserOption)

 

**Description:
 :** 

- 

Focus on a chooser option element and remove the previous chooser element from the focus order

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 322](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentChooserOption`

 

HTMLElement

 

The current chooser option element that we want to focus

 
 `previousChooserOption`

 

HTMLElement
|

null

 

The previous focused option element

 

 

#### (inner) initChooserOptionsKeyboardNavigation(body, mappedModules, chooserOptionsContainer, modal)

 

**Description:
 :** 

- 

Initialise the keyboard navigation controls for the chooser options.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 237](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `body`

 

HTMLElement

 

Our modal that we are working with

 
 `mappedModules`

 

Map

 

A map of all of the modules we are working with with K: mod_name V: {Object}

 
 `chooserOptionsContainer`

 

HTMLElement

 

The section that contains the chooser items

 
 `modal`

 

Object

 

Our created modal for the section

 

 

#### (inner) manageFavouriteState(modalBody, caller, partialFavourite)

 

**Description:
 :** 

- 

Given a user wants to change the favourite state of a module we either add or remove the status.
We also propergate this change across our map of modals.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 82](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalBody`

 

HTMLElement

 

The DOM node of the modal to manipulate

 
 `caller`

 

HTMLElement

 

 

 
 `partialFavourite`

 

function

 

Partially applied function we need to manage favourite status

 

 

#### (inner) registerListenerEvents(modal, mappedModules, partialFavourite, footerData)

 

**Description:
 :** 

- 

Register chooser related event listeners.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 109](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Promise

 

Our modal that we are working with

 
 `mappedModules`

 

Map

 

A map of all of the modules we are working with with K: mod_name V: {Object}

 
 `partialFavourite`

 

function

 

Partially applied function we need to manage favourite status

 
 `footerData`

 

Object

 

Our base footer object.

 

 

#### (inner) renderSearchResults(searchResultsContainer, searchResultsData)

 

**Description:
 :** 

- 

Render the search results in a defined container

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 365](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchResultsContainer`

 

HTMLElement

 

The container where the data should be rendered

 
 `searchResultsData`

 

Object

 

Data containing the module items that satisfy the search criteria

 

 

#### (inner) searchModules(modules, searchTerm) → {Array}

 

**Description:
 :** 

- 

Return the list of modules which have a name or description that matches the given search term.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 423](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modules`

 

Array

 

List of available modules

 
 `searchTerm`

 

String

 

The search term to match

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) setupKeyboardAccessibility(modal, mappedModules)

 

**Description:
 :** 

- 

Set up our tabindex information across the chooser.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 448](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Promise

 

Our created modal for the section

 
 `mappedModules`

 

Map

 

A map of all of the built module information

 

 

#### (inner) showModuleHelp(carousel, moduleData, modal)

 

**Description:
 :** 

- 

Given an event from the main module 'page' navigate to it's help section via a carousel.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 36](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `carousel`

 

jQuery

 

Our initialized carousel to manipulate

 
 `moduleData`

 

Object

 

Data of the module to carousel to

 
 `modal`

 

jQuery

 

We need to figure out if the current modal has a footer.

 

 

#### (inner) toggleFocusableChooserOption(chooserOption, isFocusable)

 

**Description:
 :** 

- 

Add or remove a chooser option from the focus order.

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 338](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `chooserOption`

 

HTMLElement

 

The chooser option element which should be added or removed from the focus order

 
 `isFocusable`

 

Boolean

 

Whether the chooser element is focusable or not

 

 

#### (inner) toggleSearchResultsView(modal, mappedModules, searchQuery)

 

**Description:
 :** 

- 

Toggle (display/hide) the search results depending on the value of the search query

 

**Source:
 :** 

- 
 [course/amd/src/local/activitychooser/dialogue.js](course_amd_src_local_activitychooser_dialogue.js.md), [line 382](course_amd_src_local_activitychooser_dialogue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Object

 

Our created modal for the section

 
 `mappedModules`

 

Map

 

A map of all of the modules we are working with with K: mod_name V: {Object}

 
 `searchQuery`

 

String

 

The search query
