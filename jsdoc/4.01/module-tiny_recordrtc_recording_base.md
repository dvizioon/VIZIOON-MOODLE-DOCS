# module:tiny_recordrtc/recording/base - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-tiny_recordrtc_recording_base.html

# module:tiny_recordrtc/recording/base

 

## 

 module:tiny_recordrtc/recording/base

 

 

The RecordRTC base class for audio, video, and any other future types

 

 

 

 

## Constructor

#### new (require("tiny_recordrtc/recording/base"))(editor, modal)

 

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 209](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### checkAndWarnAboutBrowserCompatibility() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser is compatible with capturing media, and display a warning if not.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 535](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 689](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### clearButtonTimer()

 

**Description:
 :** 

- 

Clear the timer for the stop recording button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 626](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### close()

 

**Description:
 :** 

- 

Close the modal and stop recording.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 356](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### configurePlayer() → {HTMLElement}

 

**Description:
 :** 

- 

Get the Player element for this type.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 93](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 501](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 849](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 162](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 126](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 658](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 136](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 182](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 114](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 103](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 153](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 638](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 344](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 272](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 723](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 408](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

The click event

 

 

#### handleRecordingStartStopRequested()

 

**Description:
 :** 

- 

Handle the click event for the recording start/stop button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 425](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleStarted()

 

**Description:
 :** 

- 

Handle the mediaRecorder `start` event.

This event is called when the recording starts.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 713](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### handleStopped()

 

**Description:
 :** 

- 

Handle the mediaRecorder `stop` event.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 700](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### hasData() → {boolean}

 

**Description:
 :** 

- 

Whether any data has been recorded.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 766](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 833](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `source`

 

string

 

The URL to view the media.

 

 

#### isReady() → {boolean}

 

**Description:
 :** 

- 

Check whether the browser is compatible.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 80](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 757](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 436](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) outsideClickHandler(event)

 

**Description:
 :** 

- 

Prevent the Modal from closing when recording is on process.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 379](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `event`

 

MouseEvent

 

The click event

 

 

#### playOnCapture() → {boolean}

 

**Description:
 :** 

- 

Whether to start playing the recording as it is captured.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 144](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 224](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) recordAgainConfirmation() → {Promise.<boolean>}

 

**Description:
 :** 

- 

Confirm whether the user wants to reset the existing recoring.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 815](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 668](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### setRecordButtonState(enabled)

 

**Description:
 :** 

- 

Enable the record button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 307](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 604](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 316](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 580](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### setUploadButtonState(enabled)

 

**Description:
 :** 

- 

Enable the upload button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 326](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 613](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 335](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 291](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) startRecording()

 

**Description:
 :** 

- 

Start the recording

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 773](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### updateRecordButtonTime()

 

**Description:
 :** 

- 

Update the time on the stop recording button.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 589](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (async) uploadRecording()

 

**Description:
 :** 

- 

Upload the recording and insert it into the editor content.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 460](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

#### (static) checkSecure() → {boolean}

 

**Description:
 :** 

- 

Check whether the hostname is either hosted over SSL, or from a valid localhost hostname.

The UserMedia API can only be used in secure contexts as noted.

 

**Source:
 :** 

- 
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 570](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

 

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 171](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 558](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

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
 [lib/editor/tiny/plugins/recordrtc/amd/src/base_recorder.js](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md), [line 510](lib_editor_tiny_plugins_recordrtc_amd_src_base_recorder.js.md)

##### Returns:

**
 Type

 :** 

boolean
