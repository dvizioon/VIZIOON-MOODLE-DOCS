# gradereport_singleview/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-gradereport_singleview_user.html

# gradereport_singleview/user

 

 

 

**Description:
 :** 

- 

Allow the user to search for learners within the singleview report.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 16](grade_report_singleview_amd_src_user.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for learners within the singleview report.

 

 

 

 

### Methods

 

#### fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 81](grade_report_singleview_amd_src_user.js.md)

##### Returns:

**
 Type

 :** 

Promise.<*>

 

#### (async) renderDropdown()

 

**Description:
 :** 

- 

Build the content then replace the node.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 41](grade_report_singleview_amd_src_user.js.md)

 

#### selectAllResultsLink() → {null}

 

**Description:
 :** 

- 

Stub out default required function unused here.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 57](grade_report_singleview_amd_src_user.js.md)

##### Returns:

**
 Type

 :** 

null

 

#### selectOneLink(userID) → {string|*}

 

**Description:
 :** 

- 

Build up the view all link that is dedicated to a particular result.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 67](grade_report_singleview_amd_src_user.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userID`

 

Number

 

The ID of the user selected.

 

##### Returns:

**
 Type

 :** 

string
|

*
