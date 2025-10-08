# API Gateway - CommanderMTG APP

This API Gateway serves as the central entry point for the CommanderMTG application, routing requests to various microservices including user management, game data, and authentication services.

**⚠️ Requirements:** 
- [Login Microservice running](https://github.com/Snr1s3/Login_microservice)
- [CommanderMTG API Microservice running](https://github.com/Snr1s3/CommanderMTGAPI.git)
- Python 3.8+

## Architecture

This gateway acts as a proxy between clients and backend microservices:
- **User Management**: Routes to Login Microservice
- **Game Data**: Routes to CommanderMTG API
- **Authentication**: Handles user login/logout
- **Data Aggregation**: Combines data from multiple services

## Configuration

Create a `settings.py` file in the `SRC/Routers/` directory with microservice URLs:

```python
# Microservice URLs
API_LOGIN_URL = "http://localhost:8443"      # Login Microservice
API_COMMANDERMTG_URL = "http://localhost:8442" # CommanderMTG API
```

## API Endpoints

### User Management

#### Get All Users
- **GET /all_users** - Retrieve all users
  ```bash
  curl http://localhost:8441/all_users
  ```

#### Get User by ID
- **GET /user/{id}** - Get specific user by ID
  ```bash
  curl http://localhost:8441/user/1
  ```

#### Create New User
- **POST /user/create** - Create a new user
  ```bash
  curl -X POST http://localhost:8441/user/create \
    -H "Content-Type: application/json" \
    -d '{
      "name": "john_doe",
      "mail": "john@example.com",
      "hash": "your_password_hash"
    }'
  ```

#### Authenticate User
- **POST /user/authenticate/** - Authenticate user credentials
  ```bash
  curl -X POST http://localhost:8441/user/authenticate/ \
    -H "Content-Type: application/json" \
    -d '{
      "name": "john_doe",
      "hash": "your_password_hash"
    }'
  ```

#### Update User
- **PUT /user/update** - Update user information
  ```bash
  curl -X PUT http://localhost:8441/user/update \
    -H "Content-Type: application/json" \
    -d '{
      "id": 1,
      "name": "john_updated",
      "mail": "john_new@example.com",
      "hash": "new_password_hash"
    }'
  ```

#### Delete User
- **DELETE /user/delete?id={id}** - Delete user by ID
  ```bash
  curl -X DELETE http://localhost:8441/user/delete?id=1
  ```

### Commander Management

#### Get All Commanders
- **GET /commanders/** - Retrieve all commanders with pagination and filtering
  ```bash
  curl "http://localhost:8441/commanders/?pag=1&limit=10&name=Atraxa"
  ```

#### Get Commander by ID
- **GET /commanders/{id}** - Get specific commander by ID
  ```bash
  curl http://localhost:8441/commanders/1
  ```

#### Create New Commander
- **POST /commanders/** - Create a new commander
  ```bash
  curl -X POST http://localhost:8441/commanders/ \
    -H "Content-Type: application/json" \
    -d '{
      "commander": "Atraxa, Praetors Voice"
    }'
  ```

#### Update Commander 
- **PUT /commanders/{id}** - Update of commander
  ```bash
  curl -X PUT http://localhost:8441/commanders/1 \
    -H "Content-Type: application/json" \
    -d '{
      "commander": "Atraxa, Praetors Voice (Updated)"
    }'
  ```

#### Delete Commander
- **DELETE /commanders/{id}** - Delete commander by ID
  ```bash
  curl -X DELETE http://localhost:8441/commanders/1
  ```

### Game Management (Partidas)

#### Get All Games
- **GET /partidas/** - Retrieve all games with pagination and filtering
  ```bash
  curl "http://localhost:8441/partidas/?pag=1&limit=10&winner=1"
  ```

#### Get Game by ID
- **GET /partidas/{id}** - Get specific game by ID
  ```bash
  curl http://localhost:8441/partidas/1
  ```

#### Create New Game
- **POST /partidas/** - Create a new game
  ```bash
  curl -X POST http://localhost:8441/partidas/ \
    -H "Content-Type: application/json" \
    -d '{
      "winner": 1
    }'
  ```

#### Update Game 
- **PUT /partidas/{id}** - Update of game
  ```bash
  curl -X PUT http://localhost:8441/partidas/1 \
    -H "Content-Type: application/json" \
    -d '{
      "winner": 2
    }'
  ```

#### Delete Game
- **DELETE /partidas/{id}** - Delete game by ID
  ```bash
  curl -X DELETE http://localhost:8441/partidas/1
  ```

### User-Commander Relationships

#### Get All User-Commander Relationships
- **GET /usuaris_commanders/** - Retrieve all relationships with pagination
  ```bash
  curl "http://localhost:8441/usuaris_commanders/?pag=1&limit=10"
  ```

#### Get Relationship by ID
- **GET /usuaris_commanders/{id}** - Get specific relationship by ID
  ```bash
  curl http://localhost:8441/usuaris_commanders/1
  ```

#### Create New Relationship
- **POST /usuaris_commanders/** - Create a new user-commander relationship
  ```bash
  curl -X POST http://localhost:8441/usuaris_commanders/ \
    -H "Content-Type: application/json" \
    -d '{
      "id_usuari": 1,
      "id_commander": 1,
      "id_partida": 1
    }'
  ```

#### Update Relationship 
- **PUT /usuaris_commanders/{id}** - Update of relationship
  ```bash
  curl -X PUT http://localhost:8441/usuaris_commanders/1 \
    -H "Content-Type: application/json" \
    -d '{
      "id_usuari": 1,
      "id_commander": 2,
      "id_partida": 1
    }'
  ```

#### Delete Relationship
- **DELETE /usuaris_commanders/{id}** - Delete relationship by ID
  ```bash
  curl -X DELETE http://localhost:8441/usuaris_commanders/1
  ```

## Usage

### Setup and Installation
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Start the FastAPI server
# Make sure that the database is running
./venv/bin/uvicorn SRC.main:app --reload --host 0.0.0.0 --port 8441
```

### Access the API
- **API Base URL**: http://localhost:8441
- **Interactive Documentation**: http://localhost:8441/docs
- **Alternative Documentation**: http://localhost:8441/redoc

## Docker Deployment

### Prerequisites
- Docker installed on your system
- PostgreSQL database running (can be in a container or host machine)

### Building the Docker Image
```bash
# Build the API Docker image
sudo docker build -t api-gateway .
```

### Running with Docker

#### Option 1: Connect to existing PostgreSQL database
```bash
# Make sure your PostgreSQL database is running first
sudo docker start postgres-db  # if using Docker for database

# Run the API container
sudo docker run -d \
  --name api-gateway-container \
  -p 8441:8441 \
  -e DB_HOST=172.17.0.1 \
  -e DB_PORT=8888 \
  -e DB_USER=postgres \
  -e DB_PASSWORD=your_password \
  -e DB_NAME=proj \
  api-gateway
```

#### Option 2: Using host database
```bash
# If database is running on host machine
sudo docker run -d \
  --name api-gateway-container \
  -p 8441:8441 \
  -e DB_HOST=172.17.0.1 \
  -e DB_PORT=5432 \
  -e DB_USER=postgres \
  -e DB_PASSWORD=your_password \
  -e DB_NAME=proj \
  api-gateway
```

### Docker Management Commands
```bash
# Check running containers
sudo docker ps

# View API logs
sudo docker logs api-gateway-container

# Stop the container
sudo docker stop api-gateway-container

# Start the container
sudo docker start api-gateway-container

# Remove the container
sudo docker rm api-gateway-container

# Remove the image
sudo docker rmi api-gateway
```

### Docker Network Notes
- Use `172.17.0.1` as DB_HOST to connect to services on the Docker host
- Make sure the PostgreSQL database accepts connections from Docker containers
- Port 8441 will be exposed for API access

