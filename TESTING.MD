# Testing

## Navigation

-   Navigation has been tested and all i working as intended.
-   If logged in you can post a blog, if not you can read and leave comments. 
-   Superusers can add ned categories from the navbar when logged in.

## Homepage
  

### Categories

-   Categories tab can be reached from all pages and works as intended.
-   Categories can also be clicked on the posts itself if you want to continue reading more about that subject. 

## Post handle

-   Posts are creared in its own window and can have pictures to it and usage of the summernote field. 
-   summernote field on a mobile will be moveable but follows the cursor when typing. This was the only way to keep the summernote field, which provides more UX then taking it away would do. Ive looked into changing it to CKeditor but that would give me a whole new set off problems that would land me in the same spot. This problem what ive understood is a common problem with summernote due to teh fact that the controls wont be responsive and therefore tha iframe where it lies wont scale as it should. 

## Account

-   logging in/out has been tested without any problems.
-   Register has been tested without problems.
-  Posts made by registered user can only me edited or deleted by that user.   

## Comments

-   Comments can be made by anyone, been tested and works as intended. 
-   Code for this has been controlled and it is working.
-   future implementation for comments could be adding a captcha to counter bots that might spam the blogposts, but for now i want to keep the comments open for everyone even non registered users since that gives feedback to blogers. 


## Profile

-   Creating a profile has been tested and works. 
-   Creating a profile gives you the ability to create a blogpost and like on other posts. 


## Administrative Tools

-   Adding a new cathegory has been moved to only superusers due to the fact that categories can get overwhelmed quickly if anyone could add to this.     


## Edit/Delete

-   Edit and delete buttons shows up once you are logged in on your own posts. trying to get past this will give you an error message.
-   Once clicked Edit or delete you will be forwarded to a confirmation page where you get the chance to go back or proceed. 


## Other

-   All pages have been checked for bugs and none has been found unless they been mentioned in the above text.
  


## Responsiveness

This application was tested for responsiveness across a variety of devices to ensure content remained readable and editable on various screen sizes.

The navigation of the site was tested by using it and trying to break it. Bugs that were found during the process has after this been fixed and will be taken up in the Bugs found section.

These tests were performed on the following devices and browsers:

-   Chrome and Firefox on Desktop
-   Chrome Laptop
-   Chrome on Tablet
-   Chrome on Samsung S21
-   Chrome on Samsung S10+
-   Firefox on Samsung S10+

## Bugs Found

-    The app has been manully tested for all the functions that are implemented with success on all but one part. The only issue that still stands are that when a category is added the server needs to reboot for that category to show up as a choice in the blogpost. This has been looked at and no problem that explains this has been found in the code itself. But i have found a possible explaination in the type off database that is being used, this seems to be a common problem within SQLlite3 which is the database type that is used by Heroku postgres app on their homepage.  follow the link for the information i found on the matter [Database limitations](https://devcenter.heroku.com/articles/sqlite3#disk-backed-storage). This could possibly be solved using a payed option instead but that has not been done and tested. 

FIXED with a __init__ def. problem lied within the code that it didnt update the category choices after a new value was added.  
    

-    Signup page threw a 500 error on creating a user. 

FIXED: This was fixed by adding ACCOUNT_EMAIL_VERIFICATION = 'none' in settings so that no verification on emaiol was required.



-  Summernote fields on the blogpost entry wasent showing up as intended. 

FIXED: This was tricky but simple when i got around it i just had to add the widget for it since my forms was already in widgets. 



- Categories tab in navbar wasent showing up on all pages.

FIXED: added a context processor to hand out the information needed to all pages across the site. 



