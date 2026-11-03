# Global - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/global.html

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

 

 

#### (constant) addContextmenuItem

 

**Description:
 :** 

- 

Given a TinyMCE contextmenu configuration, add the specified button to the end.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 179](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE contextmenu configuration, add the specified button to the end.

 

#### (constant) addMenubarItem

 

**Description:
 :** 

- 

Given a TinyMCE Menubar configuration, add the specified button to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 153](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Menubar configuration, add the specified button to the named section.

 

#### (constant) addQuickbarsToolbarItem

 

**Description:
 :** 

- 

Given a TinyMCE quickbars configuration, add items to the meun.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 196](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE quickbars configuration, add items to the meun.

 

#### (constant) addToolbarButton

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, add the specified button to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 63](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, add the specified button to the named section.

 

#### (constant) addToolbarButtons

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, add the specified buttons to the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 89](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, add the specified buttons to the named section.

 

#### (constant) addToolbarSection

 

**Description:
 :** 

- 

Insert a new section into the toolbar.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 116](lib_editor_tiny_amd_src_utils.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 795](blocks_myoverview_amd_src_view.js.md)

Reset the search icon and trigger the init for the block.

 

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
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 235](lib_editor_tiny_amd_src_utils.js.md)

Ensure that the editor is still in the DOM, removing it if it is not.

 

#### (constant) getDocumentationLink

 

**Description:
 :** 

- 

Get the link to the user documentation for the named plugin.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 208](lib_editor_tiny_amd_src_utils.js.md)

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
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 219](lib_editor_tiny_amd_src_utils.js.md)

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
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 135](blocks_myoverview_amd_src_view_nav.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 814](blocks_myoverview_amd_src_view.js.md)

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

 

#### (constant) init

 

**Description:
 :** 

- 

Initialize module

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/sort_columns.js](question_bank_columnsortorder_amd_src_sort_columns.js.md), [line 76](question_bank_columnsortorder_amd_src_sort_columns.js.md)

Initialize module

 

#### isEditing

 

**Description:
 :** 

- 

Return the current edit mode.

Components should use this method to check if edit mode is active.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 166](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 25](course_format_amd_src_local_courseeditor_mutations.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 440](lib_amd_src_local_reactive_basecomponent.js.md)

Set the lock value and locks or unlocks the element.

 

#### locked

 

**Description:
 :** 

- 

Get the current locked value from the element.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 449](lib_amd_src_local_reactive_basecomponent.js.md)

Get the current locked value from the element.

 

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
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 346](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

#### (constant) removeMenubarItems

 

**Description:
 :** 

- 

Given a TinyMCE Menubar configuration, remove the specified menu from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 361](lib_editor_tiny_amd_src_utils.js.md)

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
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 308](lib_editor_tiny_amd_src_utils.js.md)

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
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 256](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, remove the specified button from the named section.

 

#### (constant) removeToolbarButtons

 

**Description:
 :** 

- 

Given a TinyMCE Toolbar configuration, remove the specified buttons from the named section.

 

**Source:
 :** 

- 
 [lib/editor/tiny/amd/src/utils.js](lib_editor_tiny_amd_src_utils.js.md), [line 282](lib_editor_tiny_amd_src_utils.js.md)

Given a TinyMCE Toolbar configuration, remove the specified buttons from the named section.

 

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 839](blocks_myoverview_amd_src_view.js.md)

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

 

#### supportComponents

 

**Description:
 :** 

- 

Return if the current course support components to refresh the content.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 184](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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

 

 

### Methods

 

#### _activityAnchor(event)

 

**Description:
 :** 

- 

The activity anchor event.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 192](course_format_amd_src_local_courseindex_cm.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 400](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

 

 

 

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 193](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 39](course_format_amd_src_local_courseeditor_mutations.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 428](lib_amd_src_local_reactive_dragdrop.js.md)

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

 

 

#### _cancelDebouncedReloadCm(cmId)

 

**Description:
 :** 

- 

Cancel the active reload CM debounced function, if any.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 563](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 175](course_format_amd_src_local_content_actions.js.md)

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

 

 

 

 

#### (async) _cmBasicAction(stateManager, action, cmIds, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Execute a basic course module state action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 104](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 331](course_format_amd_src_local_content.js.md)

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

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 461](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 236](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 612](course_format_amd_src_local_content.js.md)

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

 

#### (async) _createSection(details)

 

**Description:
 :** 

- 

Create a new section instance.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 265](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 636](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 356](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 368](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 486](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 441](course_format_amd_src_local_content_actions.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 268](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 298](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 338](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 320](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 214](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 357](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

the event.

 

 

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 183](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 661](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 317](course_format_amd_src_local_courseindex_courseindex.js.md)

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

 

 

#### _getClosestActionMenuToogler(element) → {HTMLElement|undefined}

 

**Description:
 :** 

- 

Get the closest actions menu toggler to an action element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 504](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 524](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 99](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 445](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 136](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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

 

#### _indexContents()

 

**Description:
 :** 

- 

Regenerate content indexes.

This method is used when a legacy action refresh some content element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 453](course_format_amd_src_local_content.js.md)

 

#### _modalBodyRenderedPromise(modalParams) → {Promise}

 

**Description:
 :** 

- 

Render a modal and return a body ready promise.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 458](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `modalParams`

 

object

 

the modal params

 

##### Returns:

the modal body ready promise

**
 Type

 :** 

Promise

 

#### _prepareFields(stateManager, updateName, fields) → {Object}

 

**Description:
 :** 

- 

Add default values to state elements.

This method is called every time a webservice returns a update state message.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 200](course_format_amd_src_local_courseeditor_mutations.js.md)

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 379](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 561](lib_amd_src_local_reactive_statemanager.js.md)

 

#### _refreshAllSectionsToggler(state)

 

**Description:
 :** 

- 

Refresh the collapse/expand all sections element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 288](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

Object

 

The state data

 

 

#### _refreshCm(param)

 

**Description:
 :** 

- 

Update a course index cm using the state information.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 133](course_format_amd_src_local_courseindex_cm.js.md)

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
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 75](course_format_amd_src_local_content_section_cmitem.js.md)

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
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 168](course_format_amd_src_local_courseindex_cm.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 434](course_format_amd_src_local_content.js.md)

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

 

 

 

 

#### _refreshCourseSectionlist(param)

 

**Description:
 :** 

- 

Refresh the section list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 305](course_format_amd_src_local_courseindex_courseindex.js.md)

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

 

 

 

 

 

 

#### _refreshPageItem(details)

 

**Description:
 :** 

- 

Handle a page item update.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 146](course_format_amd_src_local_courseindex_section.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 214](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 150](course_format_amd_src_local_courseindex_cm.js.md)

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
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 126](course_format_amd_src_local_courseindex_section.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 128](course_format_amd_src_local_content_section.js.md)

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

 

 

 

 

#### _refreshSectionCmlist(param)

 

**Description:
 :** 

- 

Refresh a section cm list.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 417](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 293](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 254](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 159](course_format_amd_src_local_courseindex_courseindex.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 378](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 511](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 582](course_format_amd_src_local_content.js.md)

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

 

 

 

 

#### (async) _requestAddSection(target, event)

 

**Description:
 :** 

- 

Handle a create section request.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 357](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 368](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 260](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 186](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 414](course_format_amd_src_local_content_actions.js.md)

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

 

 

#### _scanIndex(selector, index, creationhandler)

 

**Description:
 :** 

- 

Reindex a content (section or cm) of the course content.

This method is used internally by _indexContents.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 482](course_format_amd_src_local_content.js.md)

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

 

 

#### _scrollHandler()

 

**Description:
 :** 

- 

Check the current page scroll and update the active element if necessary.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 341](course_format_amd_src_local_content.js.md)

 

#### (async) _sectionBasicAction(stateManager, action, sectionIds, targetSectionId, targetCmId)

 

**Description:
 :** 

- 

Execute a basic section state action.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 76](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 163](course_format_amd_src_local_content.js.md)

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

 

 

#### _setAddSectionLocked(locked)

 

**Description:
 :** 

- 

Disable all add sections actions.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 427](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `locked`

 

boolean

 

the new locked value.

 

 

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 319](course_format_amd_src_local_content.js.md)

 

#### (async) _updateActionsMenu(section)

 

**Description:
 :** 

- 

Update a section action menus.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 162](course_format_amd_src_local_content_section.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 149](course_format_amd_src_local_content_section.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `section`

 

object

 

the section state.

 

 

#### _updateStateSectionPreference(stateManager, preferenceName, sectionIds, preferenceValue) → {Array.<Number>|null}

 

**Description:
 :** 

- 

Private batch update for a section preference attribute.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 517](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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

 

#### accessibilityHide()

 

**Description:
 :** 

- 

Restores the aria visibility on the DOM elements changed when displaying
the dialogue popup and makes the dialogue aria hidden to allow screen
readers to navigate the main page correctly when the dialogue is closed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 800](lib_amd_src_modal.js.md)

 

#### accessibilityShow()

 

**Description:
 :** 

- 

Sets the appropriate aria attributes on this dialogue and the other
elements in the DOM to ensure that screen readers are able to navigate
the dialogue popup correctly.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 785](lib_amd_src_modal.js.md)

 

#### activeSearch(clearIcon)

 

**Description:
 :** 

- 

Change the searching icon to its' active state.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 805](blocks_myoverview_amd_src_view.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clearIcon`

 

HTMLElement

 

Our closing icon to manipulate.

 

 

#### addActions(actions)

 

**Description:
 :** 

- 

Add extra actions to the module.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 90](course_format_amd_src_local_content_actions.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `actions`

 

array

 

array of methods to execute

 

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 297](lib_amd_src_local_reactive_basecomponent.js.md)

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

 

 

#### addIconToContainer(container) → {Promise}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 33](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 

##### Returns:

The Promise used to create the icon.

**
 Type

 :** 

Promise

 

#### addIconToContainerWithPromise(container, loadingIconPromise) → {jQuery}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 53](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 
 `loadingIconPromise`

 

Promise

 

The jQuery Promise which determines the removal of the icon

 

##### Returns:

The Promise used to create and then remove the icon.

**
 Type

 :** 

jQuery

 

#### addIconToContainerWithPromise(container) → {Promise}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 85](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 

##### Returns:

A jQuery Promise to resolve when ready

**
 Type

 :** 

Promise

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 301](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 219](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 225](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 187](course_format_amd_src_local_courseeditor_exporter.js.md)

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

 

#### asyncSet(value, setFunction) → {Promise}

 

**Description:
 :** 

- 

Set or resolve and set the value using the function.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 918](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The string or jQuery promise.

 
 `setFunction`

 

function

 

The setter

 

##### Returns:

**
 Type

 :** 

Promise

 

#### attachToDOM()

 

**Description:
 :** 

- 

Attach the modal to the correct part of the page.

If it hasn't already been added it runs any
javascript that has been cached until now.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 135](lib_amd_src_modal.js.md)

 

#### calculateZIndex() → {int}

 

**Description:
 :** 

- 

Determine the highest z-index value currently on the page.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 611](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

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

 

 

 

 

#### checkImage() → {Node}

 

**Description:
 :** 

- 

Check accessiblity issue only for img type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 291](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 307](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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

 

#### cm(state, cminfo) → {Object}

 

**Description:
 :** 

- 

Generate a cm export data from the state.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 96](course_format_amd_src_local_courseeditor_exporter.js.md)

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

 

#### cmCompletion(stateManager, cmIds, complete)

 

**Description:
 :** 

- 

Mark or unmark course modules as complete.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 353](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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

Generate a compoetion export data from the cm element.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 167](course_format_amd_src_local_courseeditor_exporter.js.md)

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

 

#### cmDrag(stateManager, cmIds, dragValue)

 

**Description:
 :** 

- 

Mark or unmark course modules as dragging.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 329](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 114](course_format_amd_src_local_courseeditor_exporter.js.md)

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

 

#### (async) cmHide(stateManager, cmIds)

 

**Description:
 :** 

- 

Hide cms.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 238](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 383](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 266](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 372](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 363](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 229](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 537](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 247](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 48](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 37](course_format_amd_src_local_courseeditor_dndsection.js.md)

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

 

#### countOtherVisibleModals() → {int}

 

**Description:
 :** 

- 

Count the number of other visible modals (not including this one).

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 167](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 572](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

the current state

 

 

#### create(parent)

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 101](lib_amd_src_local_reactive_dragdrop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `parent`

 

BaseComponent

 

the parent component.

 

 

#### create(descriptor)

 

**Description:
 :** 

- 

Component create function.

Default init method will call "create" when all internal attributes are set
but before the component is not yet registered in the reactive module.

In this method any component can define its own defaults such as:

  - this.selectors {object} the default query selectors of this component.

  - this.events {object} a list of event names this component dispatch

  - extract any data from the main dom element (this.element)

  - set any other data the component uses

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 144](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

[descriptor](global.md)

 

the component descriptor

 

 

#### create(descriptor)

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 47](course_format_amd_src_local_content.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

Object

 

the component descriptor

 

 

#### create(descriptor)

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/sectiontitle.js](course_format_amd_src_local_courseindex_sectiontitle.js.md), [line 36](course_format_amd_src_local_courseindex_sectiontitle.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

Object

 

 

 

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 35](course_format_amd_src_local_courseindex_section.js.md)

 

#### create()

 

**Description:
 :** 

- 

Component creation hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/placeholder.js](course_format_amd_src_local_courseindex_placeholder.js.md), [line 50](course_format_amd_src_local_courseindex_placeholder.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/drawer.js](course_format_amd_src_local_courseindex_drawer.js.md), [line 36](course_format_amd_src_local_courseindex_drawer.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/courseindex.js](course_format_amd_src_local_courseindex_courseindex.js.md), [line 35](course_format_amd_src_local_courseindex_courseindex.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 41](course_format_amd_src_local_courseindex_cm.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 34](course_format_amd_src_local_content_section.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/activity_header.js](course_format_amd_src_local_content_activity_header.js.md), [line 39](course_format_amd_src_local_content_activity_header.js.md)

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 62](course_format_amd_src_local_content_actions.js.md)

 

#### create(descriptor)

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 36](course_format_amd_src_local_content_section_header.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

Object

 

 

 

 

#### create()

 

**Description:
 :** 

- 

Constructor hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 34](course_format_amd_src_local_content_section_cmitem.js.md)

 

#### createWarnings(description, nodes, isImageType) → {Array.<[ProblemDetail](global.md)>}

 

**Description:
 :** 

- 

Generate the data that describes the issues found.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 210](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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

Remove this modal from the DOM.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 773](lib_amd_src_modal.js.md)

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 156](lib_amd_src_local_reactive_basecomponent.js.md)

 

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 63](course_format_amd_src_local_courseeditor_dndsection.js.md)

 

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
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 238](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 411](lib_amd_src_local_reactive_basecomponent.js.md)

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 388](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### dragEnd(dropdata)

 

**Description:
 :** 

- 

The element end start hook.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 90](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 97](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 75](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 81](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 88](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 66](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the dropdata

 

 

#### drop(dropdata)

 

**Description:
 :** 

- 

Drop event handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 139](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 

 

#### drop(dropdata)

 

**Description:
 :** 

- 

Drop event handler.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 155](course_format_amd_src_local_courseeditor_dndsection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropdata`

 

Object

 

the accepted drop data

 

 

#### drop(dropdata)

 

**Description:
 :** 

- 

Drop event handler.

 

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
 [lib/amd/src/modal_registry.js](lib_amd_src_modal_registry.js.md), [line 30](lib_amd_src_modal_registry.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 204](blocks_myoverview_amd_src_view.js.md)

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

 

#### getBackdrop() → {object}

 

**Description:
 :** 

- 

Get the modal backdrop.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 187](lib_amd_src_modal.js.md)

##### Returns:

jQuery promise

**
 Type

 :** 

object

 

#### getBody() → {object}

 

**Description:
 :** 

- 

Get the modal body element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 237](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getBodyPromise() → {object}

 

**Description:
 :** 

- 

Get a promise resolving to the body region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 267](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getClasses() → {Object}

 

**Description:
 :** 

- 

Return the component drag and drop CSS classes.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 157](lib_amd_src_local_reactive_dragdrop.js.md)

##### Returns:

the dragdrop css classes

**
 Type

 :** 

Object

 

#### getColumnOrder(listRoot) → {Array}

 

**Description:
 :** 

- 

Gets the newly reordered columns to display in the question bank view.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/sort_columns.js](question_bank_columnsortorder_amd_src_sort_columns.js.md), [line 65](question_bank_columnsortorder_amd_src_sort_columns.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `listRoot`

 

Element

 

 

 

##### Returns:

**
 Type

 :** 

Array

 

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 157](blocks_myoverview_amd_src_view.js.md)

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

 

#### (async) getDialogueContent() → {Promise.<Array>}

 

**Description:
 :** 

- 

Return the dialogue content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 128](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 84](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 488](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 208](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 125](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 175](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 136](blocks_myoverview_amd_src_view.js.md)

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

 

#### getFilterValues(root) → {filters}

 

**Description:
 :** 

- 

Get filter values from DOM.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 71](blocks_myoverview_amd_src_view.js.md)

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

 

#### getFooter() → {object}

 

**Description:
 :** 

- 

Get the modal footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 247](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getFooterPromise() → {object}

 

**Description:
 :** 

- 

Get a promise resolving to the footer region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 277](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getHideCourseMenuItem(root, courseId) → {Object}

 

**Description:
 :** 

- 

Get the action menu item

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 272](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 116](course_format_amd_src_local_courseindex_section.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 77](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 113](course_format_amd_src_local_content_section.js.md)

##### Returns:

**
 Type

 :** 

element
|

null

 

#### getModal() → {object}

 

**Description:
 :** 

- 

Get the modal element of this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 217](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getModalCount() → {int}

 

**Description:
 :** 

- 

Get the unique modal count.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 287](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

int

 

#### getMyCourses(filters, limit) → {promise}

 

**Description:
 :** 

- 

Get enrolled courses from backend.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 98](blocks_myoverview_amd_src_view.js.md)

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

 

#### getPagedContentContainer(root, index) → {Object}

 

**Description:
 :** 

- 

Get the paged content container element.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 147](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 215](blocks_myoverview_amd_src_view.js.md)

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

 

#### getRoot() → {object}

 

**Description:
 :** 

- 

Get the root element of this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 207](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getSearchMyCourses(filters, limit, searchValue) → {promise}

 

**Description:
 :** 

- 

Search for enrolled courses from backend.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 117](blocks_myoverview_amd_src_view.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 231](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 141](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 283](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 199](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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

 

#### getTitle() → {object}

 

**Description:
 :** 

- 

Get the modal title element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 227](lib_amd_src_modal.js.md)

##### Returns:

jQuery object

**
 Type

 :** 

object

 

#### getTitlePromise() → {Promise}

 

**Description:
 :** 

- 

Get a promise resolving to the title region.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 257](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### getWarnings() → {Array.<[ProblemDetail](global.md)>}

 

**Description:
 :** 

- 

Find all problems with the content editable region.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 178](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 171](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 212](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 103](course_format_amd_src_local_courseindex_section.js.md)

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
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 118](course_format_amd_src_local_courseindex_cm.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 88](course_format_amd_src_local_content_section.js.md)

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
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 127](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 62](course_format_amd_src_local_content_section_cmitem.js.md)

##### Returns:

of watchers

**
 Type

 :** 

Array

 

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

 

#### hasFocus() → {bool}

 

**Description:
 :** 

- 

Check if this modal has focus.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 645](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### hasFooterContent() → {bool}

 

**Description:
 :** 

- 

Check if the footer has any content in it.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 521](lib_amd_src_modal.js.md)

##### Returns:

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

 

#### hasTransitions() → {bool}

 

**Description:
 :** 

- 

Check if this modal has CSS transitions applied.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 656](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### hide()

 

**Description:
 :** 

- 

Hide this modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 734](lib_amd_src_modal.js.md)

 

#### hideCourse(root, courseId)

 

**Description:
 :** 

- 

Hide course

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 293](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 130](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

 

#### hideDropZone()

 

**Description:
 :** 

- 

Hide the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 144](course_format_amd_src_local_courseeditor_dndsection.js.md)

 

#### hideDropZone()

 

**Description:
 :** 

- 

Hide the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 115](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

 

#### hideElement(root, id)

 

**Description:
 :** 

- 

Reset the loadedPages dataset to take into account the hidden element

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 362](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 167](blocks_myoverview_amd_src_view.js.md)

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

 

 

#### hideFooter()

 

**Description:
 :** 

- 

Hide the footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 531](lib_amd_src_modal.js.md)

 

#### hideIfNotForm()

 

**Description:
 :** 

- 

Hide this modal if it does not contain a form.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 722](lib_amd_src_modal.js.md)

 

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 672](blocks_myoverview_amd_src_view.js.md)

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

 

#### isLarge() → {bool}

 

**Description:
 :** 

- 

Check if the modal is a large modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 562](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### isSmall() → {bool}

 

**Description:
 :** 

- 

Check if the modal is a small modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 585](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### isVisible() → {bool}

 

**Description:
 :** 

- 

Check if this modal is visible.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 635](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

bool

 

#### itemsPerPageFunc(pagingLimit, root) → {Array.<Number>}

 

**Description:
 :** 

- 

Figure out how many items are going to be allowed to be rendered in the block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 538](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 71](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 457](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 567](blocks_myoverview_amd_src_view.js.md)

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
 [lib/amd/src/modal_registry.js](lib_amd_src_modal_registry.js.md), [line 41](lib_amd_src_modal_registry.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 430](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

self

 

the component to register.

 

 

#### registerCloseOnCancel()

 

**Description:
 :** 

- 

Register a listener to close the dialogue when the cancel button is pressed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 872](lib_amd_src_modal.js.md)

 

#### registerCloseOnSave()

 

**Description:
 :** 

- 

Register a listener to close the dialogue when the save button is pressed.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 895](lib_amd_src_modal.js.md)

 

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

Set up all of the event handling for the modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 815](lib_amd_src_modal.js.md)

 

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 731](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 526](blocks_myoverview_amd_src_view.js.md)

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

 

 

#### registerSelector(root)

 

**Description:
 :** 

- 

Event listener for the Display filter (cards, list).

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 62](blocks_myoverview_amd_src_view_nav.js.md)

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
 [lib/amd/src/local/reactive/statemanager.js](lib_amd_src_local_reactive_statemanager.js.md), [line 511](lib_amd_src_local_reactive_statemanager.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 362](lib_amd_src_local_reactive_basecomponent.js.md)

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 349](lib_amd_src_local_reactive_basecomponent.js.md)

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 329](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 248](blocks_myoverview_amd_src_view.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 264](lib_amd_src_local_reactive_basecomponent.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 473](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 617](blocks_myoverview_amd_src_view.js.md)

 

#### searchFunctionalityCurry() → {function}

 

**Description:
 :** 

- 

Initialize the searching functionality so we can call it when required.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 649](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 72](course_format_amd_src_local_courseeditor_exporter.js.md)

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 495](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 316](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 341](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 147](course_format_amd_src_local_courseeditor_exporter.js.md)

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 211](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 475](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 394](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 284](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

the current state manager

 
 `sectionIds`

 

array

 

the list of section ids to move

 
 `targetSectionId`

 

number

 

the target section id

 

 

#### (async) sectionShow(stateManager, sectionIds)

 

**Description:
 :** 

- 

Show sections.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 220](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 552](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

the current state

 
 `sectionIds`

 

array

 

the list of section ids to update

 

 

#### selectAndScroll(node)

 

**Description:
 :** 

- 

Set the selection and scroll to the selected element.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/accessibilitychecker/amd/src/checker.js](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md), [line 166](lib_editor_tiny_plugins_accessibilitychecker_amd_src_checker.js.md)

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

 

#### setBody(value)

 

**Description:
 :** 

- 

Set the modal body element.

This method is overloaded to take either a string value for the body or a jQuery promise that is resolved with
HTML and Javascript most commonly from a Templates.render call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 317](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The body string or jQuery promise which resolves to the body.

 

##### Fires:

- [event:filterContentUpdated](module-core_filters_events.md)

 

#### setCourseFavouriteState(courseId, status) → {Promise}

 

**Description:
 :** 

- 

Set the courses favourite status and push to repository

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 426](blocks_myoverview_amd_src_view.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 340](blocks_myoverview_amd_src_view.js.md)

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

 

#### setDraggable(value)

 

**Description:
 :** 

- 

Enable or disable the draggable property.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 190](lib_amd_src_local_reactive_dragdrop.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 459](lib_amd_src_local_reactive_basecomponent.js.md)

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

 

 

#### setFooter(value)

 

**Description:
 :** 

- 

Set the modal footer element. The footer element is made visible, if it
isn't already.

This method is overloaded to take either a string
value for the body or a jQuery promise that is resolved with HTML and Javascript
most commonly from a Templates.render call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 467](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The footer string or jQuery promise

 

 

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

 

 

#### setLarge()

 

**Description:
 :** 

- 

Mark the modal as a large modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 549](lib_amd_src_modal.js.md)

 

#### setLimit(root) → {function}

 

**Description:
 :** 

- 

Return the callback to be passed to the subscribe event

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 514](blocks_myoverview_amd_src_view.js.md)

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

 

 

#### setOrder(columns) → {Promise}

 

**Description:
 :** 

- 

Call external function set_order - inserts the updated column in the config_plugins table.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/sort_columns.js](question_bank_columnsortorder_amd_src_sort_columns.js.md), [line 55](question_bank_columnsortorder_amd_src_sort_columns.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `columns`

 

String

 

String that contains column order.

 

##### Returns:

**
 Type

 :** 

Promise

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 427](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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

 

 

#### setScrollable(value)

 

**Description:
 :** 

- 

Set this modal to be scrollable or not.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 595](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

bool

 

Whether the modal is scrollable or not

 

 

#### setSmall()

 

**Description:
 :** 

- 

Mark the modal as a small modal.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 572](lib_amd_src_modal.js.md)

 

#### setStorageValue(key, value) → {boolean}

 

**Description:
 :** 

- 

Stores a value into the course editor static storage if available

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/courseeditor.js](course_format_amd_src_local_courseeditor_courseeditor.js.md), [line 226](course_format_amd_src_local_courseeditor_courseeditor.js.md)

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

 

#### setTitle(value)

 

**Description:
 :** 

- 

Set the modal title element.

This method is overloaded to take either a string value for the title or a jQuery promise that is resolved with
HTML most commonly from a Str.get_string call.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 297](lib_amd_src_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

string
|

object

 

The title string or jQuery promise which resolves to the title.

 

 

#### setupSortableLists(listRoot)

 

**Description:
 :** 

- 

Sets up sortable list in the column sort order page.

 

**Source:
 :** 

- 
 [question/bank/columnsortorder/amd/src/sort_columns.js](question_bank_columnsortorder_amd_src_sort_columns.js.md), [line 33](question_bank_columnsortorder_amd_src_sort_columns.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `listRoot`

 

Element

 

 

 

 

#### show() → {Promise}

 

**Description:
 :** 

- 

Display this modal. The modal will be attached to the DOM if it hasn't
already been.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 675](lib_amd_src_modal.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### showCourse(root, courseId)

 

**Description:
 :** 

- 

Show course

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 316](blocks_myoverview_amd_src_view.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 123](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

 

#### showDropZone(dropdata)

 

**Description:
 :** 

- 

Display the component dropzone.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 125](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 104](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

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
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 185](blocks_myoverview_amd_src_view.js.md)

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

 

 

#### showFooter()

 

**Description:
 :** 

- 

Show the footer element.

 

**Source:
 :** 

- 
 [lib/amd/src/modal.js](lib_amd_src_modal.js.md), [line 540](lib_amd_src_modal.js.md)

 

#### standardFunctionalityCurry() → {function}

 

**Description:
 :** 

- 

The default functionality of fetching paginated courses without special handling.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view.js](blocks_myoverview_amd_src_view.js.md), [line 629](blocks_myoverview_amd_src_view.js.md)

##### Returns:

**
 Type

 :** 

function

 

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
 [lib/amd/src/local/reactive/dragdrop.js](lib_amd_src_local_reactive_dragdrop.js.md), [line 169](lib_amd_src_local_reactive_dragdrop.js.md)

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 181](lib_amd_src_local_reactive_basecomponent.js.md)

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content.js](course_format_amd_src_local_content.js.md), [line 106](course_format_amd_src_local_content.js.md)

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
 [course/format/amd/src/local/courseindex/section.js](course_format_amd_src_local_courseindex_section.js.md), [line 77](course_format_amd_src_local_courseindex_section.js.md)

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
 [course/format/amd/src/local/courseindex/cm.js](course_format_amd_src_local_courseindex_cm.js.md), [line 80](course_format_amd_src_local_courseindex_cm.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 65](course_format_amd_src_local_content_section.js.md)

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
 [course/format/amd/src/local/content/activity_header.js](course_format_amd_src_local_content_activity_header.js.md), [line 63](course_format_amd_src_local_content_activity_header.js.md)

 

#### stateReady(state)

 

**Description:
 :** 

- 

Initial state ready method.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions.js](course_format_amd_src_local_content_actions.js.md), [line 105](course_format_amd_src_local_content_actions.js.md)

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
 [course/format/amd/src/local/content/section/header.js](course_format_amd_src_local_content_section_header.js.md), [line 53](course_format_amd_src_local_content_section_header.js.md)

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
 [course/format/amd/src/local/content/section/cmitem.js](course_format_amd_src_local_content_section_cmitem.js.md), [line 52](course_format_amd_src_local_content_section_cmitem.js.md)

 

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
 [course/format/amd/src/local/courseeditor/mutations.js](course_format_amd_src_local_courseeditor_mutations.js.md), [line 456](course_format_amd_src_local_courseeditor_mutations.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stateManager`

 

StateManager

 

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 374](lib_amd_src_local_reactive_basecomponent.js.md)

 

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

 

#### updatePreferences(filter, value)

 

**Description:
 :** 

- 

Update the user preference for the block.

 

**Source:
 :** 

- 
 [blocks/myoverview/amd/src/view_nav.js](blocks_myoverview_amd_src_view_nav.js.md), [line 35](blocks_myoverview_amd_src_view_nav.js.md)

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

 

 

#### validateDropData(dropdata) → {boolean}

 

**Description:
 :** 

- 

Validate if the drop data can be dropped over the component.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/dndsectionitem.js](course_format_amd_src_local_courseeditor_dndsectionitem.js.md), [line 110](course_format_amd_src_local_courseeditor_dndsectionitem.js.md)

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
 [course/format/amd/src/local/courseeditor/dndsection.js](course_format_amd_src_local_courseeditor_dndsection.js.md), [line 107](course_format_amd_src_local_courseeditor_dndsection.js.md)

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
 [course/format/amd/src/local/courseeditor/dndcmitem.js](course_format_amd_src_local_courseeditor_dndcmitem.js.md), [line 95](course_format_amd_src_local_courseeditor_dndcmitem.js.md)

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
 [course/format/amd/src/local/content/section.js](course_format_amd_src_local_content_section.js.md), [line 100](course_format_amd_src_local_content_section.js.md)

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
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 30](lib_amd_src_local_reactive_basecomponent.js.md)

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
