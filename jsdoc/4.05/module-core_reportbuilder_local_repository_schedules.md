# core_reportbuilder/local/repository/schedules - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_reportbuilder_local_repository_schedules.html

# core_reportbuilder/local/repository/schedules

 

 

 

**Description:
 :** 

- 

Module to handle schedule AJAX requests

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/schedules.js](reportbuilder_amd_src_local_repository_schedules.js.md), [line 16](reportbuilder_amd_src_local_repository_schedules.js.md)

 

**Copyright:
 :** 

- 2021 Paul Holden 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Module to handle schedule AJAX requests

 

 

 

 

### Methods

 

#### (static) deleteSchedule(reportId, scheduleId) → {Promise}

 

**Description:
 :** 

- 

Delete schedule

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/schedules.js](reportbuilder_amd_src_local_repository_schedules.js.md), [line 34](reportbuilder_amd_src_local_repository_schedules.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reportId`

 

Number

 

 

 
 `scheduleId`

 

Number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) sendSchedule(reportId, scheduleId) → {Promise}

 

**Description:
 :** 

- 

Send schedule

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/schedules.js](reportbuilder_amd_src_local_repository_schedules.js.md), [line 51](reportbuilder_amd_src_local_repository_schedules.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reportId`

 

Number

 

 

 
 `scheduleId`

 

Number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### (static) toggleSchedule(reportId, scheduleId, scheduleEnabled) → {Promise}

 

**Description:
 :** 

- 

Toggle schedule enabled

 

**Source:
 :** 

- 
 [reportbuilder/amd/src/local/repository/schedules.js](reportbuilder_amd_src_local_repository_schedules.js.md), [line 69](reportbuilder_amd_src_local_repository_schedules.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reportId`

 

Number

 

 

 
 `scheduleId`

 

Number

 

 

 
 `scheduleEnabled`

 

Boolean

 

 

 

##### Returns:

**
 Type

 :** 

Promise
