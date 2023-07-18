
# Device Management Project

The Device Management project is a Django web application designed to manage and display a list of devices. It allows users to view a list of devices, add new devices, update existing devices, and view detailed information about each device


## Project URLs

* Device List Page: View a list of all devices.
    * URL: http://127.0.0.1:8000/app/home/

* Add Device Page: Add a new device to the database.
    * URL: http://127.0.0.1:8000/app/create/

* API Endpoint to Update Modified Date: A RESTful API endpoint to update the modified date of a device using the PUT method.

    * URL: http://127.0.0.1:8000/api/device-update/<device_id>/ (Replace <device_id> with the ID of the device to update , ex : 1,2,3)


## How to Start the Project

Follow these steps to set up and run the Device Management project:

Clone the Repository:
```bash
  git clone https://github.com/sachint97/Device-Management.git
```
Navigate to the Project Directory:

```bash
  cd Device-Management
```

Create and Activate a Virtual Environment (Optional):

On Windows
```bash
  
  python -m venv venv
  venv\Scripts\activate
```

 On macOS and Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Install the Required Dependencies:
```bash
pip install -r requirements.txt
```
Run Database Migrations:
```bash
python manage.py migrate
```

Create a Superuser (Optional - For Admin Access):
```bash
python manage.py createsuperuser
```

Start the Development Server:
```bash
python manage.py runserver
```

* Access the Application: Visit http://127.0.0.1:8000/app/home/ in your web browser to access the list of devices.

* Access the Admin Panel (Optional): If you created a superuser in Step 6, you can access the admin panel at http://127.0.0.1:8000/admin/ to manage devices and other data.

* API Endpoint: You can use the provided API endpoint (mentioned above) to update the modified date of a specific device using the PUT method.
