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
        - [Search Page](#search-page)
        - [Portfolio Page](#portfolio-page)
        - [Product Page](#product-page)
        - [Cart Page](#cart-page)
        - [Checkout Page](#checkout-page) *
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#account-page)
        - [Contact Page](#contact-page)
        - [403 Page](#403-page)
        - [404 Page](#404-page)
        - [500 Page](#500-page)
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

The main objective in creating the SMGPhotography application is to provide the user with a simple to use e-commerce site, with live filtering of object, a simple way to search for photos dependant on type or tag, and provide and automated delivery of digital prints of photos. Also to provide an easy to maintain system to the admin for maintaining the database, and presenting images, including featured images to the user.

This applications is designed with news media providers in mind who require a simple way to view the photographers entire portfolio, and filter based on requirements.

As a side goal, I have left room for expansion once I have developed my skills further, and would like to develop this into a commercially viable system with ordering features pertaining to physical prints with delivery/shipping calculated dependant on size/weight, etc, as outlined below in the [**Features Left to Implement**](#features-left-to-implement).

## Development Goal

- A project I'd be excited to show off to people as a testament to my abilities.
- Well thought out programming to account for the unpredictability of users. 
- Something that looked professional even for a novice programmer on their first venture into the Django framework, and first deployment on a PostGres database, with S3 storages.
- To learn and impliment intricate python code that would be impressive to a veteran python programmer.
- To create a viable e-commerce site that could be used by the company this design is based from, and provide them with a solution to displaying and distributing their work.

## User Stories

 **As a user I want this application to have:**
 1. A system to search for photos based on certain tags/categories/name.
 2. A website that is easy to navigate.
 3. A website which is pleasant to look at and looks professional.
 4. A way to view all my purchases after they are made.
 5. An application that is fast, with very short load times.

## Wireframes

Wireframes were built in the early stages of development to get a rough outline of the structure needed for the planned features of the site. These can be viewed below:

- [Desktop & Tablet](https://github.com/Legaeldan/siobhan-mcgowan-photography/blob/master/data/wireframes/Desktop-Tablet%20App.pdf) **Note:** Wireframes are combined as same styling is used on both Desktop and Tablet.
- [Mobile](https://github.com/Legaeldan/siobhan-mcgowan-photography/blob/master/data/wireframes/Mobile%20App.pdf)

## Design choices

The main approach to this application is made to easy to maintain, and easy to use database. To provide as many features as possible to make the entire experience simple. The following design choices were made to reflect this:

**Fonts**

- The Nav elements font **Open Sans** with a main body font **Roboto** was chosen due to it's simplistic design, as not to distract from the overall site, and to not clash with the colourful images provided in the portfolio section. With this subtle font choice, it reflects nicely on the simplistic overall white/off-white background choices.

**Colours**

- The colour choices were made to be simplistic, and to increase the standout look of elements such as the banner, and photo thumbnails.
- Colours of **white** and **off-black** were chosed to not overload the user, and maintain a simple, clean look with a nice definitive contrast from page elements, and overall page.
- **Goldenrod** was chosen as nice contrast to the **white** background and **offblack** elements of the site, and to help highlight any helpful links. **Goldenrod** was found to be the best contrast while remaining easy on the eye.

**Styling**

- Use of the **BootStrap** framework, coupled with the template **Foundry** was used to keep the site simple, only displaying relevant information, without drawing attention away from the content.
- The overall decision of square edges to all content was decided upon to keep the site looking sharp, but not harsh. Highlighting a definite edge to everything on the page, without accosting the user with too much information.

**Background**

- Background colour of  **white** was selected to better help the images and text stand out on screen, and give the elements on the page more power in standing out. This also helps accentuate the colours and images on screen, and give more depth to the overall page. This also gives the page an overall profession look, and encourages the user to understand this site belongs to a professional who they would want to work with.

# Features


## Existing Features

**Please Note: Any images missing for particular pages are due to the restrains of the mockup program used. Due to X-Frame-Options being set to SameSite, the software used is unable to display any pages that require authentication.**

### Elements on every Page

- Navbar
    
    - The navigation bar features the company name in Open Sans font. Similar to the Roboto font used in the rest of the site, but to give minor contrast to keep the page fresh.

    - Visiters who are not logged in are greeted with the standard buttons for not authorised users.
        - Home
        - Portfolio
        - Contact Us
        - Register
        - Login
        - Search icon with dropwdown text input.
        - Cart with dynamic badge for cart items, with dropdown to preview first three items in cart, and button to view full cart.

    - Visiters who are logged in are greeted with the standard buttons for authorised users.
        - Home
        - Portfolio
        - Contact Us
        - Profile
        - Logout (Provides a success message and redirects to the index page once logged out.)
        - Search icon with dropwdown text input.
        - Cart with dynamic badge for cart items, with dropdown to preview first three items in cart, and button to view full cart.

    - Logged in users are determined by the inbuilt Django auth module. These are detected by the navbar using the ```if user.is_authenticated``` in the template, and displays the relevant tabs based on this.

    - The items in cart is detected using ```if photo_count > 0```` and a badge then displays the photo count using ```photo_count```.

    - The preview of the cart is decided using a for loop on the amount of items in the cart. For the first three items, they are displayed as normal in the preview. For anything over 3, the code ```elif forloop.counter == 4````generates the line ```Plus {{ forloop.revcounter }} more items...``` where forloop.revcounter calculates the remaining items, and tells the user how many more items are in the cart.

    - If the photo counter check returns 0, then the cart preview will display the line ```<span>Nothing to show here! Best get shopping!</span>```

- Footer

    - A simplistic footer is used on this site. With the same company name as the navbar displayed in the lower left corner.

    - A link to the GitHub repository in the bottom right corner.

    - a **TOP** button to send the user back to the top of the page without scrolling.

- Loading spinner is displayed on all pages on the main container of the page. This is displayed on every page regardless of loads times, and has a delay to give animations time to begin. This is especially noticeable on the portfolio page.

### Home Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/multi-platform-mockup.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes"/>
</div>

- A heading banner is display with the option to change from the admin menu. The admin can set a boolean value of true to display an image as the banner. If there are multiple banners selected, the latest one will be displayed.

- A small portoflio to be display in the form of featured photographs. These can be set in the admin panel under the Featured boolean value.
    - The featured portfolio includes a slide up animation on page load.

- A list of reviews from clients, which can be input in the admin panel. These can also be toggled on and off with a Featured boolean value.

- A simple contact us button to route the user to the contact page.

### Search Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/search.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how portfolio page looks on all screen sizes"/>
</div>

- A page that returns all photos based on search criteria.

- Returns an error page with no results, and a search bar for user to try searching again.


### Portfolio Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/portfolio.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how portfolio page looks on all screen sizes"/>
</div>

- A filter on all photos on page. This is generate from the categories of all photos displayed on the page. The filter then changes the opacity of all irrelevant photographs on the page.

- A masonry style image gallery is displayed here, with watermarks on all photos. The masonry animation starts once the loader has disappeared.

- All images link to their individual photo page.

### Product Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/photoDetail.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how photo detail page looks on all screen sizes"/>
</div>

- Display image in thumbnail format on left side of the page.

- Displays photo details on the right. These include:
    - Photo price
    - Photo description
    - Photo dimensions
    - Photo ID or SKU number

- An add to cart button which then adds that specific photo to the cart. If item is already in the cart, it will be refused as outlined below in the cart section.

- A lightbox is applied to the image that when clicked, displays the image fullscreen in a lightbox, with easy dismissal.

### Cart Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/cart.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how photo detail page looks on all screen sizes"/>
</div>

- Displays a table filled with cart contents.
    - When there are no items in the cart, displays a non-dismissable error that there are no items in the cart
    - When items are in the cart, displays each item on it's own row. Includes a red cross icon to remove the item from the cart, and then return the user to the updated cart.

- A running total is shown on the right of the page.

- A checkout button is display that calculates the total of the cart, and redirects the user to the checkout page.

- The checkout button is conditional that there are items in the cart. If no items in the cart, the cart page is returned with an error.

### Checkout Page

- Displays a page, with a running total of all items purchased, and a payment form.

- The checkout page requires logon to view.

- Running total displayed on the left of the page displays all item names, plus prices, and the total of all items in cart.

- Order form is comprised of user details for billing purposes, and a stripe payment form which is tied to the stripe.js in the static directory. Payment is made, and once returned successfully, redirects to the profile page, with a success message that payment way made.

- If payment is unsuccessful, returns the checkout page with an error message.

- An automated delivery of purchased products is facilitated by SendGrid. Once order is completed, and email is generated with default text, and all purchased items are attached to the email, and sent to the user using the email provided during registration.

### Register Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/register.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how register page looks on all screen sizes"/>
</div>

- Displays a basic registration page, comprising of a user name, email address, and password, with password confirmation.

- If a user is currently registered using the same name, an error is attached to the page, and returned to the registration page.

### Login Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/login.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how login page looks on all screen sizes"/>
</div>

- Displays a basic login page using either the users email or username.

- Failed logon attempt returns the user back to the login page with an error.

- Successful login redirects the user back to the index page, and displays a success message that the user logged in.

### Profile Page

- Displays a page which includes a table with all purchased items attached to the account.

- All items can be viewed without a watermark by clicking the appropriate image, which opens the image in a new tab.

### Contact Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/contact.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how contact page looks on all screen sizes"/>
</div>

- Displays the contact page, which includes a map location banner.

- Map location showing where the business is located, pulled from google maps, and embedded in the page. 

- Left side of the page displays business details such as address and contact number and email.

- Basic contact form is included, which when successful, automatically generates an email using SendGrid and send to the user. Also generates a copy to be sent to the admin.

### 403 Page

- A simple 403 page, with a contact button and return to home button. Similar layout as the 404 page, but with altered text.

- A text prompt for the user to contact should they encounter this page.

- Added in the rare event that a 403 error arises.

### 404 Page

<div align="center">
    <img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/404.png" href="http://siobhan-mcgown-photography.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how 404 page looks on all screen sizes"/>
</div>

- A simple 404 page, with a contact button and return to home button.

- A text prompt for the user to contact should they encounter this page.

- Catches requests when users type in the wrong URL, or other related errors when the page cannot be found.

### 500 Page

- A simple 500 page, with a contact button and return to home button. Similar layout as the 404 page, but with altered text.

- A text prompt for the user to contact should they encounter this page.

- Added in the rare event that a 500 error arises.

## Features Left to Implement

**Features that would possibly be implemented at a later date after more research are as below:**

- A faster method of returning the users purchased images.

- A way to change images when uploading to include the content-disposition option as attachment in the meta-data of images sent to S3. This will allow users to just download instead of view the image, and then save.

- A feature to offer the users more options of one item, such as physical prints and shipping. (This is not yet provided by the business.)

# Information Architecture

## Database Choice

In the initial planning phase of this project, an SQLite3 structured database was decided upon due to it's native support in Django. On this decision, it was agreed to utilize the PostGres supported database inbuilt into Heroku to store and sort all data.

## Data Types

The types of data in this project stored in Postgres are:

- Integer
- Character varying
- Boolean
- Timestamp with time zone
- Numeric
- Text
- Date

## Collections Structure

SMGPhotography relies on the below connected database tables as outlined.


```
Schema |            Name            | Type  | Default Django Table
-------+----------------------------+-------+------------------------
public | auth_group                 | table |       Yes
public | auth_group_permissions     | table |       Yes
public | auth_permission            | table |       Yes
public | auth_user                  | table |       Yes
public | auth_user_groups           | table |       Yes
public | auth_user_user_permissions | table |       Yes
public | checkout_order             | table |
public | checkout_orderlineitem     | table |
public | django_admin_log           | table |       Yes
public | django_content_type        | table |       Yes
public | django_migrations          | table |       Yes
public | django_session             | table |       Yes
public | home_review                | table |
public | photos_category            | table |
public | photos_photo               | table |
```

The schemas for the relevant tables are outlines in the attached file below, or can be found in the **static/schemas** directory of this repository:

[All tables text file](https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/schemas/allTables.txt)

**(Please note: Some tables are omitted, including those generated by default from Django i.e. the auth tables, from the all tables file as they are handled by Django, and not specifically used in the templates for this site.)**

# Testing

As a first attempt at Python/Django programming, and a second attempt at Python in general, the code had to be scrutinized, and thoroughly tested throughout. Every function would need to be planned, and tested in depth before moving on to other functionality, as these would be tied together later in the project.

**All testing results can be found in the seperate [TESTING.md](https://github.com/Legaeldan/siobhan-mcgowan-photography/blob/master/data/testing/TESTING.md) file. 

## Test Planning

During planning and development, defensive design was taken into account. The planning of testing was split into two section. **Functionality** and **Defensive Design**. Each function was planned out carefully, then a subsection to testing was added for defensive design, in which that particular function was given every possible variable a user could give, and tested for unwanted activation.

To show the performance of the site overall. An audit was run at the final stage of development, and the results are posted as below. Due to images being used from an active business, and on the agreement that the images could only be used in their original state. I am unable to alter the images to improve performance at this time until an agreement can be reached on image alteration.

<div align="center">
<img src="https://siobhan-mcgowan-photography.s3.eu-west-1.amazonaws.com/static/img/auditResults.png" alt="Audit Results"/>
</div>


**Example:**
 - **Planning:** A page is required for users tying incorrect URL values. 
 - **Testing (Phase 1):** The page is created, and django handles all 404 requests and redirects to the 404 template..
 - **Result:** Any attempt to access an incorrect URL redirects to the 404 page.
 - **Verdict:** Test passed as expected and delete button is now operational.

**All testing results can be found in the seperate [TESTING.md](https://github.com/Legaeldan/siobhan-mcgowan-photography/blob/master/data/testing/TESTING.md) file. 

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
- [Django](https://www.djangoproject.com/)
    - This project utilises the **Django** framework to render the site, including URL configurations, and defining models for data to be stored.
- [SendGrid](https://sendgrid.com/)
    - This project uses the **sendgrid** backend and SMTP service to facilitate the automated delivery of orders, and to enable the use to send the administrator emails, with copies sent to the user.
- [BootStrap](https://getbootstrap.com/)
    - The project uses the **BootStrap** framework to simplify the structure of the website and make the website responsive easily.
- [Virtual Env](https://virtualenv.pypa.io/en/latest/)
    - This project utilise **VirtualEnv** to run a closed virtual enviroment specifically tailored for this project.
- [Stripe](https://stripe.com/)
    - This project utilise **Stripe** to process payments, and act as a go between between the user and the bank as a payment processor.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 
- [Django Storages](https://django-storages.readthedocs.io/en/latest/)
    - The project uses **Django Storages** to facilitate the transfer and storage of documents uploaded to the admin panel, and provide an easy way to sort and store media/static files, and provide dynamically generated links to all media. 

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
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [Foundry - ThemeForest](https://themeforest.net/item/foundry-multipurpose-html-variant-page-builder/11562108)
    - This project utilizes a regular license with **ThemeForest** with the **Foundry** template. 
- [Themify Icons](https://themify.me/themify-icons)
    - The project uses **Themify** to style additional website icon links.
- [PostGres](https://www.heroku.com/postgres)
    - This project uses the **Heroku Postgres** database to store all information entered through the website admin console.
- [SendGrid](https://sendgrid.com/)
    - This project uses a **sendgrid** account to handle sending customised mails to end users.
- [AWS S3](https://aws.amazon.com/s3/)
    - This project utilizes the **AWS S3** platform for storage of all media and static files.
- [HTML Validator](https://validator.w3.org/)
    - This project utilised the HTML validator provided by W3C to check and correct any issues in my current HTML code.

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

**Side Note:** For those using Visual Studio Code. A simplified way to run the runserver command, among other commonly user commands, can be added into the virtual environment. The easiest way to achieve this is add the below commands at the end of the **activate.bat** file found in **env\sctips\activate.bat**

```
doskey run=python manage.py runserver
doskey static=python manage.py collectstatic
doskey makemigrations=python manage.py makemigrations
doskey migrate=python manage.py migrate
```
For each command added, these shortcuts will be added to the terminal on each launch.

# Credits

I received inspiration and assistance on this project from [Simen Daehlin (Eventyret)](https://github.com/Eventyret), who assisted above and beyond to help improve the site. What seemed like the impossible task of understanding [Django](https://www.djangoproject.com/), and although still more understanding of this framework is required, I have the tools to create an effective e-commerce site. He has helped understand this framework a lot better, and has pointed me in the right direction everytime whenever an issue arose with how to impliment code.

# Disclaimer

Please note that all code and images in this site are for educational purposes only. All images are property of Siobhan McGowan Photograhy, and have been authorised for use in this project only. Any re-use or distribution of the images in this application is strictly prohibited. 

The template used in this project is also licensed under a single use license specific to this project, and therefor this template cannot be re-used in deployment of any other site unless a license is purchased from [ThemeForest](https://themeforest.net/item/foundry-multipurpose-html-variant-page-builder/11562108)