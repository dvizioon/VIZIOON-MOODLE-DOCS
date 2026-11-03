# mod_forum/local/grades/grader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_forum_local_grades_grader.html

# mod_forum/local/grades/grader

 

 

 

**Description:
 :** 

- 

This module will tie together all of the different calls the gradable module will make.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 16](mod_forum_amd_src_local_grades_grader.js.md)

 

**Copyright:
 :** 

- 2019 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module will tie together all of the different calls the gradable module will make.

 

 

 

 

### Members

 

#### (static, constant) launch

 

**Description:
 :** 

- 

Launch the grader interface with the specified parameters.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 399](mod_forum_amd_src_local_grades_grader.js.md)

Launch the grader interface with the specified parameters.

 

#### (static, constant) view

 

**Description:
 :** 

- 

Show the grade for a specific user.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 486](mod_forum_amd_src_local_grades_grader.js.md)

Show the grade for a specific user.

 

 

### Methods

 

#### (async, inner) displayGradingError(root, user, err)

 

**Description:
 :** 

- 

Display a grading error, typically from a failed save.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 371](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The container for the grader

 
 `user`

 

Object

 

The user who was errored

 
 `err`

 

Object

 

The details of the error

 

 

#### (inner) displayUserPicker(root, html)

 

**Description:
 :** 

- 

Helper function that replaces the user picker placeholder with what we get back from the user picker class.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 56](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

 

 
 `html`

 

String

 

 

 

 

#### (inner) fetchContentFromRender(html, js) → {array}

 

**Description:
 :** 

- 

To be removed, this is now done as a part of Templates.renderForPromise()

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 68](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `html`

 

String

 

 

 
 `js`

 

String

 

 

 

##### Returns:

An array containing the HTML, and JS.

**
 Type

 :** 

array

 

#### (inner) getSaveUserGradeFunction(root, setGradeForUser) → {function}

 

**Description:
 :** 

- 

Get the function used to save a user grade.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 339](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

The container for the grader

 
 `setGradeForUser`

 

function

 

The function that will be called.

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) getUpdateUserContentFunction(root, getContentForUser, getGradeForUser, saveGradeForUser) → {function}

 

**Description:
 :** 

- 

Here we build the function that is passed to the user picker that'll handle updating the user content area
of the grading interface.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 82](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

 

 
 `getContentForUser`

 

function

 

 

 
 `getGradeForUser`

 

function

 

 

 
 `saveGradeForUser`

 

function

 

 

 

##### Returns:

**
 Type

 :** 

function

 

#### (inner) hideSearchResultContainer(bodyContainer, userPickerContainer, searchResultsContainer)

 

**Description:
 :** 

- 

Hide the search results container and show the user picker and body content.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 142](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bodyContainer`

 

HTMLElement

 

The container element for the body content

 
 `userPickerContainer`

 

HTMLElement

 

The container element for the user picker

 
 `searchResultsContainer`

 

HTMLElement

 

The container element for the search results

 

 

#### (inner) hideUserSearchInput(toggleSearchButton, searchContainer, searchInput)

 

**Description:
 :** 

- 

Toggles the visibility of the user search.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 180](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleSearchButton`

 

HTMLElement

 

The button that toggles the search

 
 `searchContainer`

 

HTMLElement

 

The container element for the user search

 
 `searchInput`

 

HTMLElement

 

The input element for searching

 

 

#### (inner) registerEventListeners(graderLayout, userPicker, saveGradeFunction, userList)

 

**Description:
 :** 

- 

Add click handlers to the buttons in the header of the grading interface.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 237](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `graderLayout`

 

HTMLElement

 

 

 
 `userPicker`

 

Object

 

 

 
 `saveGradeFunction`

 

function

 

 

 
 `userList`

 

Array

 

List of users for the grader.

 

 

#### (async, inner) renderSearchResults(searchResultsContainer, users)

 

**Description:
 :** 

- 

Render the list of users in the search results area.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 224](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `searchResultsContainer`

 

HTMLElement

 

The container element for search results

 
 `users`

 

Array

 

The list of users to display

 

 

#### (inner) searchForUsers(userList, searchTerm) → {Array}

 

**Description:
 :** 

- 

Find the list of users who's names include the given search term.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 206](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userList`

 

Array

 

List of users for the grader

 
 `searchTerm`

 

String

 

The search term to match

 

##### Returns:

**
 Type

 :** 

Array

 

#### (inner) setContentContainerMargin(graderContainer, rightMargin)

 

**Description:
 :** 

- 

Adjusts the right margin of the content container.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 325](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `graderContainer`

 

HTMLElement

 

The container for the grader app.

 
 `rightMargin`

 

Number

 

The right margin value.

 

 

#### (inner) showSearchResultContainer(bodyContainer, userPickerContainer, searchResultsContainer)

 

**Description:
 :** 

- 

Show the search results container and hide the user picker and body content.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 129](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bodyContainer`

 

HTMLElement

 

The container element for the body content

 
 `userPickerContainer`

 

HTMLElement

 

The container element for the user picker

 
 `searchResultsContainer`

 

HTMLElement

 

The container element for the search results

 

 

#### (inner) showUserSearchInput(toggleSearchButton, searchContainer, searchInput)

 

**Description:
 :** 

- 

Toggles the visibility of the user search.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/grader.js](mod_forum_amd_src_local_grades_grader.js.md), [line 155](mod_forum_amd_src_local_grades_grader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleSearchButton`

 

HTMLElement

 

The button that toggles the search

 
 `searchContainer`

 

HTMLElement

 

The container element for the user search

 
 `searchInput`

 

HTMLElement

 

The input element for searching
