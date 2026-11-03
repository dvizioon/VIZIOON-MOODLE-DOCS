# module:mod_quiz/modal_add_random_question - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_quiz_modal_add_random_question.html

# module:mod_quiz/modal_add_random_question

 

## 

 module:mod_quiz/modal_add_random_question

 

 

 

 

#### new (require("mod_quiz/modal_add_random_question"))(root)

 

**Description:
 :** 

- 

Constructor for the Modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 95](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root jQuery element for the modal

 

 

 

 

### Methods

 

#### (async) addQuestions(cmid, addonpage, randomcount, filtercondition, newcategory, parentcategory)

 

**Description:
 :** 

- 

Call web service function to add random questions

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 325](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

number

 

course module id

 
 `addonpage`

 

number

 

the page where random questions will be added to

 
 `randomcount`

 

number

 

Number of random questions

 
 `filtercondition`

 

string

 

Filter condition

 
 `newcategory`

 

string

 

add new category

 
 `parentcategory`

 

string

 

parent category of new category

 

 

#### (inner) getCMID() → {Number}

 

**Description:
 :** 

- 

Returns the course module id for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 176](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getCategory() → {string}

 

**Description:
 :** 

- 

Returns the saved category.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 136](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) getReturnUrl() → {string}

 

**Description:
 :** 

- 

Returns the return URL for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 156](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) loadForm() → {promise}

 

**Description:
 :** 

- 

Load the add random question form in a fragement and perform some transformation
on the HTML to convert it into tabs for rendering in the modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 236](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

Resolved with form HTML and JS.

**
 Type

 :** 

promise

 

#### (inner) moveCancelButtonToTabs(form)

 

**Description:
 :** 

- 

Make sure all of the tabs have a cancel button in their fotter to sit along
side the submit button.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 221](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

jquey

 

The form element.

 

 

#### (inner) moveContentIntoTab(tabContent, tabElement)

 

**Description:
 :** 

- 

Moves a given form element inside (a child of) a given tab element.

Hides the 'legend' (e.g. header) element of the form element because the
tab has the name.

Moves the submit button into a footer element at the bottom of the form
element for styling purposes.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 186](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tabContent`

 

jquery

 

The form element to move into the tab.

 
 `tabElement`

 

jquey

 

The tab element for the form element to move into.

 

 

#### (inner) moveTabsIntoTabContent(form)

 

**Description:
 :** 

- 

Empty the tab content container and move all tabs from the form into the
tab container element.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 207](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

jquery

 

The form element.

 

 

#### (inner) setAddOnPageId(id)

 

**Description:
 :** 

- 

Set the id of the page that the question should be added to
when the user clicks the add to quiz link.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 113](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

 

#### (inner) setCMID(id)

 

**Description:
 :** 

- 

Set the course module id for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 166](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

 

 

 

#### (inner) setCategory(category)

 

**Description:
 :** 

- 

Set the category for this form. The category is a comma separated
category id and category context id.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 125](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `category`

 

string

 

 

 

 

#### (inner) setReturnUrl(url)

 

**Description:
 :** 

- 

Set the return URL for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 146](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `url`

 

string

 

 

 

 

#### (inner) show()

 

**Description:
 :** 

- 

Override the modal show function to load the form when this modal is first
shown.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 357](mod_quiz_amd_src_modal_add_random_question.js.md)
