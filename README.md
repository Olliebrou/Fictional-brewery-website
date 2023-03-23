# Fictional-brewery-website
A Django web app for a fictional Brewery. This readme file contains instructions on how to set up the project on your local machine, including how to download the repository, download Python, create a virtual environment, and download dependencies. It also includes instructions on how to run the server and how to create a Docker container from the included Dockerfile.

## Installation

### Download the Repository
Click on the "Code" button on this repository and select "Download ZIP". Alternatively, you can clone the repository using Git with the following command:

git clone https://github.com/Olliebrou/Fictional-brewery-website.git
Extract the ZIP file to your desired location.

Open a terminal window and navigate to the directory where you extracted the repository.

### This project uses Python.
If you do not have Python, you can download it here: https://www.python.org/downloads/

Use the following commands to install pip, a virtual environment and Django on a windows machine:
python -m pip install pip
pip install virtualenv
pip install virtualenvwrapper-win
mkvirtualenv <choose a name for your virtual environment>

This should automatically activate the virtual environment.

Open a terminal window and navigate to the directory where you saved the repo.


## Dependencies
In the project directory, you will find a requirements.txt file which lists all the required dependencies.

To download the dependencies, run the following command in the terminal while your virtual environment is activated:

pip install -r requirements.txt


## Running the Server
After downloading the dependencies, you can run the development server with the following command:

python manage.py runserver

The development server should now be running at http://127.0.0.1:8000/.

## Docker Setup
Download and install Docker from the official website: https://www.docker.com/get-started

Navigate to the project directory in your terminal.

Build the Docker container using the included Dockerfile with the following command:

docker build -t django-project .

Run the container using the following command:

docker run -p 8000:8000 django-project

The development server should now be running at http://127.0.0.1:8000/.

## Usage
The website requires users to login to gain access. You can register and create a new account or use the admin login.
The admin username is "admin" and the password is "password"
Using the admin user allows you to change settings on the site as well as add and delete users and beers from the store.
This can be accessed by going to http://127.0.0.1:8000/admin/ whilst being logged in as admin.


## License
This project is licensed under the MIT License. See the LICENSE file for details.
