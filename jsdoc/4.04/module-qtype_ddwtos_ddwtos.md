# qtype_ddwtos/ddwtos - Documentation

> Fonte: https://jsdoc.moodledev.io/4.04/module-qtype_ddwtos_ddwtos.html

# qtype_ddwtos/ddwtos

 

 

 

**Description:
 :** 

- 

JavaScript to make drag-drop into text questions work.

Some vocabulary to help understand this code:

The question text contains 'drops' - blanks into which the 'drags', the missing
words, can be put.

The thing that can be moved into the drops are called 'drags'. There may be
multiple copies of the 'same' drag which does not really cause problems.
Each drag has a 'choice' number which is the value set on the drop's hidden
input when this drag is placed in a drop.

These may be in separate 'groups', distinguished by colour.
Things can only interact with other things in the same group.
The groups are numbered from 1.

The place where a given drag started from is called its 'home'.

 

**Source:
 :** 

- 
 [question/type/ddwtos/amd/src/ddwtos.js](question_type_ddwtos_amd_src_ddwtos.js.md), [line 16](question_type_ddwtos_amd_src_ddwtos.js.md)

 

**Since:
 :** 

- 3.6

 

**Copyright:
 :** 

- 2018 The Open University

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

JavaScript to make drag-drop into text questions work.

Some vocabulary to help understand this code:

The question text contains 'drops' - blanks into which the 'drags', the missing
words, can be put.

The thing that can be moved into the drops are called 'drags'. There may be
multiple copies of the 'same' drag which does not really cause problems.
Each drag has a 'choice' number which is the value set on the drop's hidden
input when this drag is placed in a drop.

These may be in separate 'groups', distinguished by colour.
Things can only interact with other things in the same group.
The groups are numbered from 1.

The place where a given drag started from is called its 'home'.

 

 

 

 

### Members

 

#### (inner) init

 

**Description:
 :** 

- 

Initialise one drag-drop into text question.

 

**Source:
 :** 

- 
 [question/type/ddwtos/amd/src/ddwtos.js](question_type_ddwtos_amd_src_ddwtos.js.md), [line 962](question_type_ddwtos_amd_src_ddwtos.js.md)

Initialise one drag-drop into text question.
