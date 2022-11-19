# Random Recipes
It's very painful to search and choose what we are going to eat every day.  
I have lot of cooking book at home, so I created this script to select randomly one recipe in all of my books for each day of the week. 

## List of books

|Title|Author|
|:---:|:----:|
|Fait maison livre 1|Cyril Lignac|
|Fait maison livre 2|Cyril Lignac|
|Fait maison livre 3|Cyril Lignac|
|Fait maison livre 4|Cyril Lignac|
|Fait maison livre 5|Cyril Lignac|
|En 2h je cuisine pas cher pour toute la semaine|Stéphanie de Turckheim|


## How it works?

add your cooking books informations on [books_list.json](./books_list.json).
A book is defined by its:
- Title
- Author
- recipes-interval: it is the pages interval where the are recipes
- recipes-pages-list: it is the list of pages whare the are recipes

### Choose between "recipes-interval" and "recipes-pages-list"
recipes-interval is used when there is one recipe by double page
recipes-pages-list is used when the recipes pages are not regular interval