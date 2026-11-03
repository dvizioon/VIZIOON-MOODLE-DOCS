# gradereport_grader/collapse - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_grader_collapse.html

# gradereport_grader/collapse

 

 

 

**Description:
 :** 

- 

Allow the user to show and hide columns of the report at will.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 16](grade_report_grader_amd_src_collapse.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to show and hide columns of the report at will.

 

 

 

 

### Methods

 

#### clickHandler(e)

 

**Description:
 :** 

- 

The handler for when a user interacts with the component.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 183](grade_report_grader_amd_src_collapse.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

The triggering event that we are working with.

 

 

#### componentSelector() → {string}

 

**Description:
 :** 

- 

The overall div that contains the searching widget.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 123](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### countUpdate()

 

**Description:
 :** 

- 

Update the visual count of collapsed columns or hide the count all together.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 478](grade_report_grader_amd_src_collapse.js.md)

 

#### (async) docClickHandler(e) → {Promise.<void>}

 

**Description:
 :** 

- 

Externally defined click function to improve memory handling.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 197](grade_report_grader_amd_src_collapse.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### dropdownSelector() → {string}

 

**Description:
 :** 

- 

The dropdown div that contains the searching widget result space.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 132](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### fetchCustomFieldValues() → {array.<string, *>}

 

**Description:
 :** 

- 

If we have any custom user profile fields, grab their system & readable names to add to our string map.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 548](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

An array of associated string arrays ready for our map.

**
 Type

 :** 

array.<string, *>

 

#### fetchDataset() → {string}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 155](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### fetchRequiredGradeStrings() → {Promise.<void>}

 

**Description:
 :** 

- 

Given the set of gradable items we can possibly search, fetch their strings,
so we can report to screen readers the field that matched.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 589](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### fetchRequiredUserStrings() → {Promise.<void>}

 

**Description:
 :** 

- 

Given the set of profile fields we can possibly search, fetch their strings,
so we can report to screen readers the field that matched.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 560](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### (async) filterDataset(filterableData) → {Array}

 

**Description:
 :** 

- 

Dictate to the search component how and what we want to match upon.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 366](grade_report_grader_amd_src_collapse.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filterableData`

 

Array

 

 

 

##### Returns:

An array of objects containing the system reference and the user readable value.

**
 Type

 :** 

Array

 

#### filterMatchDataset()

 

**Description:
 :** 

- 

Given we have a subset of the dataset, set the field that we matched upon to inform the end user.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 397](grade_report_grader_amd_src_collapse.js.md)

 

#### getDataset() → {Array}

 

**Description:
 :** 

- 

Return the dataset that we will be searching upon.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 141](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

Array

 

#### (async) prefcountpipe() → {Promise.<void>}

 

**Description:
 :** 

- 

Update the user preferences, count display then render the results.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 354](grade_report_grader_amd_src_collapse.js.md)

##### Returns:

**
 Type

 :** 

Promise.<void>

 

#### registerClickHandlers()

 

**Description:
 :** 

- 

Register clickable event listeners.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 171](grade_report_grader_amd_src_collapse.js.md)

 

#### registerFormEvents()

 

**Description:
 :** 

- 

Handle the form submission within the dropdown.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 263](grade_report_grader_amd_src_collapse.js.md)

 

#### registerInputEvents()

 

**Description:
 :** 

- 

Handle any keyboard inputs.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 234](grade_report_grader_amd_src_collapse.js.md)

 

#### (async) renderDefault()

 

**Description:
 :** 

- 

Build the content then replace the node by default we want our form to exist.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 492](grade_report_grader_amd_src_collapse.js.md)

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 520](grade_report_grader_amd_src_collapse.js.md)

 

#### selectallEnable()

 

**Description:
 :** 

- 

Given we render the dropdown, Determine if we want to enable the select all checkbox.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 537](grade_report_grader_amd_src_collapse.js.md)

 

#### setPreferences()

 

**Description:
 :** 

- 

Given a user performs an action, update the users' preferences.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 162](grade_report_grader_amd_src_collapse.js.md)

 

#### (async) updateDisplay(elements)

 

**Description:
 :** 

- 

With an array of nodes, switch their classes and values.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 414](grade_report_grader_amd_src_collapse.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elements`

 

Array

 

The elements to update.

 

 

#### (async) updateDisplayForElement(element)

 

**Description:
 :** 

- 

Update display for given element, switch its classes and values.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/collapse.js](grade_report_grader_amd_src_collapse.js.md), [line 428](grade_report_grader_amd_src_collapse.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The element to update.
