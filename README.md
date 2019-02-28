[![Build Status](https://travis-ci.org/dcasey720/django_soil_submit.svg?branch=master)](https://travis-ci.org/dcasey720/django_soil_submit)


Full Stack Software Development: Easca Environmental 
=========================================================

This Django project is a combined online shop and lab managment system for an environmental science laboratory, offering a variatey of soil testing services.

The key features of the app are:

* Customer can 'Order a Sample Kit', they will then receive a sample kit in the post with a reference number
* Customer can 'Submit Sample Details' online
* Staff can 'Receive Sample' into the lab for testing
* Staff can 'Upload Results'
* Customer and Staff can 'View Report' of the sample details and results

This project was developed as the final project in a diploma in Full Stack Software Development through The Code Institute, with consultation with Soutern Scientific Services.

UX
----
The app was developed to be used by farmers requireing soil testing and by the lab staff providing the testing.

__User Stories__

User stories were developed to plan out the features for the application.

__Site Visitor User Story__

* As a site visitor I should see the different services on offer, the purpose of each service and price of each service.
* As a site visitor I should be able to add services to a shopping cart.
* As a site visitor I should be able to view the contents of the shopping cart
* As a site visitor I must log in or register to order a service a service

__Registered User User Story__

* As a registered user I should be able to place an order.
* As a registered user I should be able to pay in a secure and confidential manor.
* As a registered user I should get a valid receipt after paying.
* As a register user I should be able to submit the soil sample details online,
using a sample reference number printed on the soil sample kit received in the post.
* As a registered user I should be able to update my user info and change my password.
* As a registered user I should be able to view my order history including the status of samples being processed and view test result reports.
* As a registered user I expect the results to be presented to in a clear report.
* As a registered user I should be provided by an emailed confirmation of my orders change of status. 


__Staff User Story__

* As lab staff I should have all the features availble to a registered user, so I can submit sample details for site visits.
* As lab staff I should be able to view the full sample database.
* As lab staff I should be able to filter the database for customers, order status and location.
* As lab staff I should be able to mark samples as 'received' when the sample reaches the lab. 
* As lab staff I should be able to upload results of tests.
* As lab staff I should be able explore the full sample archive, provided with the sample details, as well as when and by who the sample was received and tested.
* As lab staff I should be able to filter the sample archive for ease of use.

__Admin User Story__

* As admin I should have all Staff privileges
* As admin I should be able to backup the database as .csv file.

Features 
---------

__Existing Features__

* Display soil sample services on offer
* User registration
* Customer can order samples
* Unique sample_reference number is generated for each sample ordered
* Customer can submit the sample details through the 'Your Portal' view. A google map is used for marking the sample position. Geocoding automatically saves the address
* Customer can view all their samples and access the report with results displayed if the results are available
* Staff can mark the sample as "received" when it comes into the lab, through the 'Lab Portal' view, this processes is time stamped and the loged in staff member is recorded
* Staff can upload the test results, through the 'Lab Portal' view, this processes is time stamped and the loged in staff member is recorded
* Staff can view all samples and access the report with results displayed if the results are available
* Customer is emailed an order is placed and when results are availalbe


__Features to be Implemented__

* ! 3hr Use HTML5 Geolocator function to set sample_location, may be awkard as the django-geoposition marker initial position is set in settings.py not in the template

*  3hr Automated Testing
*  3hr Manual Testing

* 2hr Show test results using a dc.js chart making it clear where the soil nutrients sit relatie to the nutrient threshholds for the specific land use
* 1hr Add save/print pdf button to the report
* 1hr Filter search for sample archive
* 2hr Map showing markers for all samples
* 1hr add pagniation to tables

* use input box instead of table to submit details
* javascript in seperate file



Technologies Used
-----------------------
* __VisualStudios2017__ (https://visualstudio.microsoft.com/downloads/) IDE was used in the development of the project.
* __VirtualEnvironment__ (https://docs.python.org/3/library/venv.html) was used to wrap the project.
* __Git__ (https://git-scm.com/) was used for version control.
* __GitHub__ (https://github.com/) was used to share the repository.
* __Heroku__ (https://dashboard.heroku.com/) was used to host the application.
* __Python3.6__ (https://docs.python.org/3/) was used to develop all back-end code.
* __HTML5__ (https://www.w3.org/TR/html5/) was used to develop front-end templates.
* __CSS__ (https://www.w3.org/Style/CSS/) was used for styling of front-end templates.
* __Bootstrap 3.3.7__ (https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css) was used for more effective CSS layout styling.
* __Font-Awesome 5.3.1__ (https://use.fontawesome.com/releases/v5.3.1/css/all.css) was for the icons in the header, footer and quiz template.
* __JavaScript__ was used for interactive frontend development.
* __GeoPy__ (https://geopy.readthedocs.io/en/stable/) was used to get the address of the substations
* __FluidUI__ (https://www.fluidui.com) was used to develop wireframes for the initial UI design mockups.
* __Unittest__ (https://docs.python.org/3/library/unittest.html) unit testing framework was used for the testing of none template rendering functions.
* __json__ (http://www.json.org/) was used to store and access non-database data.
* __CSVJSON__ (https://www.csvjson.com/csv2json) was used to convert CSV formatted data to json.
* __Firefox Developer Edition__ (https://www.mozilla.org/en-US/firefox/developer/) was used for debugging of the running app.
* __Stripe__
* __GeoPy__
* __GeoPosition__
* __Django-1.11.18


Testing
-----------------------

__Continuous Integration__

Travis CI was used for continuous integration insuring that the host environment and requirements are met through out hte development.

__Code Validation__

* __Python__ was validated using http://pep8online.com/. Both run.py and test_app.py are pep8 compliant.
* __HTML__ was validated using https://validator.w3.org/. Due to the python code embedded in the HTML templates there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/. No errors were found.
* __Spelling and Grammar__ was validated using Google Docs.

__Unittest Automated Testing__



__Visual Testing__

The dev tool within Firefox Development Edition was used to test that the pages were displaying correctly (alignment, spacing, position etc.) across different screen widths.


|                                                       | Galaxy S5 | Pixel 2 | Pixel 2XL | iPhone 5/SE |	iPhone 6/7/8 | iPhone 6/7/8 + | iPhone X | iPad  | iPad Pro   | Responsive 1366 x 768 | Responsive 1680 x 1050 |  
| ----------------------------------------------------- | --------- | ------- | --------- | ----------- | -------------- | -------------- | -------- | ------| ---------- | --------------------- | ---------------------- |


__Manual Testing__

The following test were performed manually.

|    Feature            |   Test Action                                                                             |   Expected Result                                |  Chrome (Desktop) |  Firefox (Desktop)  | Chrome (Mobile) |
| --------------------- | ------------------------------------------------------------------------------------------| ------------------------------------------------ | ----------------- | ------------------- | --------------- |

__Known Bugs__




Development
------------------------

Deployment
------------------------


__Requirements__

The system hosting the app must have a number of python packages installed.
A full list can be found at 

https://github.com/dcasey720/django_soil_submit/blob/master/requirements.txt

Take note that a pip freeze will include django-geoposition-0.3.1, instead of https://github.com/philippbosch/django-geoposition/archive/django-1.11.zip.
Django-geopositions latest release availabel to install with pip is 0.3.0., however this version will not work with django-1.11 and so the work around branch must be installed.

__System Variables__

The following system variables must be set in the host environment.

* STRIPE_PUBLISHABLE, publishible key assigned to you when you register an account with Stripe https://stripe.com/ie
* STRIPE_SECRET, secret key assigned to you when you register an account with Stripe https://stripe.com/ie
* EMAIL_HOST_USER, the email address you will use to send emails to application users. This can be your personnel email adress i.e. johndoe@gmail.com
* EMAIL_HOST_PASSWORD, your specified email host login password
* SECRET_KEY, generated by django when you start a new app. See setttings.py file
* GOOGLE_MAP_API_KEY, assigned when setting up a google maps api account, https://cloud.google.com/maps-platform/, insure that both 'Maps' and 'Places' products are availabe to the key.
* DATABASE_URL, generated when you set up a PostGres database, i.e. when using 'Heroku Postgres' add-on under resources when deploying app on Heroku.

__Deployed vs Development__

* The 'mock-ups' folder is removed for deployment.
* Settings.py line 34, DEBUG = False for deployment.

   

Running App
------------------------

https://easca-environmental.herokuapp.com/

