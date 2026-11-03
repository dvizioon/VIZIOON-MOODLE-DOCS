# core/chart_axis - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-core_chart_axis.html

# core/chart_axis

 

 

 

**Description:
 :** 

- 

Chart axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 16](lib_amd_src_chart_axis.js.md)

 

**Copyright:
 :** 

- 2016 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Chart axis.

 

 

 

### Classes

 

**[core/chart_axis](module-core_chart_axis-core_chart_axis.md)
 :** 

 

 

 

### Methods

 

#### (static) create(obj) → {[module:core/chart_axis](module-core_chart_axis.md)}

 

**Description:
 :** 

- 

Create a new instance of an axis from serialised data.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 108](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `obj`

 

Object

 

The data of the axis.

 

##### Returns:

**
 Type

 :** 

[module:core/chart_axis](module-core_chart_axis.md)

 

#### (inner) getLabel() → {String}

 

**Description:
 :** 

- 

Get the label of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 127](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getLabels() → {Array.<String>}

 

**Description:
 :** 

- 

Get the labels of the ticks of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 137](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

Array.<String>

 

#### (inner) getMax() → {Number}

 

**Description:
 :** 

- 

Get the maximum value of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 147](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getMin() → {Number}

 

**Description:
 :** 

- 

Get the minimum value of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 157](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) getPosition() → {String}

 

**Description:
 :** 

- 

Get the position of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 167](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

String

 

#### (inner) getStepSize() → {Number}

 

**Description:
 :** 

- 

Get the step size of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 177](lib_amd_src_chart_axis.js.md)

##### Returns:

**
 Type

 :** 

Number

 

#### (inner) setLabel(label)

 

**Description:
 :** 

- 

Set the label of the axis.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 187](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `label`

 

String

 

The label.

 

 

#### (inner) setLabels(labels)

 

**Description:
 :** 

- 

Set the labels of the values on the axis.

This automatically sets the _stepSize,
_min and _max
to define a scale from 0 to the number of labels when none of the previously
mentioned values have been modified.

You can use other values so long that your values in a series are mapped
to the values represented by your _min, _max and _stepSize.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 197](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `labels`

 

Array.<String>

 

The labels.

 

 

#### (inner) setMax(max)

 

**Description:
 :** 

- 

Set the maximum value on the axis.

When this is not set (or set to null) it is left for the output
library to best guess what should be used.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 225](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `max`

 

Number

 

The value.

 

 

#### (inner) setMin(min)

 

**Description:
 :** 

- 

Set the minimum value on the axis.

When this is not set (or set to null) it is left for the output
library to best guess what should be used.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 238](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `min`

 

Number

 

The value.

 

 

#### (inner) setPosition(position)

 

**Description:
 :** 

- 

Set the position of the axis.

This does not validate whether or not the constant used is valid
as the axis itself is not aware whether it represents the X or Y axis.

The output library has to have a fallback in case the values are incorrect.
When this is not set to module:core/chart_axis#POS_DEFAULT it is up
to the output library to choose what position fits best.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 251](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `position`

 

String

 

The value.

 

 

#### (inner) setStepSize(stepSize)

 

**Description:
 :** 

- 

Set the stepSize on the axis.

This is used to determine where ticks are displayed on the axis between min and max.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_axis.js](lib_amd_src_chart_axis.js.md), [line 275](lib_amd_src_chart_axis.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stepSize`

 

Number

 

The value.
