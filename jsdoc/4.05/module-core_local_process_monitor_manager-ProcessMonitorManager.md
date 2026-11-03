# ProcessMonitorManager - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_local_process_monitor_manager-ProcessMonitorManager.html

# ProcessMonitorManager

 

## 
 [core/local/process_monitor/manager](module-core_local_process_monitor_manager.md)~

 
 ProcessMonitorManager

 

 

 

 

#### new ProcessMonitorManager()

 

**Description:
 :** 

- 

The reactive file uploader class.

As all the upload queues are reactive, any plugin can implement its own upload monitor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/manager.js](lib_amd_src_local_process_monitor_manager.js.md), [line 36](lib_amd_src_local_process_monitor_manager.js.md)

 

**Copyright:
 :** 

- 2021 Ferran Recio 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

 

 

### Members

 

#### (package) nextId :number

 

**Description:
 :** 

- 

The next process id to use.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/manager.js](lib_amd_src_local_process_monitor_manager.js.md), [line 55](lib_amd_src_local_process_monitor_manager.js.md)

 

**Default Value:
 :** 

- 1

The next process id to use.

##### Type:

- 

number

 

 

 

### Methods

 

#### generateProcessId() → {number}

 

**Description:
 :** 

- 

Generate a unique process id.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/manager.js](lib_amd_src_local_process_monitor_manager.js.md), [line 61](lib_amd_src_local_process_monitor_manager.js.md)

##### Returns:

a generated process Id

**
 Type

 :** 

number
