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
    * [Testing](#Testing)
    * [Front end](#Front-end)
* [Further Sprints](#Further-sprints)

## Introduction
#
### **Objective**

The brief for this project was:  

Create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules.

Specifically this requires:
- Creating a functional CRUD application
- Creating a functional front-end website
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
Below is an image of my entity relationship diagram that shows the implementated structure of my database. 

![My entity relationship diagram showing a many to one relationship between the unit table and army table](https://i.imgur.com/Ww90HZ9.png)

As shown the app will model a one to many relationship between armies and units, allowing the user to create an army with many units associated with it. 

Below is a proposed entity diagram for the next development of the app in which I would add another table to store user data which would have a many to many relationship with the units table so a user have multiple units and each unit could be owned by multiple users.

![An entity relationship diagram show a many to one relationship between the unit table and army table and a many to many relationship between unit and user](https://i.imgur.com/BSWuSm0.png)
### **CI Pipeline**


Throughout this project I used continuous integration to allow smooth development to deployment, with a emphasis on automated testing. This meant that when I pushed code from my virtual machine to my GitHub repository, GitHub automatically pushed that code onto Jenkins via a webhook. Then Jenkins automatically runs tests and produces a report. Below is the pipeline of my continuous integration. 

![My CI pipeline](https://i.imgur.com/4wse78J.png)


### **Project Tracking**

To track the progress of my project I used a trello board pictured below:
![My trello board](https://i.imgur.com/HxQZyk4.png)

The board is designed so that each task is moved through each stage as the task is worked on. I have added coloured labels to each card in order to indicated which part of the project they are related to. A link to the full trello board can be found here: [My trello board](https://trello.com/b/HLRWiOv1/fundamental-project)

### **Risk assessment**

Below is my risk assessment showing both major and minor risks that are associated with this project. The bottom three risks were added part way through the project as the new risks became clear. Here is a link to the full risk assessment: [Risk assessment](https://docs.google.com/spreadsheets/d/1HnF5nKCs_Ag6NKKnCll6coHLovbo54oKSCyyRTpMuL0/edit?usp=sharing)
![My risk assessment](https://i.imgur.com/rIiNyam.png)

## Development
#
### **Testing**

The testing of the python code was done using Pytest to run different tests. Unit tests are designed to assert that if a function is run, it produces a known output. Using Jenkins these tests are run every time something is pushed up to GitHub and Jenkins will produce a report detailing whether any of the tests were successful or not. Pytest can also give a coverage report to show how many lines of code was tested. Below is a copy of the coverage report.

![Testing coverage](https://i.imgur.com/wnBKeja.png)

The Jenkins script first starts by installing python and the virtual environment module.

``` python
sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip -y
```

Then it starts a virtual environment and installs all necessary modules from the requirements file.

``` python
#setup venv and install pip requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Finally it runs pytest, going through both the unit testing and integration testing and producing the coverage report. 

``` python
python3 -m pytest --cov=application
```
### **Front end**

When a user navigates to the url or to the home page they are shown all current armies in the database along with the associated units. At the top of the page are the URL's to the different pages. This is part of the layout and so will appear on each page. 

![Home page](https://i.imgur.com/5Eba1qm.png)

Going to add army page allows you to create a new army file.

![Add army](https://i.imgur.com/X3LTonO.png)

going to the add unit page allows you to create a new unit that is associated with one of the already created armies.

![Add unit](https://i.imgur.com/Luaiitb.png)

## Further Sprints
#
In future sprints there are a couple of features I would like to implement:
* Be able to add user accounts and have each user have different units associated with their accounts.
* Calculate the total number of points each unit is worth based of the inputted points per model and quantity.
* The ability to filter units by their type not just which army they belong to.
* The aesthetic improvement, making the front end more appealing to use.

## Author
#

James Carr
