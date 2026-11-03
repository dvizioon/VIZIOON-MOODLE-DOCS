# filter_mathjaxloader/loader - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-filter_mathjaxloader_loader.html

# filter_mathjaxloader/loader

 

 

 

**Description:
 :** 

- 

Mathjax JS Loader.

 

**Source:
 :** 

- 
 [filter/mathjaxloader/amd/src/loader.js](filter_mathjaxloader_amd_src_loader.js.md), [line 15](filter_mathjaxloader_amd_src_loader.js.md)

 

**Copyright:
 :** 

- 2014 Damyon Wiese 

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Mathjax JS Loader.

 

 

 

 

### Members

 

#### (static, constant) configure

 

**Description:
 :** 

- 

Called by the filter when it is active on any page.
This does not load MathJAX yet - it addes the configuration to the head incase it gets loaded later.
It also subscribes to the filter-content-updated event so MathJax can respond to content loaded by Ajax.

 

**Source:
 :** 

- 
 [filter/mathjaxloader/amd/src/loader.js](filter_mathjaxloader_amd_src_loader.js.md), [line 50](filter_mathjaxloader_amd_src_loader.js.md)

Called by the filter when it is active on any page.
This does not load MathJAX yet - it addes the configuration to the head incase it gets loaded later.
It also subscribes to the filter-content-updated event so MathJax can respond to content loaded by Ajax.

 

#### (static, constant) contentUpdated

 

**Description:
 :** 

- 

Handle content updated events - typeset the new content.

 

**Source:
 :** 

- 
 [filter/mathjaxloader/amd/src/loader.js](filter_mathjaxloader_amd_src_loader.js.md), [line 131](filter_mathjaxloader_amd_src_loader.js.md)

Handle content updated events - typeset the new content.

 

#### (static, constant) typeset

 

**Description:
 :** 

- 

Called by the filter when an equation is found while rendering the page.

 

**Source:
 :** 

- 
 [filter/mathjaxloader/amd/src/loader.js](filter_mathjaxloader_amd_src_loader.js.md), [line 114](filter_mathjaxloader_amd_src_loader.js.md)

Called by the filter when an equation is found while rendering the page.
