needs python3 and pip installed
run start-server.sh  (eventually dit it and replace "python3" with whatever python command you use)

ip webserver : http://127.0.0.1:8000/

routes :

'Get' routes with html response :
/front/device/
/front/device/<int:pk>
/front/digital/<int:pk> + '?gpio='

'Get' routes with json response :
/front/json/device/ (+ '?reachable=true' for reachable devices only)
/front/json/device/<int:pk>

'Post' routes :
/front/digital/<int:pk> '?gpio= &value= '