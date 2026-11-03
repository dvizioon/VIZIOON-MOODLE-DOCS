# paygw_paypal/gateway_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-paygw_paypal_gateway_modal.html

# paygw_paypal/gateway_modal

 

 

 

**Description:
 :** 

- 

This module is responsible for PayPal content in the gateways modal.

 

**Source:
 :** 

- 
 [payment/gateway/paypal/amd/src/gateways_modal.js](payment_gateway_paypal_amd_src_gateways_modal.js.md), [line 16](payment_gateway_paypal_amd_src_gateways_modal.js.md)

 

**Copyright:
 :** 

- 2020 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module is responsible for PayPal content in the gateways modal.

 

 

 

 

### Members

 

#### (static, constant) process

 

**Description:
 :** 

- 

Process the payment.

 

**Source:
 :** 

- 
 [payment/gateway/paypal/amd/src/gateways_modal.js](payment_gateway_paypal_amd_src_gateways_modal.js.md), [line 53](payment_gateway_paypal_amd_src_gateways_modal.js.md)

Process the payment.

 

 

### Methods

 

#### (async, inner) showModalWithPlaceholder() → {Promise.<Modal>}

 

**Description:
 :** 

- 

Creates and shows a modal that contains a placeholder.

 

**Source:
 :** 

- 
 [payment/gateway/paypal/amd/src/gateways_modal.js](payment_gateway_paypal_amd_src_gateways_modal.js.md), [line 36](payment_gateway_paypal_amd_src_gateways_modal.js.md)

##### Returns:

**
 Type

 :** 

Promise.<Modal>

 

#### (inner) switchSdk(clientId, currency) → {Promise}

 

**Description:
 :** 

- 

Unloads the previously loaded PayPal JavaScript SDK, and loads a new one.

 

**Source:
 :** 

- 
 [payment/gateway/paypal/amd/src/gateways_modal.js](payment_gateway_paypal_amd_src_gateways_modal.js.md), [line 127](payment_gateway_paypal_amd_src_gateways_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `clientId`

 

string

 

PayPal client ID

 
 `currency`

 

string

 

The currency

 

##### Returns:

**
 Type

 :** 

Promise
