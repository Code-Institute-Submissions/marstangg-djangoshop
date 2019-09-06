<h1>Djangoshop </h1>- https://djangoshop-mt.herokuapp.com/

Djangoshop  is focused on both Front End and Back End Development skills.
A fictitious online clothing shop for men with the following requirements below:
* the website is user and mobile friendly
* the website design helps to create a good brand image
* customers can view and sort, filter products on the website, register, add products to the shopping bag, edit shopping bag, buy products and view orders on their account, as also update their delivery address or other account details.
The project was made from scratch following the guidance of the course material. 
The project was made keeping in mind possible future functionality updates. 
Pages

The website has the following pages:
* Homepage
* Products page with all products
* Individual product page
* Shopping bag page
* Checkout page
* Login/ Register page
* Shopping cart
* Checkout page 
* Payment page

Features

The features of this application are as follows:
* Ability to Register, Sign into and Logout of an Account
* Ability to browse through products easily
* Ability to select individual product for more information
* Ability to select desired product and add to shopping cart while continuing to shop
* Ability to use credit card to pay via stripe payment process.
* Ability to store credit card details for future usage.

Features Left to Implement
* Searching / filtering by categories.
* Discount coupons
* Other payment options eg. Paypal

Technologies Used

1. Django
2. Python
3. HTML
4. CSS
5. Bootstrap

Testing

Besides that the website was constantly tested during the development process. Browser developer tools were used to test HTML, CSS, JavaScript and responses from the server. For testing JavaScript console.log() function was used to log and test information and for testing Python the function print was used to test statements as also Python Console to test algorithms. The command "python manage.py shell" was often used in the terminal to test Django functions and database. The website also was tested from the user perspective and from the admin perspective.
The website was tested in all browsers and functionality changed accordingly to make sure that the website works well in all browsers (e.g. initially Bootstrap carousel was used for sliders but it did not work correctly on Internet Explorer, and after not being able to find a solution, the Slick slider was used instead which worked perfectly in all browsers).
 HTML code was validated using The W3C Markup Validation Service. Validation service noted that alt tag was missing for one image, role attribute was missing for one dropdown menu, type attribute was not required for script tag and all scripts were placed outside body element. All issues were addressed and code amended accordingly.
JavaScript code was validated with JSLint, Esprima, JSHint online validators. 
The website was tested on different screen sizes using Google Device Toolbar in Google Chrome Developer Tools as also using Mobile/RWD Tester extension in Google Chrome. The website was tested on Windows desktop computer and on various phones, S10 and iPhone 8 The website was also tested in Safari browser on iPad Pro 10.2 and on my MacBook Air.
CONTRIBUTIONS
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Deployment

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base.
The development version of my application is on GitHub and I push this code using git push origin master and the code is run and tested on Cloud 9 before being updated to heroku
Create a remote Git repo for your app on Heroku


PART 1 
1. Install the following using pip3:

sudo pip3 install gunicorn
sudo pip3 install psycopg2
sudo pip3 install whitenoise

2. Make sure to include the following settings for static files and uploads, if they are not there already:

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


3.  Create the requirements.txt file using bash

pip3 freeze --local > requirements.txt

6. 
Create a local git repo for your project and connect it to a GitHub repo. Include the relevant .gitignore file.  If you have not done so. MAKE SURE migrations folder are not excluded!

sudo git init 
sudo git add .
sudo git commit -m "First commit"
sudo git remote add origin <GITHUB REMOTE URL>
sudo git push origin master


7. Put staticfiles/  and media/ inside .gitignore
8. Log into heroku by typing in heroku login and pressing ENTER
9. Create an app ( do it via the command line, don't do it via the Heroku webpage). If you opt for the command line and the push to Heroku

heroku create <PROJECT NAME> 
git remote -v




PART 2| Installing Postgres SQL


1. 
Type in bash:

heroku addons:create heroku-postgresql

2. Install with pip3:

sudo pip3 install dj_database_url

3. Check the url of the database:

heroku config

4. Add the URL to the database configurations inside settings.py

# import at the top
import dj_database_url
# then...
DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}

5. Migrate your database

python3 manage.py migrate



You must add all the environment variables in your .bashrc over to Heroku. There are two ways to do it - through the web dashboard, or using the bash CLI.

USING BASH
For example, if I have the following in my .bashrc:


export STRIPE_PUBLISHABLE_KEY="pk_test_aaa"
export STRIPE_SECRET_KEY="sk_test_bbb"
export UPLOADCARE_SECRET_KEY="8057…."
export UPLOADCARE_PUBLIC_KEY="4466..."


First, make sure you are logged into Heroku, in the CLI, by typing:

heroku login


Then type into the CLI, following the examples below, to set your environment variables. Press [ENTER] at the end of each line.


heroku config:set STRIPE_PUBLISHABLE_KEY=pk_test_aaa
heroku config:set STRIPE_SECRET_KEY=sk_test_bbb
…

PART 3| Deploying

1. Commit the changed files


sudo pip3 freeze --local > requirements.txt
sudo git add .
git commit -m "<YOUR COMMENT MESSAGE>"
git push origin master

2. Create the procfile:


touch Procfile

3. And enter into the Procfile:


web: gunicorn <PROJECT_FOLDER>.wsgi:application

4. Add the URL of the heroku app into the ALLOWED_HOST inside settings.py
5. Add and commit, and create the superuser on the Heroku app:


sudo git add .
sudo git push heroku master
heroku run python manage.py createsuperuser

Credits

Would like to credit Justdjango for his online tutorials and videos for this project to take place.