# oriGallery

## A Description of the WebApplication.

## Table of Content

+ [Description](#description)
+ [Behaviour Driven Development](#behaviour-driven-development)
+ [Installation Requirement](#Installation)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)
+ [Live Link](#live-link)

## Description

<p>A personal gallery application that displays photos from various counties in Kenya for others to see and viewers are abled to copy the links of the photos and share or search on them online..</p>

## Behaviour Driven Development

<p>

* A user can view different stories.
* A user can click on a single photo to expand it and also view the details of the photo.
* As user can search on different categories of photos.
* A user can copy a link to the photo to share with my friends
* A user can view photos on the location they were taken.

</p>

***
## Installation

* Open Terminal `ctrl+Alt+T`

* Git clone https://github.com/RichieOrito/Ori-Gallery.git

or

* Git fork - Enter into your own repository and search-https://github.com/RichieOrito/Ori-Gallery then click on fork to add
it on your own repository.

 Navigate into the cloned project. 
`cd ori-gallery`


* Create and activate the vitual Environment and install the from requirements.txt
`$ python3.6 -m virtualenv virtual`
`$ source virtual/bin/activate`
`$ pip install -r requirements.txt`

* Setting up environment variables

Create an `.env` and add the following.
```
SECRET_KEY='<Secret_key>'
DBNAME='tribune'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<your-email>'
EMAIL_HOST_PASSWORD='<your-password>'

```

requirements from 
---
`requirements.txt`


* Start the Server to run the app
* `$ python3.6 manage.py runserver`

* Open [localhost:8000](#)
***


### Requirements

* Either a computer,phone,tablet or an Ipad

* An access to the Internet

* Python3

* Postgres

* virtualenv

*Pip

[Go Back to the top](#oriGallery)

## Technology Used

* HTML 5 - which was used to build the structure of the pages.

* CSS - which was used to style the pages incuding the left aside navigation bar.

* Figma-which was used to design the prototype of the UI.

* Python/Flask - Which was used to build the web-applications and interactivity

* Postgresql - For the database

* Heroku - For deployment

## Reference

* LMS
* W3schools
* stackOverFlow

[Go Back to the top](#oriGallery)

## Licence

MIT License

Copyright (c) [2022](#licence) [Richard Orito](#licence)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#oriGallery)

## Authors Info

Slack Profile - [Richard Omondi](https://app.slack.com/client/T0101L740P4/C010GLANY3A/user_profile/U02EZFHEJUA)

Linked - [Richard Orito](https://www.linkedin.com/in/richie-orito/)

Gmail - [richard.omondi@student.moringaschool.com]()

Github - [RICHIE ORITO](https://github.com/RichieOrito)

## Live Link

LiveLink- [Gh-pages](https://ori-gallery.herokuapp.com/)

[Go Back to the top](#oriGallery)