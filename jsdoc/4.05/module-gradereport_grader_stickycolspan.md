# gradereport_grader/stickycolspan - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-gradereport_grader_stickycolspan.html

# gradereport_grader/stickycolspan

 

 

 

**Description:
 :** 

- 

Javascript module for fixing the position of sticky headers with multiple colspans

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/stickycolspan.js](grade_report_grader_amd_src_stickycolspan.js.md), [line 16](grade_report_grader_amd_src_stickycolspan.js.md)

 

**Copyright:
 :** 

- 2022 Bas Brands 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Javascript module for fixing the position of sticky headers with multiple colspans

 

 

 

 

### Members

 

#### (static, constant) init

 

**Description:
 :** 

- 

Initialize module

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/stickycolspan.js](grade_report_grader_amd_src_stickycolspan.js.md), [line 39](grade_report_grader_amd_src_stickycolspan.js.md)

Initialize module

 

 

### Methods

 

#### (inner) defineLastRowIntersectionObserver(stickyFooterEnabled)

 

**Description:
 :** 

- 

Define the intersection observer that will make sure that the last row is properly pinned.

In certain scenarios, such as when both 'Overall average' and 'Range' are set not to be shown in the Grader report,
a user row will end up being the last row in the Grader report table. In this particular case, we want to avoid
pinning the last row.

 

**Source:
 :** 

- 
 [grade/report/grader/amd/src/stickycolspan.js](grade_report_grader_amd_src_stickycolspan.js.md), [line 85](grade_report_grader_amd_src_stickycolspan.js.md)

##### Parameters:

 

 Name

 Type

 Description

 

 

 
 `stickyFooterEnabled`

 

boolean

 

Whether the page shows a sticky footer or not.
