# core/chart_builder - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-core_chart_builder.html

# core/chart_builder

 

 

 

**Description:
 :** 

- 

Chart builder.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_builder.js](lib_amd_src_chart_builder.js.md), [line 29](lib_amd_src_chart_builder.js.md)

 

Chart builder.

 

 

 

 

### Methods

 

#### (static) make(data) → {Promise}

 

**Description:
 :** 

- 

Make a chart instance.

This takes data, most likely generated in PHP, and creates a chart instance from it
deferring most of the logic to [module:core/chart_base.create](module-core_chart_base.md).

 

**Source:
 :** 

- 
 [lib/amd/src/chart_builder.js](lib_amd_src_chart_builder.js.md), [line 40](lib_amd_src_chart_builder.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `data`

 

Object

 

The data.

 

##### Returns:

A promise resolved with the chart instance.

**
 Type

 :** 

Promise
