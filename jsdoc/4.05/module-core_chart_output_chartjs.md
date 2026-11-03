# core/chart_output_chartjs - Documentation

> Fonte: https://jsdoc.moodledev.io/4.05/module-core_chart_output_chartjs.html

# core/chart_output_chartjs

 

 

 

**Description:
 :** 

- 

Chart output for chart.js.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_output_chartjs.js](lib_amd_src_chart_output_chartjs.js.md), [line 16](lib_amd_src_chart_output_chartjs.js.md)

 

**Copyright:
 :** 

- 2016 Frédéric Massart - FMCorz.net

 

**License:
 :** 

- http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later

 

Chart output for chart.js.

 

 

 

 

### Methods

 

#### (protected, inner) getChartType() → {String}

 

**Description:
 :** 

- 

Get the chart type and handles the Chart.js specific chart types.

By default returns the current chart TYPE value. Also does the handling of specific chart types, for example
check if the bar chart should be horizontal and the pie chart should be displayed as a doughnut.

 

**Source:
 :** 

- 
 [lib/amd/src/chart_output_chartjs.js](lib_amd_src_chart_output_chartjs.js.md), [line 116](lib_amd_src_chart_output_chartjs.js.md)

##### Returns:

the chart type.

**
 Type

 :** 

String
