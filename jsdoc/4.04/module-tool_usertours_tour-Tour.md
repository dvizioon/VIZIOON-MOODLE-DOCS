# Tour - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-tool_usertours_tour-Tour.html

# Tour

 

## 
 [tool_usertours/tour](module-tool_usertours_tour.md)~

 
 Tour

 

 

 

 

#### new Tour(config)

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 64](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

object

 

The configuration object.

 

 

 

 

### Members

 

#### hasFixedPosition

 

**Description:
 :** 

- 

Check whether the target node has a fixed position, or is nested within one.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1270](admin_tool_usertours_amd_src_tour.js.md)

Check whether the target node has a fixed position, or is nested within one.

 

 

### Methods

 

#### dispatchEvent(eventName, detailopt, cancelableopt) → {CustomEvent}

 

**Description:
 :** 

- 

Fire any event handlers for the specified event.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 602](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `eventName`

 

String

 

 

 

 

 

The name of the event

 
 `detail`

 

Object

 

 

 <optional>  

 

 

 `{}`

 

Any additional details to pass into the eveent

 
 `cancelable`

 

Boolean

 

 

 <optional>  

 

 

 `false`

 

Whether preventDefault() can be called

 

##### Returns:

**
 Type

 :** 

CustomEvent

 

#### getPotentiallyVisibleSteps() → {StepList}

 

**Description:
 :** 

- 

Get potentially visible steps in a tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 380](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

A list of ordered steps

**
 Type

 :** 

StepList

 

#### isCSSAllowed() → {boolean}

 

**Description:
 :** 

- 

Is the browser actually allow CSS styles?

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 427](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

True if the browser is allowing CSS styles

**
 Type

 :** 

boolean
