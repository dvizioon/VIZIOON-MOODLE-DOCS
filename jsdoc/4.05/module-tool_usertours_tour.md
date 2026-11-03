# tool_usertours/tour - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tool_usertours_tour.html

# tool_usertours/tour

 

 

 

**Description:
 :** 

- 

A user tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 16](admin_tool_usertours_amd_src_tour.js.md)

 

**Copyright:
 :** 

- 2018 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

A user tour.

 

 

 

### Classes

 

**[Tour](module-tool_usertours_tour-Tour.md)
 :[tool_usertours/tour](module-tool_usertours_tour-tool_usertours_tour.md)
 :** 

 

 

 

### Methods

 

#### (inner) accessibilityHide()

 

**Description:
 :** 

- 

Perform accessibility changes for step hidden.

This will remove any newly added aria-hidden="true".

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1794](admin_tool_usertours_amd_src_tour.js.md)

 

#### (inner) accessibilityShow()

 

**Description:
 :** 

- 

Perform accessibility changes for step shown.

This will add aria-hidden="true" to all siblings and parent siblings.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1759](admin_tool_usertours_amd_src_tour.js.md)

 

#### (inner) addEventHandler(eventName, handler) → {Object}

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 616](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `eventName`

 

string

 

The name of the event to listen for

 
 `handler`

 

function

 

The event handler to call

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) addStepToPage(stepConfig) → {Object}

 

**Description:
 :** 

- 

Helper to add a step to the page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 786](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) announceStep(stepConfig) → {Object}

 

**Description:
 :** 

- 

Helper to announce the step on the page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 925](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) calculatePosition(elem) → {String}

 

**Description:
 :** 

- 

Calculate the inheritted position.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1739](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `elem`

 

jQuery

 

The element to calculate position for

 

##### Returns:

Calculated position

**
 Type

 :** 

String

 

#### (inner) calculateScrollTop(stepConfig) → {Number}

 

**Description:
 :** 

- 

Calculate scrollTop.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1283](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) calculateScrollTop(currentStepNode)

 

**Description:
 :** 

- 

Calculate dialogue position for page middle.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1326](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `currentStepNode`

 

jQuery

 

Current step node

 

 

#### (inner) checkMinimumRequirements()

 

**Description:
 :** 

- 

Check that the configuration meets the minimum requirements.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 183](admin_tool_usertours_amd_src_tour.js.md)

 

#### (inner) configure(config) → {Object}

 

**Description:
 :** 

- 

Prepare tour configuration.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 140](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

Object

 

The configuration object.

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) endTour() → {Object}

 

**Description:
 :** 

- 

End the current tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1116](admin_tool_usertours_amd_src_tour.js.md)

##### Fires:

- [event:tool_usertours/tourEnd](module-tool_usertours_events.md)

- [event:tool_usertours/tourEnded](module-tool_usertours_events.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) getCurrentStepNumber() → {Number}

 

**Description:
 :** 

- 

Retrieve the current step number.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 252](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

The current step number

**
 Type

 :** 

Number

 

#### (inner) getNextStepNumber(stepNumber) → {Number}

 

**Description:
 :** 

- 

Get the next step number after the currently displayed step.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 282](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

The current step number

 

##### Returns:

The next step number to display

**
 Type

 :** 

Number

 

#### (inner) getPreviousStepNumber(stepNumber) → {Number}

 

**Description:
 :** 

- 

Get the previous step number before the currently displayed step.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 306](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

The current step number

 

##### Returns:

The previous step number to display

**
 Type

 :** 

Number

 

#### (inner) getStepConfig(stepNumber) → {Object}

 

**Description:
 :** 

- 

Fetch the normalised step configuration for the specified step number.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 521](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

The step number to fetch configuration for

 

##### Returns:

The step configuration

**
 Type

 :** 

Object

 

#### (inner) getStepContainer() → {jQuery}

 

**Description:
 :** 

- 

Return the current step node.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1254](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

**
 Type

 :** 

jQuery

 

#### (inner) getStepTarget(stepConfig) → {$}

 

**Description:
 :** 

- 

Fetch the actual step target from the selector.

This should not be called until after any delay has completed.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 577](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration

 

##### Returns:

**
 Type

 :** 

$

 

#### (inner) getTemplateContent() → {$}

 

**Description:
 :** 

- 

Getter for the template content.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 776](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

**
 Type

 :** 

$

 

#### (inner) gotoStep(stepNumber, direction) → {Object}

 

**Description:
 :** 

- 

Go to the specified step in the tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 460](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

The step number to display

 
 `direction`

 

Number

 

Next or previous step

 

##### Fires:

- [event:tool_usertours/stepRender](module-tool_usertours_events.md)

- [event:tool_usertours/stepRendered](module-tool_usertours_events.md)

- [event:tool_usertours/stepHide](module-tool_usertours_events.md)

- [event:tool_usertours/stepHidden](module-tool_usertours_events.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) handleKeyDown(e)

 

**Description:
 :** 

- 

Handle key down events.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 975](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

EventFacade

 

 

 

 

#### (inner) hide(transition) → {Object}

 

**Description:
 :** 

- 

Hide any currently visible steps.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1149](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `transition`

 

Bool

 

Animate the visibility change

 

##### Fires:

- [event:tool_usertours/stepHide](module-tool_usertours_events.md)

- [event:tool_usertours/stepHidden](module-tool_usertours_events.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) init(config) → {Object}

 

**Description:
 :** 

- 

Initialise the tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 68](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `config`

 

Object

 

The configuration object.

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) isLastStep(stepNumber) → {Boolean}

 

**Description:
 :** 

- 

Is the step the final step number?

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 330](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

Step number to test

 

##### Returns:

Whether the step is the final step

**
 Type

 :** 

Boolean

 

#### (inner) isStepActuallyVisible(stepConfig) → {Boolean}

 

**Description:
 :** 

- 

Is this step actually visible?

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 395](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration to normalise

 

##### Returns:

Whether the step is actually visible

**
 Type

 :** 

Boolean

 

#### (inner) isStepPotentiallyVisible(stepConfig) → {Boolean}

 

**Description:
 :** 

- 

Is this step potentially visible?

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 343](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration to normalise

 

##### Returns:

Whether the step is the potentially visible

**
 Type

 :** 

Boolean

 

#### (inner) next() → {Object}

 

**Description:
 :** 

- 

Go to the next step in the tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 438](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) normalizeStepConfig(stepConfig) → {Object}

 

**Description:
 :** 

- 

Normalise the supplied step configuration.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 542](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration to normalise

 

##### Returns:

The normalised step configuration

**
 Type

 :** 

Object

 

#### (inner) positionBackdrop(stepConfig) → {Object}

 

**Description:
 :** 

- 

Add the backdrop.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1609](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) positionStep(stepConfig) → {Object}

 

**Description:
 :** 

- 

Position the step on the page.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1356](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) previous() → {Object}

 

**Description:
 :** 

- 

Go to the previous step in the tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 449](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) processStepListeners(stepConfig) → {Object}

 

**Description:
 :** 

- 

Process listeners for the step being shown.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 632](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

object

 

The configuration for the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) recalculateBackdropPosition(stepConfig)

 

**Description:
 :** 

- 

Recaculate where the backdrop and its cut-out should be.

This is needed when highlighted elements are off the page.
This can be called on update to recalculate it all.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1594](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

 

#### (inner) recalculatePlacement(stepConfig) → {String}

 

**Description:
 :** 

- 

For left/right placement, checks that there is room for the step at current window size.

If there is not enough room, changes placement to 'top'.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1568](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

The placement after recalculate

**
 Type

 :** 

String

 

#### (inner) renderStep(stepConfig) → {Object}

 

**Description:
 :** 

- 

The standard step renderer.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 705](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) reset() → {Object}

 

**Description:
 :** 

- 

Reset the current tour state.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 111](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) resetStepDefaults(loadOriginalConfiguration) → {Object}

 

**Description:
 :** 

- 

Reset step default configuration.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 200](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `loadOriginalConfiguration`

 

Boolean

 

Whether to load the original configuration supplied with the Tour.

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) resetStepListeners() → {Object}

 

**Description:
 :** 

- 

Reset step listeners.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 686](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) restartTour() → {Object}

 

**Description:
 :** 

- 

Restart the tour from the beginning, resetting the completionlag.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1105](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) revealStep(stepConfig) → {Object}

 

**Description:
 :** 

- 

Make the given step visible.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 893](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepConfig`

 

Object

 

The step configuration of the step

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) setCurrentStepNumber(stepNumber)

 

**Description:
 :** 

- 

Store the current step number.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 262](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepNumber`

 

Number

 

The current step number

 

 

#### (inner) setStepDefaults(stepDefaults) → {Object}

 

**Description:
 :** 

- 

Set the step defaults.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 223](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepDefaults`

 

Object

 

The step defaults to apply to all steps

 

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) show() → {Object}

 

**Description:
 :** 

- 

Show the current steps.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1240](admin_tool_usertours_amd_src_tour.js.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

#### (inner) startTour(startAt) → {Object}

 

**Description:
 :** 

- 

Start the current tour.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 1070](admin_tool_usertours_amd_src_tour.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `startAt`

 

Number

 

Which step number to start at. If not specified, starts at the last point.

 

##### Fires:

- [event:tool_usertours/tourStart](module-tool_usertours_events.md)

- [event:tool_usertours/tourStarted](module-tool_usertours_events.md)

##### Returns:

this.

**
 Type

 :** 

Object

 

 

### Type Definitions

 

#### StepList

 

**Description:
 :** 

- 

A list of steps.

 

**Source:
 :** 

- 
 [admin/tool/usertours/amd/src/tour.js](admin_tool_usertours_amd_src_tour.js.md), [line 24](admin_tool_usertours_amd_src_tour.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `stepId`

 

Number

 

The id of the step in the database

 
 `position`

 

Number

 

The position of the step within the tour (zero-indexed)

 

A list of steps.

##### Type:

- 

Array.<Object>
