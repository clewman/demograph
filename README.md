# Demograph
## Public Access Analytics- Analytics for the People
A PDX Code Guild Capstone Project


Project Overview
This web application allows users to pull information from a database and create custom graphs. These graphs can be used for a variety of uses, including: student reports in science, social science, and English; socially motivated groups who need graphs in their reports, social media, advertising, and more; the farming industry who need data on exports, commodities, farm scale, consumption, sales, and labor; as well as for any person interested in seeing the relationship between poverty, education, employment, population size, food access, and farm characteristics. 

This project will be wrapped in Django and include Python for parsing through the government data set, JavaScript to enhance the user experience, chartjs to display the charts, and basic CSS and HTML with either Bootstrap and Materialize. 

When a user first goes to the page, they will see the story written in the first div. Under the story is a short introduction into how to use the site/graphs, along with an example graph. After they click the "begin" button, they will be taken to a page where they will see an empty title box with an input field for them to enter the title, and an empty chart beneath with a watermark in it. (The watermark is just for aesthetics so they don't see a completely blank box.) As soon as they save their title, the title appears at the top of the chart. Then a new input box slides in that allows the user to input the type of graph they would like to create. After that is chosen, the options for graph types slides down and to the right. Another input box slides in where they input the region they would like to compare the data in. After they choose the region, that box slides to the top right and another one slides in that allows them to select the data for the x axis, then the y axis. As elements are chosen, they are automatically populated into the graph. When all of the selections are made, the final presentation has three columns at the top with region, x axis, and y axis. These have dropdowns with the info so it can be changed. Under that is a large canvas on the left that has the labeled graph. On the right is the graph type options, with a small box underneath containing options for exporting the graph as a pdf, sharing the graph, and saving the graph. 
Functionality
Walk through the application from the user's perspective. What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

Data Model
What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'.

Schedule
Here you'll want to come up with some (very rough) estimates of the timeframe for each section. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.
