# tiny_aiplacement/commands - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_aiplacement_commands.html

# tiny_aiplacement/commands

 

 

 

**Description:
 :** 

- 

Commands helper for the Moodle tiny_aiplacement plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/commands.js](lib_editor_tiny_plugins_aiplacement_amd_src_commands.js.md), [line 16](lib_editor_tiny_plugins_aiplacement_amd_src_commands.js.md)

 

**Copyright:
 :** 

- 2024 Matt Porritt 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Commands helper for the Moodle tiny_aiplacement plugin.

 

 

 

 

### Members

 

#### (static, constant) getSetup

 

**Description:
 :** 

- 

Get the setup function for the buttons.

This is performed in an async function which ultimately returns the registration function as the
Tiny.AddOnManager.Add() function does not support async functions.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/aiplacement/amd/src/commands.js](lib_editor_tiny_plugins_aiplacement_amd_src_commands.js.md), [line 48](lib_editor_tiny_plugins_aiplacement_amd_src_commands.js.md)

Get the setup function for the buttons.

This is performed in an async function which ultimately returns the registration function as the
Tiny.AddOnManager.Add() function does not support async functions.
