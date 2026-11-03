# tiny_aiplacement/loading - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_loading.html

# tiny_aiplacement/loading

 

 

 

**Description:
 :** 

- 

Tiny AI loading screen handling.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/loading.js](lib_editor_tiny_plugins_aiplacement_amd_src_loading.js.md), [line 16](lib_editor_tiny_plugins_aiplacement_amd_src_loading.js.md)

 

**Copyright:
 :** 

- 2024 Matt Porritt 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Tiny AI loading screen handling.

 

 

 

 

### Methods

 

#### (static) loadingMessages(element, delay) → {Promise.<function(): void>}

 

**Description:
 :** 

- 

Display a series of messages one by one with a specified delay between each message.

Returns a promise that resolves when the final message is displayed.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/loading.js](lib_editor_tiny_plugins_aiplacement_amd_src_loading.js.md), [line 57](lib_editor_tiny_plugins_aiplacement_amd_src_loading.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

The element to display the messages in.

 
 `delay`

 

number

 

The delay between each message in milliseconds.

 

##### Returns:

A function to stop the message cycling.

**
 Type

 :** 

Promise.<function(): void>
