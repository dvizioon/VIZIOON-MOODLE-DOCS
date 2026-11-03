# qbank_managecategories/events - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-qbank_managecategories_events.html

# qbank_managecategories/events

 

 

 

**Description:
 :** 

- 

Reactive events for qbank_managecategories

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/events.js](question_bank_managecategories_amd_src_events.js.md), [line 18](question_bank_managecategories_amd_src_events.js.md)

 

Reactive events for qbank_managecategories

 

 

 

 

### Methods

 

#### (inner) notifyQbankManagecategoriesStateUpdated(detail, container) → {CustomEvent}

 

**Description:
 :** 

- 

Trigger an event to indicate that the activity state is updated.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/events.js](question_bank_managecategories_amd_src_events.js.md), [line 35](question_bank_managecategories_amd_src_events.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `detail`

 

Object

 

the full state

 
 `container`

 

HTMLElement

 

the custom event target (document if none provided)

 

##### Fires:

- [event:qbankManagecategoriesStateUpdated](module-qbank_managecategories_events.md)

##### Returns:

**
 Type

 :** 

CustomEvent

 

 

### Events

 

#### qbankManagecategoriesStateUpdated

 

**Description:
 :** 

- 

Event triggered when the activity reactive state is updated.

 

**Source:
 :** 

- 
 [question/bank/managecategories/amd/src/events.js](question_bank_managecategories_amd_src_events.js.md), [line 25](question_bank_managecategories_amd_src_events.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `nodes`

 

Array

 

The list of parent nodes which were updated

 

##### Type:

- 

CustomEvent
