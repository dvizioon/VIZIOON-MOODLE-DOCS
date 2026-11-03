# gradereport_user/gradecategorytoggle - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-gradereport_user_gradecategorytoggle.html

# gradereport_user/gradecategorytoggle

 

 

 

**Description:
 :** 

- 

Javascript module for toggling the visibility of the grade categories in the user report.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/gradecategorytoggle.js](grade_report_user_amd_src_gradecategorytoggle.js.md), [line 16](grade_report_user_amd_src_gradecategorytoggle.js.md)

 

**Copyright:
 :** 

- 2022 Mihail Geshoski 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript module for toggling the visibility of the grade categories in the user report.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Init method.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/gradecategorytoggle.js](grade_report_user_amd_src_gradecategorytoggle.js.md), [line 135](grade_report_user_amd_src_gradecategorytoggle.js.md)

Init method.

 

 

### Methods

 

#### (inner) registerListenerEvents(userReportId)

 

**Description:
 :** 

- 

Register related event listeners.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/gradecategorytoggle.js](grade_report_user_amd_src_gradecategorytoggle.js.md), [line 29](grade_report_user_amd_src_gradecategorytoggle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userReportId`

 

string

 

The ID of the user report container element.

 

 

#### (inner) toggleCategory(toggleElement)

 

**Description:
 :** 

- 

Method that handles the category toggle action.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/gradecategorytoggle.js](grade_report_user_amd_src_gradecategorytoggle.js.md), [line 49](grade_report_user_amd_src_gradecategorytoggle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleElement`

 

object

 

The category toggle node that was clicked.

 

 

#### (inner) updateParentCategoryRowspans(toggleElement, num)

 

**Description:
 :** 

- 

Method that updates the rowspan value of all 'parent' category rows of a given category node.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/gradecategorytoggle.js](grade_report_user_amd_src_gradecategorytoggle.js.md), [line 96](grade_report_user_amd_src_gradecategorytoggle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `toggleElement`

 

object

 

The category toggle node that was clicked.

 
 `num`

 

int

 

The number we want to add or subtract from the rowspan value of the 'parent' category row elements.
