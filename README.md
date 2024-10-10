# Bike Rentals Data Analysis Dashboard 🚴‍♂️📊

This repository contains a **Streamlit Dashboard** and **Data Analysis Notebook** to explore the relationship between **weather conditions**, **season**, and **month** with the total number of bike rentals. The data comes from a cleaned version of the bike-sharing dataset.

## Overview
The main focus of this project is to analyze how different environmental and temporal factors, such as weather conditions, seasons, and months, affect bike rentals for both casual and registered users.

### Key Features
- **Total Bike Rentals Analysis:**
  - Analyze the total number of rentals by weather conditions (clear, cloudy, rainy, etc.).
  - Identify the months with the highest and lowest bike rental numbers.
  - Understand how different seasons impact bike rental activities.
  
- **Data Cleaning:**
  - Removed outliers from the dataset for accurate analysis.
  - Converted the `dteday` column from object to datetime format for proper time-series analysis.

- **Visualization:**
  - Dashboard visualizes bike rental trends based on weather, season, and month.
  - Interactive visualizations created with **Streamlit**.

## Data Source
[Download the dataset here](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)

## Project Structure
- `Dashboard.py`: Streamlit dashboard to visualize the analysis results.
- `requirements.txt`: List of dependencies needed to run the dashboard.
- `day_cleaned.csv`: The cleaned dataset used for analysis.
- `Proyek_Analisis_Data.ipynb`: Jupyter notebook with detailed data exploration and analysis steps.

## Setup Environment

To set up the environment, follow these steps:

1. Create a virtual environment (Optional but recommended):
    ```bash
    python -m venv bike-rentals-env
    ```

2. Activate the virtual environment (For Windows, MacOS, and Linux):
    ```bash
    # Windows:
    .\bike-rentals-env\Scripts\activate

    # MacOS/Linux:
    source bike-rentals-env/bin/activate
    ```

3. (Optional) If you encounter issues while activating the environment on Windows, run the following command to modify the execution policy:
    ```bash
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Run the Streamlit App

Once the dependencies are installed, run the following command to start the Streamlit dashboard:

```bash
streamlit run Dashboard.py


