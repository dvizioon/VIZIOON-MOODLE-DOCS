# BulkSelector - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/BulkSelector.html

# BulkSelector

 

## 

 BulkSelector

 

 

 

 

#### new BulkSelector(courseEditor)

 

**Description:
 :** 

- 

The class constructor.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 30](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `courseEditor`

 

CourseEditor

 

the original actions component.

 

 

 

 

### Methods

 

#### checkAllSelected() → {Boolean}

 

**Description:
 :** 

- 

Checks if all selectable elements are selected.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 121](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Returns:

true if all are selected

**
 Type

 :** 

Boolean

 

#### processNewSelection(id, elementType, settings)

 

**Description:
 :** 

- 

Process a new selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 47](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `id`

 

Number

 

 

 
 `elementType`

 

String

 

cm or section

 
 `settings`

 

Object

 

special selection settings

###### Properties

 

 Name

 Type

 Description

 

 

 
 `all`

 

Boolean

 

if the action is over all elements of the same type

 
 `range`

 

Boolean

 

if the action is over a range of elements

 

 

 

 

#### selectAll(value)

 

**Description:
 :** 

- 

Select all elements of the current type.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 104](course_format_amd_src_local_content_actions_bulkselection.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `value`

 

Boolean

 

the wanted selected value

 

 

#### switchCurrentSelection()

 

**Description:
 :** 

- 

Switch between section and cm selection.

 

**Source:
 :** 

- 
 [course/format/amd/src/local/content/actions/bulkselection.js](course_format_amd_src_local_content_actions_bulkselection.js.md), [line 74](course_format_amd_src_local_content_actions_bulkselection.js.md)
