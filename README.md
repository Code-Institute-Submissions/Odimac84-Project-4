![picture of responsiveness](assets/images/responsive.jpg)


# [LINK FOR LIVE VIEW](https://project4-odimac.herokuapp.com/)

# Content

1. Introduction
2. User experience (UX)
3. Colors
4. The page
5. User stories
6. Testing
7. Deploying to github pages
8. Validation
9. Tech used
10. Credits
11. Updated for resubmission




# Introduction
My idea starting this project was to make a Blog where anyone could share whatever they wanted, sky was supposed to be the limit. This was cause writing could be so important for some and i didnt want to limit anyone to what they could vent about.

I had my own ups and downs in life and one thing that always helped me is writing, that have been my escape to get things off my chest and start working with it. So this project therefore fall quite close to my heart seeing that ive been there, and I been blogging to make things easier to break down.

## Wireframes from the beginning

![picture of wireframe landingpage](assets/images/Home.png)
![picture of wireframe login](assets/images/Login.png)
![picture of wireframe infopage](assets/images/info.png)
![picture of wireframe memberspage](assets/images/members-page.png)
![picture of wireframe profilepage](assets/images/My-profile.png)
![picture of wireframe registerpage](assets/images/register.png)

As my project progressed I both felt that i could not implement all i wanted and i also felt that alot off the things i thought about in the beginning would be a distracted and could take less space then originally intended. Also i found it that without having the opertunity to read the blogs without being a member then it would not be as easy if i want to go live for real with it and let people join it. So at the end of the day i decided to go for a diffrent design but still keep the concept of what my page was about. 

And for the members page and profile page, those are still there in my mind to be implemented at a later date. If they will follow the looks of the wireframes are still to be seen but i do know some of the fields i want to have there for when that project can take off. 

# User experience (UX)
![picture of comment section](assets/images/blogentry-other.jpg)
![picture of category selector](assets/images/categories-drop.jpg)
![picture of edit entry](assets/images/edit-post.jpg)
![picture of registration](assets/images/register.jpg)
![picture of logout](assets/images/signout.jpg)


As seen in above pictures the registration is easy and it wont take the user long to get started. the things asked for is kept to a bare minimum so that they can get going fast and at the same time it offers a great deal of privacy to the user. 

Ive also kept it open so that you can still read and comment on blog-posts without being a member so that even if you dont want to sign up you can still interact with the authors. Navigating the categories can be done either by the drop down on the top navbar or by clicking the blog post category.

# Colors #

![picture of page](assets/images/logged-in-home.jpg)
![picture of blogentry input](assets/images/blog-post.jpg)

I went for a darker theme on this site since its timeless and it will make the blog posts being the stars off the show. On the main page there is a box with a slightly darker tone then the background just to mark it out just the slightest and make it look nicer sitting there with the short text about the page.


# User stories
Me as a developer wanted to build a page where people mainly could vent out and tell their story, but still safe enough that they had the control to take that off whenever they wished. Its not always that we wish for our thoughts to be on display for the entire world to see. Sometimes we want to change our mind or unread our minds. 

## User ##
![picture of add ing a comment](assets/images/add-comment.jpg)
![picture of your own blogpost](assets/images/blogentry-own.jpg)
![picture of homescreen when not a member](assets/images/home-not-member.jpg)
![picture of sign in page](assets/images/signin.jpg)


- As a user i want to be able to create a blog that is shared with others. (Implemented)
- As a User i want to be able to like a post i read. (Implemented)
- As a User i want to be able to style my blogpost. (Implemented)
- As a user i want to be able to filter the blogs in categories to read only what interests me. (Implemented)
- As a User i want to be able to add images to my blog to show what i write about. (Implemented)
- As a user i want to be able to connect by messages to other people writing. ( Not implemented)
- As a User i want to be able to comment on other peoples blogs. (Implemented)
- As a User I want to be able to add a Category to my blog to show what it is about. (Implemented)
- As a user I want to be able to edit or delete my blogs entries. (Implemented)
- As a user i want to be able to create a blog that is shared with others. (Implemented)
- As a user i want to be able to edit my profile for the blog. (Not implemented)

## Possible features to add  ##

- Message system between users
- Replies on comments
- Email verification on signup
- Profile page
- Captcha for comments if not verified user

# Testing

![picture of Database structure](assets/images/Database.jpg) 

Exept from this testing i have also run the page through both lighthouse and GTmetrix and the results are shown below. 

![picture of lighthouse](assets/images/lighthouse.jpg)

![picture of GTmetrix](assets/images/gtmetrix.jpg)

## Further testing 

When the page was deployed i went through all off the pages and tried all the functions. After the bugs had been fixed everything is in order exept from the issue with the category add function. I still left it on the site since if i would choose to work on this project after my time at CI this is a function that i want to have there and also i will add this to a payed database and that function should work or change the type of database.

Both CSS and HTML has been tested so that it works and does what it is intended to do. The jigsaw showed no errors in the CSS and the HTML validator showed no major errors within the HTML at the time of testing. 

Deeper Testing document [here](TESTING.md)


# Validation
 

### Links to validation images ###

- [pep8 first picture](assets/images/pep8num1.jpg)
- [pep8 second picture](assets/images/pep8num2.jpg)


# Deploying to Heroku

- First you need to have the project ready on Github.
    - Make sure that your Creds file is in gitignore if needed
    - Add the requirements.txt my using the command "pip3 freeze > requirements.txt"

- we also need to add a Procfile with e following info in it.
    - web: gunicorn Project4.wsgi (this will tell the app how to use the code.)


- Now when this is set we can move on

- Go onto [Heroku](https://id.heroku.com/login)

- Login or create a new account if you dont have one already.

- Click create new app.

- Choose name for your project, and your region.

- Go to setting.

- Click on reveal config vars 
    - Here you add CLOUDINARY_URL, DATABASE_URL and your secret_key

- Next we add build packs
    - we need to add python here 

- Go to resources and search for Postgres, and install the Heroku Postgres

- Now head over to Deploy 

- Connect to github login.

- Search for the repo you want by typing in your repo name. And connect to this one with the button. 

- After this we click the deploy button at the bottom.


# Tech used

The site is built using HTML5 and CSS3 and apart from that I have got certain elements from other sources that will be mentioned below.

- [GitHub](https://www.github.com)
Hold the respiratory for this project along with files.
    
- [Gitpod](https://www.gitpod.io)
the platform ive been deploying my code on.
    
- [FontAwesome](https://fontawesome.com)
for the socialmedia icons
     
- [PEP8 Validation](http://pep8online.com/)
CSS jigsaw validator.
    
- [Heroku](https://heroku.com/)
For deployment of the site and application
        
- [Django](https://www.djangoproject.com/)
Framework used to build the site and application.

# Credit

Credit goes out to the slack community for helping out when needed with pointers or just cheering me on. Especially thanks to Daisy_mentor for helping me in times off need. All those calls and your eagly eyes with expirience helped me when i got stuck.

Special thanks to Felipe Souza Alarcon aswell to find the time to respond to my questions and giving me tips and pointers where needed.


# Updates for resubmission

-   Categories tab in navbar is now present on all pages.
-   Categories now updates after a new category is made.
-   Add category is now a superuser only feature 
-   Responsiveness has been looked at and fixed on mobiles. 
-   Testing.MD holds the information about testing of the site.
-   Docstrings has been added in codebase.
-   Heroku deployment has been added to readme.md



![Flow of the site](assets/images/siteflow.jpg)

Picture above shows how the site is built and how the models work together.
Post is the Center of the site since this is what it is all about and this was the main piece that was built. on that i did hang up some extra features that was good for UX but also made to give feedback to the user.

Comments and likes are the 2 features that are there to provide the user feedback and reason i keep comments open even for non registered users is that this will make it easier for anyone to provide feedback. Even if this makes the page easier targets for spam, this as said above can be countred using a captcha for non verified users in a future update of the site. 