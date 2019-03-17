[![Build Status](https://travis-ci.org/dcasey720/django_soil_lab.svg?branch=master)](https://travis-ci.org/dcasey720/django_soil_lab)


Full Stack Software Development: Soil Laboratory LIMS
=========================================================

This Django project is a combined online shop and laboratory information management system (LIMS) for an environmental science laboratory, offering a variety of soil testing services.

The key features of the app are:

* Customer can 'Browse' the range of soil testing services offered
* Customer can 'Order' a sample test kit of their choosing (In production the sample collection kit will be posted to to the customer)
* Customer can 'Submit Sample Details' online. GPS tagging the sample using their devices location identification functionalities
* Staff can 'Receive Sample' into the lab for testing
* Staff can 'Upload Results'
* Customer and Staff can 'View Report' of the sample details and results

This project was developed as the final project in a diploma in Full Stack Software Development through The Code Institute, with consultation with Southern Scientific Services (https://southernscientificireland.com/).

The running site can be accessed here https://dc-easca-environmental.herokuapp.com/

UX
----
The app was developed to be used by individual farmers and agricultural advisors requiring soil testing and by the lab staff providing the testing.

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

* As lab staff I should have all the features available to a registered user, so I can submit sample details for site visits.
* As lab staff I should be able to view the full sample database.
* As lab staff I should be able to filter the database for customers, order status and location.
* As lab staff I should be able to mark samples as 'received' when the sample reaches the lab.
* As lab staff I should be able to upload results of tests.
* As lab staff I should be able explore the full sample archive, provided with the sample details, as well as when and by who the sample was received and tested.
* As lab staff I should be able to filter the sample archive for ease of use.

__Admin User Story__

* As admin I should have all Staff privileges
* As admin I should be able to backup the database as .csv file.

__Wireframes__

Wireframe mock ups were developed using FluidUI and can be viewed here - https://github.com/dcasey720/django_soil_lab/tree/master/mock-ups

Features
---------

__Existing Features__

* Display soil sample services on offer
* User registration
* Customer can order samples
* Unique sample_reference number is generated for each sample ordered
* Customer can submit the sample details through the 'Your Portal' view. A google map is used for marking the sample position. HTML5 geolocation is used for initialising the marker position Geocoding automatically saves the address
* Customer can view all their samples and access the report with results displayed if the results are available
* Staff can mark the sample as "received" when it comes into the lab, through the 'Lab Portal' view, this processes is time stamped and the logged in staff member is recorded
* Staff can upload the test results, through the 'Lab Portal' view, this processes is time stamped and the logged in staff member is recorded
* Staff can view all samples and access the report with results displayed if the results are available
* Sample report shows the sample details (including the position on a google maps window), the results for each test is shows in a color coded table.
* Customer is emailed when an order is placed and when results are available
* Pagination of tables in Your Portal
* Filter of samples in Lab Portal

__Future Features__

* As admin I should be able to backup the database as .csv file.
* Barcodes reflecting the sample reference will be printed on stickers which will be applied on each sample kit
* Barcode scanner will be used for dispatching and receiving the samples
* Results will be uploaded from CSV files generated by the lab testing equipment
* Develop results tables for the other elements tested for by the lab i.e. B, Mg, Cu, Zn & ER Mn ect

Technologies Used
-----------------------
* __VisualStudios2017__ (https://visualstudio.microsoft.com/downloads/) IDE was used in the development of the project.
* __VirtualEnvironment__ (https://docs.python.org/3/library/venv.html) was used to wrap the project.
* __Git__ (https://git-scm.com/) was used for version control.
* __GitHub__ (https://github.com/) was used to share the repository.
* __Heroku__ (https://dashboard.heroku.com/) was used to host the application.
* __Python3.6__ (https://docs.python.org/3/) was used to develop all back-end code.
* __Django-1.11.18 (https://www.djangoproject.com/) web development framework was utilised for efficient app development.
* __HTML5__ (https://www.w3.org/TR/html5/) was used to develop front-end templates.
* __CSS__ (https://www.w3.org/Style/CSS/) was used for styling of front-end templates.
* __Bootstrap 3.3.7__ (https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css) was used for more effective CSS layout styling.
* __Font-Awesome 5.3.1__ (https://use.fontawesome.com/releases/v5.3.1/css/all.css) was for the icons were used for user familier icons.
* __JavaScript__ was used for accessing Google Maps API and changing page display icons based on state i.e. collapse/expand icons and accessing client side features i.e. getLocation.
* __Google Maps__ (https://developers.google.com/maps/documentation/) was used to display map windows and select locations.
* __Google Fonts __ (https://fonts.google.com/) were used for the nav bar text and the home page quote.
* __FluidUI__ (https://www.fluidui.com) was used to develop wireframes for the initial UI design mockups.
* __Firefox Developer Edition__ (https://www.mozilla.org/en-US/firefox/developer/) was used for debugging of the running app.
* __Stripe__ (https://www.stripe.com) was used for secure credit card payments
* __django-geoposition__ (https://pypi.org/project/django-geoposition/) was used to enable to select a geographical location using the a google maps API
* __GeoPy__ (https://geopy.readthedocs.io/en/stable/) was used to get the address of sample locations set using django-geoposition
* __Pillow__(https://pypi.org/project/Pillow/) Python Imaging Library used for interpreting images
* __PostgresSQL__(https://www.postgresql.org/) open source object-relational database was used for storing data
* __Whitenoise__ (https://pypi.org/project/whitenoise/)  allows the web app to serve its own static files
* __Canvas__ (https://www.canva.com/) was used to develop a logo for the site though in the end font awesome and standard text were used

Testing
-----------------------

__Code Institute Testers__

As this site is designed by both lab staff and customers and the actions possible by each is reliant on the other, I commend the following. It is best to use two different browsers i.e. Chrome and Firefox so that the tester can be logged in as two users at once.

* Open the site and sign in as a Staff Member using __username:__ nice_assessor __password:__ StaffPass1
* In a seperate browser register a new account using your email address to receive the confirmation emails
* __As customer__ add a number of different sample tests to your cart and continue to purchase the testing services
* Once an order has been placed you will receive a confirmation email
* __As staff__ go to 'Lab Portal' and using the 'Sample Archive' filter function filter for the username you set yourself for your customer persona. If it is the latest sample order it will be at the top of the list by default.
* Copy and paste one of your ordered sample reference numbers into the 'Dispatch Sample' section. You will see in the 'Sample Archive' that the samples status has been updated
* __As customer__ go to 'Your Portal'. You will again see the disaptched sample and the ordered samples in the 'Live Samples' section.
* Copy and paste the dispatched sample reference into the 'Submit Sample Details' section. The 'Submit Sample Details' form will be displayed
* Fill out the sample details form. For the sample location try using the different methods detailed on the form.
* Once submitted you can view the details you have submitted by clicking on the 'Details' button in the 'Live Samples' section. Note the status has been updated to 'Submitted'
* __As staff__ go to 'Lab Portal' copy and paste the submitted sample reference into the 'Receive Sample' section to record that the sample has been received into the lab. Note the status update in the 'Sample Archive' section
* Select your received sample reference from the drop down selector in the 'Upload Results' section and enter result values. Though the results fields do not have limits use the following real worl possible results P=2, K=55, pH=7, LR_pH=10
* __As customer__ you will receive an email informing you that your results are available. Follow the link in the email to 'Your Portal' and you will see the sample in the 'Completed Samples' section
* Click 'View Report' and you will see that the results are displayed color coded relative to thresholds shown.
* __As staff__ you can also view this report by finding the sample in the 'Sample Archive' of 'Lab Portal'. Alternativily you could filter for 'Status' = 'Complete' and view previously tested samples.



__Code Validation__

* __Python__ was validated using http://pep8online.com/.
* __HTML__ was validated using https://validator.w3.org/. Due to the Django template code embedded in the HTML there were a number of errors.
* __CSS__ was validated using https://jigsaw.w3.org/css-validator/. No errors were found.
* __Spelling and Grammar__ was validated using Google Docs.
* __JavaScript__ was validated using https://jshint.com/

__Continuous Integration__

Travis CI was used for continuous integration insuring that the host environment and requirements are met through out the development.
As I have included staticfiles/ in .gitignore, 'python manage.py collectstatic' had to be included in the .travis.yml (https://github.com/dcasey720/django_soil_lab/blob/master/.travis.yml) file before the tests for the test to pass.

__Automated Testing__

As part of the continuous integration testing a number of automated tests were developed. The automated tests can be found at the following links:

https://github.com/dcasey720/django_soil_lab/blob/master/samples/tests_views.py
https://github.com/dcasey720/django_soil_lab/blob/master/samples/tests_app.py
https://github.com/dcasey720/django_soil_lab/blob/master/products/tests.py

Though thorough manual testing was carried out, see below for details,
more automated tests should have been developed through out the development of the different project features to insure all features worked correctly with each added feature.

__Visual Testing__

The dev tool within Firefox Development Edition was used to test that the pages were displaying correctly (alignment, spacing, position etc.) across different screen widths.


|                                                       | Galaxy S5 | Galaxy S7      | Pixel 2 | Pixel 2XL | iPhone 5/SE | iPhone 6/7/8 | iPhone 6/7/8 + | iPhone X | iPad  | iPad Pro   | Responsive 1366 x 768 | Responsive 1680 x 1050 |  
| ----------------------------------------------------- | --------- | -------------- | ------- | --------- | ----------- | ------------ | -------------- | -------- | ------| ---------- | --------------------- | ---------------------- |
| Home                                                  | OK        | NOK<sup>1</sup>| OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| About                                                 | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Nav - Collapse/ Expand in xs, hover and focus         | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Services                                              | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Log in/ Register                                      | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Cart                                                  | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Checkout                                              | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Your Portal - Collapse/ Expand in xs, hover and focus | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Enter Details                                         | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Lab Portal                                            | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Order Confirmation Email                              | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Results In Email                                      | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |
| Sample Report                                         | OK        | OK             | OK      | OK        | OK          | OK           | OK             | OK       | OK    | OK         | OK                    | OK                     |

Note: 1. When viewing the Home screen on my own phone the background image is not shown. It shows correctly for all screen sizes when viewed through Firefox dev tools,
and on consulting Code Institute on the issue the tutor confirmed that the background was displaying correctly on his iPhone 5/SE. All caches have been cleared on my phone and still the issue persists.

__Manual Testing__

The following test were performed manually.


|    Feature                      |   Test Action                                        |   Expected Result                                    |  Chrome (Desktop) |  Firefox (Desktop)  | IE (Desktop)    | Chrome (Mobile) |
| ------------------------------- | -----------------------------------------------------| ---------------------------------------------------- | ----------------- | ------------------- | --------------- | --------------- |
| Pre-Test State                  | Insure you are logged out and on the 'Home' page     |                                                      |                   |                     |                 |                 |
| Registration                    | Click 'Log In  ' in nav                              | Log in page displays with login and registration forms|       OK         |       OK            |       OK        |       OK        |                                           
|                                 | Click 'Create Account'                               | Alert: to fill out required fields                   |       OK          |       OK            |       OK        |       OK        |
|                                 | Fill out required fields -> Click 'Create Account'   | Home page displayed,                                 |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Registration success message,                        |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | User logged in,                                      |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Your Portal visible in nav                           |       OK          |       OK            |       OK        |       OK        |
| Log Out                         | Click 'Log Out' in nav                               | Home page displayed,                                 |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Log out success message,                             |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | User logged in,                                      |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Your Portal not visible in nav                       |       OK          |       OK            |       OK        |       OK        |
| Add items to cart               | Click 'Services' in nav                              | Services page displayed                              |       OK          |       OK            |       OK        |       OK        |                                                
|                                 | Set 'Soil 1-SS' quantity = 0 ->  Click 'Add'         | Alert: Stating the range must be >= 1                |       OK          |       OK            |       OK        |       OK        |
|                                 | Set 'Soil 1-SS' quantity = 2 -> Click 'Add'          | Nav cart (top right) shows 2 items                   |       OK          |       OK            |       OK        |       OK        |
| Amend quantity of items in cart | Click 'Cart' in nav                                  | Cart page displayed                                  |       OK          |       OK            |       OK        |       OK        |                                                
|                                 | Set 'Soil 1-SS' quantity = 4 -> Click 'Amend'       | Cart badge shows 4 items                             |       OK          |       OK            |       OK        |       OK        |                                               
|                                 | Set 'Soil 1-SS' quantity = 0 -> Click 'Amend'       | Cart badge shows 0 items                             |       OK          |       OK            |       OK        |       OK        |                                               
| Order Sample                    | Click 'Services' in nav                              | Services page displayed                              |       OK          |       OK            |       OK        |       OK        |                                                
|                                 | Set 'Soil 1-SS' quantity = 3 -> Click 'Add'          | Nav cart (top right) shows 2 items                   |       OK          |       OK            |       OK        |       OK        |
|                                 | Click 'Cart' in nav                                  | Cart page displayed                                  |       OK          |       OK            |       OK        |       OK        |
|                                 | Click 'Checkout'                                     | Login page displayed                                 |       OK          |       OK            |       OK        |       OK        |
|                                 | Login                                                | Checkout page displayed                              |       OK          |       OK            |       OK        |       OK        |
|                                 | Click 'Submit Payment'                               | Alert: to fill out required fields                   |       OK          |       OK            |       OK        |       OK        |
|                                 | Fill out required fields -> Click 'Submit Payment'   | Services page displayed, cart shows empty            |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Order confirmation email received by customer        |       OK          |       OK            |       OK        |       OK        |
| Dispatch Sample                 | Log in as a staff username: nice_assessor password: StaffPass1 | Home page displayed,                       |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Log in success message,                              |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | User logged in,                                      |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Your Portal and Lab Portal visible in nav            |       OK          |       OK            |       OK        |       OK        |                                                  
|                                 | Click 'Lab Portal' in nav                            | Lab Portal page displayed                            |       OK          |       OK            |       OK        |       OK        |
|                                 | In the Dispatch Section enter one of the ordered sample references, you can use the Sample Archive section to find the most recent samples | Sample Dispatched success message displayed |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Sample status shows dispatched in sample archive     |       OK          |       OK            |       OK        |       OK        |
| Submit Sample Details           | Log in as the customer -> Click 'Your Portal'        | Your Portal page displayed                           |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Status of active and completed samples displayed in relevant sections |       OK          |       OK            |       OK        |       OK        |
|                                 | In the Submit Details section enter a sample reference that has been dispatched | Submit Sample form page displayed |       OK          |       OK            |       OK        |       OK        |
|                                 | Click Use Device Location                            | Browser request action appears, once user agrees, current latitude and longitude are entered in input box |       OK          |       OK            |       OK        |       OK        |
|                                 | Enter required fields and click Submit Sample        | Your Portal page is displayed                        |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Active sample archive shoes submitted sample and can view details |       OK          |       OK            |       OK        |       OK        |
| Receive Sample                  | Log in as staff -> Click 'Lab Portal'                | Lab Portal page displayed                            |       OK          |       OK            |       OK        |       OK        |
|                                 | In the Receive Sample section enter a submitted sample ref | Success message displayed                      |       OK          |       OK            |       OK        |       OK        |
| Upload Sample Results           | In the Upload Results section, select the received sample |                                                 |       OK          |       OK            |       OK        |       OK        |
|                                 | Enter sample results -> Click Submit Results         | Success message displayed                            |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Sample results can be seen in the sample report      |       OK          |       OK            |       OK        |       OK        |
|                                 |                                                      | Email sent to customer informing them that the results are available |       OK          |       OK            |       OK        |       OK        |
| LinkedIn Footer Link            | Click LinkedIn link in footer                        | Opens LinkedIn profile in new tab or in LinkedIn app |       OK          |       OK            |       OK        |       OK        |
| Email Link                      | Click email link in header                           | Opens default email composer                         |       OK          |       OK            |       OK        |       OK        |
| Phone number Link               | Click phone number link in header                     | Calls number on mobile device/ asks to select phone app on desktop |       OK          |       OK            |       OK        |       OK        |


__Console Log Errors__

Though all features functioned correctly there were a number of errors visible in the console log that are worthy of note.
* The following is generated when the Submit Details View is rendered in firefox: 


Request to access cookie or storage on “https://maps.google.com/maps/api/js?key=AIzaSyBegg5R7eMRpK9EHJGEp6xrQuD0ImzTfyA” was blocked because it came from a tracker and content blocking is enabled.

and in Edge:


SCRIPT7002: XMLHttpRequest: Network Error 0x80700013, http://download.microsoft.com/download/B/9/F/B9FF9327-7A72-4165-BF91-9B7EEB6C579B/DeviceList.json

* The following is generated when the Lab Report view is rendered in firefox, I imagine due to the API key being set as a template variable:


You have included the Google Maps JavaScript API multiple times on this page. This may cause unexpected errors.


Google Maps JavaScript API warning: NoApiKeys https://developers.google.com/maps/documentation/javascript/error-messages#no-api-keys


Google Maps JavaScript API warning: InvalidKey https://developers.google.com/maps/documentation/javascript/error-messages#invalid-key




Development
------------------------

This site was developed in consultation with Southern Scientific. They were looking to digitalise some of their lab processes, reducing the time lab technicians and field surveyors spent transferring data from paper to online records.
I was given a tour of their lab and run through of their processes. It was apparent that a lot of time could be saved and so money saved,
if sample details could be submitted by the customer directly to a cloud database and that being able to GPS tag the sampe would greatly improve the tracking of a customers land over time.

As the geo tagging of samples seemed important to the process time was spent researching the different options available through Django in achieving this. GeoDjango was first explored but seemed overkill for the features required for this project.
Django-geotagging, django-location-field and django-google-maps were also investigated but in the end django-geoposition was used for its simplicity. I ran into issues running the stable release with django 1.11 and had to use an alternative work around branch, details can be found in the deploy section below.

Django-geoposition allows the user to select and save a location to a model using a google maps widget, however it does not get the users current location. A script was developed (https://github.com/dcasey720/django_soil_lab/blob/master/static/js/getLocation.js) making use of HTML5 getLocation function that uses the client
side location features available (either GPS or IP location) to set the location of the user. This was important so that samples could be accurately geotagged when taking field samples. As the django-geoposition map marker initial position are set in Settings.py and the widget used display is generated from this,
it was proving difficult to get the current location to recenter and reposition the marker automatically when the location is found. Though not the most user intuitive the 'how to' style help provided with the model entry was a compromise that isn't too complicated. Geopy was used to get the address of the gps location separately to the django-geoposition.

As this project will be adopted in some way by Southern Scientific, the color scheme, font styles, background images and layouts were mimicked for easy integration. Time was spent developing a logo using https://www.canva.com/ and paint, these can be found here https://github.com/dcasey720/django_soil_lab/tree/master/mock-ups/Canvas%20developed%20logos.
It was proving difficult to set the logo background to transparent to blend in nicely with the navbar, so in the end a simple brand logo was developed with standard font and a font-awesome leaf icon.

For the development of the samples results tables in the sample report, the following publication was consulted https://www.teagasc.ie/media/website/publications/2016/soil-fertility-green.pdf. For the purpose of this project I concentrated on showing the results for only most basic of tests offered by Southern Scientific, testing Potassium, Phosphorus, pH and Lime Requirement pH.
The thresholds used in the tables were for grassland land use and these should be programmed more appropriately for the other land uses. The tables of note from the teagasc publication can be found here https://github.com/dcasey720/django_soil_lab/tree/master/mock-ups/Example%20Test%20Result%20Tables.

It sould be noted that Django has been use for other LIMS systems most notibly https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5192047/. Though the MASTR-MS LIMS was not referenced in the development of this projects it gave me and Southern Scientific confidence that Django is an industry capable framework that can be adapted for their needs.

There are a number of operations that are purposefully awkward by design. The 'Dispatch Sample', 'Receive Sample' and 'Submit Sample Details' input box require that the whole sample reference number be entered. Autocomplete for these form entries were considered but thought that if possible reference numbers were shown there would be a greater possibility that
the user would select one of the given possibilities rather than the one in there hand. In production the dispatch and receive entries will be carried out by a USB connected barcode scanner with this site running locally.

__Notes on Code__

* All custom css tags created in the development of this project include '_', this allows me to quickly see what items I have styled and what items already have style attributes.
* A number of the forms generated by django for use in the templates were unpacked for layout purposes i.e. ln14 https://github.com/dcasey720/django_soil_lab/blob/master/samples/templates/submitdetails.html.
I was unable to apply the 'as_bootstrap' styling to the unpacked form, however by including 'form | as bootstrap' in comments before the form the correct stylings were applied.
If left not commented out the form would be rendered twice. I consulted Code Institute on the issue and found it an oddity for which they could not resolve and so the hacky method used remains.
* Loose CSS coupling was carried out through out the templates with all custom css contained in https://github.com/dcasey720/django_soil_lab/tree/master/static/css.
However where django generated urls were used for background images the 'background-image' style attribute was included in the the html code. i.e. ln19 https://github.com/dcasey720/django_soil_lab/blob/master/templates/base.html
* All Javascript code is run from external js files in the static folder https://github.com/dcasey720/django_soil_lab/tree/master/static/js.
However where django tags were used global javascript variables were declared in the html template for use in the scripts. i.e. ln354 https://github.com/dcasey720/django_soil_lab/blob/master/samples/templates/viewreport.html

Deployment
------------------------

__Requirements__

The system hosting the app must have a number of python packages installed.
A full list can be found at

https://github.com/dcasey720/django_soil_lab/blob/master/requirements.txt

Take note that a pip freeze will show django-geoposition==0.3.1, this is not a valid release and will fail both travis and heroku builds.
Django-geoposition latest release available to install with pip is 0.3.0., however this version will not work with django-1.11 and so the work around branch must be installed.

The django-1.11 work around branch is referenced in the requirements as 'geoposition.git@4ed91215a36e737c71fbdc023f134bd2cfe445b3#egg=django-geoposition'.
Alternatively the repo can be referenced using the zip folder https://github.com/philippbosch/django-geoposition/archive/django-1.11.zip.

__System Variables__

The following system variables must be set in the host environment.

* STRIPE_PUBLISHABLE, publishable key assigned to you when you register an account with Stripe https://stripe.com/ie
* STRIPE_SECRET, secret key assigned to you when you register an account with Stripe https://stripe.com/ie
* EMAIL_HOST_USER, the email address you will use to send emails to application users.
This can be your personal email address i.e. johndoe@gmail.com. If using gmail you must allow Less Secure App Access in your accounts security settings https://myaccount.google.com/security.
I set up a dummy gmail account, eascatest@gmail.com, so that my personal email was not left vulnerable by downgrading the security.
* EMAIL_HOST_PASSWORD, your specified email host login password
* SECRET_KEY, generated by django when you start a new app. See setttings.py file
* GOOGLE_MAP_API_KEY, assigned when setting up a google maps api account, https://cloud.google.com/maps-platform/, insure that both 'Maps' and 'Places' products are available to the key.
* DATABASE_URL, generated when you set up a PostGres database, i.e. when using 'Heroku Postgres' add-on under resources when deploying app on Heroku.

__Deployed vs Development__

__gitignore__

A number files and folders in the local development environment were not deployed with the project. These files and folders were included in a .gitignore file.

As virtual environment wrapper was used for development. The following associated files were omitted from the git repo from the initial git;

* Include/
* Lib/
* Scripts/
* pip-selfcheck.json
* tcl/

As the deployed project uses a Postgres database the locally generated db.sqlite file was also omitted from git repo from the initial git.

Django generates a staticfiles directory when running collectstatic, this contains a copy of all the static files in the project directories. This was also omitted from the git.
As mentioned in the test section, a collectstatic command had to be initiated in the travis.yml file so that continuous testing would pass.
Though there were no security risks with including the staticfiles directory, these files can be generated by the future developers themselves and once removed GitHub correctly shows the project as being primarily Python coded.

All system variables were declared in an env.py file. As many of these variables were passwords this too was from git repo from the initial git.

If env.py file is not found DEBUG is set to False, this insures that while developing on my local machine the application runs in debug mode but once deployed debug mode is deactivated. Ln36 https://github.com/dcasey720/django_soil_lab/blob/master/django_soil_submit/settings.py

Note: The 'mock-ups' folder was included in the git repo throughout,
normally I would remove the mock-ups from the final deployment, but as the Heroku app was deployed by link to the GitHub repo I thought it better to keep them in the repo.

Credits
------------

__Content__

The text for the About section and product descriptions were taken from https://southernscientificireland.com/

__Media__

The home and nav background images were taken from https://southernscientificireland.com/. All other images were taken from https://images.google.com/

__Acknowledgements__

The project was developed from conversations with Southern Scientific Environmental Services.

Running App
------------------------

https://dc-easca-environmental.herokuapp.com/



