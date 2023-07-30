# Basic Fixed Asset Management System
This is a first draft of a python script. My goal is to eventually build a fixed assets management system that generates QR codes to make data storage and acessibility
easier for accountants.

Overview:

The Fixed Assets Management System is a Python application that allows you to manage information about fixed assets of a company. 
It enables you to store data related to each fixed asset, such as Asset ID, Asset Name, Asset Type, Acquisition Date, Original Cost, Useful life, and Depreciation per month. 
Additionally, the application can generate QR codes for each fixed asset, which can be scanned to retrieve asset information.

Features:

Add new fixed assets with relevant details to your fixed asset ledger
Generate QR codes for each fixed asset.
Store asset information in a CSV file for easy access and retrieval.

Installation:

Clone the repository to your local machine.
Make sure you have Python 3.x installed.
Install the required libraries using pip:
Copy code
pip install python-csv
Place the CSV file containing fixed asset data (e.g., "FA_simulated_07.26.23.csv") in the same directory as the Python script.

Usage:

Run the Python script "fixed_assets.py" using the terminal or your preferred Python development environment.
The application will load the fixed asset data from the CSV file.
Follow the on-screen instructions to perform various actions, such as adding new fixed assets or generating QR codes.
The generated QR codes can be scanned to retrieve asset information on supported devices.

Example CSV Format:
sql
Copy the following code or import and transform it to a csv file:

*Asset ID,Asset Name,Asset Type,Acquisition Date,Original Cost,Useful life,Depreciation per month
1,Computer,Laptop,2023-05-15,1200,5,20
2,Printer,Office Equipment,2023-04-10,400,4,10
3,Desk,Furniture,2023-06-20,300,8,5
...*

The repository also has an example CSV file. Feel free to modify it, along with the python script as needed. I will add more to this project as 
I get better and more knowledgable with database management and software development.
