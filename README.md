# Wphase catalog - Documentation
*This document's purpose is to describe the wphase catalog's structure and help developers who want to improve it getting familiar with its architecture.*

## Information
This project is written using Django 1.8 and Python 3.2. It currently uses the following libraries :
* numpy
* matplotlib
* psycopg2-2.6

Please report bugs to <zacharie.duputel@unistra.fr>.
    

## Global structure
The app inserts itself in a Django project, therefore has the structure of the following tree :

<pre>
wphase_catalog/
  manage.py
  mysite_wphase/
    __init__.py
    settings.py
    urls.py
    wsgi.py
  media/
  wphase/
    migrations/
    templates/
    __init__.py
    admin.py
    forms.py
    models.py
    tests.py
    urls.py
    views.py
</pre>


For more information about creation of a Django project, please consult the [Django documentation](https://docs.djangoproject.com/en/1.8/).

### mysite_wphase
This folder contains all the data shared by all the apps that are included in the project : here, it does not make much sense since we only have one app.

* **__ init__.py** is an empty file that tells Python that mysite_wphase should be considered a Python package.
* **settings.py** contains the configuration for the project, like database setup.
* **urls.py** contains the URL declarations for the project.
* **wsgi.py** is an entry-point for WSGI-compatible web servers to serve the project.

### media
This folder contains all the pictures that are used in the project. In our case, it contains all the beach balls corresponding to each solution under the name "*eventid*_*solution-type*.png".  
It is not contained in the GitHub depository, you have to create one of your own. 

### wphase
This folder contains everything that is specific to the app. 

* **migrations/** contains records of the changes made on the models, and therefore on the database.
* **templates/** contains the html templates created for the app.
* **admin.py** describes how the data is displayed and disposed of on the admin interface.
* **forms.py** describes as Python classes the forms used in the app.
* **models.py** describes as Python classes the models registered in database.
* **tests.py** contains the tests for the app.
* **urls.py** contains the URLS patterns to navigate in the app.
* **views.py** contains the types of views and the methods used in the app.


## Practical Structure

### Models
#### Event
This model contains the epicenter information and the comments from executing wpinversion code.

&nbsp;&nbsp;&nbsp; **Methods**

* **__str__(self)** returns a concatenation of the event's ID and its region.
* **date(self)** returns the origin time of the event in datetime format.
* **capsule(self)** return the first line of CMTSOLUTION format in a string.

#### Solution
This model contains the data specific to a solution.

&nbsp;&nbsp;&nbsp; **Methods**

* **__ str__(self)** returns a concatenation of its related event's __str__ and the type of solution.
* **get_all_stations()** returns a list of all the stations present in the database, without considering the channels.
* **plot(self, fname[, npx, figsize, colors])** creates the solution's beach ball and saves it as "*eventid*_*solution-type*.png" in the media folder.
* **get_centroid_time(self)** returns the centroid time in datetime format.

### Views
&nbsp;&nbsp;&nbsp; **Classes**

* **IndexView(generic.ListView) :** Its QuerySet contains a list of the 5 last occurred events under the name *latest_event_list*.

* **EventView(generic.DetailView) :** Uses the Event model ; its context object is a list of the solutions related to the event.

* **SolutionView(generic.DetailView) :** Uses the Solution model.

* **SearchView(generic.ListView) :** Its QuerySet contains a blank occurence of SearchForm under the name *form*.

* **ResultsView(generic.ListView) :** Its context object is a list of solutions which fill the search requirements. It is empty by default.

&nbsp;&nbsp;&nbsp; **Methods**

* **search(request) :** Checks the POST data and renders a ResultsView with the corresponding solutions as context object. Also saves the solutions' IDs, the required types of solution and the output format in the session data ; creates the Paginator for results pagination ; calls *plot* if needed.

* **generate_txt(request, results) :** Creates a TXT file containing all the results in CMTSOLUTION format and returns it, making the navigator ask the user if they want to save it.

* **my_logout(request) :** A personal logout created to avoid the redirection on the Django Administration page ; simply redirects to index.


### Templates
#### wphase
* **index.html** displays the last 5 occurred events.
* **search_form.html** displays a form based on the SearchForm class.
* **results.html** displays the results using the session data.
* **event.html** displays the event's information and its related solutions.
* **solution.html** displays the solution's information and its related event.

#### registration
* **login.html** displays a connexion form. Code suggested by [Django documentation](https://docs.djangoproject.com/fr/1.8/topics/auth/default/#auth-web-requests).

### Forms
* **SearchForm** describes the fields that will be used for the research.

### Tests
The tests are yet to be written.
