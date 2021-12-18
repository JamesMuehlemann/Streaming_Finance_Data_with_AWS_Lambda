# James Muehlemann - Project 2 
## 12.2.21
### Project Overview
In this project, I was tasked with analyzing 10 Gb of Yelp data housed across 5 different JSON files. I did this by provisioning a Spark Cluster through AWS EMR to load the data and run analysis on it. The reason for using technology like AWS EMR and PySpark is that these information sources are too large to store locally and must be handled with technology that enables analysis of larger sets of data. The technologies I leveraged to complete this project are:
- Python via Jupyter Notebook
- AWS EMR
- PySpark
- AWS S3 Storage

### File Hierarchy
| File/Directory | Description |
| ------ | ------ |
| project02  | Root Project 2 Folder |
|+ -- Analysis.ipynb | .ipynb file for running Python Script |
| + -- Analysis.pdf | .pdf file of the Jupyter Notebook Analysis |
| + --  assets/ | Folder housing cluster and notebook configurations |
| + --  + -- cluster_configuration.jpg | Screenshot of EMR Cluster Configuration |
| + --  + -- notebook_configuration.jpg | Screenshot of Notebook Configuration|
| + --  README.md | README discussing details of project 2 |

### Cluster Configuration
![cluster_configuration](assets/cluster_configuration.jpg)

### Notebook Configuration
![notebook_configuration](assets/notebook_configuration.jpg)
