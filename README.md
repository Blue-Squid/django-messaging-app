# django-messaging-app
blog-messaging application with user authentication driven application.

1) Secret Key from settings.py is removed to protect local machine from non-local Users, but project should function normally once new 
   project is stated using (django-admin startproject [name]) command. 
2) Initially the application was dependent on MySQL database but I had to switch to SQLITE as I encountered minor issues with contrib.auth
   Should work fine once migrations are made. 
3) I had an idea to further develop the application to add security clearances, like say for instance high level communication won't be 
   shared by low ranking users. But the idea was scrapped due to time constraints. Be sure to implement it in future.
   
