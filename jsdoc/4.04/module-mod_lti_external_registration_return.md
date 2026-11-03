# mod_lti/external_registration_return - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-mod_lti_external_registration_return.html

# mod_lti/external_registration_return

 

 

 

**Description:
 :** 

- 

Handles the return params from the external registration page after it
redirects back to Moodle.

See also: mod/lti/externalregistrationreturn.php

 

**Source:
 :** 

- 
 [mod/lti/amd/src/external_registration_return.js](mod_lti_amd_src_external_registration_return.js.md), [line 16](mod_lti_amd_src_external_registration_return.js.md)

 

**Since:
 :** 

- 3.1

 

**Copyright:
 :** 

- 2015 Ryan Wyllie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Handles the return params from the external registration page after it
redirects back to Moodle.

See also: mod/lti/externalregistrationreturn.php

 

 

 

 

### Methods

 

#### (inner) init(message, error, id, status)

 

**Description:
 :** 

- 

If this was rendered in an iframe then trigger the external registration
complete behaviour in the parent page and provide the params returned from
the external registration page.

 

**Source:
 :** 

- 
 [mod/lti/amd/src/external_registration_return.js](mod_lti_amd_src_external_registration_return.js.md), [line 41](mod_lti_amd_src_external_registration_return.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `message`

 

String

 

The registration message from the external registration page

 
 `error`

 

String

 

The registration error message from the external registration page, if
there was an error.

 
 `id`

 

Integer

 

The tool proxy id for the external registration.

 
 `status`

 

String

 

Whether the external registration was successful or not.
