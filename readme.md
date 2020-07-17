[![codebeat badge](https://codebeat.co/badges/b41c7300-bc2e-4775-b8cb-9f69ea32a81a)](https://codebeat.co/projects/github-com-brayokenya-awwwards-master)

# Awwwards

#### A Django awwwards clone

## User Story
User can sign in to the application to start using.
User can upload my websites to the application.
User can view any profile with all websites.
User can Rate a website

## API ENDPOINTS

[User Endpoint](https://awards111.herokuapp.com/users/)


## Author
[Brian Kiiru](https://github.com/brayokenya)

## Technologies Used
* Python 3.8.1
* Django 3.0.8
* Postgress
* HTML5  
* CSS3
* Javascript
* jQuery 3.4.1
* Bootstrap 4



## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install django==3.0.8`**
* This project requires you to have a secret key from Cloudinary to facilitate cloud storage of uploaded images.
    * The secret key can be gotten by creating a free Cloudinary account, starting a new project and navigating to the dashboard
    * The key should be stored as an enviremnetal variable in an .env file as hown below
        * **`SECRET=<your secret key here>`**
    * More info onhow to use the Django ft Cloudinary library can be found [here](https://cloudinary.com/documentation/django_integration)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/brayokenya/Awwwards.gitgit`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.


## Known Bugs
* No known bugs


## Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:
* kiirubrian21@gmail.com

## Live Site link
You can view the live application by following this [link](https://awwwardsu1.herokuapp.com/).

## License
#### [*GNU License*](LICENSE)
