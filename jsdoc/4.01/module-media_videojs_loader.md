# media_videojs/loader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-media_videojs_loader.html

# media_videojs/loader

 

 

 

**Description:
 :** 

- 

Video JS loader.

This takes care of applying the filter on content which was dynamically loaded.

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 16](media_player_videojs_amd_src_loader.js.md)

 

**Copyright:
 :** 

- 2016 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Video JS loader.

This takes care of applying the filter on content which was dynamically loaded.

 

 

 

 

### Members

 

#### (inner) List :object

 

**Description:
 :** 

- 

of languages and translations for the current page

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 39](media_player_videojs_amd_src_loader.js.md)

of languages and translations for the current page

##### Type:

- 

object

 

 

#### (inner) The :string

 

**Description:
 :** 

- 

language that is used in the player

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 36](media_player_videojs_amd_src_loader.js.md)

language that is used in the player

##### Type:

- 

string

 

 

#### (inner) Whether :bool

 

**Description:
 :** 

- 

this is the first load of videojs module

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 33](media_player_videojs_amd_src_loader.js.md)

this is the first load of videojs module

##### Type:

- 

bool

 

 

 

### Methods

 

#### (static) setUp(lang)

 

**Description:
 :** 

- 

Initialisei teh videojs Loader.

Adds the listener for the event to then notify video.js.

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 51](media_player_videojs_amd_src_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `lang`

 

string

 

Language to be used in the player

 

##### Listens to Events:

- [event:filterContentUpdated](module-core_filters_events.md)

 

#### (inner) getLanguageJson() → {Promise}

 

**Description:
 :** 

- 

Returns the json object of the language strings to be used in the player.

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 119](media_player_videojs_amd_src_loader.js.md)

##### Returns:

**
 Type

 :** 

Promise

 

#### (inner) notifyVideoJS(e)

 

**Description:
 :** 

- 

Notify video.js of new nodes.

 

**Source:
 :** 

- 
 [media/player/videojs/amd/src/loader.js](media_player_videojs_amd_src_loader.js.md), [line 71](media_player_videojs_amd_src_loader.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `e`

 

Event

 

The event.
