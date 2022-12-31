# EPMS Project Management System

![EPMS First Page Look!](static/images/Dahboard view.png) 

<details>
<summary>
More screenshots
</summary>

![Invoice demo](static/images/invoice View.png)
![translators rating app!](static/images/Translators Rating APP.png)



</details>
## About the app

This app is an end-to-end project management tool built with translators in mind. It helps to manage and automate translation and localization workflows with ease. It is designed for the my current comapny in mind and the basic aim is to manage our client requirements, our company’s internal processes,
and vendor management in one seamless online environment using a dockerized django app.
The EPMS Translation Project Management System has the following features and app components:

* Translation and Localization Project Manaement capability with full CRUD functionality.
* Client Management app with full CRUD capability. 
* Vendor(Translators) Management app with full CRUD capability  
* A Dashboard analtics using CHART js, and django query capability. 
* Client PDF Invoice generation capability by using weasyprint from docker. 
* Vendor PDF PO generation capability by using weasyprint from docker. 
* Vendor Job Management app with crud functionality.
* Client Order Management app with CRUD capability.
* A system of rating mechanism for vendors task based industry specific criteria's.

## Built using:
- Python with Django framework and Jinja templating language
- Docker
- Chart Js
- weasyprint
- Django all auth

## Getting started:
- Clone this repository or fork it
    - To clone this repository type git clone `https://github.com/Henoker/epms.git` on your command line
    - To fork this repository, click fork button of this repository then type git clone `https://github.com/<your username>/epms.git`
- Install all the dependencies of this project by typing `docker-compose up -d --build ` on the command line
- configure your Postgres Databse 
- Migrate the database by typing `docker-compose exec web python manage.py makemigrations` on the command line
- Run the project locally by typing `docker-compose exec web python manage.py runserver` on the command line
    - NB: to run it on your local network, type `python manage.py runserver 0.0.0.0:8000`
- You project will be accessible in your localhost or local network.


## License
Distributed under the [MIT](https://github.com/Henoker/bookstore/blob/master/LICENSE) License. See [`LICENSE`](https://github.com/Henoker/epms/blob/master/LICENSE) for more information.

## Contact
- Henock Beyene Testfatsion - [hennybany@gmail.com](mailto:hennybany@gmail.com)
- Project link: https://github.com/Henoker/epms

## Love my effort?

<a href='https://www.linkedin.com/in/henock-beyene-tesfatsion-921ba54b/' target='_blank'><img height='35' style='border:0px;height:34px;' src='static/images/download.jpg' border='0' alt='Hire me at LinkediN' />