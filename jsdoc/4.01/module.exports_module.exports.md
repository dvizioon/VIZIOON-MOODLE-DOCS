# exports - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module.exports_module.exports.html

# exports

 

## 

 exports

 

 

 

 

#### new exports()

 

**Description:
 :** 

- 

Constructor.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/logger.js](lib_amd_src_local_reactive_logger.js.md), [line 47](lib_amd_src_local_reactive_logger.js.md)

 

 

 

## 

 exports

 

 

 

 

#### new exports(descriptor)

 

**Description:
 :** 

- 

The class constructor.

The only param this method gets is a constructor with all the mandatory
and optional component data. Component will receive the same descriptor
as create method param.

This method will call the "create" method before registering the component into
the reactive module. This way any component can add default selectors and events.

 

**Source:
 :** 

- 
 [lib/amd/src/local/reactive/basecomponent.js](lib_amd_src_local_reactive_basecomponent.js.md), [line 60](lib_amd_src_local_reactive_basecomponent.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `descriptor`

 

[descriptor](global.md)

 

data to create the object.

 

 

 

 

## 

 exports

 

 

 

 

#### new exports(reactive)

 

**Description:
 :** 

- 

Class constructor.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/exporter.js](course_format_amd_src_local_courseeditor_exporter.js.md), [line 32](course_format_amd_src_local_courseeditor_exporter.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `reactive`

 

CourseEditor

 

the course editor object

 

 

 

 

## 

 exports

 

 

 

 

#### new exports(mainElement, selectors, preventcache)

 

**Description:
 :** 

- 

Setup the core/tree keyboard navigation.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/courseeditor/contenttree.js](course_format_amd_src_local_courseeditor_contenttree.js.md), [line 43](course_format_amd_src_local_courseeditor_contenttree.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `mainElement`

 

Element
|

undefined

 

an alternative main element in case it is not from the parent component

 
 `selectors`

 

Object
|

undefined

 

alternative selectors

 
 `preventcache`

 

boolean

 

if the elements cache must be disabled.
