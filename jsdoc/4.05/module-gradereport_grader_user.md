# module:gradereport_grader/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_grader_user.html

# module:gradereport_grader/user

 

## 

 module:gradereport_grader/user

 

 

 

 

#### new (require("gradereport_grader/user"))(baseUrl)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 40](grade_report_grader_amd_src_user.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `baseUrl`

 

string

 

The base URL for the page.

 

 

 

 

### Methods

 

#### fetchDataset() → {Promise.<*>}

 

**Description:
 :** 

- 

Get the data we will be searching against in this component.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 54](grade_report_grader_amd_src_user.js.md)

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
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 63](grade_report_grader_amd_src_user.js.md)

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
 [grade/report/grader/amd/src/user.js](grade_report_grader_amd_src_user.js.md), [line 75](grade_report_grader_amd_src_user.js.md)

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
