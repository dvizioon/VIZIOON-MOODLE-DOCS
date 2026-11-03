# DropZone - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_dropzone-DropZone.html

# DropZone

 

## 
 [core/dropzone](module-core_dropzone.md)~

 
 DropZone

 

 

 

 

#### new DropZone(dropZoneElement, fileTypes, callback)

 

**Description:
 :** 

- 

Constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 68](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropZoneElement`

 

Element

 

The element to render the dropzone.

 
 `fileTypes`

 

String

 

The file types that are allowed to be uploaded. Example: image/*

 
 `callback`

 

CallableFunction

 

The function to call when a file is dropped.

 

 

 

 

### Members

 

#### callback :CallableFunction

 

**Description:
 :** 

- 

The function to call when a file is dropped.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 53](lib_amd_src_dropzone.js.md)

The function to call when a file is dropped.

##### Type:

- 

CallableFunction

 

 

#### dropZoneElement :Element

 

**Description:
 :** 

- 

The element to render the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 41](lib_amd_src_dropzone.js.md)

The element to render the dropzone.

##### Type:

- 

Element

 

 

#### dropZoneLabel :string

 

**Description:
 :** 

- 

The label to display in the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 59](lib_amd_src_dropzone.js.md)

The label to display in the dropzone.

##### Type:

- 

string

 

 

#### fileTypes :String

 

**Description:
 :** 

- 

The file types that are allowed to be uploaded.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 47](lib_amd_src_dropzone.js.md)

The file types that are allowed to be uploaded.

##### Type:

- 

String

 

 

 

### Methods

 

#### getDropZoneContainerFromEvent(e) → {HTMLElement|bool}

 

**Description:
 :** 

- 

Get the dropzone container.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 142](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

HTMLElement
|

bool

 

#### getDropZoneFromEvent(e) → {HTMLElement|bool}

 

**Description:
 :** 

- 

Get the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 132](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

HTMLElement
|

bool

 

#### getFileElementFromEvent(e) → {HTMLElement|bool}

 

**Description:
 :** 

- 

Get the file element.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 152](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.

 

##### Returns:

**
 Type

 :** 

HTMLElement
|

bool

 

#### getLabel() → {String}

 

**Description:
 :** 

- 

Get the label to display in the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 170](lib_amd_src_dropzone.js.md)

##### Returns:

The label to display in the dropzone.

**
 Type

 :** 

String

 

#### init() → {DropZone}

 

**Description:
 :** 

- 

Initialise the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 80](lib_amd_src_dropzone.js.md)

##### Returns:

**
 Type

 :** 

DropZone

 

#### (async) renderDropZone(dropZoneElement, fileTypes) → {Promise}

 

**Description:
 :** 

- 

Render the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 181](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `dropZoneElement`

 

Element

 

The element to render the dropzone.

 
 `fileTypes`

 

String

 

The file types that are allowed to be uploaded.

 

##### Returns:

**
 Type

 :** 

Promise

 

#### setLabel(label)

 

**Description:
 :** 

- 

Set the label to display in the dropzone.

 

**Source:
 :** 

- 
 [lib/amd/src/dropzone.js](lib_amd_src_dropzone.js.md), [line 161](lib_amd_src_dropzone.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `label`

 

String

 

The label to display in the dropzone.
