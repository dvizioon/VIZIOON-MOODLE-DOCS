# core/loadingicon - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_loadingicon.html

# core/loadingicon

 

 

 

**Description:
 :** 

- 

Contain the logic for the loading icon.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 16](lib_amd_src_loadingicon.js.md)

 

**Copyright:
 :** 

- 2019 Andrew Nicols 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for the loading icon.

 

 

 

 

### Methods

 

#### (inner) addIconToContainer(container) → {Promise}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 32](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 

##### Returns:

The Promise used to create the icon.

**
 Type

 :** 

Promise

 

#### (inner) addIconToContainerWithPromise(container, loadingIconPromise) → {jQuery}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 52](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 
 `loadingIconPromise`

 

Promise

 

The jQuery Promise which determines the removal of the icon

 

##### Returns:

The Promise used to create and then remove the icon.

**
 Type

 :** 

jQuery

 

#### (inner) addIconToContainerWithPromise(container) → {Promise}

 

**Description:
 :** 

- 

Add a loading icon to the end of the specified container and return an unresolved promise.

Resolution of the returned promise causes the icon to be faded out and removed.

 

**Source:
 :** 

- 
 [lib/amd/src/loadingicon.js](lib_amd_src_loadingicon.js.md), [line 84](lib_amd_src_loadingicon.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `container`

 

jQuery
|

HTMLElement

 

The element to add the spinner to

 

##### Returns:

A jQuery Promise to resolve when ready

**
 Type

 :** 

Promise
