Requirments:
1:Clint required to send key and username as query parameters.
2:Length of key should be 7 characters.
3:The first character should be lower case alphabet symbol which should be last character of username.
4:The third character should be 'Z'.
5:The 5th character should be first character of username.

==========================Example:==========================================
username:admin 
key:n2Z4a67
============================================================================

=========================How to send request via postman====================
----------------------------------------------------------------------------
GET-->http://127.0.0.1:8000/api/?username=admin&key=n2Z4a67
PUT-->http://127.0.0.1:8000/api/1/?username=admin&key=n2Z4a67
----------------------------------------------------------------------------
Params-->key-->username||value-->admin
Params-->key-->key||value-->n2Z4a67
=============================================================================