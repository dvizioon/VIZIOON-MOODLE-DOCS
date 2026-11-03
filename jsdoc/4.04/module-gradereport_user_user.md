# gradereport_user/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-gradereport_user_user.html

# gradereport_user/user

 

 

 

**Description:
 :** 

- 

Allow the user to search for learners within the user report.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 16](grade_report_user_amd_src_user.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for learners within the user report.

 

 

 

 

### Methods

 

#### fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 87](grade_report_user_amd_src_user.js.md)

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
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 41](grade_report_user_amd_src_user.js.md)

 

#### selectAllResultsLink() → {string|*}

 

**Description:
 :** 

- 

Build up the view all link.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 60](grade_report_user_amd_src_user.js.md)

##### Returns:

**
 Type

 :** 

string
|

*

 

#### selectOneLink(userID) → {string|*}

 

**Description:
 :** 

- 

Build up the link that is dedicated to a particular result.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 74](grade_report_user_amd_src_user.js.md)

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
