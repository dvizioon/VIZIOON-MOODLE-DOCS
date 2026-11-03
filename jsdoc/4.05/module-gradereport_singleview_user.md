# module:gradereport_singleview/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_singleview_user.html

# module:gradereport_singleview/user

 

## 

 module:gradereport_singleview/user

 

 

 

 

#### new (require("gradereport_singleview/user"))(baseUrl)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 34](grade_report_singleview_amd_src_user.js.md)

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
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 85](grade_report_singleview_amd_src_user.js.md)

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
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 46](grade_report_singleview_amd_src_user.js.md)

 

#### selectAllResultsLink() → {null}

 

**Description:
 :** 

- 

Stub out default required function unused here.

 

**Source:
 :** 

- 
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 62](grade_report_singleview_amd_src_user.js.md)

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
 [grade/report/singleview/amd/src/user.js](grade_report_singleview_amd_src_user.js.md), [line 72](grade_report_singleview_amd_src_user.js.md)

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
