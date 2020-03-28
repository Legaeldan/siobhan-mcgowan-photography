<a href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank"><img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/readme-banner.png" alt="SMGPhotography logo"/></a>

# Siobhan McGowan Photography [![Build Status](https://travis-ci.com/Legaeldan/siobhan-mcgowan-photography.svg?branch=master)](https://travis-ci.com/Legaeldan/siobhan-mcgowan-photography)

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/multi-platform-mockup.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes"/>
</div>
<br>

## Introduction

SMGPhotography was created by Kieran Cunnane on the back of an enquiry about creating a simple e-commerce site to furnish local media establishments with a site to retrieve photography that may be used in their local paper/site.

The photographer in question approach myself to design a simple site to showcase their work, and make it possible for users to purchase digital prints of her work. And for local news outlets to purchase her work without constant direct interaction with the owner.

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Development Goal**](#development-goal)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design choices**](#design-choices)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Portfolio Page](#portfolio-page)
        - [Product Page](#product-page)
        - [Cart Page](#cart-page)
        - [Checkout Page](#checkout-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#account-page)
        - [Contact Page](#contact-page)
        - [404 Page](#404-page)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Types**](#data-types)
    - [**Collections Structure**](#collections-structure)

4. [**Testing**](#testing)
    - [**Test Planning**](#test-planning)
    - [**Known Bugs**](#known-bugs)

5. [**Technologies Used**](#technologies-used)
    - [**Languages**](#Languages)
    - [**Frameworks/Libraries**](#frameworks/libraries)
    - [**Software**](#Software)
    - [**Additional Resources**](#additional-resources)

6. [**Deployment**](#deployment)
    - [**Deployment to Heroku**](#deployment-to-heroku)
    - [**Running this project locally**](#running-this-project-locally)

7. [**Credits**](#credits)

8. [**Disclaimer**](#disclaimer)


# UX


## Project Goals

## Development Goal

## User Stories

## Wireframes

## Design choices

# Features


## Existing Features


### Elements on every Page

### Home Page

### Portfolio Page

### Product Page

### Cart Page

### Checkout Page

### Register Page

### Login Page

### Profile Page

### Contact Page

### 404 Page


## Features Left to Implement

# Information Architecture


## Database Choice

## Data Types

## Collections Structure


# Testing


## Test Planning

## Known Bugs


# Technologies Used


## Languages
- [Python](https://www.python.org/)
    - The project uses **Python** to run the application.
- [HTML](en.wikipedia.org/wiki/HTML)
    - The project uses **HTML** to structure the DOM.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** to style and theme pages..
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - The project uses **Javascript** to allow for DOM manipulation.

## Frameworks/Libraries
-[Django](https://www.djangoproject.com/)
    - This project utilises the **Django** framework to render the site, including URL configurations, and defining models for data to be stored.
-[SendGrid](https://sendgrid.com/)
    - This project uses the **sendgrid** backend and SMTP service to facilitate the automated delivery of orders, and to enable the use to send the administrator emails, with copies sent to the user.
- [BootStrap](https://getbootstrap.com/)
    - The project uses the **BootStrap** framework to simplify the structure of the website and make the website responsive easily.
- [Virtual Env](https://virtualenv.pypa.io/en/latest/)
    - This project utilise **VirtualEnv** to run a closed virtual enviroment specifically tailored for this project.
- [Stripe](https://stripe.com/)
    - This project utilise **Stripe** to process payments, and act as a go between between the user and the bank as a payment processor.



## Software
- [Visual Studio Code](https://code.visualstudio.com/)
    - The project uses **Visual Studio Code** to create all files contained in the site, and push to GitHub.
- [Git](https://git-scm.com/downloads)
    - This project uses **Git** to commit and push all files to the [GitHub Repository](https://github.com/Legaeldan/milestone-2).
- [GIMP](https://www.gimp.org/)
    - This project used tools in **GIMP** to create and edit images such as the logo and favicon.
- [Visio](https://www.microsoft.com/en-ie/p/visio-standard-2019/cfq7ttc0k7cf?activetab=pivot%3aoverviewtab)
    - This project used tools in **Visio** to create, edit, and present wireframes in a more professional manner.

## Additional Resources
Foundry - ThemeForest
-[Themify Icons](https://themify.me/themify-icons)
    - The project uses **Themify** to style additional website icon links.
PostGres

# Deployment

This project was developed using [Visual Studio Code](https://code.visualstudio.com/), [Python](https://www.python.org/), and [Git](https://git-scm.com/downloads), committed to a local [Git](https://git-scm.com/downloads) repository, and pushed to [GitHub](https://github.com/Legaeldan/siobhan-mcgowan-photography) using a locally installed version of [Git](https://git-scm.com/downloads) via command prompt.

The main method of deployment is [Heroku](https://siobhan-mcgowan-photography.herokuapp.com/), connected directly to my [GitHub Repository](https://github.com/Legaeldan/siobhan-mcgowan-photography), and deployed within the [Heroku Dashboard](https://www.heroku.com/).

## Deployment to Heroku

To deploy this page to [Heroku](https://www.heroku.com/) from its [GitHub repository](https://github.com/Legaeldan/siobhan-mcgowan-photography), the following steps were taken: 
1. Log into [Heroku](https://dashboard.heroku.com/). 
2. From the main dashboard, select the **New** dropdown, then select **Create new app**.
3. Give you app a unique name, and select the region you wish to deploy to.
4. Select resources from the top of the page. And search for **postgres** and **sendgrid**. Select **Heroku Postgres** and **SendGrid**. Add both as a free/hobby account. Sendgrid will require billing information to be entered, but will not be charged for mails **under 12,000**.
5. select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
6. Select **GitHub** as the method of deployment.
7. Log in using your **Github credentials.** 
8. Select your username, and search for the reposity in the **repo-name** box.
9. Select **Connect** on the repository you wish to connect to.
10. Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**
11. After the application is built, select **Settings** from the top of the page.
12. Select **Reveal Config Vars**.
13. Add the config keys for **IP**, **PORT**, **AWS_SECRET_ACCESS_KEY**, **AWS_SECRET_KEY_ID**, **DATABASE_URL**, **EMAIL_HOST_PASSWORD**, **EMAIL_HOST_USER**, **EMAIL_MASTER_SENDER**, **SECRET_KEY**, **STRIPE_PUBLISHABLE**, and **STRIPE_SECRET** (These will not be published here for security reasons).
14. Select **More** from the top right of the page, and select **Restart all dynos**.

## Running this project locally

**Please note: This project was created and run on Windows in Visual Studio Code with a Virtual Enviroment using Python 3 and Git. Please ensure you have Python 3 and Git installed locally before running this project. For other OS or Code Editors, please refer to the relevant documentation for your enviroment.**

**Preferred Requirements:**  
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Git](https://git-scm.com/downloads)
 - [Python](https://www.python.org/)
 - An account with [Stripe](https://www.stripe.com/). Please refer to the [Stripe Documentation](https://stripe.com/docs) for more help.
 - An account with [SendGrid](https://sendgrid.com/). Please refer to the [SendGrid Documentation](https://sendgrid.com/docs/) for more help.
 - An account with [AWS S3](https://aws.amazon.com/s3/). Please refer to the [S3 Documentation](https://docs.aws.amazon.com/s3/index.html) for more help.



To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/Legaeldan/siobhan-mcgowan-photography).
2. Under the repository name, click the green "Clone or download" button.
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local editor program, open a terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.

```
git clone https://github.com/Legaeldan/siobhan-mcgowan-photography
```

7. Press Enter. Your local clone will be created.
8. From the terminal, type ```pip3 install virtualenv```
9. Once the above is complete, type ```virtualenv env```. This will create your local virtual enviroment.
10. Create a folder in the root directory called **.vscode**.
11. In the **.vscode** folder, create a file called **settings.json**
12. Insert the below code into the settings.json file, wait for the enviroment to load (This can be seen in the lower left hand corner of VSCode).
```json
{
  "python.pythonPath": "env\\Scripts\\python.exe",
  "python.linting.pylintArgs": [
    "--load-plugins=pylint_django"
],
  "terminal.integrated.env.windows": {
      "SECRET_KEY": "[Insert secret key here]",
      "IP": "127.0.0.1",
      "PORT":"9100",
      "AWS_SECRET_ACCESS_KEY": "[Insert AWS Secret Access Key here]",
      "AWS_SECRET_KEY_ID": "[Insert AWS Secret Key here",
      "DATABASE_URL": "[Insert Postgres URL here]",
      "STRIPE_PUBLISHABLE": "[Insert Stripe Publishable Key here]",
      "STRIPE_SECRET": "[Insert Stripe Secret Key here]",
      "EMAIL_HOST_USER": "apikey",
      "EMAIL_HOST_PASSWORD": "[Insert Sendgird API Key here]",
    }
}
```
13. Restart VSCode. The bottom left should now state **Python X.X.X 64/32-bit ('env':virtualenv)**
14. Open a terminal windows. The directory in terminal should now be preceeded by **(env)**, stating the enviroment is now active.
15. From the terminal, type ```pip3 install -r requirements.txt```.
16. Once complete, type ```python manage.py makemigrations``` to create database micgrations.
17. Once migrations are complete, type ````python manage.py migrate```. This will create the fields in the database for your data.
18. Type in the terminal ```python manage.py runserver```.

For more help on cloning a repository on Github, please click [here](https://help.github.com/en/articles/cloning-a-repository).


# Credits

I received inspiration and assistance on this project from [Simen Daehlin (Eventyret)](https://github.com/Eventyret), who assisted above and beyond to help improve the site. What seemed like the impossible task of understanding [Django](https://www.djangoproject.com/), became far simpler that originally believed. He has helped understand this language a lot better, and has pointed me in the right direction everytime whenever an issue arose with how to impliment code.

# Disclaimer