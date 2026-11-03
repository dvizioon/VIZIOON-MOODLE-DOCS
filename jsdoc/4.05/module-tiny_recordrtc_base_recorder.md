# module:tiny_recordrtc/base_recorder - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-tiny_recordrtc_base_recorder.html

# module:tiny_recordrtc/base_recorder

 

## 

 module:tiny_recordrtc/base_recorder

 

 

The RecordRTC base class for audio, video, and any other future types

 

 

 

 

## Constructor

#### new (require("tiny_recordrtc/base_recorder"))(editor, modal)

 

**Description:
 :** 

- 

Constructor for the RecordRTC class

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 40](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `editor`

 

TinyMCE

 

The Editor to which the content will be inserted

 
 `modal`

 

Modal

 

The Moodle Modal that contains the interface used for recording

 

 

 

 

### Methods

 

#### (async) captureUserMedia()

 

**Description:
 :** 

- 

Start capturing the User Media and handle success or failure of the capture.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 213](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### checkAndWarnAboutBrowserCompatibility() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser is compatible with capturing media, and display a warning if not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 613](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### cleanupStream()

 

**Description:
 :** 

- 

Clean up the stream.

This involves stopping any track which is still active.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 816](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### clearButtonTimer()

 

**Description:
 :** 

- 

Clear the timer for the stop recording button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 715](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### close()

 

**Description:
 :** 

- 

Close the modal and stop recording.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 385](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### configurePlayer() → {HTMLElement}

 

**Description:
 :** 

- 

Get the Player element for this type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 97](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

The player element, typically an audio or video tag.

**
 Type

 :** 

HTMLElement

 

#### getButtonContainer(purpose) → {HTMLElement}

 

**Description:
 :** 

- 

Helper to get the container that a button is in.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 577](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `purpose`

 

string

 

The button purpose

 

##### Returns:

**
 Type

 :** 

HTMLElement

 

#### getEmbedTemplateContext(templateContext) → {Object}

 

**Description:
 :** 

- 

Add or modify the template parameters for the specified type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 1014](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `templateContext`

 

Object

 

The Tempalte context to use

 

##### Returns:

The finalised template context

**
 Type

 :** 

Object

 

#### getEmbedTemplateName() → {string}

 

**Description:
 :** 

- 

Get the name of the template used when embedding the URL in the editor content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 166](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

string

 

#### getFileName(prefix) → {string}

 

**Description:
 :** 

- 

Get a filename for the generated file.

Typically this function will take a prefix and add a type-specific suffix such as the extension to it.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 130](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `prefix`

 

string

 

The prefix for the filename generated by the recorder.

 

##### Returns:

**
 Type

 :** 

string

 

#### getMaxUploadSize() → {number}

 

**Description:
 :** 

- 

Get the maximum file size that can be uploaded.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 779](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

The max byte size

**
 Type

 :** 

number

 

#### getMediaConstraints() → {Object}

 

**Description:
 :** 

- 

Get a list of constraints as required by the getUserMedia() function.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 140](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

**See:
 :** 

- [https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#constraints](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)

 

##### Returns:

**
 Type

 :** 

Object

 

#### getParsedRecordingOptions() → {object}

 

**Description:
 :** 

- 

Get the options for the MediaRecorder.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 186](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

The options for the MediaRecorder instance.

**
 Type

 :** 

object

 

#### getRecordingOptions() → {Object}

 

**Description:
 :** 

- 

Get any recording options passed into the MediaRecorder.
Please note that the mimeType will be fetched from getSupportedTypes().

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 118](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

**See:
 :** 

- [https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/MediaRecorder#options](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/MediaRecorder)

 

##### Returns:

**
 Type

 :** 

Object

 

#### getSupportedTypes() → {Array.<string>}

 

**Description:
 :** 

- 

Get the list of supported mimetypes for this recorder.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 107](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

**See:
 :** 

- [https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/isTypeSupported](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/isTypeSupported)

 

##### Returns:

The list of supported mimetypes.

**
 Type

 :** 

Array.<string>

 

#### getTimeLimit() → {number}

 

**Description:
 :** 

- 

Get the time limit for this recording type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 157](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

The time limit in seconds.

**
 Type

 :** 

number

 

#### getTimeRemaining() → {Object}

 

**Description:
 :** 

- 

Get the time remaining for the recording.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 755](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

The minutes and seconds remaining.

**
 Type

 :** 

Object

 

#### handleCaptureFailure(error)

 

**Description:
 :** 

- 

Handle failure to capture the User Media.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 373](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `error`

 

Error

 

 

 

 

#### handleCaptureSuccess(stream)

 

**Description:
 :** 

- 

Handle successful capture of the User Media.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 276](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stream`

 

MediaStream

 

The stream as captured by the User Media.

 

 

#### handleDataAvailable(event)

 

**Description:
 :** 

- 

Handle the mediaRecorder `dataavailable` event.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 873](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

Event

 

 

 

 

#### handleModalClick(event)

 

**Description:
 :** 

- 

Handle a click within the Modal.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 465](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

The click event

 

 

#### handlePaused()

 

**Description:
 :** 

- 

Handle the mediaRecorder `pause` event.

This event is called when the recording pauses.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 853](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handlePlayerError()

 

**Description:
 :** 

- 

Handle the player `error` event.

This event is called when the player throws an error.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 410](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handlePlayerLoadedMetadata()

 

**Description:
 :** 

- 

Handles the event when the player's metadata has been loaded.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 423](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleRecordingPauseResumeRequested()

 

**Description:
 :** 

- 

Handle the click event for the recording pause/resume button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 497](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleRecordingStartStopRequested()

 

**Description:
 :** 

- 

Handle the click event for the recording start/stop button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 486](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleResume()

 

**Description:
 :** 

- 

Handle the mediaRecorder `resume` event.

This event is called when the recording resumes.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 863](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleStarted()

 

**Description:
 :** 

- 

Handle the mediaRecorder `start` event.

This event is called when the recording starts.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 840](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleStopped()

 

**Description:
 :** 

- 

Handle the mediaRecorder `stop` event.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 827](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### hasData() → {boolean}

 

**Description:
 :** 

- 

Whether any data has been recorded.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 925](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### (async) insertMedia(source)

 

**Description:
 :** 

- 

Insert the HTML to embed the recording into the editor content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 998](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

string

 

The URL to view the media.

 

 

#### isPaused() → {boolean}

 

**Description:
 :** 

- 

Check whether the recording is paused.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 916](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### isReady() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser is compatible.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 84](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### isRecording() → {boolean}

 

**Description:
 :** 

- 

Check whether the recording is in progress.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 907](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### (async) onMediaStopped()

 

**Description:
 :** 

- 

Handle the media stream after it has finished.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 510](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) outsideClickHandler(event)

 

**Description:
 :** 

- 

Prevent the Modal from closing when recording is on process.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 436](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

The click event

 

 

#### pauseButtonTimer()

 

**Description:
 :** 

- 

Pause the timer for the stop recording button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 727](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### playOnCapture() → {boolean}

 

**Description:
 :** 

- 

Whether to start playing the recording as it is captured.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 148](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

Whether to start playing the recording as it is captured.

**
 Type

 :** 

boolean

 

#### prefetchContent()

 

**Description:
 :** 

- 

Prefetch some of the content that will be used in the UI.

Note: not all of the strings used are pre-fetched.
Some of the strings will be fetched because their template is used.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 228](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) recordAgainConfirmation() → {Promise.<boolean>}

 

**Description:
 :** 

- 

Confirm whether the user wants to reset the existing recoring.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 980](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

Whether the user confirmed the reset.

**
 Type

 :** 

Promise.<boolean>

 

#### requestRecordingStop()

 

**Description:
 :** 

- 

Stop the recording.
Please note that this should only stop the recording.
Anything related to processing the recording should be handled by the
mediaRecorder's stopped event handler which is processed after it has stopped.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 789](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) setPauseButtonTextFromString(string)

 

**Description:
 :** 

- 

Set the text of the pause button using a language string.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 691](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `string`

 

string

 

The string identifier

 

 

#### setPauseButtonVisibility(visible)

 

**Description:
 :** 

- 

Configure button visibility for the pause button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 330](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `visible`

 

boolean

 

Set the visibility of the button.

 

 

#### setPlayerState(state)

 

**Description:
 :** 

- 

Sets the state of the audio player, including visibility, muting, and controls.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 360](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `state`

 

boolean

 

A boolean indicating the audio player state.

 

 

#### setRecordButtonState(enabled)

 

**Description:
 :** 

- 

Enable the record button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 311](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `enabled`

 

boolean
|

null

 

Set the button state

 

 

#### (async) setRecordButtonTextFromString(string)

 

**Description:
 :** 

- 

Set the text of the record button using a language string.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 682](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `string`

 

string

 

The string identifier

 

 

#### setRecordButtonVisibility(visible)

 

**Description:
 :** 

- 

Configure button visibility for the record button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 320](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `visible`

 

boolean

 

Set the visibility of the button.

 

 

#### (async) setStopRecordingButton()

 

**Description:
 :** 

- 

Update the content of the stop recording button timer.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 658](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### setUploadButtonState(enabled)

 

**Description:
 :** 

- 

Enable the upload button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 341](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `enabled`

 

boolean
|

null

 

Set the button state

 

 

#### (async) setUploadButtonTextProgress(progress)

 

**Description:
 :** 

- 

Set the upload button text progress.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 702](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `progress`

 

number

 

The progress

 

 

#### setUploadButtonVisibility(visible)

 

**Description:
 :** 

- 

Configure button visibility for the upload button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 350](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `visible`

 

boolean

 

Set the visibility of the button.

 

 

#### setupPlayerSource()

 

**Description:
 :** 

- 

Setup the player to use the stream as a source.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 295](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### startButtonTimer()

 

**Description:
 :** 

- 

Start the timer for the start recording button.
If the recording was paused, the timer will resume from the pause time.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 739](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) startRecording()

 

**Description:
 :** 

- 

Start the recording

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 932](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### updateRecordButtonTime()

 

**Description:
 :** 

- 

Update the time on the stop recording button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 667](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) uploadRecording()

 

**Description:
 :** 

- 

Upload the recording and insert it into the editor content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 536](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (static) checkSecure() → {boolean}

 

**Description:
 :** 

- 

Check whether the hostname is either hosted over SSL, or from a valid localhost hostname.

The UserMedia API can only be used in secure contexts as noted.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 648](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

**See:
 :** 

- [https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#privacy_and_security](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)

 

##### Returns:

Whether the plugin can be loaded.

**
 Type

 :** 

boolean

 

#### (static) getModalClass() → {Modal}

 

**Description:
 :** 

- 

Fetch the Class of the Modal to be displayed.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 175](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

Modal

 

#### (static) hasUserMedia() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser supports WebRTC.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 636](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean

 

#### (static) isBrowserCompatible() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser is compatible with capturing media.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 586](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean
