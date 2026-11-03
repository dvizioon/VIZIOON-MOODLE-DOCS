# core_grades/edittree_weight - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_grades_edittree_weight.html

# core_grades/edittree_weight

 

 

 

**Description:
 :** 

- 

This module provides functionality for managing weight calculations and adjustments for grade items.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 16](grade_amd_src_edittree_weights.js.md)

 

**Copyright:
 :** 

- 2023 Shamim Rezaie 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

This module provides functionality for managing weight calculations and adjustments for grade items.

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initializes the weight management module with optional configuration.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 274](grade_amd_src_edittree_weights.js.md)

Initializes the weight management module with optional configuration.

 

#### (inner) decimalSeparator :string

 

**Description:
 :** 

- 

The character used as the decimal separator for number formatting.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 63](grade_amd_src_edittree_weights.js.md)

The character used as the decimal separator for number formatting.

##### Type:

- 

string

 

 

#### (inner, constant) grade :Object

 

**Description:
 :** 

- 

An object representing grading-related constants.
The same as what's defined in lib/grade/constants.php.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 52](grade_amd_src_edittree_weights.js.md)

##### Properties:

 

 Name

 Type

 Description

 

 

 
 `aggregation`

 

Object

 

Aggregation settings.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `sum`

 

number

 

Aggregation method: sum.

 

 

 
 `type`

 

Object

 

Grade type settings.

###### Properties

 

 Name

 Type

 Description

 

 

 
 `none`

 

number

 

Grade type: none.

 
 `value`

 

number

 

Grade type: value.

 
 `scale`

 

number

 

Grade type: scale.

 

 

 

An object representing grading-related constants.
The same as what's defined in lib/grade/constants.php.

##### Type:

- 

Object

 

 

#### (inner) oldExtraCreditCalculation :boolean

 

**Description:
 :** 

- 

This setting indicates if we should use algorithm prior to MDL-49257 fix for calculating extra credit weights.
Even though the old algorithm has bugs in it, we need to preserve existing grades.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 71](grade_amd_src_edittree_weights.js.md)

This setting indicates if we should use algorithm prior to MDL-49257 fix for calculating extra credit weights.
Even though the old algorithm has bugs in it, we need to preserve existing grades.

##### Type:

- 

boolean

 

 

#### (inner, constant) selectors :Object

 

**Description:
 :** 

- 

Selectors.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 32](grade_amd_src_edittree_weights.js.md)

Selectors.

##### Type:

- 

Object

 

 

 

### Methods

 

#### (inner) formatFloat(number, decimalPointsopt, minDecimalsopt) → {string}

 

**Description:
 :** 

- 

Formats a floating-point number as a string with the specified number of decimal places.
Unnecessary trailing zeros are removed up to the specified minimum number of decimal places.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 251](grade_amd_src_edittree_weights.js.md)

##### Parameters:

 

 Name

 Type

 Attributes

 Default

 Description

 

 

 
 `number`

 

number

 

 

 

 

 

The float value to be formatted.

 
 `decimalPoints`

 

number

 

 

 <optional>  

 

 

 `3`

 

The number of decimal places to use.

 
 `minDecimals`

 

number

 

 

 <optional>  

 

 

 `1`

 

The minimum number of decimal places to use.

 

##### Returns:

The formatted weight value with the specified decimal places.

**
 Type

 :** 

string

 

#### (inner) parseWeight(weightString) → {number}

 

**Description:
 :** 

- 

Parses a weight string and returns a normalized float value.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 263](grade_amd_src_edittree_weights.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `weightString`

 

string

 

The weight as a string, possibly with localized formatting.

 

##### Returns:

The parsed weight as a float. If parsing fails, returns 0.

**
 Type

 :** 

number

 

#### (inner) recalculateNaturalWeights(categoryElement)

 

**Description:
 :** 

- 

Recalculates the natural weights for grade items within a given category.

 

**Source:
 :** 

- 
 [grade/amd/src/edittree_weights.js](grade_amd_src_edittree_weights.js.md), [line 80](grade_amd_src_edittree_weights.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `categoryElement`

 

HTMLElement

 

The DOM element representing the category.
