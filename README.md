# Project Name: Blog

  This project aims to provide some basic blog functionality like:

  - adding product to cart, 
  - changing quantity of products, counting total price,
  - adding comments,
  - counting comments,
  - sending email by using Celery task,
  - autocomplete by ElasticSearch,
  - possibility to sign in via Facebook and GitHub.

# Project Structure:

  Project contains five application:
  
  1.Blog with Entry model.Following fields of Entry model:

    - Title
    - Body
    - Created
    - Modified
    - Pub_date
    - Comments_count

  2.Article with Article model.Fields of Article model are the same like in Entry model

  3.Comments with Comment model.Following fields of  of Comment model:

    - Body
    - Created

  4.Products with Product model.Following fields of  of Comment model:

    - Name
    - Price

  5.Cart with classic cart functionalities like:

    - Add products
    - Change quantity
    - Count total price

# Project status:

  	Project hasn't done yet
  
# Usage illustrations:  	
  ElasticSearch with autocomplete function:  	
  
  ![ElasticSearch](https://user-images.githubusercontent.com/56914063/97323190-d2626680-1870-11eb-9fb1-ebb8f333c130.png)

  Celery:

  <img width="480" alt="Zrzut ekranu 2020-10-27 o 16 38 38" src="https://user-images.githubusercontent.com/56914063/97325149-f757d900-1872-11eb-8fcb-ce17a51b5b99.png">
  
  Article comments using Celery:
  
  ![Zrzut ekranu 2020-10-27 o 16 57 38](https://user-images.githubusercontent.com/56914063/97327737-8e259500-1875-11eb-9e60-13fdfe0ebb3c.png)
  
  Login via Facebook and GitHub:
  
  ![Zrzut ekranu 2020-10-27 o 16 47 21](https://user-images.githubusercontent.com/56914063/97326274-202c9e00-1874-11eb-9168-3ca98d88637a.png)
  
  Authorization:
  
  ![Zrzut ekranu 2020-10-27 o 16 49 49](https://user-images.githubusercontent.com/56914063/97326625-7994cd00-1874-11eb-86dc-9620b52dc2eb.png)

  Cart Display:
  
  ![Zrzut ekranu 2020-10-27 o 16 48 44](https://user-images.githubusercontent.com/56914063/97326455-510cd300-1874-11eb-9241-afd6e98e339f.png)

  Total price of products:

  ![Zrzut ekranu 2020-10-27 o 17 03 19](https://user-images.githubusercontent.com/56914063/97328512-6256df00-1876-11eb-8fb6-457f19b3bb41.png)

  
# Sources:

https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html

https://docs.djangoproject.com/en/3.1/

https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html

https://stackoverflow.com/

https://www.itread01.com/content/1549417528.html
