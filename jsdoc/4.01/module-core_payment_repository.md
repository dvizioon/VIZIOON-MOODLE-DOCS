# core_payment/repository - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_payment_repository.html

# core_payment/repository

 

 

 

**Description:
 :** 

- 

Repository for payment subsystem.

 

**Source:
 :** 

- 
 [payment/amd/src/repository.js](payment_amd_src_repository.js.md), [line 16](payment_amd_src_repository.js.md)

 

**Copyright:
 :** 

- 2020 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Repository for payment subsystem.

 

 

 

 

### Methods

 

#### (inner) getAvailableGateways(component, paymentArea, itemId) → {Promise.<Array.<PaymentGateway>>}

 

**Description:
 :** 

- 

Returns the list of gateways that can process payments in the given currency.

 

**Source:
 :** 

- 
 [payment/amd/src/repository.js](payment_amd_src_repository.js.md), [line 33](payment_amd_src_repository.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `component`

 

string

 

 

 
 `paymentArea`

 

string

 

 

 
 `itemId`

 

number

 

 

 

##### Returns:

**
 Type

 :** 

Promise.<Array.<PaymentGateway>>

 

 

### Type Definitions

 

#### PaymentGateway

 

**Description:
 :** 

- 

A Payment Gateway

 

**Source:
 :** 

- 
 [payment/amd/src/repository.js](payment_amd_src_repository.js.md), [line 26](payment_amd_src_repository.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `shortname`

 

string

 

 

 
 `name`

 

string

 

 

 
 `description`

 

string

 

 

 

A Payment Gateway

##### Type:

- 

Object
