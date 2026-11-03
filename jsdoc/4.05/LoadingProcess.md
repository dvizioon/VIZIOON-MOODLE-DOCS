# LoadingProcess - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/LoadingProcess.html

# LoadingProcess

 

## 

 LoadingProcess

 

 

 

 

#### new LoadingProcess()

 

**Description:
 :** 

- 

The process wrapper class.

This module is used to update a process in the process monitor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 16](lib_amd_src_local_process_monitor_loadingprocess.js.md)

 

**Copyright:
 :** 

- 2022 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

 

### Classes

 

**[LoadingProcess](LoadingProcess_LoadingProcess.md)
 :** 

 

 

 

### Members

 

#### data

 

**Description:
 :** 

- 

Return the process extra data.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 208](lib_amd_src_local_process_monitor_loadingprocess.js.md)

Return the process extra data.

 

#### id

 

**Description:
 :** 

- 

Return the process internal id

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 200](lib_amd_src_local_process_monitor_loadingprocess.js.md)

Return the process internal id

 

#### name

 

**Description:
 :** 

- 

Return the process name

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 192](lib_amd_src_local_process_monitor_loadingprocess.js.md)

Return the process name

 

 

### Methods

 

#### finish()

 

**Description:
 :** 

- 

Mark the process as finished.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 162](lib_amd_src_local_process_monitor_loadingprocess.js.md)

 

#### getData() → {Object}

 

**Description:
 :** 

- 

Returns the current rpocess data.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 184](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Returns:

the process data

**
 Type

 :** 

Object

 

#### onError(callback)

 

**Description:
 :** 

- 

Define a error process callback function.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 106](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `callback`

 

function

 

the callback function

 

 

#### onFinish(callback)

 

**Description:
 :** 

- 

Define a finished process callback function.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 90](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `callback`

 

function

 

the callback function

 

 

#### onRemove(callback)

 

**Description:
 :** 

- 

Define a removed from monitor process callback function.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 98](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `callback`

 

function

 

the callback function

 

 

#### remove()

 

**Description:
 :** 

- 

Remove the process from the monitor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 173](lib_amd_src_local_process_monitor_loadingprocess.js.md)

 

#### setError(error)

 

**Description:
 :** 

- 

Set the process error string.

Note: set the error message will mark the process as finished.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 138](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `error`

 

String

 

the string message

 

 

#### setExtraData(extraData)

 

**Description:
 :** 

- 

Stores extra information to the process.

This method is used to add information like the course, the user
or any other needed information.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 127](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `extraData`

 

Object

 

any extra process information to store

 

 

#### setName(name)

 

**Description:
 :** 

- 

Rename the process

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 154](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

String

 

the new process name

 

 

#### setPercentage(percentage)

 

**Description:
 :** 

- 

Set the process percentage.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 114](lib_amd_src_local_process_monitor_loadingprocess.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `percentage`

 

Number
