### Overall:

**Responsiveness-**

 - **Planning:**This project was required to be totally responsive, and mobile friendly as it would be intended to be used on the fly. hence the choice of the Foundry theme relying heavily on BootStrap as my main framework for it's cut down components that result in a clean, uncluttered view, with access to all features through hidden buttons and menus. Testing was done using dev-tools during the entire project, and also a final test of the entire site after completion.
 - **Testing:** Testing throughout the project was relatively simple using the Foundry/Bootstrap class modifiers.
 - **Result:** A clean, responsive site, that works as expected. With no stray elements, or unwanted spacings.
 - **Verdict:** Test passed as expected and the site is responsive.

**Design**
 - **Planning:** Overal design had to be contrasting, to make specific elements jump out at the user. A template called Foundry was used to achieve this.
 - **Testing:** A specific template from the pack was chosen. All version were shown to testers, and notes taken on favourites.
 - **Result:** The overall theme of the site worked, and all tester were happy with the layout and design.
 - **Verdict:** Test passed, and overall design of the site works well together.

**HTML Code**
 - **Planning:** HTML Code would need to be checked on a regular basis to ensure it is up to the standard for HTML code.
 - **Testing:** Code was regularly run through the HTML Validator application provided by W3.
 - **Result:** Code passed with no errors meaning it is up to standard.
 - **Verdict:** Test passed, and overall code of the site is up to standard.

### Features:

**404 Handling**
 - **Planning:** A page is required for users tying incorrect URL values. 
 - **Testing:** The page is created, and django handles all 404 requests and redirects to the 404 template. All attempts to access invalid URLS returns the 404 page.
 - **Result:** Any attempt to access an incorrect URL redirects to the 404 page.
 - **Verdict:** Test passed as expected and delete button is now operational.

**Search**
 - **Planning:** A search feature would be needed for users to search for specific photos.
 - **Testing (Phase 1):** Search feature implimented and returns photos that contain the search query in the name, but would not search other aspects of the object. Multiple search attempts only return those items where query is contained within the name of the item.
 - **Testing (Phase 2):** Search function updated to check multiple fields. Search now checks category and tags. Searched multiple items, and items returned if query is contained in the name, category, or tags.
 - **Results:** Search function works as expected, and returns every possible result based on search criteria.
 - **Verdict:** Search function works as expected.

**Banner**
 - **Planning:** A banner required for the landing page of the site.  
 - **Testing (Phase 1):** Banner displayed as expected, but was static. A new function was required for the site admin to have the ability to change to banner.
 - **Testing (Phase 2):** Function added to change banner. Banner did not load when multiple banners were selected.
 - **Testing (Phase 3):** For loop changed to only accept the final image in a loop.
 - **Results:** Banner now functions as expected even with multiple files selected, and admin can change as needed.
 - **Verdict:** Banner displays and works as expected.

**Landing Gallery**
 - **Planning:** A small gallery is required to display a small choice selection of the photographers work, to showcase the best of the collection.
 - **Testing (Phase 1):** The gallery animates as expected, but images are static and unchangeable.
 - **Testing (Phase 2):** After adding a featured button to uploads, the admin can now check what photos they wish to be displayed.
 - **Results:** Admin is able to select and display photos based on preference, and gallery animates nicely in line with the rest of the site.
 - **Verdict:** Landing Gallery works as expected.

**Login**
 - **Planning:** A simple login system is required for users to login and pay for items.
 - **Testing:** Utilising the inbuilg Django auth module, a simple login system was created using either the username or email of the user. Logged user in, and accessed user only pages where login is required. Inputting invalid credentials returned an error message. Correct login details returned a success message and redirect to the index page.
 - **Results:** Users are able to log in as expected. Login returns a message based on error or success, and feeds back to the user on the relevant page.
 - **Verdict:** Login system works as expected.

**Logout**
 - **Planning:** A logout function for users who are logged in, and wish to log back out.
 - **Testing:** User logged out and tried to access user only pages. Bounced back to login page whenever tried without logging in.
 - **Results:** Funtion works as expected.
 - **Verdict:** Logout works as expected.

**Register**
 - **Planning:** A simple register function is required to obtain the minimum details to create an account.
 - **Testing:** A register function is created using the django auth module is created and tested. All works, and minimal details are sent to the user table. In the event of any issues, a message is sent back to the form to show that there was an error in submission.
 - **Results:** Register form works as expected with optimal results.
 - **Verdict:** Registration form works as expected.

 **Cart**
 - **Planning:** A preview image was needed to display that the user has items in the cart, and preview the first few of that list.
 - **Testing (Phase 1):** The cart button on hover previews all items in the cart. If more than a few items are in the cart, the preview can spread past the page and make the body longer.
 - **Testing (Phase 2):** A loop was added to only display the first 3 items in the cart, and display a message of how many more there are in the cart. 
 - **Results:** Cart preview shows only 3 items, and calculates the remaining items to let the user know how many more they have to view.
 - **Verdict:** Cart preview works as expected.

**Portfolio Gallery**
 - **Planning:** A basica gallery to show the user all that is available for them to buy, but also show the photographers complete works.
 - **Testing (Phase 1):** Gallery displays all images, but just images. Filtering is needed.
 - **Testing (Phase 2):** Added filter to the top of the page, which generates based on what categories are in the selection. Filters work by effectively displaying only the affected categories. 
 - **Results:** Filter works effectively without affecting the size of the page, and removing the need for redirecting to apply a filter.
 - **Verdict:** Gallery displays as expected, and effectively.

**Photo Details**
 - **Planning:** A page for displaying all relevant information about a photo. 
 - **Testing (Phase 1):** Initial test shows the only the basic information was being displayed, and users wished to know the dimensions of the image they were purchasing.
 - **Testing (Phase 2):** Added dimensions and ID number as SKU. Users requested being able to inspect the image in full size. Preview needs to be added.
 - **Testing (Phase 3):** Added lightbox to the image preview. Image can now be seen in full detail, with a watermark.
 - **Results:** Photo details page shows effectively all the photo has to offer.
 - **Verdict:** Phot details page works as expected.

 **Cart Page**
 - **Planning:** A simple page to show all the items in a users cart.
 - **Testing (Phase 1):** Page shows all items that are in the cart, but is very cluttered. Will move to a table instead of a gallery to show the cart.
 - **Testing (Phase 2):** Page now displays as a table with small thumbnails. Added small button to remove from cart if needed and redirect.
 - **Testing (Phase 3):** Found that users can checkout with no items. Checkout redirect needs to be added in checkout phase. Added warning message if no items are in the cart. Found users can add photo multiple times.
 - **Testing (Phase 4):** Added a condition to check cart before adding items. Users can no longer add a photo multiple times.
 - **Results:** Cart effectively shows the relevant information, and prevents the user from doing unexpected actions such as add a single item multiple times.
 - **Verdict:** Cart works effectively and prevents user actions as expected.

 **Checkout Page**
 - **Planning:** Checkout page required to take user billing details, along with credit card details. 
 - **Testing (Phase 1):** Basic stripe functionality set up. Users cannot process payments as the form is not recieving the stripe ID.
 - **Testing (Phase 2):** ID setup incorrectly in JS. Form is now detected. Discovered users can try and and process payments of €0, resulting in a failed payment. Adding check on cart before allowing users into checkout page.
 - **Testing (Phase 3):** Users can no longer enter an empty cart, and are required to input something into the cart first. Decision made to add automated delivery of items.
 - **Testing (Phase 4):** Users can now submit orders, and automatic delivery via sendgrid of items in cart is then emailed to user.
 - **Results:** Checkout page now works as expected after multiple changes. Payments are processed for the correct amounts dependant on cart. Also deliverys purchased items to the user automatically.
 - **Verdict:** Checkout page works as expected.

 **Profile Page**
 - **Planning:** A page needed to view all purchased items that the user has ordered. 
 - **Testing (Phase 1):** Page renders the same gallery as the portfolio page, but found to be repetitive. Adjustments to display needed.
 - **Testing (Phase 2):** Page now renders a table of what the user has purchased. Discovered that if user has accidentally deleted email from purchase, then they lose the photo. Correction to this to be made on the profile page.
 - **Testing (Phase 3):** Adjusted thumbnails to link to an unwatermarked version of the photo for their own use. Link currently opens as normal link. Adding _blank target to open in new page.
 - **Testing (Phase 4):** Page found to render slowly due to checking EVERY order line in the db. Changed the object function from all to get a query set matching the current logged in username. Increase noticed on render times.
 - **Results:** Profile page displays correctly, and all links open in new tab, prevent users navigating away from the page they are on.
 - **Verdict:** Profile page works effectively, and display correctly.