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

![scraping_mars_news_png](https://user-images.githubusercontent.com/103263248/180039447-c009da06-02b6-42b0-a091-b5ae73f38a08.png)

Creating a new DataFrame from the HTML table for Mars. Only pulling the desired data from the table and assigning columns to the new DataFrame. Setting the Description column to the DataFrame's index. The DataFrame is converted back to HTML-ready code.

![Mars_facts_df_png](https://user-images.githubusercontent.com/103263248/180039485-7c337165-7ef7-4a3c-96e3-a4509ae21667.png)

Automate finding and clicking the featured image for Mars. Pull the most recent JPL image instead of grabbing the URL directly. 

![featured_photo_scraping_png](https://user-images.githubusercontent.com/103263248/180039516-d3b92070-d47e-45bb-b264-a9c0a36d9c21.png)

## Scraping Full-Resolution Mars Hemisphere Images and Titles

Use the Chrome Developer Tools to inspect the page for the elements we want to scrape. Create a list to hold the image URL string and title for the hemispheres. Retrieve the hemisphere image URL and titles. Loop through the image URLs, click the link and find the [sample] image anchor tag and get the [href]. Save the image URL string and the image title as the key that is stored in the respective dictionary.

![hemisphere_scraping_png](https://user-images.githubusercontent.com/103263248/180039584-086b419b-b847-464e-bee0-e6b3e4459c3f.png)

## Store the data in MongoDB

MongoDB was used to store the data from the web scrape. 

![mongodb_mars_app_png](https://user-images.githubusercontent.com/103263248/180039612-39405029-a33d-4bb7-868d-1504f8a04713.png)

## Flask web application to display the data as HTML/CSS

Flask web application is run to display the data from the web scrape. 

![flask_png](https://user-images.githubusercontent.com/103263248/180039630-7ac963e9-541d-49e4-a413-3c6d8abddc8c.png)

## Website after Scraping:

![mission_to_mars_png](https://user-images.githubusercontent.com/103263248/180039654-41022cc2-b96e-49c7-9dff-917624656274.png)

## Bootstrap 3 to modify the HTML

Making the webpage mobile-responsive.

![mobile_responsive_png](https://user-images.githubusercontent.com/103263248/180039676-001243de-7f2d-4c5e-96ef-1877822036cc.png)

Additional components to style the webpage.

![style_the_html_png](https://user-images.githubusercontent.com/103263248/180039726-6b512069-978a-46ef-9f80-ac8ce4e55a7b.png)

* Styled the background with colors. 

* Changing the text colors to be visible with the new colors.

* Styling text titles to "strong" for bold text.

* Changing the button color to warning to match new color scheme.

* Setting high-resolution Mars hemisphere images to round thumbnail style.

