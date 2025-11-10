# Comparison of Dijkstra and A* Algorithms for Shortest Path using pgRouting
**Author:** Vasundhra Singh  
**Course:** COL868 – Special Topics in Data Management  

---

## 📘 Project Overview

This project explores and compares two classic graph search algorithms — **Dijkstra** and **A\*** — for computing the shortest paths in a geospatial road network using **PostgreSQL**, **PostGIS**, and **pgRouting**.  

The main objective is to:
- Demonstrate how routing algorithms can be executed directly inside a spatial database.
- Compare their performance (execution time) for increasing route distances.
- Analyze scalability, accuracy, and efficiency.

The dataset used is OpenStreetMap (OSM) road data for India’s **North-Eastern Zone**, imported into PostgreSQL and converted into a routable graph.  
Experiments were performed using **pgRouting** functions for both algorithms.

---

## 🧩 System Requirements

| Component | Specification |
|------------|---------------|
| OS | Ubuntu 20.04 (or any Linux-based system) |
| PostgreSQL | 14.x |
| PostGIS | 3.4.x |
| pgRouting | 3.5.x |
| osm2pgsql | latest |
| Python | 3.x (for result plotting) |

Hardware used:
- 4 CPU cores  
- 8 GB RAM  
- 150 GB + 200 GB HDD (mounted for data storage)

---

## ⚙️ Project Setup Instructions

### **Step 1: Install Required Packages**
Install PostgreSQL, PostGIS, and pgRouting on your machine:
```bash
    sudo apt update
    sudo apt install postgresql postgis postgresql-14-pgrouting osm2pgsql
```

### **Step 2: Create a New Database**
Log into PostgreSQL and create a database for the project:
```bash
sudo -u postgres psql
CREATE DATABASE osm_project;
\c osm_project
CREATE EXTENSION postgis;
CREATE EXTENSION pgrouting;
```

### **Step 3: Import OpenStreetMap Data**
Download the OSM extract (for example, north-eastern-zone-latest.osm.pbf) and import it:
```bash
osm2pgsql -d osm_project -U postgres -H localhost -W -P 5432 north-eastern-zone-latest.osm.pbf
```

### **Step 4: Load and Prepare Data**
Use the SQL commands provided in the project_queries.sql file to:
- Filter and extract road data
- Create source and target nodes
- Build network topology (pgr_createTopology)
- Assign costs to road segments


### **Step 5: Run Experiments**
Once the database is ready:
- Execute Dijkstra and A* queries from the SQL file.
- Record execution times for different distances (e.g., 500 m, 1 km, 2 km).
- Enable timing in psql using \timing on.

### **Step 6: Plot Results**
Use the included Python script (plot_results.py) to visualize performance:
```bash
python3 plot_results.py
```
This script plots execution time (ms) vs distance (m) for both algorithms.


NOTE: Link to download data- https://download.geofabrik.de/asia/india/north-eastern-zone.html
