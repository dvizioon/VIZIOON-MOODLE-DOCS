# core_calendar/event_form - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_calendar_event_form.html

# core_calendar/event_form

 

 

 

**Description:
 :** 

- 

A javascript module to enhance the event form.

 

**Source:
 :** 

- 
 [calendar/amd/src/event_form.js](calendar_amd_src_event_form.js.md), [line 16](calendar_amd_src_event_form.js.md)

 

**Copyright:
 :** 

- 2017 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A javascript module to enhance the event form.

 

 

 

 

### Methods

 

#### (inner) addCourseGroupSelectListeners(formElement)

 

**Description:
 :** 

- 

Listen for when the user changes the group course when configuring
a group event and filter the options in the group select to only
show the groups available within the course the user has selected.

 

**Source:
 :** 

- 
 [calendar/amd/src/event_form.js](calendar_amd_src_event_form.js.md), [line 31](calendar_amd_src_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formElement`

 

object

 

The root form element

 

 

#### (inner) init(formId)

 

**Description:
 :** 

- 

Initialise all of the form enhancements.

 

**Source:
 :** 

- 
 [calendar/amd/src/event_form.js](calendar_amd_src_event_form.js.md), [line 66](calendar_amd_src_event_form.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `formId`

 

string

 

The value of the form's id attribute
