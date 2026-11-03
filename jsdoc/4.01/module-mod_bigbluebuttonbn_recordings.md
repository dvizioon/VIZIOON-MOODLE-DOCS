# mod_bigbluebuttonbn/recordings - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-mod_bigbluebuttonbn_recordings.html

# mod_bigbluebuttonbn/recordings

 

 

 

**Description:
 :** 

- 

JS for the recordings page on mod_bigbluebuttonbn plugin.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/recordings.js](mod_bigbluebuttonbn_amd_src_recordings.js.md), [line 16](mod_bigbluebuttonbn_amd_src_recordings.js.md)

 

**Copyright:
 :** 

- 2021 Blindside Networks Inc

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JS for the recordings page on mod_bigbluebuttonbn plugin.

 

 

 

 

### Methods

 

#### (inner) formatDate(locale, date) → {array}

 

**Description:
 :** 

- 

Format the supplied date per the specified locale.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/recordings.js](mod_bigbluebuttonbn_amd_src_recordings.js.md), [line 77](mod_bigbluebuttonbn_amd_src_recordings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `locale`

 

string

 

 

 
 `date`

 

number

 

 

 

##### Returns:

**
 Type

 :** 

array

 

#### (inner) getFormattedData(response) → {array}

 

**Description:
 :** 

- 

Format response data for the table.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/recordings.js](mod_bigbluebuttonbn_amd_src_recordings.js.md), [line 93](mod_bigbluebuttonbn_amd_src_recordings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `response`

 

string

 

JSON-encoded table data

 

##### Returns:

**
 Type

 :** 

array

 

#### (inner) init(tableId, searchFormId)

 

**Description:
 :** 

- 

Initialise recordings code.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/recordings.js](mod_bigbluebuttonbn_amd_src_recordings.js.md), [line 402](mod_bigbluebuttonbn_amd_src_recordings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableId`

 

String

 

in which we will display the table

 
 `searchFormId`

 

String

 

The Id of the relate.

 

 

#### (inner) setupDatatable(tableId, searchFormId, response) → {Promise}

 

**Description:
 :** 

- 

Setup the data table for the specified BBB instance.

 

**Source:
 :** 

- 
 [mod/bigbluebuttonbn/amd/src/recordings.js](mod_bigbluebuttonbn_amd_src_recordings.js.md), [line 339](mod_bigbluebuttonbn_amd_src_recordings.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `tableId`

 

String

 

in which we will display the table

 
 `searchFormId`

 

String

 

The Id of the relate.

 
 `response`

 

object

 

The response from the data request

 

##### Returns:

**
 Type

 :** 

Promise
