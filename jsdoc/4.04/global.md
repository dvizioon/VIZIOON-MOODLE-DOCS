# Global - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/global.html

# Global

 

## 

 

 

 

 

 

 

 

 

 

### Members

 

#### StorageWrapper :Object

 

**Description:
 :** 

- 

Wraps browsers localStorage object

 

**Source:
 :** 

- 
 [lib/amd/src/localstorage.js](lib_amd_src_localstorage.js.md), [line 28](lib_amd_src_localstorage.js.md)

Wraps browsers localStorage object

##### Type:

- 

Object

 

 

#### The :string

 

**Description:
 :** 

- 

placeholder character used for standard strings (unclean)

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 27](lib_amd_src_local_templates_renderer.js.md)

placeholder character used for standard strings (unclean)

##### Type:

- 

string

 

 

#### The :string

 

**Description:
 :** 

- 

placeholder character used for cleaned strings

 

**Source:
 :** 

- 
 [lib/amd/src/local/templates/renderer.js](lib_amd_src_local_templates_renderer.js.md), [line 30](lib_amd_src_local_templates_renderer.js.md)

placeholder character used for cleaned strings

##### Type:

- 

string

 

 

#### (constant) addContextmenuItem

 

**Description:
 :** 

- 

Given a TinyMCE contextmenu configuration, add the specified button to the end.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 201](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE contextmenu configuration, add the specified button to the end.

 

#### (constant) addMenubarItem

 

**Description:
 :** 

- 

Given a TinyMCE Menubar configuration, add the specified button to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 165](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Menubar configuration, add the specified button to the named section.

 

#### (constant) addQuickbarsToolbarItem

 

**Description:
 :** 

- 

Given a TinyMCE quickbars configuration, add items to the menu.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 217](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE quickbars configuration, add items to the menu.

 

#### (constant) addToolbarButton

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, add the specified button to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 65](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, add the specified button to the named section.

 

#### (constant) addToolbarButtons

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, add the specified buttons to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 100](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, add the specified buttons to the named section.

 

#### (constant) addToolbarSection

 

**Description:
 :** 

- 

Insert a new section into the toolbar.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 127](lib_editor_tiny_amd_src_utils.js.md)

Insert a new section into the toolbar.

 

#### (constant) byCategory

 

**Description:
 :** 

- 

Emoji data based on the data available from https://github.com/iamcal/emoji-data.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/data.js](lib_amd_src_emoji_data.js.md), [line 23](lib_amd_src_emoji_data.js.md)

 

**Copyright:
 :** 

- 2019 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

Emoji data based on the data available from https://github.com/iamcal/emoji-data.

 

#### (constant) clearSearch

 

**Description:
 :** 

- 

Reset the search icon and trigger the init for the block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 822](blocks_myoverview_amd_src_view.js.md)

Reset the search icon and trigger the init for the block.

 

#### current :[LoadingProcess](LoadingProcess.md)

 

**Description:
 :** 

- 

the current uploading process.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 36](lib_amd_src_local_process_monitor_processqueue.js.md)

the current uploading process.

##### Type:

- 

[LoadingProcess](LoadingProcess.md)

 

 

#### (constant) displayFilepicker

 

**Description:
 :** 

- 

Helper to display a filepicker and return a Promise.

The Promise will resolve when a file is selected, or reject if the file type is not found.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 42](lib_editor_tiny_amd_src_utils.js.md)

Helper to display a filepicker and return a Promise.

The Promise will resolve when a file is selected, or reject if the file type is not found.

 

#### editorUpdates :Map

 

**Description:
 :** 

- 

the courses pending to be updated.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 31](lib_amd_src_local_process_monitor_loadingprocess.js.md)

the courses pending to be updated.

##### Type:

- 

Map

 

 

#### endTime

 

**Description:
 :** 

- 

Timestamp at which time runs out.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 31](mod_assign_amd_src_timer.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `endTime`

 

Number

 

 

 

Timestamp at which time runs out.

 

#### (constant) ensureEditorIsValid

 

**Description:
 :** 

- 

Ensure that the editor is still in the DOM, removing it if it is not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 259](lib_editor_tiny_amd_src_utils.js.md)

Ensure that the editor is still in the DOM, removing it if it is not.

 

#### errorCallback :function

 

**Description:
 :** 

- 

the error callback if any.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 46](lib_amd_src_local_process_monitor_loadingprocess.js.md)

the error callback if any.

##### Type:

- 

function

 

 

#### extraData :Object

 

**Description:
 :** 

- 

any extra process information to store.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 34](lib_amd_src_local_process_monitor_loadingprocess.js.md)

any extra process information to store.

##### Type:

- 

Object

 

 

#### finishedCallback :function

 

**Description:
 :** 

- 

the finished callback if any.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 40](lib_amd_src_local_process_monitor_loadingprocess.js.md)

the finished callback if any.

##### Type:

- 

function

 

 

#### (constant) getDocumentationLink

 

**Description:
 :** 

- 

Get the link to the user documentation for the named plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 232](lib_editor_tiny_amd_src_utils.js.md)

Get the link to the user documentation for the named plugin.

 

#### (constant) getImagePath

 

**Description:
 :** 

- 

Get the image path for the specified image.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 27](lib_editor_tiny_amd_src_utils.js.md)

Get the image path for the specified image.

 

#### (constant) getPluginMetadata

 

**Description:
 :** 

- 

Get the default plugin metadata for the named plugin.
If no URL is provided, then a URL is generated pointing to the standard Moodle Documentation.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 243](lib_editor_tiny_amd_src_utils.js.md)

Get the default plugin metadata for the named plugin.
If no URL is provided, then a URL is generated pointing to the standard Moodle Documentation.

 

#### (constant) init

 

**Description:
 :** 

- 

Initialise the timeline view navigation by adding event listeners to
the navigation elements.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 179](blocks_timeline_amd_src_view_nav.js.md)

Initialise the timeline view navigation by adding event listeners to
the navigation elements.

 

#### (constant) init

 

**Description:
 :** 

- 

Initialise the timeline view navigation by adding event listeners to
the navigation elements.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 131](blocks_myoverview_amd_src_view_nav.js.md)

Initialise the timeline view navigation by adding event listeners to
the navigation elements.

 

#### (constant) init

 

**Description:
 :** 

- 

Intialise the courses list and cards views on page load.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 841](blocks_myoverview_amd_src_view.js.md)

Intialise the courses list and cards views on page load.

 

#### (constant) init

 

**Description:
 :** 

- 

Initialise all of the modules for the overview block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/main.js](blocks_myoverview_amd_src_main.js.md), [line 31](blocks_myoverview_amd_src_main.js.md)

Initialise all of the modules for the overview block.

 

#### isEditing

 

**Description:
 :** 

- 

Return the current edit mode.

Components should use this method to check if edit mode is active.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 245](course_format_amd_src_local_courseeditor_courseeditor.js.md)

Return the current edit mode.

Components should use this method to check if edit mode is active.

 

#### isLoggerSet :boolean

 

**Description:
 :** 

- 

Flag to determine whether the screen reader-only logger has already been set, so we only need to set it once.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 26](course_format_amd_src_local_courseeditor_mutations.js.md)

Flag to determine whether the screen reader-only logger has already been set, so we only need to set it once.

##### Type:

- 

boolean

 

 

#### locked

 

**Description:
 :** 

- 

Set the lock value and locks or unlocks the element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 441](lib_amd_src_local_reactive_basecomponent.js.md)

Set the lock value and locks or unlocks the element.

 

#### locked

 

**Description:
 :** 

- 

Get the current locked value from the element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 450](lib_amd_src_local_reactive_basecomponent.js.md)

Get the current locked value from the element.

 

#### manager :ProcessMonitorManager

 

**Description:
 :** 

- 

the page monitor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 37](lib_amd_src_local_process_monitor_loadingprocess.js.md)

the page monitor.

##### Type:

- 

ProcessMonitorManager

 

 

#### pending :Array

 

**Description:
 :** 

- 

the pending queue.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/processqueue.js](lib_amd_src_local_process_monitor_processqueue.js.md), [line 33](lib_amd_src_local_process_monitor_processqueue.js.md)

the pending queue.

##### Type:

- 

Array

 

 

#### prepare

 

**Description:
 :** 

- 

Prepares to begin a drag operation - call with a mousedown or touchstart event.

If the returned object has 'start' true, then you can set up a drag proxy, and call
start. This function will call preventDefault automatically regardless of whether
starting or not.

 

**Source:
 :** 

- 
 [lib/amd/src/dragdrop.js](lib_amd_src_dragdrop.js.md), [line 312](lib_amd_src_dragdrop.js.md)

Prepares to begin a drag operation - call with a mousedown or touchstart event.

If the returned object has 'start' true, then you can set up a drag proxy, and call
start. This function will call preventDefault automatically regardless of whether
starting or not.

 

#### (constant) removeMenubarItem

 

**Description:
 :** 

- 

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 370](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

#### (constant) removeMenubarItems

 

**Description:
 :** 

- 

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 385](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

#### (constant) removeSubmenuItem

 

**Description:
 :** 

- 

Remove the specified sub-menu item from the named section.
Recreate a menu with the same sub-menu items but remove the specified item.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 332](lib_editor_tiny_amd_src_utils.js.md)

Remove the specified sub-menu item from the named section.
Recreate a menu with the same sub-menu items but remove the specified item.

 

#### (constant) removeToolbarButton

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, remove the specified button from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 280](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, remove the specified button from the named section.

 

#### (constant) removeToolbarButtons

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, remove the specified buttons from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 306](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, remove the specified buttons from the named section.

 

#### removedCallback :function

 

**Description:
 :** 

- 

the removed callback if any.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/loadingprocess.js](lib_amd_src_local_process_monitor_loadingprocess.js.md), [line 43](lib_amd_src_local_process_monitor_loadingprocess.js.md)

the removed callback if any.

##### Type:

- 

function

 

 

#### (constant) reset

 

**Description:
 :** 

- 

Reset the courses views to their original
state on first page load.courseOffset

This is called when configuration has changed for the event lists
to cause them to reload their data.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 866](blocks_myoverview_amd_src_view.js.md)

Reset the courses views to their original
state on first page load.courseOffset

This is called when configuration has changed for the event lists
to cause them to reload their data.

 

#### (constant) serialize

 

**Description:
 :** 

- 

Serialize form values into a string.

This must be used instead of URLSearchParams, which does not correctly encode nested values such as arrays.

 

**Source:
 :** 

- 
 [lib/form/amd/src/util.js](lib_form_amd_src_util.js.md), [line 25](lib_form_amd_src_util.js.md)

Serialize form values into a string.

This must be used instead of URLSearchParams, which does not correctly encode nested values such as arrays.

 

#### start

 

**Description:
 :** 

- 

Call to start a drag operation, in response to a mouse down or touch start event.
Normally call this after calling prepare and receiving start true (you can probably
skip prepare if only supporting drag not touch).

Note: The caller is responsible for creating a 'drag proxy' which is the
thing that actually gets dragged. At present, this doesn't really work
properly unless it is added directly within the body tag.

You also need to ensure that there is CSS so the proxy is absolutely positioned,
and styled to look like it is floating.

You also need to absolutely position the proxy where you want it to start.

 

**Source:
 :** 

- 
 [lib/amd/src/dragdrop.js](lib_amd_src_dragdrop.js.md), [line 333](lib_amd_src_dragdrop.js.md)

Call to start a drag operation, in response to a mouse down or touch start event.
Normally call this after calling prepare and receiving start true (you can probably
skip prepare if only supporting drag not touch).

Note: The caller is responsible for creating a 'drag proxy' which is the
thing that actually gets dragged. At present, this doesn't really work
properly unless it is added directly within the body tag.

You also need to ensure that there is CSS so the proxy is absolutely positioned,
and styled to look like it is floating.

You also need to absolutely position the proxy where you want it to start.

 

#### start

 

**Description:
 :** 

- 

Starts automatic scrolling if user moves near edge of window.
This should be called in response to mouse down or touch start.

 

**Source:
 :** 

- 
 [lib/amd/src/autoscroll.js](lib_amd_src_autoscroll.js.md), [line 197](lib_amd_src_autoscroll.js.md)

Starts automatic scrolling if user moves near edge of window.
This should be called in response to mouse down or touch start.

 

#### state

 

**Description:
 :** 

- 

Return the current state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 190](lib_amd_src_local_reactive_reactive.js.md)

Return the current state.

 

#### stop

 

**Description:
 :** 

- 

Stops automatic scrolling. This should be called in response to mouse up or touch end.

 

**Source:
 :** 

- 
 [lib/amd/src/autoscroll.js](lib_amd_src_autoscroll.js.md), [line 204](lib_amd_src_autoscroll.js.md)

Stops automatic scrolling. This should be called in response to mouse up or touch end.

 

#### summaryDisplayLoaded :boolean

 

**Description:
 :** 

- 

Whether the summary display has been loaded.

If true, this means that courses have been loaded with the summary text.
Otherwise, switching to the summary display mode will require course data to be fetched with the summary text.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 74](blocks_myoverview_amd_src_view.js.md)

Whether the summary display has been loaded.

If true, this means that courses have been loaded with the summary text.
Otherwise, switching to the summary display mode will require course data to be fetched with the summary text.

##### Type:

- 

boolean

 

 

#### supportComponents

 

**Description:
 :** 

- 

Return if the current course support components to refresh the content.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 263](course_format_amd_src_local_courseeditor_courseeditor.js.md)

Return if the current course support components to refresh the content.

 

#### timeoutId

 

**Description:
 :** 

- 

ID of the timeout that updates the clock.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 38](mod_assign_amd_src_timer.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `timeoutId`

 

Number

 

 

 

ID of the timeout that updates the clock.

 

#### timer

 

**Description:
 :** 

- 

The timer element.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 45](mod_assign_amd_src_timer.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `timer`

 

Element

 

 

 

The timer element.

 

#### (constant) updateEditorState

 

**Description:
 :** 

- 

Updates the state of the editor.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 401](lib_editor_tiny_amd_src_utils.js.md)

Updates the state of the editor.

 

 

### Methods

 

#### _activityAnchor(event)

 

**Description:
 :** 

- 

The activity anchor event.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 197](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

 

 

 

#### _addEventTotalMovement(event)

 

**Description:
 :** 

- 

Add the total amout of movement to a mouse event.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 430](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

 

 

 

#### _addIdsToSelection(stateManager, typeName, ids)

 

**Description:
 :** 

- 

Add some ids to the current bulk selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 729](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `typeName`

 

String

 

the type name (section/cm)

 
 `ids`

 

array

 

the list of ids

 

 

#### _allSectionToggler(event)

 

**Description:
 :** 

- 

Handle the collapse/expand all sections button.

Toggler click is delegated to the main course content element because new sections can
appear at any moment and this way we prevent accidental double bindings.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 196](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the triggered event

 

 

#### _callEditWebservice(action, courseId, ids, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Private method to call core_courseformat_update_course webservice.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 40](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `action`

 

string

 

 

 
 `courseId`

 

number

 

 

 
 `ids`

 

array

 

 

 
 `targetSectionId`

 

number

 

optional target section id (for moving actions)

 
 `targetCmId`

 

number

 

optional target cm id (for moving actions)

 

 

#### _callParentMethod(methodname, dropdata, event)

 

**Description:
 :** 

- 

Convenient method for calling parent component functions if present.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 458](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `methodname`

 

string

 

the name of the method

 
 `dropdata`

 

Object

 

the current drop data object

 
 `event`

 

Event

 

the original event

 

 

#### _cancelBulk()

 

**Description:
 :** 

- 

Cancel bulk handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 201](course_format_amd_src_local_content_bulkedittools.js.md)

 

#### _cancelDebouncedReloadCm(cmId)

 

**Description:
 :** 

- 

Cancel the active reload CM debounced function, if any.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 610](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmId`

 

Number

 

 

 

 

#### _checkSectionlist(detail)

 

**Description:
 :** 

- 

Check the section list and disable some options if needed.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 183](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

Object

 

the update details.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state object.

 

 

 

 

#### _closeMonitor()

 

**Description:
 :** 

- 

Close the monitor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/monitor.js](lib_amd_src_local_process_monitor_monitor.js.md), [line 117](lib_amd_src_local_process_monitor_monitor.js.md)

 

#### (async) _cmBasicAction(stateManager, action, cmIds, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Execute a basic course module state action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 106](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `action`

 

string

 

the action name

 
 `cmIds`

 

array

 

the cm ids

 
 `targetSectionId`

 

number

 

optional target section id (for moving actions)

 
 `targetCmId`

 

number

 

optional target cm id (for moving actions)

 

 

#### _completionHandler(event)

 

**Description:
 :** 

- 

Activity manual completion listener.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 352](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the custom ecent

 

 

#### _completionHandler(event)

 

**Description:
 :** 

- 

Activity manual completion listener.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/activity_header.js](course_format_amd_src_local_content_activity_header.js.md), [line 78](course_format_amd_src_local_content_activity_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the custom event

###### Properties

 

 Name

 Type

 Description

 

 

 
 `detail`

 

object

 

the event details

 

 

 

 

#### _containsOnlyFiles(event) → {boolean}

 

**Description:
 :** 

- 

Check if the dragged event contains only files.

Files dragging does not generate drop data because they came from outside the page and the component
must check it before validating the event.

Some browsers like Firefox add extra types to file dragging. To discard the false positives
a double check is necessary.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 499](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the original event.

 

##### Returns:

if the drag dataTransfers contains files.

**
 Type

 :** 

boolean

 

#### (async) _createCm(param)

 

**Description:
 :** 

- 

Create a newcm instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 243](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

 

 
 `element`

 

Object

 

 

 

 

 

 

#### _createCmItem(container, cmid) → {Element}

 

**Description:
 :** 

- 

Create a new course module item in a section.

Thos method will append a fake item in the container and trigger an ajax request to
replace the fake element by the real content.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 667](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Element

 

the container element (section)

 
 `cmid`

 

Number

 

the course-module ID

 

##### Returns:

the created element

**
 Type

 :** 

Element

 

#### (async) _createListItem(args)

 

**Description:
 :** 

- 

Create a monitor item.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/monitor.js](lib_amd_src_local_process_monitor_monitor.js.md), [line 95](lib_amd_src_local_process_monitor_monitor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

the watcher arguments

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

the item state data

 

 

 

 

#### (async) _createSection(details)

 

**Description:
 :** 

- 

Create a new section instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 272](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data.

 
 `element`

 

Object

 

the element data.

 

 

 

 

#### _createSectionItem(container, sectionid) → {Element}

 

**Description:
 :** 

- 

Create a new section item.

This method will append a fake item in the container and trigger an ajax request to
replace the fake element by the real content.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 691](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Element

 

the container element (section)

 
 `sectionid`

 

Number

 

the course-module ID

 

##### Returns:

the created element

**
 Type

 :** 

Element

 

#### _deleteCm(param)

 

**Description:
 :** 

- 

Remove a cm from the list.

The actual DOM element removal is delegated to the cm component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 363](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

 

 

 

 

 

#### _deleteSection(details)

 

**Description:
 :** 

- 

Remove a section from the list.

The actual DOM element removal is delegated to the section component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 375](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the element data.

 

 

 

 

#### _destroyModal(modal, element)

 

**Description:
 :** 

- 

Hide and later destroy a modal.

Behat will fail if we remove the modal while some boostrap collapse is executing.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 729](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Modal

 

 

 
 `element`

 

HTMLElement

 

the dom element to focus on.

 

 

#### _disableLink(element)

 

**Description:
 :** 

- 

Replace an element with a copy with a different tag name.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 680](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Element

 

the original element

 

 

#### _dragEnd(event)

 

**Description:
 :** 

- 

Drag end event handler.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 295](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _dragEnter(event)

 

**Description:
 :** 

- 

Drag enter event handler.

The JS drag&drop API triggers several dragenter events on the same element because it bubbles the
child events as well. To prevent this form affecting the dropzones display, this methods use
"entercount" to determine if it's one extra child event or a valid one.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 326](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _dragLeave(event)

 

**Description:
 :** 

- 

Drag over leave handler.

The JS drag&drop API triggers several dragleave events on the same element because it bubbles the
child events as well. To prevent this form affecting the dropzones display, this methods use
"entercount" to determine if it's one extra child event or a valid one.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 367](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _dragOver(event)

 

**Description:
 :** 

- 

Drag over event handler.

We only use dragover event when a draggable action starts inside a valid dropzone. In those cases
the API won't trigger any dragEnter because the dragged alement was already there. We use the
dropzonevisible to determine if the component needs to display the dropzones or not.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 348](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _dragStart(event)

 

**Description:
 :** 

- 

Drag start event handler.

This method will generate the current dropable data. This data is the one used to determine
if a droparea accepts the dropping or not.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 241](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _drop(event)

 

**Description:
 :** 

- 

Drop event handler.

This method will call both hideDropZones and drop methods on the parent component.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 386](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

#### _enableBulk()

 

**Description:
 :** 

- 

Dispatch the enable bulk mutation.

The enable bulk button is outside of the course content main div.
Because content/actions captures click events only in the course
content, this button needs to trigger the enable bulk mutation
by itself.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittoggler.js](course_format_amd_src_local_content_bulkedittoggler.js.md), [line 106](course_format_amd_src_local_content_bulkedittoggler.js.md)

 

#### _expandSectionNode(element, forceValue)

 

**Description:
 :** 

- 

Expand a section node.

By default the method will use element.indexcollapsed to decide if the
section is opened or closed. However, using forceValue it is possible
to open or close a section independant from the indexcollapsed attribute.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 176](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the course module state element

 
 `forceValue`

 

boolean

 

optional forced expanded value

 

 

#### (async) _fixOrder(container, neworder, selector, dettachedelements, createMethod)

 

**Description:
 :** 

- 

Fix/reorder the section or cms order.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 716](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Element

 

the HTML element to reorder.

 
 `neworder`

 

Array

 

an array with the ids order

 
 `selector`

 

string

 

the element selector

 
 `dettachedelements`

 

Object

 

a list of dettached elements

 
 `createMethod`

 

function

 

method to create missing elements

 

 

#### _fixOrder(container, neworder, allitems)

 

**Description:
 :** 

- 

Fix/reorder the section or cms order.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 324](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

Element

 

the HTML element to reorder.

 
 `neworder`

 

Array

 

an array with the ids order

 
 `allitems`

 

Array

 

the list of html elements that can be placed in the container

 

 

#### _getActivitySectionURL(cm) → {String}

 

**Description:
 :** 

- 

Get the anchor link in section page for the cm.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 224](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cm`

 

Object

 

the course module data.

 

##### Returns:

the anchor link.

**
 Type

 :** 

String

 

#### _getClosestActionMenuToogler(element) → {HTMLElement|undefined}

 

**Description:
 :** 

- 

Get the closest actions menu toggler to an action element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 747](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLElement

 

the action link element

 

##### Returns:

**
 Type

 :** 

HTMLElement
|

undefined

 

#### _getDebouncedReloadCm(cmId) → {function}

 

**Description:
 :** 

- 

Generate or get a reload CM debounced function.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 557](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmId`

 

Number

 

 

 

##### Returns:

the debounced reload function

**
 Type

 :** 

function

 

#### _getDraggableData() → {Object}

 

**Description:
 :** 

- 

Get the draggable data of this component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 110](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Returns:

exported course module drop data

**
 Type

 :** 

Object

 

#### _getDropData(event) → {Object|undefined}

 

**Description:
 :** 

- 

Get the current dropdata for a specific event.

The browser can generate drag&drop events related to several user interactions:

  - Drag a page elements: this case is registered in the activeDropData map

  - Drag some HTML selections: ignored for now

  - Drag a file over the browser: file drag may appear in the future but for now they are ignored.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 475](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the original event.

 

##### Returns:

with the dragged data (or undefined if none)

**
 Type

 :** 

Object
|

undefined

 

#### (async) _getLoggerEntry(stateManager, action, itemIds, data) → {Object}

 

**Description:
 :** 

- 

Get log entry for the current action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 139](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `action`

 

string

 

the action name

 
 `itemIds`

 

Array.<int>
|

null

 

the element ids

 
 `data`

 

Object
|

undefined

 

extra params for the log entry

###### Properties

 

 Name

 Type

 Description

 

 

 
 `itemType`

 

string
|

undefined

 

the element type (will be taken from action if none)

 
 `targetSectionId`

 

int
|

null
|

undefined

 

the target section id

 
 `targetCmId`

 

int
|

null
|

undefined

 

the target cm id

 
 `component`

 

String
|

null
|

undefined

 

optional component (for format plugins)

 

 

 

##### Returns:

the log entry

**
 Type

 :** 

Object

 

#### _getTargetIds(target) → {Array.<Number>}

 

**Description:
 :** 

- 

Return the ids represented by this element.

Depending on the dataset attributes the action could represent a single id
or a bulk actions with all the current selected ids.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 197](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

HTMLElement

 

 

 

##### Returns:

array of Ids

**
 Type

 :** 

Array.<Number>

 

#### _handleUnselectAll()

 

**Description:
 :** 

- 

Process unselect all elements.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 231](course_format_amd_src_local_content_bulkedittools.js.md)

 

#### _indexContents()

 

**Description:
 :** 

- 

Regenerate content indexes.

This method is used when a legacy action refresh some content element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 486](course_format_amd_src_local_content.js.md)

 

#### _isCmBulkEnabled(bulk) → {Boolean}

 

**Description:
 :** 

- 

Check if cm bulk selection is available.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 166](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulk`

 

Object

 

the current state bulk attribute

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### _isSectionBulkEditable() → {Boolean}

 

**Description:
 :** 

- 

Check if the section is bulk editable.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 170](course_format_amd_src_local_content_section_header.js.md)

##### Returns:

**
 Type

 :** 

Boolean

 

#### _isSectionBulkEnabled(bulk) → {Boolean}

 

**Description:
 :** 

- 

Check if cm bulk selection is available.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 159](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulk`

 

Object

 

the current state bulk attribute

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### _isSelected(bulk) → {Boolean}

 

**Description:
 :** 

- 

Check if the cm id is part of the current bulk selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 180](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulk`

 

Object

 

the current state bulk attribute

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### _isSelected(bulk) → {Boolean}

 

**Description:
 :** 

- 

Check if the cm id is part of the current bulk selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 178](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulk`

 

Object

 

the current state bulk attribute

 

##### Returns:

**
 Type

 :** 

Boolean

 

#### _loadFileHandlers()

 

**Description:
 :** 

- 

Load the file hanlders promise.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 140](course_format_amd_src_local_courseeditor_courseeditor.js.md)

 

#### _modalBodyRenderedPromise(ModalClass, modalParams) → {Promise}

 

**Description:
 :** 

- 

Render a modal and return a body ready promise.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 698](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `ModalClass`

 

Modal

 

the modal class

 
 `modalParams`

 

object

 

the modal params

 

##### Returns:

the modal body ready promise

**
 Type

 :** 

Promise

 

#### _mouseLeave()

 

**Description:
 :** 

- 

Mouse leave handler.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 229](lib_amd_src_local_reactive_dragdrop.js.md)

 

#### _mouseOver()

 

**Description:
 :** 

- 

Mouse over handle.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 222](lib_amd_src_local_reactive_dragdrop.js.md)

 

#### (async) _openSectionIfNecessary()

 

**Description:
 :** 

- 

Open the section if the anchored activity is inside.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 89](course_format_amd_src_local_content_section.js.md)

 

#### _prepareFields(stateManager, updateName, fields) → {Object}

 

**Description:
 :** 

- 

Add default values to state elements.

This method is called every time a webservice returns a update state message.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 203](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

##### Returns:

final fields data

**
 Type

 :** 

Object

 

#### _processEvent(event) → {Object|false}

 

**Description:
 :** 

- 

Process a drag and drop event and delegate logic to the parent component.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 409](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the drag and drop event

 

##### Returns:

the dropdata or null if the event should not be processed

**
 Type

 :** 

Object
|

false

 

#### _publishEvents()

 

**Description:
 :** 

- 

Internal method to publish events.

This is a private method, it will be invoked when the state is set back to read only mode.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 576](lib_amd_src_local_reactive_statemanager.js.md)

 

#### _refreshActions(param)

 

**Description:
 :** 

- 

Refresh the visible action buttons depending on the selection type.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 184](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the affected element (bulk in this case).

 

 

 

 

#### _refreshActivityCard(bulk, selected)

 

**Description:
 :** 

- 

Update the activity card depending on the bulk selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 135](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `bulk`

 

Object

 

the current bulk state data

 
 `selected`

 

Boolean

 

if the activity is selected.

 

 

#### _refreshAllSectionsToggler(state)

 

**Description:
 :** 

- 

Refresh the collapse/expand all sections element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 309](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

The state data

 

 

#### _refreshBulk(param)

 

**Description:
 :** 

- 

Update a bulk options.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 119](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 

 

 

 

#### _refreshBulk(param)

 

**Description:
 :** 

- 

Update the bulk editing interface.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 108](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 

 

 

 

#### _refreshCm(param)

 

**Description:
 :** 

- 

Update a course index cm using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 138](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### _refreshCm(param)

 

**Description:
 :** 

- 

Update a course index cm using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 95](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### _refreshCmName(param)

 

**Description:
 :** 

- 

Update a course module name on the whole page.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 254](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### (async) _refreshCompletion(details)

 

**Description:
 :** 

- 

Update the activity completion icon.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 173](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 
 `element`

 

Object

 

the element data

 

 

 

 

#### _refreshCourseSectionlist(param)

 

**Description:
 :** 

- 

Refresh the section list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 467](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the full state object.

 

 

 

 

#### _refreshCourseSectionlist(param)

 

**Description:
 :** 

- 

Refresh the section list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 312](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

 

 

 

 

 

#### _refreshEnabled(param)

 

**Description:
 :** 

- 

Hide and show the bulk edit tools.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 116](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details (state.bulk in this case).

 

 

 

 

#### (async) _refreshItem(args)

 

**Description:
 :** 

- 

Create a monitor item.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/process.js](lib_amd_src_local_process_monitor_process.js.md), [line 93](lib_amd_src_local_process_monitor_process.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

the watcher arguments

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

the item state data

 

 

 

 

#### _refreshPageItem(details)

 

**Description:
 :** 

- 

Handle a page item update.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 147](course_format_amd_src_local_courseindex_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data.

 
 `element`

 

Object

 

the course state data.

 

 

 

 

#### _refreshPageItem(details)

 

**Description:
 :** 

- 

Handle a page item update.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 207](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data.

 
 `element`

 

Object

 

the course state data.

 

 

 

 

#### _refreshPageItem(details)

 

**Description:
 :** 

- 

Handle a page item update.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 155](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `details`

 

Object

 

the update details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the course state data.

 

 

 

 

#### _refreshSection(param)

 

**Description:
 :** 

- 

Update a course index section using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 127](course_format_amd_src_local_courseindex_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

Object

 

details the update details.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the section element

 

 

 

 

#### _refreshSection(param)

 

**Description:
 :** 

- 

Update a content section using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 148](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### (async) _refreshSectionBulkSelector(param)

 

**Description:
 :** 

- 

Update the bulk checkbox when the section name changes.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 100](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the section info

 

 

 

 

#### _refreshSectionCmlist(param)

 

**Description:
 :** 

- 

Refresh a section cm list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 450](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### _refreshSectionCmlist(param)

 

**Description:
 :** 

- 

Refresh a section cm list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 300](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

 

 

 

 

 

#### _refreshSectionCollapsed(args)

 

**Description:
 :** 

- 

Update section collapsed state via bootstrap 4 if necessary.

Formats that do not use bootstrap 4 must override this method in order to keep the section
toggling working.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 275](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

The state data

 
 `element`

 

Object

 

The element to update

 

 

 

 

#### _refreshSectionCollapsed(args)

 

**Description:
 :** 

- 

Update section collapsed.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 152](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

The leement to be expanded

 

 

 

 

#### _refreshSectionNumber(param)

 

**Description:
 :** 

- 

Update a course section when the section number changes.

The courseActions module used for most course section tools still depends on css classes and
section numbers (not id). To prevent inconsistencies when a section is moved, we need to refresh
the

Course formats can override the section title rendering so the frontend depends heavily on backend
rendering. Luckily in edit mode we can trigger a title update using the inplace_editable module.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 395](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

Object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### _refreshSectionTitle(param)

 

**Description:
 :** 

- 

Update a course section name on the whole page.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 434](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details.

 

 

 

 

#### _refreshSectionTitle(param)

 

**Description:
 :** 

- 

Update the section when the section name changes.

The section header have several HTML that uses the section name
for accessibility and behat tests. This method updates them all.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 88](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the section info

 

 

 

 

#### _refreshSelectAll(param)

 

**Description:
 :** 

- 

Refresh the select all element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 160](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the affected element (bulk in this case).

 

 

 

 

#### (async) _refreshSelectCount(param)

 

**Description:
 :** 

- 

Refresh the selection count.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 145](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

the affected element (bulk in this case).

 

 

 

 

#### _refreshToggler(param)

 

**Description:
 :** 

- 

Update a content section using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittoggler.js](course_format_amd_src_local_content_bulkedittoggler.js.md), [line 93](course_format_amd_src_local_content_bulkedittoggler.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

 

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

Object

 

details the update details (state.bulk in this case).

 

 

 

 

#### _refreshTools(param)

 

**Description:
 :** 

- 

Refresh the tools depending on the current selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 133](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param`

 

object

 

the state watcher information

###### Properties

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the full state data.

 
 `element`

 

Object

 

the affected element (bulk in this case).

 

 

 

 

#### _reloadCm(param0)

 

**Description:
 :** 

- 

Reload a course module contents.

Most course module HTML is still strongly backend dependant.
Some changes require to get a new version of the module.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 544](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param0`

 

object

 

the watcher details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

the state object

 

 

 

 

#### _reloadSection(param0)

 

**Description:
 :** 

- 

Reload a course section contents.

Section HTML is still strongly backend dependant.
Some changes require to get a new version of the section.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 629](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `param0`

 

details

 

the watcher details

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

the state object

 

 

 

 

#### _removeIdsFromSelection(stateManager, typeName, ids)

 

**Description:
 :** 

- 

Remove some ids to the current bulk selection.

The method resets the selection type if the current selection is empty.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 757](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `typeName`

 

String

 

the type name (section/cm)

 
 `ids`

 

array

 

the list of ids

 

 

#### _removeProcess()

 

**Description:
 :** 

- 

Close the process.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/process.js](lib_amd_src_local_process_monitor_process.js.md), [line 112](lib_amd_src_local_process_monitor_process.js.md)

 

#### (async) _requestAddSection(target, event)

 

**Description:
 :** 

- 

Handle a create section request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 406](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestCmAvailability(target)

 

**Description:
 :** 

- 

Handle a cm availability change request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 576](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 

 

#### (async) _requestCmDelete(target, event)

 

**Description:
 :** 

- 

Handle a delete cm request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 525](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestCmDuplicate(target, event)

 

**Description:
 :** 

- 

Handle a course module duplicate request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 509](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestDeleteSection(target, event)

 

**Description:
 :** 

- 

Handle a delete section request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 417](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestMoveCm(target, event)

 

**Description:
 :** 

- 

Handle a move cm request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 301](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestMoveSection(target, event)

 

**Description:
 :** 

- 

Handle a move section request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 219](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestMutationAction(target, event, mutationName)

 

**Description:
 :** 

- 

Basic mutation action helper.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 490](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 
 `mutationName`

 

string

 

the mutation name

 

 

#### (async) _requestSectionAvailability(target)

 

**Description:
 :** 

- 

Handle a section availability change request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 600](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 

 

#### (async) _requestToggleSelectionCm(target, event)

 

**Description:
 :** 

- 

Handle a toggle cm selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 469](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### (async) _requestToggleSelectionSection(target, event)

 

**Description:
 :** 

- 

Handle a toggle section selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 479](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the dispatch action element

 
 `event`

 

Event

 

the triggered event

 

 

#### _scanIndex(selector, index, creationhandler)

 

**Description:
 :** 

- 

Reindex a content (section or cm) of the course content.

This method is used internally by _indexContents.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 515](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selector`

 

string

 

the DOM selector to scan

 
 `index`

 

*

 

the index attribute to update

 
 `creationhandler`

 

*

 

method to create a new indexed element

 

 

#### _scanPageAnchorCmInfo() → {Object|null}

 

**Description:
 :** 

- 

Calculate the cm info from the current page anchor.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 374](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Returns:

the cm info or null if not found.

**
 Type

 :** 

Object
|

null

 

#### _scrollHandler()

 

**Description:
 :** 

- 

Check the current page scroll and update the active element if necessary.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 362](course_format_amd_src_local_content.js.md)

 

#### (async) _sectionBasicAction(stateManager, action, sectionIds, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Execute a basic section state action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 77](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `action`

 

string

 

the action name

 
 `sectionIds`

 

array

 

the section ids

 
 `targetSectionId`

 

number

 

optional target section id (for moving actions)

 
 `targetCmId`

 

number

 

optional target cm id (for moving actions)

 

 

#### _sectionTogglers(event)

 

**Description:
 :** 

- 

Setup sections toggler.

Toggler click is delegated to the main course content element because new sections can
appear at any moment and this way we prevent accidental double bindings.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 166](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the triggered event

 

 

#### _sectionTogglers(event)

 

**Description:
 :** 

- 

Setup sections toggler.

Toggler click is delegated to the main course index element because new sections can
appear at any moment and this way we prevent accidental double bindings.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 124](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the triggered event

 

 

#### _selectAllClick(event)

 

**Description:
 :** 

- 

Handle special select all cases.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 215](course_format_amd_src_local_content_bulkedittools.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

 

 

 

#### _setAddSectionLocked(locked)

 

**Description:
 :** 

- 

Disable all add sections actions.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 666](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `locked`

 

boolean

 

the new locked value.

 

 

#### _setCheckboxValue(checked, disabled)

 

**Description:
 :** 

- 

Modify the checkbox element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 139](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `checked`

 

Boolean

 

the new checked value

 
 `disabled`

 

Boolean

 

the new disabled value

 

 

#### _setCheckboxValue(checked, disabled)

 

**Description:
 :** 

- 

Modify the checkbox element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 146](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `checked`

 

Boolean

 

the new checked value

 
 `disabled`

 

Boolean

 

the new disabled value

 

 

#### _setupMutationRadioButtonModal(modal, ids)

 

**Description:
 :** 

- 

Add events to a mutation selector radio buttons modal.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 621](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modal`

 

Modal

 

 

 
 `ids`

 

Array.<Number>

 

the section or cm ids to apply the mutation

 

 

#### _startProcessing()

 

**Description:
 :** 

- 

Setup the component to start a transaction.

Some of the course actions replaces the current DOM element with a new one before updating the
course state. This means the component cannot preload any index properly until the transaction starts.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 340](course_format_amd_src_local_content.js.md)

 

#### (async) _updateActionsMenu(section)

 

**Description:
 :** 

- 

Update a section action menus.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 183](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `section`

 

object

 

the section state.

 

 

#### _updateBadges(section)

 

**Description:
 :** 

- 

Update a section badges using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 170](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `section`

 

object

 

the section state.

 

 

#### _updateMonitor(args)

 

**Description:
 :** 

- 

Create a monitor item.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/monitor.js](lib_amd_src_local_process_monitor_monitor.js.md), [line 110](lib_amd_src_local_process_monitor_monitor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

object

 

the watcher arguments

###### Properties

 

 Name

 Type

 Description

 

 

 
 `element`

 

object

 

the display state data

 

 

 

 

#### _updateStateSectionPreference(stateManager, preferenceName, sectionIds, preferenceValue) → {Array.<Number>|null}

 

**Description:
 :** 

- 

Private batch update for a section preference attribute.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 638](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `preferenceName`

 

string

 

the preference name

 
 `sectionIds`

 

array

 

the affected section ids

 
 `preferenceValue`

 

boolean

 

the new preferenceValue value

 

##### Returns:

sections ids with the preference value true or null if no update is required

**
 Type

 :** 

Array.<Number>
|

null

 

#### activeSearch(clearIcon)

 

**Description:
 :** 

- 

Change the searching icon to its' active state.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 832](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clearIcon`

 

HTMLElement

 

Our closing icon to manipulate.

 

 

#### activeSearchState(clearSearchIcon, timelineViewRoot)

 

**Description:
 :** 

- 

Show the clear search icon.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 156](blocks_timeline_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clearSearchIcon`

 

object

 

Clear search icon element.

 
 `timelineViewRoot`

 

object

 

The root element for the timeline view

 

 

#### addActions(actions)

 

**Description:
 :** 

- 

Add extra actions to the module.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 98](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actions`

 

array

 

array of methods to execute

 

 

#### addClickHandler(handler)

 

**Description:
 :** 

- 

Add a click handler to the list of handlers.

 

**Source:
 :** 

- 
 [admin/amd/src/plugin_management_table.js](admin_amd_src_plugin_management_table.js.md), [line 54](admin_amd_src_plugin_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `handler`

 

function

 

A handler to call on a click event

 

 

#### addEventListener(target, type, listener)

 

**Description:
 :** 

- 

Add and bind an event listener to a target and keep track of all event listeners.

The native element.addEventListener method is not object oriented friently as the
"this" represents the element that triggers the event and not the listener class.
As components can be unregister and removed at any time, the BaseComponent provides
this method to keep track of all component listeners and do all of the bind stuff.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 298](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the event target

 
 `type`

 

string

 

the event name

 
 `listener`

 

function

 

the class method that recieve the event

 

 

#### addLoggerEntry(entry)

 

**Description:
 :** 

- 

Add a new log entry into the reactive logger.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 464](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `entry`

 

[LoggerEntry](global.md)

 

 

 

 

#### addMutations(newFunctions)

 

**Description:
 :** 

- 

Add individual functions to the mutations.

Note new mutations will be added to the existing ones. To replace the full mutation
object with a new one, use setMutations method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 149](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newFunctions`

 

Object

 

an object with new mutation functions.

 

 

#### (async) addSection(stateManager, targetSectionId)

 

**Description:
 :** 

- 

Add a new section to a specific course location.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 358](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `targetSectionId`

 

number

 

optional the target section id

 

 

#### addSelectors(newSelectors)

 

**Description:
 :** 

- 

Add or update the component selectors.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 220](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newSelectors`

 

Object

 

an object of new selectors.

 

 

#### addToFavourites(root, courseId)

 

**Description:
 :** 

- 

Add course to favourites

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 251](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id number

 

 

#### addUpdateTypes(newFunctions)

 

**Description:
 :** 

- 

Add methods to process update state messages.

The state manager provide a default update, create and delete methods. However,
some applications may require to override the default methods or even add new ones
like "refresh" or "error".

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 213](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `newFunctions`

 

Object

 

the new update types functions.

 

 

#### allItemsArray(state) → {Array}

 

**Description:
 :** 

- 

Return a sorted list of all sections and cms items in the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 228](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 

##### Returns:

all sections and cms items in the state.

**
 Type

 :** 

Array

 

#### (async) allSectionsIndexCollapsed(stateManager, collapsed)

 

**Description:
 :** 

- 

Update the course index collapsed attribute of all sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 604](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `collapsed`

 

boolean

 

the new collapsed value

 

 

#### arrayEquals(a1, a2) → {Boolean}

 

**Description:
 :** 

- 

Compare two arrays which contain primitive types to see if they are equal.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 346](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `a1`

 

Array

 

first array.

 
 `a2`

 

Array

 

second array.

 

##### Returns:

boolean true if they both contain the same elements in the same order, else false.

**
 Type

 :** 

Boolean

 

#### bulkEnable(stateManager, enabled)

 

**Description:
 :** 

- 

Enable/disable bulk editing.

Note: reenabling the bulk will clean the current selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 666](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `enabled`

 

Boolean

 

the new bulk state.

 

 

#### bulkReset(stateManager)

 

**Description:
 :** 

- 

Reset the current selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 679](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 

 

#### callWatchersHandler(event)

 

**Description:
 :** 

- 

State changed listener.

This function take any state change and send it to the proper watchers.

To prevent internal state changes from colliding with other reactive instances, only the
general "state changed" is triggered at document level. All the internal changes are
triggered at private target level without bubbling. This way any reactive instance can alert
only its own watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 131](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

CustomEvent

 

 

 

 

#### canUseStealth(state, cmIds) → {Boolean}

 

**Description:
 :** 

- 

Check is some activities of a list can be stealth.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 252](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 
 `cmIds`

 

Array.<Number>

 

the module ids to check

 

##### Returns:

if any of the activities can be stealth.

**
 Type

 :** 

Boolean

 

#### checkAllBulkSelected(courseEditor) → {Boolean}

 

**Description:
 :** 

- 

Check if all possible elements are selected.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 388](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseEditor`

 

CourseEditor

 

 

 

##### Returns:

if all elements of the current type are selected.

**
 Type

 :** 

Boolean

 

#### checkImage() → {Node}

 

**Description:
 :** 

- 

Check accessiblity issue only for img type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 289](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Returns:

A complete list of all warnings and problems.

**
 Type

 :** 

Node

 

#### checkTableCaption() → {Node}

 

**Description:
 :** 

- 

Look for any table without a caption.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 305](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Returns:

A complete list of all warnings and problems.

**
 Type

 :** 

Node

 

#### clean()

 

**Description:
 :** 

- 

Clean local storage

 

**Source:
 :** 

- 
 [lib/amd/src/localstorage.js](lib_amd_src_localstorage.js.md), [line 55](lib_amd_src_localstorage.js.md)

 

#### clearSearchState(clearSearchIcon, timelineViewRoot)

 

**Description:
 :** 

- 

Hide the clear search icon.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 167](blocks_timeline_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clearSearchIcon`

 

object

 

Clear search icon element.

 
 `timelineViewRoot`

 

object

 

The root element for the timeline view

 

 

#### cm(state, cminfo) → {Object}

 

**Description:
 :** 

- 

Generate a cm export data from the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 110](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 
 `cminfo`

 

Object

 

the course module state data.

 

##### Returns:

**
 Type

 :** 

Object

 

#### (async) cmCompletion(stateManager, cmIds, complete)

 

**Description:
 :** 

- 

Mark or unmark course modules as complete.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 425](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of course modules ids

 
 `complete`

 

bool

 

the new completion value

 

 

#### cmCompletion(state, cminfo) → {Object}

 

**Description:
 :** 

- 

Generate a completion export data from the cm element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 205](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 
 `cminfo`

 

Object

 

the course module state data.

 

##### Returns:

**
 Type

 :** 

Object

 

#### (async) cmDelete(stateManager, cmIds)

 

**Description:
 :** 

- 

Delete cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 385](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of section ids

 

 

#### cmDrag(stateManager, cmIds, dragValue)

 

**Description:
 :** 

- 

Mark or unmark course modules as dragging.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 401](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of course modules ids

 
 `dragValue`

 

bool

 

the new dragging value

 

 

#### cmDraggableData(state, cmid) → {Object|null}

 

**Description:
 :** 

- 

Generate a dragable cm data structure.

This method is used by any draggable course module element to generate drop data
for its reactive/dragdrop instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 128](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

*

 

the state object

 
 `cmid`

 

*

 

the cours emodule id

 

##### Returns:

**
 Type

 :** 

Object
|

null

 

#### (async) cmDuplicate(stateManager, cmIds, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Duplicate course modules

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 261](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of course modules ids

 
 `targetSectionId`

 

number
|

undefined

 

the optional target sectionId

 
 `targetCmId`

 

number
|

undefined

 

the target course module id

 

 

#### (async) cmHide(stateManager, cmIds)

 

**Description:
 :** 

- 

Hide cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 241](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### cmLock(stateManager, cmIds, lockValue)

 

**Description:
 :** 

- 

Lock or unlock course modules.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 493](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of course modules ids

 
 `lockValue`

 

bool

 

the new locked value

 

 

#### (async) cmMove(stateManager, cmids, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Move course modules to specific course location.

Note that one of targetSectionId or targetCmId should be provided in order to identify the
new location:

  - targetCmId: the activities will be located avobe the target cm. The targetSectionId
value will be ignored in this case.

  - targetSectionId: the activities will be appended to the section. In this case
targetSectionId should not be present.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 299](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmids`

 

array

 

the list of cm ids to move

 
 `targetSectionId`

 

number

 

the target section id

 
 `targetCmId`

 

number

 

the target course module id

 

 

#### (async) cmMoveLeft(stateManager, cmIds)

 

**Description:
 :** 

- 

Move cms to the left: indent = 0.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 455](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### (async) cmMoveRight(stateManager, cmIds)

 

**Description:
 :** 

- 

Move cms to the right: indent = 1.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 446](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### (async) cmNoGroups(stateManager, cmIds)

 

**Description:
 :** 

- 

Set cms group mode to NOGROUPS.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 464](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### cmSelect(stateManager, cmIds)

 

**Description:
 :** 

- 

Select a list of cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 692](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### (async) cmSeparateGroups(stateManager, cmIds)

 

**Description:
 :** 

- 

Set cms group mode to SEPARATEGROUPS.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 482](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### (async) cmShow(stateManager, cmIds)

 

**Description:
 :** 

- 

Show cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 232](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### cmState(stateManager, cmids)

 

**Description:
 :** 

- 

Get updated state data related to some cm ids.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 778](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state

 
 `cmids`

 

array

 

the list of cm ids to update

 

 

#### (async) cmStealth(stateManager, cmIds)

 

**Description:
 :** 

- 

Stealth cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 250](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### cmUnselect(stateManager, cmIds)

 

**Description:
 :** 

- 

Unselect a list of cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 701](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### (async) cmVisibleGroups(stateManager, cmIds)

 

**Description:
 :** 

- 

Set cms group mode to VISIBLEGROUPS.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 473](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `cmIds`

 

array

 

the list of cm ids

 

 

#### collapseGroup(item)

 

**Description:
 :** 

- 

Collpase a group item.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 180](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

JQuery

 

the jQuery object

 

 

#### configDragDrop(sectionid, state, fullregion)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 39](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionid`

 

number

 

the section id

 
 `state`

 

Object

 

the initial state

 
 `fullregion`

 

Element

 

the complete section region to mark as dragged

 

 

#### configDragDrop(sectionitem)

 

**Description:
 :** 

- 

Register state values and the drag and drop subcomponent.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 54](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionitem`

 

BaseComponent

 

section item component

 

 

#### configDragDrop(cmid)

 

**Description:
 :** 

- 

Configure the component drag and drop.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 37](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `cmid`

 

number

 

course module id

 

 

#### configState(state)

 

**Description:
 :** 

- 

Save some values form the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 43](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state

 

 

#### count(args) → {Promise}

 

**Description:
 :** 

- 

Get a count of LTI tool types and tool proxies from Moodle for the given
search args.

See also:
mod/lti/classes/external.php get_tool_types_and_proxies_count()

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_types_and_proxies.js](mod_lti_amd_src_tool_types_and_proxies.js.md), [line 48](mod_lti_amd_src_tool_types_and_proxies.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Search parameters

 

##### Returns:

Promise that will be resolved when the ajax call returns.

**
 Type

 :** 

Promise

 

#### course(state) → {Object}

 

**Description:
 :** 

- 

Generate the course export data from the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 47](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 

##### Returns:

**
 Type

 :** 

Object

 

#### (async) courseState(stateManager)

 

**Description:
 :** 

- 

Get the full updated state data of the course.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 813](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state

 

 

#### createWarnings(description, nodes, isImageType) → {Array.<[ProblemDetail](global.md)>}

 

**Description:
 :** 

- 

Generate the data that describes the issues found.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 208](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `description`

 

String

 

Description of this failure.

 
 `nodes`

 

Array.<HTMLElement>

 

An array of failing nodes.

 
 `isImageType`

 

boolean

 

Whether the warnings are related to image type checks

 

##### Returns:

A set of problem details

**
 Type

 :** 

Array.<[ProblemDetail](global.md)>

 

#### defaultCreate(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process a create state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 307](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### defaultDelete(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process a delete state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 326](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### defaultOverride(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process an override state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 424](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### defaultPrepareFields(stateManager, updateName, fields) → {Object}

 

**Description:
 :** 

- 

Prepare fields for processing.

This method is used to add default values or calculations from the frontend side.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 295](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

##### Returns:

final fields data

**
 Type

 :** 

Object

 

#### defaultPut(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process a put state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 397](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### defaultRemove(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process a remove state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 351](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### defaultUpdate(stateManager, updateName, fields)

 

**Description:
 :** 

- 

Process a update state message.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 376](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

Object

 

the state manager

 
 `updateName`

 

String

 

the state element to update

 
 `fields`

 

Object

 

the new data

 

 

#### destroy()

 

**Description:
 :** 

- 

Component destroy hook.

BaseComponent call this method when a component is unregistered or removed.

Components may override this method to clean the HTML or do some action when the
component is unregistered or removed.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 157](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### destroy()

 

**Description:
 :** 

- 

Remove all subcomponents dependencies.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 68](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

 

#### destroy()

 

**Description:
 :** 

- 

Remove all subcomponents dependencies.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 69](course_format_amd_src_local_courseeditor_dndsection.js.md)

 

#### destroy()

 

**Description:
 :** 

- 

Remove all subcomponents dependencies.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 53](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

 

#### dispatch(actionName, params)

 

**Description:
 :** 

- 

Dispatch a change in the state.

This method is the only way for components to alter the state. Watchers will receive a
read only state to prevent illegal changes. If some user action require a state change, the
component should dispatch a mutation to trigger all the necessary logic to alter the state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 369](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actionName`

 

string

 

the action name (usually the mutation name)

 
 `params`

 

mixed

 

any number of params the mutation needs.

 

 

#### dispatch(args)

 

**Description:
 :** 

- 

Dispatch a change in the state.

Usually reactive modules throw an error directly to the components when something
goes wrong. However, course editor can directly display a notification.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 349](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

mixed

 

any number of params the mutation needs.

 

 

#### dispatchRegistrationFail()

 

**Description:
 :** 

- 

Dispatch a component registration fail event to inform the parent node.

As dispatchRegistrationSuccess, this method will communicate the registration fail to the
parent node to inform the possible parent component.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 412](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### dispatchRegistrationSuccess()

 

**Description:
 :** 

- 

Dispatch a component registration event to inform the parent node.

The registration event is different from the rest of the component events because
is the only way in which components can communicate its existence to a possible parent.
Most components will be created by including a mustache file, child components
must emit a registration event to the parent DOM element to alert about the registration.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 389](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### distanceBetweenElements(element) → {number}

 

**Description:
 :** 

- 

Calculate the distance between the centres of two elements.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 322](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `element`

 

HTMLLIElement

 

DOM node of a list item.

 

##### Returns:

number the distance in pixels.

**
 Type

 :** 

number

 

#### dragEnd(dropdata)

 

**Description:
 :** 

- 

The element end start hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 101](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### dragEnd(dropdata)

 

**Description:
 :** 

- 

The element drop end hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 103](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### dragEnd(dropdata)

 

**Description:
 :** 

- 

The element drop end hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 84](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### dragEnd()

 

**Description:
 :** 

- 

End dragging.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 214](question_type_ordering_amd_src_drag_reorder.js.md)

 

#### dragMove()

 

**Description:
 :** 

- 

Move the proxy to the current mouse position.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 173](question_type_ordering_amd_src_drag_reorder.js.md)

 

#### dragStart(dropdata)

 

**Description:
 :** 

- 

The element drop start hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 92](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### dragStart(dropdata)

 

**Description:
 :** 

- 

The element drop start hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 94](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### dragStart(dropdata)

 

**Description:
 :** 

- 

The element drop start hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 75](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### drop(dropdata, event)

 

**Description:
 :** 

- 

Drop event handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 155](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 
 `event`

 

Event

 

the drop event

 

 

#### drop(dropdata, event)

 

**Description:
 :** 

- 

Drop event handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 177](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 
 `event`

 

Event

 

the drop event

 

 

#### drop(dropdata, event)

 

**Description:
 :** 

- 

Drop event handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 145](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 
 `event`

 

Event

 

the drop event

 

 

#### enterCallback(jQueryItem)

 

**Description:
 :** 

- 

Handle enter key on a collpasible node.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 90](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `jQueryItem`

 

JQuery

 

the jQuery object

 

 

#### expandAllGroups()

 

**Description:
 :** 

- 

Expand all groups.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 189](course_format_amd_src_local_courseeditor_contenttree.js.md)

 

#### expandGroup(item)

 

**Description:
 :** 

- 

Expand a group item.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 169](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

JQuery

 

the jQuery object

 

 

#### fileDraggableData(state, dataTransfer) → {Object|null}

 

**Description:
 :** 

- 

Generate a file draggable structure.

This method is used when files are dragged on the browser.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 184](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

*

 

the state object

 
 `dataTransfer`

 

*

 

the current data tranfer data

 

##### Returns:

**
 Type

 :** 

Object
|

null

 

#### formatSeconds(secs) → {String}

 

**Description:
 :** 

- 

Helper method to convert time remaining in seconds into HH:MM:SS format.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 47](mod_assign_amd_src_timer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `secs`

 

Number

 

Time remaining in seconds to get value for.

 

##### Returns:

Time remaining in HH:MM:SS format.

**
 Type

 :** 

String

 

#### get(type) → {object}

 

**Description:
 :** 

- 

Get a registered type of modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_registry.js](lib_amd_src_modal_registry.js.md), [line 31](lib_amd_src_modal_registry.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

string

 

The type of modal to get

 

##### Returns:

The registered config for the modal

**
 Type

 :** 

object

 

#### get(key) → {boolean|string}

 

**Description:
 :** 

- 

Get a value from local storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/localstorage.js](lib_amd_src_localstorage.js.md), [line 32](lib_amd_src_localstorage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

The cache key to check.

 

##### Returns:

False if the value is not in the cache, or some other error - a string otherwise.

**
 Type

 :** 

boolean
|

string

 

#### get(name, id) → {Object|undefined}

 

**Description:
 :** 

- 

Get an element from the state or form an alternative state object.

The altstate param is used by external update functions that gets the current
state as param.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 478](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

String

 

the state object name

 
 `id`

 

*

 

and object id for state maps.

 

##### Returns:

the state object found

**
 Type

 :** 

Object
|

undefined

 

#### get(name, id) → {Object|undefined}

 

**Description:
 :** 

- 

Get state data.

Components access the state frequently. This convenience method is a shortcut to
this.reactive.state.stateManager.get() method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 204](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

String

 

the state object name

 
 `id`

 

*

 

an optional object id for state maps.

 

##### Returns:

the state object found

**
 Type

 :** 

Object
|

undefined

 

#### getActiveItem() → {Element|undefined}

 

**Description:
 :** 

- 

Return the current active node.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 77](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Returns:

the active item if any

**
 Type

 :** 

Element
|

undefined

 

#### getAddFavouriteMenuItem(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the action menu item

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 230](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id.

 

##### Returns:

The add to favourite menu item.

**
 Type

 :** 

Object

 

#### getClasses() → {Object}

 

**Description:
 :** 

- 

Return the component drag and drop CSS classes.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 159](lib_amd_src_local_reactive_dragdrop.js.md)

##### Returns:

the dragdrop css classes

**
 Type

 :** 

Object

 

#### getContent() → {object}

 

**Description:
 :** 

- 

Return the jQuery element with the content. This will return either
the unread notification container or the all notification container
depending on which is currently visible.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 100](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

jQuery object currently visible content contianer

**
 Type

 :** 

object

 

#### getCourseId(root) → {Number}

 

**Description:
 :** 

- 

Get the course id from a favourite element.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 183](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The favourite icon container element.

 

##### Returns:

Course id.

**
 Type

 :** 

Number

 

#### getCurrentOrder() → {Array}

 

**Description:
 :** 

- 

Get the current order of the list containing itemDragging.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 333](question_type_ordering_amd_src_drag_reorder.js.md)

##### Returns:

Array of strings, the id of each element in order.

**
 Type

 :** 

Array

 

#### (async) getDialogueContent() → {Promise.<Array>}

 

**Description:
 :** 

- 

Return the dialogue content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 126](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Returns:

A template promise containing the rendered dialogue content.

**
 Type

 :** 

Promise.<Array>

 

#### getDraggableData() → {Object}

 

**Description:
 :** 

- 

Get the draggable data of this component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 93](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Returns:

exported course module drop data

**
 Type

 :** 

Object

 

#### getElementLocked(target) → {boolean}

 

**Description:
 :** 

- 

Get the current locked value from the element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 489](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the event target

 

##### Returns:

**
 Type

 :** 

boolean

 

#### getElements(query, dataId) → {NodeList}

 

**Description:
 :** 

- 

Get the all subelement that match a query selector.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 209](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `query`

 

string
|

undefined

 

optional subelement query

 
 `dataId`

 

string
|

undefined

 

optional data-id value

 

##### Returns:

the DOM elements

**
 Type

 :** 

NodeList

 

#### getEvents() → {Object}

 

**Description:
 :** 

- 

Return the component custom event names.

Components may override this method to provide their own events.

Component custom events is an important part of component reusability. This function
is static because is part of the component definition and should be accessible from
outsite the instances. However, values will be available at instance level in the
this.events object.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 126](lib_amd_src_local_reactive_basecomponent.js.md)

##### Returns:

the component events.

**
 Type

 :** 

Object

 

#### getExporter() → {Exporter}

 

**Description:
 :** 

- 

Return a data exporter to transform state part into mustache contexts.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 254](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Returns:

the exporter class

**
 Type

 :** 

Exporter

 

#### getFavouriteIconContainer(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the container element for the favourite icon.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 162](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id number

 

##### Returns:

The favourite icon container

**
 Type

 :** 

Object

 

#### (async) getFileHandlersPromise() → {Promise}

 

**Description:
 :** 

- 

Return the course file handlers promise.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 271](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Returns:

the promise for file handlers.

**
 Type

 :** 

Promise

 

#### getFilesDraggableData(dataTransfer) → {Array}

 

**Description:
 :** 

- 

Convert a file dragging event into a proper dragging file list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 344](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dataTransfer`

 

DataTransfer

 

the event to convert

 

##### Returns:

of file list info.

**
 Type

 :** 

Array

 

#### getFilterValues(root) → {filters}

 

**Description:
 :** 

- 

Get filter values from DOM.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 82](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the courses view.

 

##### Returns:

Set filters.

**
 Type

 :** 

filters

 

#### getFormatString(key, param) → {Promise.<String>}

 

**Description:
 :** 

- 

Execute a get string for a possible format overriden editor string.

Return the proper getString promise for an editor string using the core_courseformat
of the format_PLUGINNAME compoment depending on the current view format setup.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 206](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

String

 

the string key

 
 `param`

 

string
|

undefined

 

The param for variable expansion in the string.

 

##### Returns:

a getString promise

**
 Type

 :** 

Promise.<String>

 

#### getHideCourseMenuItem(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the action menu item

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 298](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id.

 

##### Returns:

The hide course menu item.

**
 Type

 :** 

Object

 

#### getIds(name) → {Array}

 

**Description:
 :** 

- 

Get all element ids from the given state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 498](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `name`

 

String

 

the state object name

 

##### Returns:

the element ids.

**
 Type

 :** 

Array

 

#### getInitialPromise() → {Promise}

 

**Description:
 :** 

- 

Generate a promise that will be resolved when the initial state is loaded.

In most cases the final state will be loaded using an ajax call. This is the reason
why states manager are created unlocked and won't be reactive until the initial state is set.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 168](lib_amd_src_local_reactive_statemanager.js.md)

##### Returns:

the resulting promise

**
 Type

 :** 

Promise

 

#### getLastCm() → {element|null}

 

**Description:
 :** 

- 

Get the last CM element of that section.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 117](course_format_amd_src_local_courseindex_section.js.md)

##### Returns:

**
 Type

 :** 

element
|

null

 

#### getLastCm() → {element|null}

 

**Description:
 :** 

- 

Get the last CM element of that section.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 83](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Returns:

the las course module element of the section.

**
 Type

 :** 

element
|

null

 

#### getLastCm() → {element|null}

 

**Description:
 :** 

- 

Get the last CM element of that section.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 133](course_format_amd_src_local_content_section.js.md)

##### Returns:

**
 Type

 :** 

element
|

null

 

#### getMyCourses(filters, limit) → {promise}

 

**Description:
 :** 

- 

Get enrolled courses from backend.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 109](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filters`

 

object

 

The filters for this view.

 
 `limit`

 

int

 

The number of courses to show.

 

##### Returns:

Resolved with an array of courses.

**
 Type

 :** 

promise

 

#### getNotificationElement(id) → {object|null}

 

**Description:
 :** 

- 

Find the notification element for the given id.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 191](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

int

 

 

 

##### Returns:

The notification element

**
 Type

 :** 

object
|

null

 

#### getOffset() → {int}

 

**Description:
 :** 

- 

Get the offset value for the current state of the popover in order
to sent to the backend to correctly paginate the notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 112](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

current offset

**
 Type

 :** 

int

 

#### getPageAnchorCmInfo()

 

**Description:
 :** 

- 

Return the current page anchor cm info.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 387](course_format_amd_src_local_courseeditor_courseeditor.js.md)

 

#### getPagedContentContainer(root, index) → {Object}

 

**Description:
 :** 

- 

Get the paged content container element.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 173](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `index`

 

Number

 

Rendered page index.

 

##### Returns:

The rendered paged container.

**
 Type

 :** 

Object

 

#### getRemoveFavouriteMenuItem(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the action menu item

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 241](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id.

 

##### Returns:

The remove from favourites menu item.

**
 Type

 :** 

Object

 

#### getSearchMyCourses(filters, limit, searchValue) → {promise}

 

**Description:
 :** 

- 

Search for enrolled courses from backend.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 135](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filters`

 

object

 

The filters for this view.

 
 `limit`

 

int

 

The number of courses to show.

 
 `searchValue`

 

string

 

What does the user want to search within their courses.

 

##### Returns:

Resolved with an array of courses.

**
 Type

 :** 

promise

 

#### getSelector(selectorName) → {string|undefined}

 

**Description:
 :** 

- 

Return a component selector.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 232](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `selectorName`

 

string

 

the selector name

 

##### Returns:

the query selector

**
 Type

 :** 

string
|

undefined

 

#### (async) getServerCourseState() → {Object}

 

**Description:
 :** 

- 

Load the current course state from the server.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 220](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Returns:

the current course state

**
 Type

 :** 

Object

 

#### getShowCourseMenuItem(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the action menu item

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 309](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id.

 

##### Returns:

The show course menu item.

**
 Type

 :** 

Object

 

#### getState() → {Promise}

 

**Description:
 :** 

- 

Return the initial state promise.

Typically, components do not require to use this promise because registerComponent
will trigger their stateReady method automatically. But it could be useful for complex
components that require to combine state, template and string loadings.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 208](lib_amd_src_local_reactive_reactive.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### getStorageValue(key) → {boolean|string}

 

**Description:
 :** 

- 

Get a value from the course editor static storage if any.

The course editor static storage uses the sessionStorage to store values from the
components. This is used to prevent unnecesary template loadings on every page. However,
the storage does not work if no sessionStorage can be used (in debug mode for example),
if the page is in editing mode or if the initial state change from the last page.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 300](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

the key to get

 

##### Returns:

the storage value or false if cannot be loaded

**
 Type

 :** 

boolean
|

string

 

#### getTableRoot(e) → {HTMLElement|bool}

 

**Description:
 :** 

- 

Get the table root from an event.

 

**Source:
 :** 

- 
 [admin/amd/src/plugin_management_table.js](admin_amd_src_plugin_management_table.js.md), [line 79](admin_amd_src_plugin_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

 

 

##### Returns:

**
 Type

 :** 

HTMLElement
|

bool

 

#### getWarnings() → {Array.<[ProblemDetail](global.md)>}

 

**Description:
 :** 

- 

Find all problems with the content editable region.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 176](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Returns:

A complete list of all warnings and problems.

**
 Type

 :** 

Array.<[ProblemDetail](global.md)>

 

#### getWatchers() → {array}

 

**Description:
 :** 

- 

Return the list of watchers that component has.

Each watcher is represented by an object with two attributes:

  - watch (string) the specific state event to watch. Example 'section.visible:updated'

  - handler (function) the function to call when the watching state change happens

Any component shoudl override this method to define their state watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 172](lib_amd_src_local_reactive_basecomponent.js.md)

##### Returns:

array of watchers.

**
 Type

 :** 

array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Return the component watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/process.js](lib_amd_src_local_process_monitor_process.js.md), [line 80](lib_amd_src_local_process_monitor_process.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Return the component watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/monitor.js](lib_amd_src_local_process_monitor_monitor.js.md), [line 81](lib_amd_src_local_process_monitor_monitor.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Return the component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 215](course_format_amd_src_local_content.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 104](course_format_amd_src_local_courseindex_section.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 123](course_format_amd_src_local_courseindex_cm.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 108](course_format_amd_src_local_content_section.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 103](course_format_amd_src_local_content_bulkedittools.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittoggler.js](course_format_amd_src_local_content_bulkedittoggler.js.md), [line 81](course_format_amd_src_local_content_bulkedittoggler.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Return the component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 135](course_format_amd_src_local_content_actions.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 72](course_format_amd_src_local_content_section_header.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### getWatchers() → {Array}

 

**Description:
 :** 

- 

Component watchers.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 70](course_format_amd_src_local_content_section_cmitem.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

#### (async) handleBlockProtectToggle(tableRoot, e)

 

**Description:
 :** 

- 

Handle toggling of block protection.

 

**Source:
 :** 

- 
 [admin/amd/src/block_management_table.js](admin_amd_src_block_management_table.js.md), [line 51](admin_amd_src_block_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 
 `e`

 

Event

 

 

 

 

#### handleItemClick(event, jQueryItem)

 

**Description:
 :** 

- 

Handle an item click.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 117](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the click event

 
 `jQueryItem`

 

jQuery

 

the item clicked

 

 

#### (async) handleStateToggle(tableRoot, e)

 

**Description:
 :** 

- 

Handle state toggling.

 

**Source:
 :** 

- 
 [admin/amd/src/plugin_management_table.js](admin_amd_src_plugin_management_table.js.md), [line 122](admin_amd_src_plugin_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableRoot`

 

HTMLElement

 

 

 
 `e`

 

Event

 

 

 

 

#### hasDoneInitialLoad() → {bool}

 

**Description:
 :** 

- 

Check if the first load of notification has been triggered for the current
state of the popover.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 132](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

true if first notification loaded, false otherwise

**
 Type

 :** 

bool

 

#### hasLoadedAllContent() → {bool}

 

**Description:
 :** 

- 

Check if we've loaded all of the notifications for the current popover
state.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 143](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

true if all notifications loaded, false otherwise

**
 Type

 :** 

bool

 

#### hideCourse(root, courseId)

 

**Description:
 :** 

- 

Hide course

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 319](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id number

 

 

#### hideDropZone()

 

**Description:
 :** 

- 

Hide the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 145](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

 

#### hideDropZone()

 

**Description:
 :** 

- 

Hide the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 164](course_format_amd_src_local_courseeditor_dndsection.js.md)

 

#### hideDropZone()

 

**Description:
 :** 

- 

Hide the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 135](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

 

#### hideElement(root, id)

 

**Description:
 :** 

- 

Reset the loadedPages dataset to take into account the hidden element

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 383](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `id`

 

Number

 

The course id number

 

 

#### hideFavouriteIcon(root, courseId)

 

**Description:
 :** 

- 

Hide the favourite icon.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 193](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The favourite icon container element.

 
 `courseId`

 

Number

 

Course id number.

 

 

#### hideUnreadCount()

 

**Description:
 :** 

- 

Hide the unread notification count badge on the menu toggle.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 182](message_output_popup_amd_src_notification_popover_controller.js.md)

 

#### incrementOffset()

 

**Description:
 :** 

- 

Increment the offset for the current state, if required.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 123](message_output_popup_amd_src_notification_popover_controller.js.md)

 

#### init()

 

**Description:
 :** 

- 

Initialize the page.

 

**Source:
 :** 

- 
 [message/amd/src/default_notification_preferences.js](message_amd_src_default_notification_preferences.js.md), [line 95](message_amd_src_default_notification_preferences.js.md)

 

#### init(timerId)

 

**Description:
 :** 

- 

Set up the submission timer.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 116](mod_assign_amd_src_timer.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `timerId`

 

Number

 

Unique ID of the timer element.

 

 

#### initializePagedContent(root, promiseFunction, inputValue)

 

**Description:
 :** 

- 

Initialise the courses list and cards views on page load.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 697](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `root`

 

object

 

 

 

The root element for the courses view.

 
 `promiseFunction`

 

function

 

 

 

How do we fetch the courses and what do we do with them?

 
 `inputValue`

 

null
|

string

 

 

 `null`

 

What to search for

 

 

#### isDropzoneVisible() → {boolean}

 

**Description:
 :** 

- 

Return the current drop-zone visible of the element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 168](lib_amd_src_local_reactive_dragdrop.js.md)

##### Returns:

if the dropzone should be visible or not

**
 Type

 :** 

boolean

 

#### isGroupCollapsed(jQueryItem) → {boolean}

 

**Description:
 :** 

- 

Check if a gorup item is collapsed.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 137](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `jQueryItem`

 

JQuery

 

the jQuery object

 

##### Returns:

if the element is collapsed

**
 Type

 :** 

boolean

 

#### itemMovedByClick(e)

 

**Description:
 :** 

- 

Handles the movement of an item by click.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 245](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

MouseEvent

 

The pointer event.

 

 

#### itemsPerPageFunc(pagingLimit, root) → {Array.<Number>}

 

**Description:
 :** 

- 

Figure out how many items are going to be allowed to be rendered in the block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 559](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `pagingLimit`

 

Number

 

How many courses to display

 
 `root`

 

Object

 

The course overview container

 

##### Returns:

How many courses will be rendered

**
 Type

 :** 

Array.<Number>

 

#### listedSectionIds(state) → {Array.<Number>}

 

**Description:
 :** 

- 

Get the IDs of the sections that are listed as regular sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 70](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 

##### Returns:

the list of section ids that are listed.

**
 Type

 :** 

Array.<Number>

 

#### (async) loadCourse(courseId, serverStateKey)

 

**Description:
 :** 

- 

Set up the course editor when the page is ready.

The course can only be loaded once per instance. Otherwise an error is thrown.

The backend can inform the module of the current state key. This key changes every time some
update in the course affect the current user state. Some examples are:

  - The course content has been edited

  - The user marks some activity as completed

  - The user collapses or uncollapses a section (it is stored as a user preference)

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 73](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

number

 

course id

 
 `serverStateKey`

 

string

 

the current backend course cache reference

 

 

#### loadMoreNotifications() → {object}

 

**Description:
 :** 

- 

Send a request for more notifications from the server, if we aren't already
loading some and haven't already loaded all of them.

Takes into account the current mode of the popover and will request only
unread notifications if required.

All notifications are marked as read by the server when they are returned.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 251](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

jQuery promise that is resolved when notifications have been
retrieved and added to the DOM

**
 Type

 :** 

object

 

#### loadStaticContent() → {boolean}

 

**Description:
 :** 

- 

Load the course index from the session storage if any.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/placeholder.js](course_format_amd_src_local_courseindex_placeholder.js.md), [line 75](course_format_amd_src_local_courseindex_placeholder.js.md)

##### Returns:

true if the static version is loaded form the session

**
 Type

 :** 

boolean

 

#### (async) loadTemplateContent(state)

 

**Description:
 :** 

- 

Load the course index template.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/placeholder.js](course_format_amd_src_local_courseindex_placeholder.js.md), [line 91](course_format_amd_src_local_courseindex_placeholder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### markAllAsRead() → {Promise}

 

**Description:
 :** 

- 

Send a request to the server to mark all unread notifications as read and update
the unread count and unread notification elements appropriately.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 297](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### midX(node) → {number}

 

**Description:
 :** 

- 

Get the x-position of the middle of the DOM node represented by the given jQuery object.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 302](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

jQuery

 

jQuery wrapping a DOM node.

 

##### Returns:

Number the x-coordinate of the middle (left plus half outerWidth).

**
 Type

 :** 

number

 

#### midY(node) → {number}

 

**Description:
 :** 

- 

Get the y-position of the middle of the DOM node represented by the given jQuery object.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 312](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

jQuery

 

jQuery wrapped DOM node.

 

##### Returns:

Number the y-coordinate of the middle (top plus half outerHeight).

**
 Type

 :** 

number

 

#### module:core/emoji/auto_complete(root, textArea, hasSuggestionCallback, selectCallback)

 

**Description:
 :** 

- 

Initialise the emoji auto complete.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/auto_complete.js](lib_amd_src_emoji_auto_complete.js.md), [line 243](lib_amd_src_emoji_auto_complete.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The root container element for the auto complete

 
 `textArea`

 

Element

 

The text area element to monitor for auto complete

 
 `hasSuggestionCallback`

 

function

 

Callback for when there are auto-complete suggestions

 
 `selectCallback`

 

function

 

Callback for when the user selects an emoji

 

 

#### module:core/emoji/picker(root, selectCallback)

 

**Description:
 :** 

- 

Initialise the emoji picker.

 

**Source:
 :** 

- 
 [lib/amd/src/emoji/picker.js](lib_amd_src_emoji_picker.js.md), [line 825](lib_amd_src_emoji_picker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Element

 

The root element for the picker

 
 `selectCallback`

 

function

 

Callback for when the user selects an emoji

 

 

#### module:core/menu_navigation(elementRoot)

 

**Description:
 :** 

- 

The initial entry point that a given module can pass a HTMLElement.

 

**Source:
 :** 

- 
 [lib/amd/src/menu_navigation.js](lib_amd_src_menu_navigation.js.md), [line 174](lib_amd_src_menu_navigation.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elementRoot`

 

HTMLElement

 

The menu to add handlers upon.

 

 

#### module:core/moremenu(menu)

 

**Description:
 :** 

- 

Initialise the more menus.

 

**Source:
 :** 

- 
 [lib/amd/src/moremenu.js](lib_amd_src_moremenu.js.md), [line 195](lib_amd_src_moremenu.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `menu`

 

HTMLElement

 

The navbar moremenu.

 

 

#### module:mod_forum/local/grades/local/grader/gradingpanel(component, context, gradingComponent, gradingSubtype, itemName) → {Object}

 

**Description:
 :** 

- 

Get the grade panel setter and getter for the current component.
This function dynamically pulls the relevant gradingpanel JS file defined in the grading method.
We do this because we do not know until execution time what the grading type is and we do not want to import unused files.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/local/grader/gradingpanel.js](mod_forum_amd_src_local_grades_local_grader_gradingpanel.js.md), [line 37](mod_forum_amd_src_local_grades_local_grader_gradingpanel.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

String

 

The component being graded

 
 `context`

 

Number

 

The contextid of the thing being graded

 
 `gradingComponent`

 

String

 

The thing providing the grading type

 
 `gradingSubtype`

 

String

 

The subtype fo the grading component

 
 `itemName`

 

String

 

The name of the thing being graded

 

##### Returns:

**
 Type

 :** 

Object

 

#### module:mod_forum/local/grades/local/grader/user_picker(users, showUserCallback, preChangeUserCallback, currentUserIDopt) → {UserPicker}

 

**Description:
 :** 

- 

Create a new user picker.

 

**Source:
 :** 

- 
 [mod/forum/amd/src/local/grades/local/grader/user_picker.js](mod_forum_amd_src_local_grades_local_grader_user_picker.js.md), [line 196](mod_forum_amd_src_local_grades_local_grader_user_picker.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `users`

 

Array

 

 

 

The list of users

 
 `showUserCallback`

 

function

 

 

 

The function to call to show a specific user

 
 `preChangeUserCallback`

 

function

 

 

 

The fucntion to call to save the grade for the current user

 
 `currentUserID`

 

Number

 

 

 <optional>  

 

The userid of the current user

 

##### Returns:

**
 Type

 :** 

UserPicker

 

#### noCoursesRender(root) → {promise}

 

**Description:
 :** 

- 

Given there are no courses to render provide the rendered template.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 478](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the courses view.

 

##### Returns:

jQuery promise resolved after rendering is complete.

**
 Type

 :** 

promise

 

#### pageBuilder(coursesData, currentPage, pageData, actions, activeSearch)

 

**Description:
 :** 

- 

Mutates and controls the loadedPages array and handles the bootstrapping.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 592](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Default

 Description

 

 

 
 `coursesData`

 

Array
|

Object

 

 

 

Array of all of the courses to start building the page from

 
 `currentPage`

 

Number

 

 

 

What page are we currently on?

 
 `pageData`

 

Object

 

 

 

Any current page information

 
 `actions`

 

Object

 

 

 

Paged content helper

 
 `activeSearch`

 

null
|

boolean

 

 

 `null`

 

Are we currently actively searching and building up search results?

 

 

#### processUpdate(updateName, action, fields, updateTypes)

 

**Description:
 :** 

- 

Process a single state update.

Note this method will not lock or unlock the state by itself.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 259](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `updateName`

 

string

 

the state element to update

 
 `action`

 

string

 

to action to perform

 
 `fields`

 

object

 

the new data

 
 `updateTypes`

 

Object

 

optional functions to override the default update types.

 

 

#### processUpdates(updates, updateTypes)

 

**Description:
 :** 

- 

Process a state updates array and do all the necessary changes.

Note this method unlocks the state while it is executing and relocks it
when finishes.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 230](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `updates`

 

array

 

 

 
 `updateTypes`

 

Object

 

optional functions to override the default update types.

 

 

#### query(args) → {Promise}

 

**Description:
 :** 

- 

Get a list of LTI tool types and tool proxies from Moodle for the given
search args.

See also:
mod/lti/classes/external.php get_tool_types_and_proxies()

 

**Source:
 :** 

- 
 [mod/lti/amd/src/tool_types_and_proxies.js](mod_lti_amd_src_tool_types_and_proxies.js.md), [line 27](mod_lti_amd_src_tool_types_and_proxies.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `args`

 

Object

 

Search parameters

 

##### Returns:

Promise that will be resolved when the ajax call returns.

**
 Type

 :** 

Promise

 

#### register(type, module, template)

 

**Description:
 :** 

- 

Register a modal with the registry.

 

**Source:
 :** 

- 
 [lib/amd/src/modal_registry.js](lib_amd_src_modal_registry.js.md), [line 40](lib_amd_src_modal_registry.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `type`

 

string

 

The type of modal (must be unique)

 
 `module`

 

function

 

The modal module (must be a constructor function of type core/modal)

 
 `template`

 

string

 

The template name of the modal

 

 

#### registerChildComponent(component)

 

**Description:
 :** 

- 

Register a child component into the reactive instance.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 431](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

self

 

the component to register.

 

 

#### registerComponent(component) → {object}

 

**Description:
 :** 

- 

Register a new component.

Component can provide some optional functions to the reactive module:

  - getWatchers: returns an array of watchers

  - stateReady: a method to call when the initial state is loaded

It can also provide some optional attributes:

  - name: the component name (default value: "Unkown component") to customize debug messages.

The method will also use dispatchRegistrationSuccess and dispatchRegistrationFail. Those
are BaseComponent methods to inform parent components of the registration status.
Components should not override those methods.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 222](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

object

 

the new component

###### Properties

 

 Name

 Type

 Attributes

 Description

 

 

 
 `name`

 

string

 

 

 <optional>  

 

the component name to display in warnings and errors.

 
 `dispatchRegistrationSuccess`

 

function

 

 

 <optional>  

 

method to notify registration success

 
 `dispatchRegistrationFail`

 

function

 

 

 <optional>  

 

method to notify registration fail

 
 `getWatchers`

 

function

 

 

 <optional>  

 

getter of the component watchers

 
 `stateReady`

 

function

 

 

 <optional>  

 

method to call when the state is ready

 

 

 

##### Returns:

the registered component

**
 Type

 :** 

object

 

#### registerEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the default_notification_preferences page.

 

**Source:
 :** 

- 
 [message/amd/src/default_notification_preferences.js](message_amd_src_default_notification_preferences.js.md), [line 37](message_amd_src_default_notification_preferences.js.md)

 

#### registerEventListeners()

 

**Description:
 :** 

- 

Add all of the required event listeners for this notification popover.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 322](message_output_popup_amd_src_notification_popover_controller.js.md)

 

#### registerEventListeners(root, page)

 

**Description:
 :** 

- 

Listen to, and handle events for the myoverview block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 758](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The myoverview block container element.

 
 `page`

 

HTMLElement

 

The whole HTMLElement for our block.

 

 

#### registerPagedEventHandlers(root, namespace)

 

**Description:
 :** 

- 

Intialise the paged list and cards views on page load.
Returns an array of paged contents that we would like to handle here

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 547](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the courses view

 
 `namespace`

 

string

 

The namespace for all the events attached

 

 

#### registerSearch(root, timelineViewRoot)

 

**Description:
 :** 

- 

Event listener for the "search" input field in the timeline navigation that allows for
searching the activity name, course name and activity type.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 133](blocks_timeline_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the timeline block

 
 `timelineViewRoot`

 

object

 

The root element for the timeline view

 

 

#### registerSelector(root)

 

**Description:
 :** 

- 

Event listener for the Display filter (cards, list).

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 58](blocks_myoverview_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the overview block

 

 

#### registerStateAction(field, prop, action, data)

 

**Description:
 :** 

- 

Register a state modification and generate the necessary events.

This method is used mainly by proxy helpers to dispatch state change event.
However, mutations can use it to inform components about non reactive changes
in the state (only the two first levels of the state are reactive).

Each action can produce several events:

  - The specific attribute updated, created or deleter (example: "cm.visible:updated")

  - The general state object updated, created or deleted (example: "cm:updated")

  - If the element has an ID attribute, the specific event with id (example: "cm[42].visible:updated")

  - If the element has an ID attribute, the general event with id (example: "cm[42]:updated")

  - A generic state update event "state:update"

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 526](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `field`

 

string

 

the affected state field name

 
 `prop`

 

string
|

null

 

the affecter field property (null if affect the full object)

 
 `action`

 

string

 

the action done (created/updated/deleted)

 
 `data`

 

*

 

the affected data

 

 

#### registerTimelineDaySelector(root, timelineViewRoot)

 

**Description:
 :** 

- 

Event listener for the day selector ("Next 7 days", "Next 30 days", etc).

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 47](blocks_timeline_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the timeline block

 
 `timelineViewRoot`

 

object

 

The root element for the timeline view

 

 

#### registerViewSelector(root, timelineViewRoot)

 

**Description:
 :** 

- 

Event listener for the "sort" button in the timeline navigation that allows for
changing between the timeline dates and courses views.

On a view change we tell the timeline view module that the view has been shown
so that it can handle how to display the appropriate view.

 

**Source:
 :** 

- 
 [blocks/timeline/amd/src/view_nav.js](blocks_timeline_amd_src_view_nav.js.md), [line 105](blocks_timeline_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the timeline block

 
 `timelineViewRoot`

 

object

 

The root element for the timeline view

 

 

#### remove()

 

**Description:
 :** 

- 

Remove a previously rendered component instance.

This method will remove the component HTML and unregister it from the
reactive module.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 363](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### removeAllEventListeners()

 

**Description:
 :** 

- 

Remove all event listeners from this component.

This method is called also when the component is unregistered or removed.

Note that only listeners registered with the addEventListener method
will be removed. Other manual listeners will keep active.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 350](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### removeEventListener(target, type, listener)

 

**Description:
 :** 

- 

Remove an event listener from a component.

This method allows components to remove listeners without keeping track of the
listeners bind versions of the method. Both addEventListener and removeEventListener
keeps internally the relation between the original class method and the bind one.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 330](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the event target

 
 `type`

 

string

 

the event name

 
 `listener`

 

function

 

the class method that recieve the event

 

 

#### removeFromFavourites(root, courseId)

 

**Description:
 :** 

- 

Remove course from favourites

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 274](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id number

 

 

#### renderComponent(target, file, data) → {Promise}

 

**Description:
 :** 

- 

Render a new Component using a mustache file.

It is important to note that this method should NOT be used for loading regular mustache files
as it returns a Promise that will only be resolved if the mustache registers a component instance.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 265](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

element

 

the DOM element that contains the component

 
 `file`

 

string

 

the component mustache file to render

 
 `data`

 

*

 

the mustache data

 

##### Returns:

a promise of the resulting component instance

**
 Type

 :** 

Promise

 

#### renderCourses(root, coursesData) → {promise}

 

**Description:
 :** 

- 

Render the dashboard courses.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 494](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the courses view.

 
 `coursesData`

 

array

 

containing array of returned courses.

 

##### Returns:

jQuery promise resolved after rendering is complete.

**
 Type

 :** 

promise

 

#### renderNotifications(notifications, container) → {object}

 

**Description:
 :** 

- 

Render the notification data with the appropriate template and add it to the DOM.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 203](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `notifications`

 

array

 

Notification data

 
 `container`

 

object

 

jQuery object the container to append the rendered notifications

 

##### Returns:

jQuery promise that is resolved when all notifications have been
rendered and added to the DOM

**
 Type

 :** 

object

 

#### renderUnreadCount()

 

**Description:
 :** 

- 

Show the unread notification count badge on the menu toggle if there
are unread notifications, otherwise hide it.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 165](message_output_popup_amd_src_notification_popover_controller.js.md)

 

#### resetGlobals()

 

**Description:
 :** 

- 

In cases when switching between regular rendering and search rendering we need to reset some variables.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 642](blocks_myoverview_amd_src_view.js.md)

 

#### searchFunctionalityCurry() → {function}

 

**Description:
 :** 

- 

Initialize the searching functionality so we can call it when required.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 674](blocks_myoverview_amd_src_view.js.md)

##### Returns:

**
 Type

 :** 

function

 

#### section(state, sectioninfo) → {Object}

 

**Description:
 :** 

- 

Generate a section export data from the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 86](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the current state.

 
 `sectioninfo`

 

Object

 

the section state data.

 

##### Returns:

**
 Type

 :** 

Object

 

#### (async) sectionContentCollapsed(stateManager, sectionIds, collapsed)

 

**Description:
 :** 

- 

Update the course content collapsed attribute of some sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 616](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the affected section ids

 
 `collapsed`

 

boolean

 

the new collapsed value

 

 

#### (async) sectionDelete(stateManager, sectionIds)

 

**Description:
 :** 

- 

Delete sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 373](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of course modules ids

 

 

#### sectionDrag(stateManager, sectionIds, dragValue)

 

**Description:
 :** 

- 

Mark or unmark course sections as dragging.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 413](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids

 
 `dragValue`

 

bool

 

the new dragging value

 

 

#### sectionDraggableData(state, sectionid) → {Object|null}

 

**Description:
 :** 

- 

Generate a dragable cm data structure.

This method is used by any draggable section element to generate drop data
for its reactive/dragdrop instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 162](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

*

 

the state object

 
 `sectionid`

 

*

 

the cours section id

 

##### Returns:

**
 Type

 :** 

Object
|

null

 

#### (async) sectionHide(stateManager, sectionIds)

 

**Description:
 :** 

- 

Hides sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 214](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids

 

 

#### (async) sectionIndexCollapsed(stateManager, sectionIds, collapsed)

 

**Description:
 :** 

- 

Update the course index collapsed attribute of some sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 585](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the affected section ids

 
 `collapsed`

 

boolean

 

the new collapsed value

 

 

#### sectionLock(stateManager, sectionIds, lockValue)

 

**Description:
 :** 

- 

Lock or unlock course sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 504](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids

 
 `lockValue`

 

bool

 

the new locked value

 

 

#### (async) sectionMove(stateManager, sectionIds, targetSectionId)

 

**Description:
 :** 

- 

Move course modules to specific course location.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 320](course_format_amd_src_local_courseeditor_mutations.js.md)

 

**Deprecated::** 

- since Moodle 4.4 MDL-77038.

 

**To Do:
 :** 

- MDL-80116 This will be deleted in Moodle 4.8.

 

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids to move

 
 `targetSectionId`

 

number

 

the target section id

 

 

#### (async) sectionMoveAfter(stateManager, sectionIds, targetSectionId)

 

**Description:
 :** 

- 

Move course modules after a specific course location.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 340](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids to move

 
 `targetSectionId`

 

number

 

the target section id

 

 

#### sectionSelect(stateManager, sectionIds)

 

**Description:
 :** 

- 

Select a list of sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 710](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of cm ids

 

 

#### (async) sectionShow(stateManager, sectionIds)

 

**Description:
 :** 

- 

Show sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 223](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids

 

 

#### sectionState(stateManager, sectionIds)

 

**Description:
 :** 

- 

Get updated state data related to some section ids.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 793](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state

 
 `sectionIds`

 

array

 

the list of section ids to update

 

 

#### sectionUnselect(stateManager, sectionIds)

 

**Description:
 :** 

- 

Unselect a list of sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 719](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `sectionIds`

 

array

 

the list of cm ids

 

 

#### selectAllBulk(courseEditor, value)

 

**Description:
 :** 

- 

Select/unselect all element of the selected type.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 377](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseEditor`

 

CourseEditor

 

 

 
 `value`

 

Boolean

 

if the elements must be selected or unselected.

 

 

#### selectAndScroll(node)

 

**Description:
 :** 

- 

Set the selection and scroll to the selected element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 164](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `node`

 

node

 

 

 

 

#### set(key, value) → {boolean}

 

**Description:
 :** 

- 

Set a value to local storage. Remember - all values must be strings.

 

**Source:
 :** 

- 
 [lib/amd/src/localstorage.js](lib_amd_src_localstorage.js.md), [line 43](lib_amd_src_localstorage.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

string

 

The cache key to set.

 
 `value`

 

string

 

The value to set.

 

##### Returns:

False if the value can't be saved in the cache, or some other error - true otherwise.

**
 Type

 :** 

boolean

 

#### setBlockProtectState(plugin, state) → {Promise}

 

**Description:
 :** 

- 

Set the block protection state.

 

**Source:
 :** 

- 
 [admin/amd/src/block_management_table.js](admin_amd_src_block_management_table.js.md), [line 35](admin_amd_src_block_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `plugin`

 

string

 

 

 
 `state`

 

number

 

 

 

##### Returns:

**
 Type

 :** 

Promise

 

#### setCourseFavouriteState(courseId, status) → {Promise}

 

**Description:
 :** 

- 

Set the courses favourite status and push to repository

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 447](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

Course id to favourite.

 
 `status`

 

boolean

 

new favourite status.

 

##### Returns:

Repository promise.

**
 Type

 :** 

Promise

 

#### setCourseHiddenState(courseId, status) → {Promise}

 

**Description:
 :** 

- 

Set the courses hidden status and push to repository

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 366](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseId`

 

Number

 

Course id to favourite.

 
 `status`

 

Boolean

 

new hidden status.

 

##### Returns:

Repository promise.

**
 Type

 :** 

Promise

 

#### setDragImage() → {HTMLElement}

 

**Description:
 :** 

- 

Return the custom activity card drag shadow image.

The element returned will be used when the user drags the card.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 85](course_format_amd_src_local_content_section_cmitem.js.md)

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### setDraggable(value)

 

**Description:
 :** 

- 

Enable or disable the draggable property.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 203](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

bool

 

the new draggable value

 

 

#### setDraggable(value)

 

**Description:
 :** 

- 

Enable or disable the draggable property.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 79](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

bool

 

the new draggable value

 

 

#### setDraggable(value)

 

**Description:
 :** 

- 

Enable or disable the draggable property.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 64](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

bool

 

the new draggable value

 

 

#### setElementLocked(target, locked)

 

**Description:
 :** 

- 

Lock/unlock an element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 460](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `target`

 

Element

 

the event target

 
 `locked`

 

boolean

 

the new locked value

 

 

#### setInitialState(initialState)

 

**Description:
 :** 

- 

Loads the initial state.

Note this method will trigger a state changed event with "state:loaded" actionname.

The state mode will be set to read only when the initial state is loaded.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 138](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `initialState`

 

object

 

 

 

 

#### setInitialState(stateData)

 

**Description:
 :** 

- 

Set the initial state.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 144](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateData`

 

object

 

the initial state data.

 

 

#### setLimit(root) → {function}

 

**Description:
 :** 

- 

Return the callback to be passed to the subscribe event

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 535](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

object

 

The root element for the courses view

 

##### Returns:

Partially applied function that'll execute when passed a limit

**
 Type

 :** 

function

 

#### setLoadedAllContent(val)

 

**Description:
 :** 

- 

Set the state of the loaded all content property for the current state
of the popover.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 154](message_output_popup_amd_src_notification_popover_controller.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `val`

 

bool

 

True if all content is loaded, false otherwise

 

 

#### setLogger(logger)

 

**Description:
 :** 

- 

Set the logger class instance.

Reactive instances can provide alternative loggers to provide advanced logging.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 456](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `logger`

 

[Logger](Logger.md)

 

 

 

 

#### setMutations(manager)

 

**Description:
 :** 

- 

Replace the current mutations with a new object.

This method is designed to override the full mutations class, for example by extending
the original one. To add some individual mutations, use addMutations instead.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 177](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `manager`

 

object

 

the new mutations intance

 

 

#### setPageItem(stateManager, type, id, isStatic)

 

**Description:
 :** 

- 

Set the page current item.

Only one element of the course state can be the page item at a time.

There are several actions that can alter the page current item. For example, when the user is in an activity
page, the page item is always the activity one. However, in a course page, when the user scrolls to an element,
this element get the page item.

If the page item is static means that it is not meant to change. This is important because
static page items has some special logic. For example, if a cm is the static page item
and it is inside a collapsed section, the course index will expand the section to make it visible.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 537](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 
 `type`

 

String
|

undefined

 

the element type (section or cm). Undefined will remove the current page item.

 
 `id`

 

Number
|

undefined

 

the element id

 
 `isStatic`

 

boolean
|

undefined

 

if the page item is static

 

 

#### setPluginState(methodname, plugin, state) → {Promise}

 

**Description:
 :** 

- 

Set the plugin state (enabled or disabled)

 

**Source:
 :** 

- 
 [admin/amd/src/plugin_management_table.js](admin_amd_src_plugin_management_table.js.md), [line 96](admin_amd_src_plugin_management_table.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `methodname`

 

string

 

The web service to call

 
 `plugin`

 

string

 

The name of the plugin to set the state for

 
 `state`

 

number

 

The state to set

 

##### Returns:

**
 Type

 :** 

Promise

 

#### setReadOnly(readonly)

 

**Description:
 :** 

- 

Locks or unlocks the state to prevent illegal updates.

Mutations use this method to modify the state. Once the state is updated, they must
block again the state.

All changes done while the state is writable will be registered using registerStateAction.
When the state is set again to read only the method will trigger _publishEvents to communicate
changes to all watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 184](lib_amd_src_local_reactive_statemanager.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `readonly`

 

bool

 

if the state is in read only mode enabled

 

 

#### setStorageValue(key, value) → {boolean}

 

**Description:
 :** 

- 

Stores a value into the course editor static storage if available

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 327](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `key`

 

String

 

the key to store

 
 `value`

 

*

 

the value to store (must be compatible with JSON,stringify)

 

##### Returns:

true if the value is stored

**
 Type

 :** 

boolean

 

#### showCourse(root, courseId)

 

**Description:
 :** 

- 

Show course

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 342](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container

 
 `courseId`

 

Number

 

Course id number

 

 

#### showDropZone()

 

**Description:
 :** 

- 

Display the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 138](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

 

#### showDropZone(dropdata)

 

**Description:
 :** 

- 

Display the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 137](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 

 

#### showDropZone(dropdata)

 

**Description:
 :** 

- 

Display the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 124](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 

 

#### showFavouriteIcon(root, courseId)

 

**Description:
 :** 

- 

Show the favourite icon.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 211](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

Object

 

The course overview container.

 
 `courseId`

 

Number

 

Course id number.

 

 

#### standardFunctionalityCurry() → {function}

 

**Description:
 :** 

- 

The default functionality of fetching paginated courses without special handling.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 654](blocks_myoverview_amd_src_view.js.md)

##### Returns:

**
 Type

 :** 

function

 

#### startDrag(e, details)

 

**Description:
 :** 

- 

Start dragging.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 137](question_type_ordering_amd_src_drag_reorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event which is either mousedown or touchstart.

 
 `details`

 

Object

 

Object with start (boolean flag) and x, y (only if flag true) values

 

 

#### startListeners()

 

**Description:
 :** 

- 

Start the listeners for the list.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 110](question_type_ordering_amd_src_drag_reorder.js.md)

 

#### stateReady()

 

**Description:
 :** 

- 

Initial state ready method.

This method will add all the necessary event listeners to the component depending on the
parent methods.

  - Add drop events to the element if the parent component has validateDropData method.

  - Configure the elements draggable if the parent component has getDraggableData method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 180](lib_amd_src_local_reactive_dragdrop.js.md)

 

#### stateReady()

 

**Description:
 :** 

- 

Reactive module will call this method when the state is ready.

Component can override this method to update/load the component HTML or to bind
listeners to HTML entities.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 182](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/process.js](lib_amd_src_local_process_monitor_process.js.md), [line 70](lib_amd_src_local_process_monitor_process.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [lib/amd/src/local/process_monitor/monitor.js](lib_amd_src_local_process_monitor_monitor.js.md), [line 68](lib_amd_src_local_process_monitor_monitor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 109](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/sectiontitle.js](course_format_amd_src_local_courseindex_sectiontitle.js.md), [line 70](course_format_amd_src_local_courseindex_sectiontitle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 78](course_format_amd_src_local_courseindex_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### (async) stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

This stateReady to be async because it loads the real courseindex.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/placeholder.js](course_format_amd_src_local_courseindex_placeholder.js.md), [line 62](course_format_amd_src_local_courseindex_placeholder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

object

 

the initial state

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 80](course_format_amd_src_local_courseindex_courseindex.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 81](course_format_amd_src_local_courseindex_cm.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the course state.

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 67](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### stateReady()

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittools.js](course_format_amd_src_local_content_bulkedittools.js.md), [line 87](course_format_amd_src_local_content_bulkedittools.js.md)

 

#### stateReady()

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/bulkedittoggler.js](course_format_amd_src_local_content_bulkedittoggler.js.md), [line 67](course_format_amd_src_local_content_bulkedittoggler.js.md)

 

#### stateReady()

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/activity_header.js](course_format_amd_src_local_content_activity_header.js.md), [line 63](course_format_amd_src_local_content_activity_header.js.md)

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 113](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data.

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 62](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the initial state

 

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 59](course_format_amd_src_local_content_section_cmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

the state data

 

 

#### stop()

 

**Description:
 :** 

- 

Stop the timer, if it is running.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 67](mod_assign_amd_src_timer.js.md)

 

#### submitTagCreateUpdateForm(questionId, contextId, formdata) → {promise}

 

**Description:
 :** 

- 

Submit the form data for the question tags form.

 

**Source:
 :** 

- 
 [question/bank/tagquestion/amd/src/repository.js](question_bank_tagquestion_amd_src_repository.js.md), [line 26](question_bank_tagquestion_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `questionId`

 

Number

 

 

 
 `contextId`

 

Number

 

 

 
 `formdata`

 

string

 

The URL encoded values from the form

 

##### Returns:

**
 Type

 :** 

promise

 

#### switchBulkSelection(courseEditor)

 

**Description:
 :** 

- 

Switch the current bulk selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 366](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseEditor`

 

CourseEditor

 

 

 

 

#### toggleBulkSelectionAction(courseEditor, target, event, elementType)

 

**Description:
 :** 

- 

Process a bulk selection toggle action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 337](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseEditor`

 

CourseEditor

 

 

 
 `target`

 

HTMLElement

 

the action element

 
 `event`

 

Event

 

 

 
 `elementType`

 

String

 

cm or section

 

 

#### toggleGroup(item)

 

**Description:
 :** 

- 

Toggle a group item.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 148](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `item`

 

JQuery

 

the jQuery object

 

 

#### unlockAll(stateManager)

 

**Description:
 :** 

- 

Unlock all course elements.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 566](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

[StateManager](StateManager.md)

 

the current state manager

 

 

#### unregister()

 

**Description:
 :** 

- 

Unregister the component from the reactive module.

This method will disable the component logic, event listeners and watchers
but it won't remove any HTML created by the component. However, it will trigger
the destroy hook to allow the component to clean parts of the interface.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 375](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### unregisterComponent(component) → {object}

 

**Description:
 :** 

- 

Unregister a component and its watchers.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 347](lib_amd_src_local_reactive_reactive.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

object

 

the object instance to unregister

 

##### Returns:

the deleted component

**
 Type

 :** 

object

 

#### update()

 

**Description:
 :** 

- 

Function to update the clock with the current time left.

 

**Source:
 :** 

- 
 [mod/assign/amd/src/timer.js](mod_assign_amd_src_timer.js.md), [line 78](mod_assign_amd_src_timer.js.md)

 

#### updateButtonAriaLabel()

 

**Description:
 :** 

- 

Set the correct aria label on the menu toggle button to be read out by screen
readers. The message will indicate the state of the unread notifications.

 

**Source:
 :** 

- 
 [message/output/popup/amd/src/notification_popover_controller.js](message_output_popup_amd_src_notification_popover_controller.js.md), [line 76](message_output_popup_amd_src_notification_popover_controller.js.md)

 

#### updatePreferences(filter, value) → {Promise}

 

**Description:
 :** 

- 

Update the user preference for the block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 37](blocks_myoverview_amd_src_view_nav.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `filter`

 

String

 

The type of filter: display/sort/grouping.

 
 `value`

 

String

 

The current preferred value.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### updateProxy()

 

**Description:
 :** 

- 

Update proxy's position.

 

**Source:
 :** 

- 
 [question/type/ordering/amd/src/drag_reorder.js](question_type_ordering_amd_src_drag_reorder.js.md), [line 201](question_type_ordering_amd_src_drag_reorder.js.md)

 

#### uploadFiles(sectionId, sectionNum, files) → {Promise}

 

**Description:
 :** 

- 

Upload a file list to the course.

This method is a wrapper to the course file uploader.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 285](course_format_amd_src_local_courseeditor_courseeditor.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `sectionId`

 

number

 

the section id

 
 `sectionNum`

 

number

 

the section number

 
 `files`

 

Array

 

and array of files

 

##### Returns:

the file queue promise

**
 Type

 :** 

Promise

 

#### validateDropData(dropdata) → {boolean}

 

**Description:
 :** 

- 

Validate if the drop data can be dropped over the component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 121](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the exported drop data.

 

##### Returns:

**
 Type

 :** 

boolean

 

#### validateDropData(dropdata) → {boolean}

 

**Description:
 :** 

- 

Validate if the drop data can be dropped over the component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 113](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the exported drop data.

 

##### Returns:

**
 Type

 :** 

boolean

 

#### validateDropData(dropdata) → {boolean}

 

**Description:
 :** 

- 

Validate if the drop data can be dropped over the component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 104](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the exported drop data.

 

##### Returns:

**
 Type

 :** 

boolean

 

#### validateDropData(dropdata) → {boolean}

 

**Description:
 :** 

- 

Validate if the drop data can be dropped over the component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 120](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the exported drop data.

 

##### Returns:

**
 Type

 :** 

boolean

 

 

### Type Definitions

 

#### LoggerEntry

 

**Description:
 :** 

- 

Logger entry structure.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/srlogger.js](lib_amd_src_local_reactive_srlogger.js.md), [line 30](lib_amd_src_local_reactive_srlogger.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `feedbackMessage`

 

string

 

Feedback message.

 

Logger entry structure.

##### Type:

- 

object

 

 

#### LoggerEntry

 

**Description:
 :** 

- 

Logger entry structure.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/logger.js](lib_amd_src_local_reactive_logger.js.md), [line 30](lib_amd_src_local_reactive_logger.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `feedbackMessage`

 

string

 

Feedback message.

 

Logger entry structure.

##### Type:

- 

object

 

 

#### ProblemDetail

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 30](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Type:

- 

object

 

 

#### ProblemNode

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 37](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

##### Type:

- 

object

 

 

#### description

 

**Description:
 :** 

- 

The component descriptor data structure.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/reactive.js](lib_amd_src_local_reactive_reactive.js.md), [line 53](lib_amd_src_local_reactive_reactive.js.md)

##### Properties:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `eventName`

 

string

 

 

 

the custom event name used for state changed events

 
 `eventDispatch`

 

function

 

 

 

the state update event dispatch function

 
 `target`

 

Element

 

 

 <optional>  

 

the target of the event dispatch. If not passed a fake element will be created

 
 `mutations`

 

Object

 

 

 <optional>  

 

an object with state mutations functions

 
 `state`

 

Object

 

 

 <optional>  

 

an object to initialize the state.

 

The component descriptor data structure.

##### Type:

- 

object

 

 

#### descriptor

 

**Description:
 :** 

- 

The component descriptor data structure.

This structure is used by any component and init method to define the way the component will interact
with the interface and whith reactive instance operates. The logic behind this object is to avoid
unnecessary dependancies between the final interface and the state logic.

Any component interacts with a single main DOM element (description.element) but it can use internal
selector to select elements within this main element (descriptor.selectors). By default each component
will provide it's own default selectors, but those can be overridden by the "descriptor.selectors"
property in case the mustache wants to reuse the same component logic but with a different interface.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 31](lib_amd_src_local_reactive_basecomponent.js.md)

##### Properties:

 

 Name

 Type

 Attributes

 Description

 

 

 
 `reactive`

 

Reactive

 

 

 

an optional reactive module to register in

 
 `element`

 

DOMElement

 

 

 

all components needs an element to anchor events

 
 `selectors`

 

object

 

 

 <optional>  

 

an optional object to override query selectors

 

The component descriptor data structure.

This structure is used by any component and init method to define the way the component will interact
with the interface and whith reactive instance operates. The logic behind this object is to avoid
unnecessary dependancies between the final interface and the state logic.

Any component interacts with a single main DOM element (description.element) but it can use internal
selector to select elements within this main element (descriptor.selectors). By default each component
will provide it's own default selectors, but those can be overridden by the "descriptor.selectors"
property in case the mustache wants to reuse the same component logic but with a different interface.

##### Type:

- 

object
