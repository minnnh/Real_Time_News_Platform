### connection with client
- client is using react js to connect to server host.  
- server is using node js ("express": a layer built on the top of the Node js) to help manage servers and routes.     

### connection with backend-server
- server is using jayson to connect with backend-server rpc,  which would allow server to use the method in backend-server.  

### rpc_client
- use jayson connect with rpc backend-server
- import the method of backend-server

### middleware
- create the middleware that will protect selected routes and ensure that a user is authenticated before allowing their requests to go through
- `next()` in `app.use()` refers to pass to next layer of middleware

### models
- use mongoose to manage the schema (speciifically 'User' schema here)
- UserSchema:
	+ {'email': , 'password': }

### passport
- identify the user with the help of mongoose and other security method

### routes
- set up the router for each features
- auth '/auth'
	+ post: '/signup'
	+ post: '/login'
- news '/news'
	+ get: '/'
	+ get: '/userId/:userId/pageNum/:pageNum'
	+ post: '/userId/:userId/newsId/:newsId'

### app.js
- have to get the passport first, and then it can go to other routers