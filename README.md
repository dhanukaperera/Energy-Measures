## Dev notes

Feature Suggestions :
* Allow users to see the total cost as they select measures, without needing to submit the form.
* Add sorting and filtering options to the measures list. For example, we could allow users to sort the measures by name or cost, or filter the measures by tags or categories. This would require adding additional UI elements to the page and modifying the Django view function and Measure Model to handle the sorting and filtering logic.
* Allow users to save their selection of measures for future reference. This would require creating a user authentication system and a way for users to save and load their selected measures
* Add additional metadata to the measures, such as images or descriptions, and display this information alongside the measure names and costs. This would require modifying the Measure model and view functions to handle the new data, as well as updating the HTML and CSS to display the new information.
* Display the C02 footprint the users can save by applying the measures.

Development Process:
* Add the "recommended" property to the Measure model
* Create a database migration script using the following cmd ```python manage.py makemigrations app```
* Run the migration script using the following cmd ```python manage.py migrate```
* Create ```admin.py``` script and register Measure model
* Create a superuser and login to admin mode in ```http://localhost:8000/admin``` add sample Measure data
* Get the measures using ``` Measure.objects.all()``` and pass the it to ```measures.html```
* Create the table view and display list of measures. Add a conditional statement to highlight if the measure is "Recommended"
* To display the styles create a ```static/css/style.css``` and add the static styles path in ```urls.py```
* Update the measure view and add checkbox to select item and warp in a form and submit.
* Handle POST request in calculate the total price and pass the value to ```measures.html```