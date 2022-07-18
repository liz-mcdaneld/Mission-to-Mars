# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set the executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# Mars Facts
# Adding HTML to a DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert df back to html
df.to_html

# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# Parser
html = browser.html
browser.visit(url)
html_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.
hemisphere_image_titles = []
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.
mars_hemisphere_html = browser.html
mars_hemisphere_soup = soup(mars_hemisphere_html,"html.parser")
mars_hemispheres =  mars_hemisphere_soup.find_all("div", class_ = "item")

# Loop through the full-resolution image URL
for item in mars_hemispheres:
    
    # Create an empty dictionary
    hemispheres = {}
    
    link = item.find("a",class_="itemLink product-item").get("href")
    hemisphere_url = url + link
    print(hemisphere_url)
    
    browser.visit(hemisphere_url)
    hemisphere_html = browser.html
    hemisphere_soup = soup(hemisphere_html,"html.parser")
    
    # Image 
    image = hemisphere_soup.find("img",class_ = "wide-image").get("src")
    
    # Title
    title = hemisphere_soup.find("h2",class_ = "title").text
    
    # Add image urls to hemispheres dictionary
    hemispheres["title"] = title
    hemispheres["img_url"] = f'{url}{image}'
    hemisphere_image_urls.append(hemispheres)
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

