# Code/Astro 2026 Group 6 Project
### Authors: Sophie Clark, Ipsita Thakre, Anusha S, Anne-Claire Michel, and Yassmine Abdelhalim
Project goal: generate a program that intakes a user input for the year, then plots the mass-radius distribution for exoplanets detected up to that year, with a color-coding based on the detection method. If time permits, add a feature to pop up with further information about the exoplanet (i.e. host name, detection reference, etc.) when hovering over its point on the plot.

### Main code structure
1. Read in CSV file with the exoplanet data, and identify relevant columns (priority: mass*sin(i), planet radius, discovery method, & discovery year; secondary priority: planet name, host name, gaia_dr3_id, discovery reference, discovery facility, RA & Dec). Perhaps generate a pandas DataFrame with all the relevant columns for easier indexing.
2. Function that intakes a certain year, then filters the data by only rows where the discovery year <= the user input year.
3. Function that plots mass*sin(i) vs. radius, with each point color-coded by its discovery method (must include a legend). Must include a title with the user's input of the year. Label axes, add a grid to the plot.
4. Function that generates a textbox when a user hovers over a point on the plot, with the textbox showing the planet name, the host name, gaid dr3 id, discovery reference (author & year), discovery facility, and the RA & Dec. Will take some formatting to make sure everything looks correct. 
