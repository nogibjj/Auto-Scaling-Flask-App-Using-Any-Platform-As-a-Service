# IDS_706-Data_Engineering_Systems
## Individual Project 4 -  Auto Scaling Flask App Using Any Platform As a Service

### PURPOSE

This project is for a data engineering course (Individual-Project 4). The purpose of this project is to develop a data pipeline using Databricks. The primary goal is to create an efficient and functional pipeline that includes at least one data source and one data sink.

***

### PROCESS

The code performs ETL-Query operations:  
Extract (E): Extract a dataset from a URL in CSV format.  
Transform (T): Utilizes Spark SQL to amalgamate two datasets, ensuring they are primed for analysis.  
Load (L): Transfers the transformed data into the destination data store, leveraging Delta Lake.  
   
***

### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```

***

### Workflows

On running the above commands, it runs successfully.

