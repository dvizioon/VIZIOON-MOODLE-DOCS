# core_calendar/month_navigation_drag_drop - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_calendar_month_navigation_drag_drop.html

# core_calendar/month_navigation_drag_drop

 

 

 

**Description:
 :** 

- 

A javascript module to handle calendar drag and drop in the calendar
month view navigation.

This code is run each time the calendar month view is re-rendered. We
only register the event handlers once per page load so that the in place
DOM updates that happen on month change don't continue to register handlers.

 

**Source:
 :** 

- 
 [calendar/amd/src/month_navigation_drag_drop.js](calendar_amd_src_month_navigation_drag_drop.js.md), [line 16](calendar_amd_src_month_navigation_drag_drop.js.md)

 

**Copyright:
 :** 

- 2017 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to handle calendar drag and drop in the calendar
month view navigation.

This code is run each time the calendar month view is re-rendered. We
only register the event handlers once per page load so that the in place
DOM updates that happen on month change don't continue to register handlers.

 

 

 

 

### Methods

 

#### (inner) init(rootElement)

 

**Description:
 :** 

- 

Initialise the event handlers for the drag events.

 

**Source:
 :** 

- 
 [calendar/amd/src/month_navigation_drag_drop.js](calendar_amd_src_month_navigation_drag_drop.js.md), [line 211](calendar_amd_src_month_navigation_drag_drop.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rootElement`

 

object

 

The element containing calendar nav links
