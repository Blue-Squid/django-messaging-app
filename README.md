# django-messaging-app
blog-messaging application with user authentication driven application.

1) Secret Key from settings.py is removed to protect local machine from non-local Users, but project should function normally once new 
   project is stated using (django-admin startproject [name]) command. 
2) Initially the application was dependent on MySQL database but I had to switch to SQLITE as I encountered minor issues with contrib.auth
   Should work fine once migrations are made. 
3) I had an idea to further develop the application to add security clearances, like say for instance high level communication won't be 
   shared by low ranking users. But the idea was scrapped due to time constraints. Be sure to implement it in future.
4) Data Models are simplified to make use of compact nature of Django 2.0.5 Only the most necessary information is pooled into model          classes, the remaining data is stored as staff users table to make use of existing schema.
5) Need for Java Script is reduced if not entirely redudant in this project as JINJA logic was far simpler and helped in achieving clean      code.
