# Code/Astro 2026 Group 6 Project: NASA Exoplanet Archive Visualizer
### Authors: Sophie Clark, Ipsita Thakre, Anusha S, Anne-Claire Michel, and Yassmine Abdelhalim
Project goal: generate a program that intakes a user input for the year, then plots the mass-radius distribution for exoplanets detected up to that year, with a color-coding based on the detection method. If time permits, add a feature to pop up with further information about the exoplanet (i.e. host name, detection reference, etc.) when hovering over its point on the plot.

### Main code structure
1. Build a query for the NASA Exoplanet Archive that downloads the most current data (see https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html), then generate a pandas DataFrame with the data. 
2. Identify relevant columns (priority: mass*sin(i), planet radius, discovery method, & discovery year; secondary priority: planet name, host name, gaia_dr3_id, discovery reference, discovery facility, RA & Dec). Create a new DataFrame with only the relevant columns. (I have uploaded a CSV file so this can still be done before the query part is completed)
3. Allow the user to input a year, then remove all rows from the DataFrame in which the discovery year is greater than the user's input year.
4. Plot mass*sin(i) vs. radius, with each point color-coded by its discovery method. Must include a legend for the colors, a title with the user's input year, axes labels, and a grid on the plot.
5. (Interactive module) Generate a textbox when the user hovers over a point on the plot, with the textbox showing the planet name, the host name, Gaia DR3 ID, discovery reference (author & year), discovery facility, and the RA & Dec.
6. Save the interactive figure with a name indicating what year the user input.
