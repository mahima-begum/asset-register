# asset-register

Name:
Asset register

Descripion:
The purpose of this project is for employees to be able to log all IT assets they are in possession of, so that the organisation can keep track of this. 
In this web app, users can register accounts if they meet the validation criteria. They can then login and add all assets, and modify existing assets they own. 
There are existing admin users that can also add and modify assets but have permission to do this for all assets rather than just theirs. In addition to this, they are able to delete assets where necessary. 

Registration Page:
When registering, there is validation on user input to ensure that they enter a unique username, a unique email address, a username less than 15 characters, an alphanumeric username, matching passwords, a password greater than 10 characters, a password with at least 1 number, a password with at least 1 lowercase letter, a password with at least 1 uppercase letter and a password with at least 1 special character (@, #, $ or !).

Login Page:
The login page allows users to sign in, or redirect to registering an account or accessing the admin portal. 
When the username and password is entered, this is authenticated against the database and if there is a match then the page will redirect to show all assets.
Otherwise an error message will show stating invalid credentials have been entered.

All Assets Page:
After users have successfully logged in or have added new assets, they are redirected to the all assets page. This page shows a table of assets with an edit buton for each row. The assets shown can vary based on whether the user logged in a standard user or an admin user. 
If a standard user, the table will show all assets logged by this user.
If an admin user, the table will show all assets logged by every user with a column showing the username of the user that added the asset. There is also a delete button for each row so that asset entries can be permanently removed from the database table. 

Add Asset Page:
There is an add asset button on the All Assets page which redirects to the add asset form. This captures all asset fields with some fields set as mandatory for completion and others as not. Once the mandatory fields are completed, the user can click the "save asset" button to save this to the database. Alternatively, this progress can be scrapped and the user can return to the All Assets page by clicking on the "view all assets" button.

Edit Asset Page:
When the edit button is clicked for an asset on the All Assets page, this will show a similar form to the Add Asset page with the existing asset data prepopulated. This data can then be amended as required and clicking the "update" button will save the changes. Alternatively, this progress can be scrapped and the user can return to the All Assets page by clicking on the "view all assets" button.






