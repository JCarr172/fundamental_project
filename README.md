# fundamental_project


## Contents
* [Introduction](#introduction)
    * [Objective](#Objective)
    * [Plan](#Plan)
* [Architecture](#architecture)
    * [Database Structure](#Database-Structure)
    * [CI Pipeline](#CI-Pipeline)
    * [Project Tracking](#Project-Tracking)
    * [Risk Assessment](#Risk-Assessment)
* [Development](#development)
* [Front-End Design](#front-end)
* [Footer](#footer)

## Introduction
#
### **Objective**

The brief for this project was:  

Create a CRUD application with ultisation of supporting tools, methodologies and technologies that encapsulate all core modules.

Specificlly this requires:
- Creating a functional CRUD appliction
- Creating a functional front-end webiste
- A project tracking system
- A version control system
- Automated testing
- A database  with at minimum one to many relationship
- Risk assessment


### **Plan**

For this project I have decided to make a website where a user can store information about their Warhammer collection, such as:
* Creating an army category that includes:
    * Army name
    * The armies faction
    * The current codex edition
* Creating a record of units owned that includes:
    * Name of the unit
    * The army that unit belongs to
    * What type of unit it is
    * The price of that unit, per model
    * How many models owned

The user will be able to view all of the details stored for each unit or army as well as being able to update or delete any information stored. 

I will be using Python to acheive the back end functionality of this application, Flask to create the front end functionality and using Git and Github for my version control system.
## Architecture
#
### **Database Structure**
Below is an image of my entity relationship diagram that shows the implentated structure of my database. 

![My entity relationship diagram showing a many to one relationship between the unit table and army table](https://i.imgur.com/Ww90HZ9.png)

As shown the app will model a one to many relationship between armies and units, allowing the user to create an army with many units associated with it. 

Below is a proposed entity diagram for the next development of the app in which I would add another table to store user data which would have a many to many relationship with the units table so a user have multiple units and each unit could be owned by multiple users.

![An entity relationship diagram show a many to one relationship between the unit table and army table and a many to many relationship between unit and user](https://i.imgur.com/BSWuSm0.png)
### **CI Pipeline**

![My CI pipeline](https://i.imgur.com/4wse78J.png)

### **Project Tracking**

[My trello board](https://trello.com/b/HLRWiOv1/fundamental-project)

### **Risk assessment**

## Development
#


## Front end
#


## Footer
#

