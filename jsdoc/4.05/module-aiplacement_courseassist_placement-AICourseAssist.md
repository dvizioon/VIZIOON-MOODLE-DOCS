# AICourseAssist - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-aiplacement_courseassist_placement-AICourseAssist.html

# AICourseAssist

 

## 
 [aiplacement_courseassist/placement](module-aiplacement_courseassist_placement.md)~

 
 AICourseAssist

 

 

 

 

#### new AICourseAssist(userId, contextId)

 

**Description:
 :** 

- 

Constructor.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 55](ai_placement_courseassist_amd_src_placement.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `userId`

 

Integer

 

The user ID.

 
 `contextId`

 

Integer

 

The context ID.

 

 

 

 

### Members

 

#### contextId :Integer

 

**Description:
 :** 

- 

The context ID.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 48](ai_placement_courseassist_amd_src_placement.js.md)

The context ID.

##### Type:

- 

Integer

 

 

#### userId :Integer

 

**Description:
 :** 

- 

The user ID.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 43](ai_placement_courseassist_amd_src_placement.js.md)

The user ID.

##### Type:

- 

Integer

 

 

 

### Methods

 

#### acceptPolicy() → {Promise.<Object>}

 

**Description:
 :** 

- 

Accept the policy.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 280](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

**
 Type

 :** 

Promise.<Object>

 

#### addPadding()

 

**Description:
 :** 

- 

Add padding to the page to make space for the AI drawer.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 255](ai_placement_courseassist_amd_src_placement.js.md)

 

#### closeAIDrawer()

 

**Description:
 :** 

- 

Close the AI drawer.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 223](ai_placement_courseassist_amd_src_placement.js.md)

 

#### displayError()

 

**Description:
 :** 

- 

Display the error.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 368](ai_placement_courseassist_amd_src_placement.js.md)

 

#### displayLoading()

 

**Description:
 :** 

- 

Display the loading spinner.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 306](ai_placement_courseassist_amd_src_placement.js.md)

 

#### displayPolicy()

 

**Description:
 :** 

- 

Display the policy.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 295](ai_placement_courseassist_amd_src_placement.js.md)

 

#### displayResponse(content)

 

**Description:
 :** 

- 

Display the response.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 356](ai_placement_courseassist_amd_src_placement.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `content`

 

String

 

The content to display.

 

 

#### (async) displaySummary()

 

**Description:
 :** 

- 

Display the summary.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 317](ai_placement_courseassist_amd_src_placement.js.md)

 

#### getTextContent() → {String}

 

**Description:
 :** 

- 

Get the text content of the main region.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 380](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

The text content.

**
 Type

 :** 

String

 

#### hasGeneratedContent() → {boolean}

 

**Description:
 :** 

- 

Check if the AI drawer has generated content or not.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 288](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

True if the AI drawer has generated content, false otherwise.

**
 Type

 :** 

boolean

 

#### isAIDrawerOpen() → {boolean}

 

**Description:
 :** 

- 

Check if the AI drawer is open.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 180](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

True if the AI drawer is open, false otherwise.

**
 Type

 :** 

boolean

 

#### (async) isPolicyAccepted() → {bool}

 

**Description:
 :** 

- 

Check if the policy is accepted.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 272](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

True if the policy is accepted, false otherwise.

**
 Type

 :** 

bool

 

#### isRequestCancelled() → {boolean}

 

**Description:
 :** 

- 

Check if the request is cancelled.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 188](ai_placement_courseassist_amd_src_placement.js.md)

##### Returns:

True if the request is cancelled, false otherwise.

**
 Type

 :** 

boolean

 

#### openAIDrawer()

 

**Description:
 :** 

- 

Open the AI drawer.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 199](ai_placement_courseassist_amd_src_placement.js.md)

 

#### registerErrorEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the error.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 140](ai_placement_courseassist_amd_src_placement.js.md)

 

#### registerEventListeners()

 

**Description:
 :** 

- 

Register event listeners.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 73](ai_placement_courseassist_amd_src_placement.js.md)

 

#### registerPolicyEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the policy.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 118](ai_placement_courseassist_amd_src_placement.js.md)

 

#### registerResponseEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the response.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 154](ai_placement_courseassist_amd_src_placement.js.md)

 

#### removePadding()

 

**Description:
 :** 

- 

Remove padding from the page.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 263](ai_placement_courseassist_amd_src_placement.js.md)

 

#### toggleAIDrawer()

 

**Description:
 :** 

- 

Toggle the AI drawer.

 

**Source:
 :** 

- 
 [ai/placement/courseassist/amd/src/placement.js](ai_placement_courseassist_amd_src_placement.js.md), [line 244](ai_placement_courseassist_amd_src_placement.js.md)
