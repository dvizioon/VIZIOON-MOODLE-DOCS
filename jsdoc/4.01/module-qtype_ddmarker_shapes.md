# qtype_ddmarker/shapes - Documentation

> Fonte: https://jsdoc.moodledev.io/4.01/module-qtype_ddmarker_shapes.html

# qtype_ddmarker/shapes

 

 

 

**Description:
 :** 

- 

Library of classes for handling simple shapes.

These classes can represent shapes, let you alter them, can go to and from a string
representation, and can give you an SVG representation.

 

**Source:
 :** 

- 
 [question/type/ddmarker/amd/src/shapes.js](question_type_ddmarker_amd_src_shapes.js.md), [line 18](question_type_ddmarker_amd_src_shapes.js.md)

 

**Copyright:
 :** 

- 2018 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Library of classes for handling simple shapes.

These classes can represent shapes, let you alter them, can go to and from a string
representation, and can give you an SVG representation.

 

 

 

### Classes

 

**[Circle](module-qtype_ddmarker_shapes-Circle.md)
 :[NullShape](module-qtype_ddmarker_shapes-NullShape.md)
 :[Point](module-qtype_ddmarker_shapes-Point.md)
 :[Polygon](module-qtype_ddmarker_shapes-Polygon.md)
 :[Rectangle](module-qtype_ddmarker_shapes-Rectangle.md)
 :[Shape](module-qtype_ddmarker_shapes-Shape.md)
 :** 

 

 

 

### Members

 

#### (inner) createSvgElement

 

**Description:
 :** 

- 

Make a new SVG DOM element as a child of svg.

 

**Source:
 :** 

- 
 [question/type/ddmarker/amd/src/shapes.js](question_type_ddmarker_amd_src_shapes.js.md), [line 800](question_type_ddmarker_amd_src_shapes.js.md)

Make a new SVG DOM element as a child of svg.

 

 

### Methods

 

#### (inner) getSimilar(shapeType, shape) → {Shape}

 

**Description:
 :** 

- 

Make a shape of the given type that is similar to the shape of the original type.

 

**Source:
 :** 

- 
 [question/type/ddmarker/amd/src/shapes.js](question_type_ddmarker_amd_src_shapes.js.md), [line 829](question_type_ddmarker_amd_src_shapes.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `shapeType`

 

String

 

the new type of shape to make

 
 `shape`

 

Shape

 

the shape to copy

 

##### Returns:

the similar shape of a different type.

**
 Type

 :** 

Shape

 

#### (inner) make(shapeType, label) → {Shape}

 

**Description:
 :** 

- 

Make a shape of the given type.

 

**Source:
 :** 

- 
 [question/type/ddmarker/amd/src/shapes.js](question_type_ddmarker_amd_src_shapes.js.md), [line 809](question_type_ddmarker_amd_src_shapes.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `shapeType`

 

String

 

 

 
 `label`

 

String

 

 

 

##### Returns:

the requested shape.

**
 Type

 :** 

Shape
