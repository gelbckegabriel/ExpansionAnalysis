<div>
  <h1><strong>Expansion Analysis - Data Engineering (ETL)</strong></h1>
  <p>This Expansion Analysis is a Data engineering project using skills to complete an ETL (Extract, Transform and Load) pipeline for accessing data from a website and processing to meet requirements.
  </p>
  <h4>Author: <a href=https://www.linkedin.com/in/gabrielgelbcke/ target="_blank">©GabrielGelbcke</a></h4>

  <br>

  <h2>:wrench: Programming Languages & Tools used:</h2>
  <div id="tools">
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python Logo" height="40" width="40" />
    <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original-wordmark.svg" alt="Pycharm Logo" height="40" width="40" />
  </div>

  <br>

  <h2>:open_file_folder: Project Scenario:</h2>
  <p>
    An international firm that is looking to expand its business in different countries across the world has recruited me. I have been hired as a junior Data Engineer and I’m
    tasked with creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the
    International Monetary Fund (IMF). Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.
    <br><br>
    You can find the required data on <a href="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29" target="_blank">this
      wikipedia webpage</a>.
    <br>
    <ul>
      <li>The required information needs to be made accessible as a JSON file 'Countries_by_GDP.json' as well as a table 'Countries_by_GDP' in a database file 'World_Economies.db'
        with attributes 'Country' and 'GDP_USD_billion.'</li>
      <li>Your boss wants you to demonstrate the success of this code by running a query on the database table to display only the entries with more than a 100 billion USD economy.
        Also, log the entire process of execution in a file named 'etl_project_log.txt'.</li>
      <li>You must create a Python code 'etl_project_gdp.py' that performs all the required tasks.</li>
    </ul>
  </p>

  <br>
  
  <h2>:round_pushpin: Objective:</h2>
  <p>
    Create an extraction, transformation and loading process of data from a wikipedia page that will load the desired information in a CSV file, and also in a database (if needed).
  </p>

  <br>

  <h2>:mag: My Mission:</h2>
  <ul>
    <li>Write a data extraction function to retrieve the relevant information from the required URL.</li>
    <li>Transform the available GDP information into 'Billion USD' from 'Million USD'.</li>
    <li>Load the transformed information to the required CSV file and as a database file.</li>
    <ul>
      <li>Database connection was commented, the only automation used was CSV file.</li>
    </ul>
    <li>Run the required query on the database.</li>
    <li>Log the progress of the code with appropriate timestamps.</li>
  </ul>

  <br>

  <h2>:memo: Branches:</h2>
  <ul>
  <li>main:</li>

  ```
  Contains the folder where is the main code to run etl_process and also where you can find the output from it.
  ```

  <li>env:</li>

  ```
  Contains the libraries and documents for the venv that I created for this project.
  ```

  </ul>

  <br>

  <h2>:globe_with_meridians: Reference:</h2>
  <ul>
    <li><strong>Coursera reference:</strong> <a href="https://www.coursera.org/learn/python-project-for-data-engineering/ungradedLti/Rg7gf/practice-project-extract-transform-and-load-gdp-data" target="_blank">Click Here</a></li>
    <li><strong>Wikipedia page:</strong> <a href="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29" target="_blank">Click Here</a></li>
  </ul>

