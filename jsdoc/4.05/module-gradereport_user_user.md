# module:gradereport_user/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_user_user.html

# module:gradereport_user/user

 

## 

 module:gradereport_user/user

 

 

 

 

#### new (require("gradereport_user/user"))(baseUrl)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 34](grade_report_user_amd_src_user.js.md)

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
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 90](grade_report_user_amd_src_user.js.md)

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
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 46](grade_report_user_amd_src_user.js.md)

 

#### selectAllResultsLink() → {string|*}

 

**Description:
 :** 

- 

Build up the view all link.

 

**Source:
 :** 

- 
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 65](grade_report_user_amd_src_user.js.md)

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
 [grade/report/user/amd/src/user.js](grade_report_user_amd_src_user.js.md), [line 78](grade_report_user_amd_src_user.js.md)

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
