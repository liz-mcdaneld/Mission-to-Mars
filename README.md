# Mission to Mars
## Overview
 Scrape websites for the latest Mars news, facts about Mars, featured image of Mars, and photos of its four hemispheres. Data that is scraped will be stored in Mongo database. Create a web application to display the data and alter the design using Bootstrap.

## Purpose
* Use Chrome Developer Tools to identify HTML components.
*  Use BeautifulSoup and Splinter to automate web scraping.
* Use Mongo to store the data.
* Create web application using Flask to display the data in HTML.
* Use Bootstrap components to polish and customize the HTML.

## Web Scraping Mars data

Chrome Developer Tools, the inspect tool, is used on the website to find the HTML components to scrape the latest news articles. Using BeautifulSoup and Splinter to find the data and scrape it from the websites.

[scraping_news]

Creating a new DataFrame from the HTML table for Mars. Only pulling the desired data from the table and assigning columns to the new DataFrame. Setting the Description column to the DataFrame's index. The DataFrame is converted back to HTML-ready code.

[mars_facts_png]

Automate finding and clicking the featured image for Mars. Pull the most recent JPL image instead of grabbing the URL directly. 

[featured_photo]

## Scraping Full-Resolution Mars Hemisphere Images and Titles

Use the Chrome Developer Tools to inspect the page for the elements we want to scrape. Create a list to hold the image URL string and title for the hemispheres. Retrieve the hemisphere image URL and titles. Loop through the image URLs, click the link and find the [sample] image anchor tag and get the [href]. Save the image URL string and the image title as the key that is stored in the respective dictionary.

[hemisphere scraping]

## Store the data in MongoDB

MongoDB was used to store the data from the web scrape. 

[Mongo]

## Flask web application to display the data as HTML/CSS

Flask web application is run to display the data from the web scrape. 

[Flask]

## Website after Scraping:

[Website]

## Bootstrap 3 to modify the HTML

Making the webpage mobile-responsive.

[mobile]

Additional components to style the webpage.

[style]

* Styled the background with colors. 
* Changing the text colors to be visible with the new colors.
* Styling text titles to "strong" for bold text.
* Changing the button color to warning to match new color scheme.
* Setting high-resolution Mars hemisphere images to round thumbnail style.

