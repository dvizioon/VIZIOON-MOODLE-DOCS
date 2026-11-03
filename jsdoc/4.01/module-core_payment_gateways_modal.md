# core_payment/gateways_modal - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_payment_gateways_modal.html

# core_payment/gateways_modal

 

 

 

**Description:
 :** 

- 

Contain the logic for the gateways modal.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 16](payment_amd_src_gateways_modal.js.md)

 

**Copyright:
 :** 

- 2019 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Contain the logic for the gateways modal.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Set up the payment actions.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 178](payment_amd_src_gateways_modal.js.md)

Set up the payment actions.

 

 

### Methods

 

#### (async, inner) processPayment(gateway, component, paymentArea, itemId, description) → {Promise.<string>}

 

**Description:
 :** 

- 

Process payment using the selected gateway.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 170](payment_amd_src_gateways_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `gateway`

 

string

 

The gateway to be used for payment

 
 `component`

 

string

 

Name of the component that the itemId belongs to

 
 `paymentArea`

 

string

 

Name of the area in the component that the itemId belongs to

 
 `itemId`

 

number

 

An internal identifier that is used by the component

 
 `description`

 

string

 

Description of the payment

 

##### Returns:

**
 Type

 :** 

Promise.<string>

 

#### (inner) registerEventListeners()

 

**Description:
 :** 

- 

Register event listeners for the module.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 38](payment_amd_src_gateways_modal.js.md)

 

#### (inner) selectSingleGateway(root)

 

**Description:
 :** 

- 

Auto-select the gateway if there is only one gateway.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 136](payment_amd_src_gateways_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

An HTMLElement that contains the cost region

 

 

#### (async, inner) show(rootNode, options)

 

**Description:
 :** 

- 

Shows the gateway selector modal.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 56](payment_amd_src_gateways_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `rootNode`

 

HTMLElement

 

 

 
 `options`

 

Object

 

Additional options

###### Properties

 

 Name

 Type

 Description

 

 

 
 `focusOnClose`

 

HTMLElement

 

The element to focus on when the modal is closed.

 

 

 

 

#### (async, inner) updateCostRegion(root, defaultCost) → {Promise.<void>}

 

**Description:
 :** 

- 

Shows the cost of the item the user is purchasing in the cost region.

 

**Source:
 :** 

- 
 [payment/amd/src/gateways_modal.js](payment_amd_src_gateways_modal.js.md), [line 151](payment_amd_src_gateways_modal.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `root`

 

HTMLElement

 

An HTMLElement that contains the cost region

 
 `defaultCost`

 

string

 

The default cost that is going to be displayed if no gateway is selected

 

##### Returns:

**
 Type

 :** 

Promise.<void>
