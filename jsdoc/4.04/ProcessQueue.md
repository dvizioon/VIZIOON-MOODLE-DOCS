# ProcessQueue - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/ProcessQueue.html

# ProcessQueue

 

## 

 ProcessQueue

 

 

 

 

#### new ProcessQueue()

 

**Description:
 :** 

- 

A process queue manager.

Adding process to the queue will guarante process are executed in sequence.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 22](lib_amd_src_local_process_monitor_processqueue.js.md)

 

**Copyright:
 :** 

- 2022 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

 

### Classes

 

**[ProcessQueue](ProcessQueue_ProcessQueue.md)
 :** 

 

 

 

### Methods

 

#### (async) _continueProcessing()

 

**Description:
 :** 

- 

Continue the queue processing if no current process is defined.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 103](lib_amd_src_local_process_monitor_processqueue.js.md)

 

#### _currentProcessor() → {FileUploader}

 

**Description:
 :** 

- 

Return the current file uploader.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 96](lib_amd_src_local_process_monitor_processqueue.js.md)

##### Returns:

**
 Type

 :** 

FileUploader

 

#### _discardCurrent()

 

**Description:
 :** 

- 

Discard the current process and execute the next one if any.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 84](lib_amd_src_local_process_monitor_processqueue.js.md)

 

#### addError(processName, errorMessage)

 

**Description:
 :** 

- 

Adds a new pending upload to the queue.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 76](lib_amd_src_local_process_monitor_processqueue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `processName`

 

String

 

the file info

 
 `errorMessage`

 

String

 

the file processor

 

 

#### addPending(processName, processor)

 

**Description:
 :** 

- 

Adds a new pending upload to the queue.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 56](lib_amd_src_local_process_monitor_processqueue.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `processName`

 

String

 

the process name

 
 `processor`

 

function

 

the execution function
