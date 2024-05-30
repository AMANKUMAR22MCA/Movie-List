# Movie Library

Movie Library is a web application that allows users to create and manage their own movie lists. Users can register, log in, search for movies using the OMDB API, and add movies to their selected lists.

## Features

- User Registration and Login
- Search for Movies
- Create and Manage Movie Lists
- Add Movies to Lists

## Technologies Used

- Frontend: HTML, CSS, JavaScript, Bootstrap, Axios
- Backend: Django, Django REST Framework
- Database: MySQL

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL
- OMDB API Key

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/movie-library.git
    cd movie-library
    ```

2. Set up the virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    ```sh
    mysql -u root -p
    CREATE DATABASE movie_library;
    ```

5. Configure your `.env` file with the following variables:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_NAME=movie_library
    DATABASE_USER=root
    DATABASE_PASSWORD=your_db_password
    DATABASE_HOST=localhost
    DATABASE_PORT=3306
    OMDB_API_KEY=your_omdb_api_key
    ```

6. Run the database migrations:

    ```sh
    python manage.py migrate
    ```

7. Start the development server:

    ```sh
    python manage.py runserver
    ```

8. Open the application in your browser at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **Register**: `/api/register/` (POST)
- **Login**: `/api/login/` (POST)
- **Search Movie**: `/api/search/` (POST)
- **Create Movie List**: `/api/movie_lists/` (POST)
- **Get Movie Lists**: `/api/movie_lists/` (GET)
- **Add Movie to List**: `/api/movie_lists/<list_id>/add_movie/` (POST)

## Usage

1. Register a new user.
2. Log in with the registered user credentials.
3. Create a new movie list.
4. Search for a movie by title.
5. Select a movie list.
6. Add the searched movie to the selected list.
7. View your movie lists.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Bootstrap](https://getbootstrap.com/)
- [Axios](https://github.com/axios/axios)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [OMDB API](http://www.omdbapi.com/)

![image](https://github.com/AMANKUMAR22MCA/Movie-List/assets/126316303/bf87e29c-9efa-4a09-b9d5-77b3a7f50390) <br>
![image](https://github.com/AMANKUMAR22MCA/Movie-List/assets/126316303/2c4c9250-588a-4d2c-be84-9d84cf575ac7) <br>
![image](https://github.com/AMANKUMAR22MCA/Movie-List/assets/126316303/6ccc71c7-eddf-4577-9fe9-a994f8357d4b) <br>
![image](https://github.com/AMANKUMAR22MCA/Movie-List/assets/126316303/91bf8d25-da16-45fe-832f-a788cdcadc00) <br>
![image](https://github.com/AMANKUMAR22MCA/Movie-List/assets/126316303/f463c2f6-4fa6-420d-84eb-88506ba3056b) <br>




