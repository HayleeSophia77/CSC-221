## M8 Final Project Overview

This project/program is a Streamlit application designed to analyze student enrollment data. Users can upload a CSV file and get:

* Average credits per program
* Average credits per division
* Trends across semesters
* Bar and line visualizations
* Filtered datasets exportable as CSV files

The application filters out certificate programs(codes starting with C) and evaluates only program data(codes starting with A).

## Files Included

* main.py
* functions.py
* run_app.py
* dist/Final_Project.exe
* student-data-since-2023.csv
* README.md

NOTE: You may also see 'build' and 'Final_Project.spec' in the folder. These are PyInstaller build artifacts and are not required to run the app.

## How to Run the Application(Executable Version)

* Open the project folder
* Open the dist folder
* Double-click:
	Final_Project.exe
* In the console window, when you see a message similar to(this may open a browser automatically):
	 You can now view your Streamlit app in your browser.

     Local URL: http://localhost:8501
* Open a web browser and go to:
	http://localhost:8501

NOTE: The EXE was tested on my machine and launches the app correctly via 'http://localhost:8501'.

## How to Run the Application in VS Code

* Open the folder: Final_Project-Haylee_Paredes
* Open a new terminal: Top menu -> Terminal -> New Terminal
* Create a virtual environment: python -m venv venv
* Activate the virtual environment: venv\Scripts\activate
* Install required packages: pip install streamlit pandas matplotlib seaborn
* Run the Streamlit application: streamlit run main.py
* When Streamlit prints a Local URL (usually http://localhost:8501), open that URL in your browser to use the app.

## How to Run the Application in CMD

* Open Command Prompt
* Navigate to the project folder
* Create a virtual environment: python -m venv venv
* Activate the virtual environment: venv\Scripts\activate
* Install required packages: pip install streamlit pandas matplotlib seaborn
* Run the Streamlit application: streamlit run main.py
* Open the Local URL shown in the terminal (usually http://localhost:8501) in your browser.

## Design Decisions

I split my project into two files to keep things organized. The main.py file handles the Streamlit interface and everything the user interacts with, while functions.py does all the data processing and plotting behind the scenes. The app filters out certificate programs and only looks at programs starting with “A” since that’s what the assignment focused on.

For the analysis, I included both required options: By Program and By Division. Each one lets the user pick semesters and see the results in tables and charts. I used pandas groupby to calculate the average credits because it’s fast and straightforward. The charts use matplotlib with seaborn styling so they look cleaner, and I made sure the legends don’t block any data. The app also validates the uploaded CSV and shows clear errors if something’s wrong, and users can download the filtered results as CSV files.