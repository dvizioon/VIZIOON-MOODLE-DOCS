# module:mod_assign/user - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-mod_assign_user.html

# module:mod_assign/user

 

## 

 module:mod_assign/user

 

 

 

 

#### new (require("mod_assign/user"))(baseUrl)

 

**Description:
 :** 

- 

Construct the class.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/user.js](mod_assign_amd_src_user.js.md), [line 44](mod_assign_amd_src_user.js.md)

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
 [mod/assign/amd/src/user.js](mod_assign_amd_src_user.js.md), [line 76](mod_assign_amd_src_user.js.md)

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
 [mod/assign/amd/src/user.js](mod_assign_amd_src_user.js.md), [line 64](mod_assign_amd_src_user.js.md)

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
 [mod/assign/amd/src/user.js](mod_assign_amd_src_user.js.md), [line 86](mod_assign_amd_src_user.js.md)

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
