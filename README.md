# ProjectLife

![Project Life preview](GoLscreenshot.jpg){width=50%} 


## Table of contents
* [General info](#general-info)
* [Deployment](#deploy)
* [Technologies](#technologies)
* [Setup](#setup)
  

## General info

This is a training project in the Flask learning course. The project realizes the [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) (GoF) in a browser.
Two versions are realized: (i) life in a box and (ii) life on a torus. 
They differ by the way how the number of cell's neighbors is calculated. 

## Deployment

The app was deployed on the Heroku server using a Docker container but has now been deleted due to hosting costs. 
It can be restored upon request. 
<!-- Please try at https://flaskgamelife-e9965bc6d371.herokuapp.com/-->

## Technologies
The project is created with:
* Python 3.9.13 
* Flask==2.3.2
* Jinja2==3.1.2
* gunicorn==21.2.0
It was tested in a browser 
* Microsoft Edge Version 114.0.1823.43 (Official Build) (64-bit)

## Setup
Clone this repo to your desktop or download zip and unpack

## Usage
After you clone this repo to your desktop,   run pip install -r requirements.txt
to install all the dependencies.

Once the dependencies are installed, you can run app.py file to start the application. You will then be able to access it at localhost:5000
