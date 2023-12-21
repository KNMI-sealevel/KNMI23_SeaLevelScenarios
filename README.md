# KNMI23_SeaLevelScenarios
 Code used to develop the KNMI23 sea level scenarios and produce figures for the user report and scientific report.
 
 ## Use the code to make scenarios for a new regions
First the NETCDF files of a the base scenarios need to be produced in [SLProj](https://github.com/dlebars/SLProj). There a new region needs to be defined.

Then produce the long term projections, up to 2300, using _LongTermProj.ipynb_. Make sure to update the link to the base projections.

Finally, the Low Likelihood High Impact (LLHI) scenarios can be made with _LPHI.ipynb_.



