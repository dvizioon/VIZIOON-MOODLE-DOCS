# mod_quiz/modal_add_random_question - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_quiz_modal_add_random_question.html

# mod_quiz/modal_add_random_question

 

 

 

**Description:
 :** 

- 

Contain the logic for the add random question modal.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 16](mod_quiz_amd_src_modal_add_random_question.js.md)

 

**Copyright:
 :** 

- 2018 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for the add random question modal.

 

 

 

 

### Methods

 

#### (inner) getAddOnPageId() → {int}

 

**Description:
 :** 

- 

Returns the saved page id for the question to be added to.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 110](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getCMID() → {int}

 

**Description:
 :** 

- 

Returns the course module id for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 171](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getCategory() → {string}

 

**Description:
 :** 

- 

Returns the saved category.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 131](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### (inner) getContextId() → {int}

 

**Description:
 :** 

- 

Retrieve the saved Moodle context id.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 88](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### (inner) getReturnUrl() → {string}

 

**Description:
 :** 

- 

Returns the return URL for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 151](mod_quiz_amd_src_modal_add_random_question.js.md)

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 239](mod_quiz_amd_src_modal_add_random_question.js.md)

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 224](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `form`

 

jquey

 

The form element.

 

 

#### (inner) moveFormElementIntoTab(formElement, tabElement)

 

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 181](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formElement`

 

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 210](mod_quiz_amd_src_modal_add_random_question.js.md)

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 98](mod_quiz_amd_src_modal_add_random_question.js.md)

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 161](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

 

#### (inner) setCategory(category)

 

**Description:
 :** 

- 

Set the category for this form. The category is a comma separated
category id and category context id.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 120](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `category`

 

string

 

 

 

 

#### (inner) setContextId(id)

 

**Description:
 :** 

- 

Save the Moodle context id that the question bank is being
rendered in.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 77](mod_quiz_amd_src_modal_add_random_question.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

 

#### (inner) setReturnUrl(url)

 

**Description:
 :** 

- 

Set the return URL for the form.

 

**Source:
 :** 

- 
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 141](mod_quiz_amd_src_modal_add_random_question.js.md)

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
 [mod/quiz/amd/src/modal_add_random_question.js](mod_quiz_amd_src_modal_add_random_question.js.md), [line 283](mod_quiz_amd_src_modal_add_random_question.js.md)
