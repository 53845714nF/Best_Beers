⚠️ **This project is not intended to promote or encourage the consumption of alcohol. Alcohol is a drug. Regular drinking can make you dependent on it. Alcohol is leading risk factor for death, disease and disability.** ⚠️

# Best_Beers
Welcome to Best Beers! This is a web application built using Django framework that helps you manage your beer inventory.
With Best Beers, you can create, update and delete beers, view details about each beer.
You can also view breweries and where they are located in the world.

## Installation
To install Django Beer Manager, follow these steps:
 1. Clone the repository or download the zip file.
 2. Install Python3 and pip3 if they are not already installed.
 3. Install the required packages by running the following command in your terminal:
  ```
  pip3 install -r requirements.txt
  ```
  4. Run the database migrations by running the following command in your terminal:
  ```
  python3 manage.py migrate
  ```
  5. Import Data (Optional if you don't want to use the included sqlite.db.)
  ```
  python3 manage.py runscript import_data
  ```
  6.Finally, start the development server by running the following command:
  ```
  python3 manage.py runserver
  ```

## Usage
Once you have installed Best_Beers, you can access it by navigating to http://localhost:8000/ in your web browser.
Here are some of the things you can do with Django Beer Manager:

 - Create a new beer: Click the "Create new Beer" button and fill out the form with the details of the beer you want to add.
 - Update a beer: Click the "✍" button next to the beer you want to update and make changes to the beer's details.
 - Delete a beer: Click the "✘" button next to the beer you want to delete.
 - View beer details: Click the name of a beer to view its details.

## Data sources of the Project
The data for this project comes from the [OpenBeerDB project](https://openbeerdb.com/).

The CSV files were not as good than expected.
