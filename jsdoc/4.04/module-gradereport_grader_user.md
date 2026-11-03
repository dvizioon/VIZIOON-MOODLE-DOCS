# gradereport_grader/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-gradereport_grader_user.html

# gradereport_grader/user

 

 

 

**Description:
 :** 

- 

Allow the user to search for learners within the grader report.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 16](grade_report_grader_amd_src_user.js.md)

 

**Copyright:
 :** 

- 2023 Mathew May 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Allow the user to search for learners within the grader report.

 

 

 

 

### Methods

 

#### fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 50](grade_report_grader_amd_src_user.js.md)

##### Returns:

**
 Type

 :** 

Promise.<*>

 

#### selectAllResultsLink() → {string|*}

 

**Description:
 :** 

- 

Build up the view all link.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 59](grade_report_grader_amd_src_user.js.md)

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
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 72](grade_report_grader_amd_src_user.js.md)

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
