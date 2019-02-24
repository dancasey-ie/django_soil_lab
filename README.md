[![Build Status](https://travis-ci.org/dcasey720/django_soil_submit.svg?branch=master)](https://travis-ci.org/dcasey720/django_soil_submit)


Full Stack Software Development: Easca Environmental 
=========================================================

This project was developed as the final project in a diploma in Full Stack Software Development through The Code Institute. 
The web-app developed digitalises processes for a made up envirnonmental science lab, Easca Environmental, offering a variatey of soil testing services.
The app was developed with consultation with Southern Scientific, with the intention of adopting the app for digitising their processes, 
reducing paper work and allowing lab technicians to concentrating on the science.

With the app a customer can choose and order a soil sample kit appropriete to their needs.
After receiveing the sample kit in the post, the customer can submit required sample details (location, date, soil type etc)
online, before sending the soil sample into the lab.
The staff can keep record of the status of the sample through the web app and after testing upload the results as a report for the customer to view.

The app is developed using Django framework for efficient developement. A Postgres relational database is used for the storing data.

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


UX
----


__User Stories__

User stories were developed to plan out the features for the application.

__Site Visitor User Story__
*As a site visitor I should see the different services on offer, the purpose of each service and price of each service.
*As a site visitor I should be able to add services to a shopping cart (water sample kit, soil sample kit).
*As a site visitor I should be able to view the contents of the shopping cart
*As a site visitor I should be made aware that the prices in the shopping cart are preliminary, that they will not be charged when ordering but will be charged when the result are availables, at which point they will have more options for customising the the test and thus its final cost. 
*As a site visitor I must log in or register to order a service a service

__Registered User User Story__
*As a registered user I should be able to place an order.
*As a registered user I should be able to pay for the results in a secure and confidential manor.
*As a registered user I should get a valid receipt after paying.
*As a register user I should be able to submit the soil sample details online,
using a sample reference number printed on the soil sample kit received in the post.
*As a registered user I should be able to update my user info and change my password.
*As a registered user I should be able to view my order history including the status of samples being processed and view test result reports.
*As a registered user I expect the results to be presented to me in a clear graphical manor.
*As a registered user I should be provided by an emailed confirmation of my orders change of status. 


__Staff User Story__
*As lab staff I should have all the features availble to a registered user, so I can submit sample details for site visits
*As lab staff I should be able to view the full sample database.
*As lab staff I should be able to filter the database for customers, order status and location.
*As lab staff I should be able to mark samples as 'received' when the sample reaches the lab. 
A record should be kept of who received the sample and when it was received. This should be automated using the login in user.
*As lab staff I should be able to upload results of tests.
A record should be kept of who tested the sample and when it was tested. This should be automated using the login in user.

__Admin User Story__
*As admin I should have all Staff privileges
*As admin I should be able to change registered user passwords
*As admin I should be able to delete users from the database
*As admin I should be able to backup the database as .csv file.



Features and Process
-----------------

__Existing Features__




Testing
-----------------------

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

__Hosting__

The application is hosted on Heroku.

A Procfile is required by Heroku to know what language to launch the application as. 
In Heroku the config variables were set:

IP: 

__Requirements__

The requirements for running the app can be found at:
https://github.com/dcasey720/django_soil_submit/blob/master/requirements.txt

__Deployed vs Development__


   

Running App
------------------------

https://easca-environmental.herokuapp.com/

