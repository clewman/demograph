# Demograph
## Public Access Analytics- Analytics for the People
A PDX Code Guild Capstone Project

This web application allows users to pull information from a database and create custom graphs. These graphs can be used for a variety of uses, including: student reports in science, social science, and English; socially motivated groups who need graphs in their reports, social media, advertising, and more; as well as for any person interested in seeing the relationship between poverty, education, employment, population size, and food access. 

This project will be wrapped in Django and include Python for parsing through the government data set, JavaScript to enhance the user experience, the D3 library, Plot.ly, to display the charts, and basic CSS and HTML with Materialize. 

When a user first goes to the page, they will see the story written in the first div. Under the story is a short introduction into how to use the site/graphs, along with an example graph. After they click the "begin" button, they will be taken to a page where they will see an empty title box with an input field for them to enter the title, and an empty chart beneath with a watermark in it. (The watermark is just for aesthetics so they don't see a completely blank box.) As soon as they save their title, the title appears at the top of the chart. Then a new input box slides in that allows the user to input the type of graph they would like to create. After that is chosen, the options for graph types slides down and to the right. Another input box slides in where they input the region they would like to compare the data in. After they choose the region, that box slides to the top right and another one slides in that allows them to select the data for the x axis, then the y axis. As elements are chosen, they are automatically populated into the graph. When all of the selections are made, the final presentation has three columns at the top with region, x axis, and y axis. These have dropdowns with the info so it can be changed. Under that is a large canvas on the left that has the labeled graph. On the right is the graph type options, with a small box underneath containing options for exporting the graph as a pdf, sharing the graph, and saving the graph. 

The input boxes will first appear using Materialize's Media Left Align Caption, which slides a div in. The database, SQLite, will capture the user input and add it to the database in this order: 1. title 2. map type 3. region 4. x axis 5. y axis. (Note: all fields will be required.) As each input is added to the database, Django will then update the chartjs with the new information. After each user input, Materialize will slide the input div to the right and stay there until the final page. The final page will use Materialize dropdowns for title, map type, region, and axes; display the full chartjs chart; and have two extra boxes with additional functionality- map types and print, save, and share. 

The data that I will need to store are: Title, Map Type, Region, X Axis, and Y Axis. 

Additional features: If I decide to allow users to save their maps/charts, then I will also need to create a user login system. If I have time, I would also like to use the charts to create predictive graphs based on past data.

Week 1: Create Django project, app, and associated files. Add templates and Materialize. Build models and views. 

Week 2: Create basic (non-js) divs, dropdowns, and input fields in templates. Add charts/maps and test. 

Week 3: Connect input and divs with Javascript for dropdowns and sliding divs. Probably more charts/maps.

Week 4: Style, catch user errors, and iron out kinks
