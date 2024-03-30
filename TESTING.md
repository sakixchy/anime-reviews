## Feature Testing

### Navigation
The navigation is responsive and switches to a burger menu icon on smaller screen sizes.

| Feature            | Description                                                                                   | Expected Outcome                                                        | Pass/Fail |
|--------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------|
| **Home Icon Link** | The home icon link redirects users to the home page.                                         | Users are redirected to the home page when clicking the home icon.    | Pass      |
| **Home Link**      | Clicking the home link redirects users to the home page.                                      | Users are redirected to the home page when clicking the home link.    | Pass      |
| **Signup**         | Clicking the Signup link directs users to the Signup form.                                     | Successful signup redirects users to the home page.                   | Pass      |
| **Login**          | Clicking the login link directs users to the Login form.                                       | Successful login redirects users to the home page.                   | Pass      |
| **Create Reviews** | While authenticated, clicking the create review link directs user to Create Review form.       | Users are directed to the create review form.                         | Pass      |
| **My Reviews**     | While authenticated, clicking the My Reviews link directs users to a page displaying their own reviews. | Users can see a list of their own reviews on the My Reviews page. | Pass      |
| **Logout**         | While logged in, clicking the logout link ends the user session and redirects to the home page. | User session ends and they are redirected to the home page.         | Pass      |

### Filter Button
| Feature           | Description                                                | Expected Outcome                                                            | Pass/Fail |
|-------------------|------------------------------------------------------------|-----------------------------------------------------------------------------|-----------|
| **Filter Button** | A Filter button on the home page for sorting options.      | Clicking the filter button displays options to sort by latest, oldest, A-Z, and Z-A. | Pass      |

### CRUD
The testing is applicable only for authenticated users.

### Create 
| Feature         | Description                                                                        | Expected Outcome                                                          | Pass/Fail |
|-----------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-----------|
| **Create Review** | Ensure all required fields (title, content, rating, and image) are filled before submitting. | Users are unable to submit the form if any of the required fields are empty. | Pass     |
| **Submit Button** | Clicking the submit button after filling the form triggers the form submission.    | Upon successful submission, a message confirming successfully submitted is displayed. | Pass      |

### Read
| Feature          | Description                                                              | Expected Outcome                                                                  | Pass/Fail |
|------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------|
| **Read Review**  | Ensure that users can view a selected review from "My Reviews" and see associated comments. | Users can select a review from "My Reviews" and view it along with associated comments. | Pass      |

### Update
| Feature                 | Description                                                                                             | Expected Outcome                                                                    | Pass/Fail |
|-------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-----------|
| **Edit Review**         | Users can click the edit button to modify an existing review.                                           | Clicking the edit button allows users to make changes to the review content.        | Pass      |
| **Save Changes Button** | Users can save the modifications made to the review using the "Save Changes" button.                    | Clicking the "Save Changes" button saves the changes made to the review.            | Pass      |
| **Confirmation Message**| Upon successfully saving changes, a confirmation message is displayed to the user.                      | After saving changes, users receive a confirmation message confirming the update.   | Pass      |

### Delete 
| Feature                      | Description                                                                                     | Expected Outcome                                                                                           | Pass/Fail |
|------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------|
| **Delete Review**            | Users can delete an existing review.                                                            | Clicking the delete button prompts a confirmation modal to confirm deletion.                               | Pass      |
| **Confirmation Modal**       | A confirmation modal is displayed when attempting to delete a review.                           | The confirmation modal includes options to proceed with deletion or cancel the action.                     | Pass      |
| **Back Button (Modal)**      | Within the confirmation modal, users can navigate back to the review without deleting it.       | Clicking the back button redirects users to the review page without deleting the review.                   | Pass      |
| **Delete Button (2nd Time)** | After confirming deletion, users are presented with a delete button again to confirm deletion.  | Clicking the delete button a second time within the modal triggers the deletion of the review.             | Pass      |
| **Confirmation Message**     | Upon successfully deleting the review, a confirmation message is displayed to the user.         | After deletion, users receive a confirmation message confirming the deletion of the review.                | Pass      |

### Commenting
| Feature                      | Description                                                                                          | Expected Outcome                                                                                                                     | Pass/Fail |
|------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Commenting on Reviews**    | Users can post comments on reviews.                                                                  | After entering a comment in the comment field, the placeholder text disappears.                                                      | Pass      |
| **Placeholder Text**         | The comment field has placeholder text indicating where users should enter their comments.           | When the comment field is empty, the placeholder text is displayed.                                                                  | Pass      |
| **Comment Post Button**      | Users can click the "Post Comment" button to submit their comment.                                   | Clicking the "Post Comment" button submits the comment for posting.                                                                  | Pass      |
| **Confirmation Message**     | After posting a comment, a confirmation message is displayed to the user.                            | Upon successful posting of a comment, a confirmation message appears indicating the comment was posted.                              | Pass      |

### Liking / Disliking Reviews
| Feature                      | Description                                                                                          | Expected Outcome                                                                                                                     | Pass/Fail |
|------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Liking/Disliking Reviews** | Users can like or dislike reviews by clicking the respective buttons.                                | Clicking the like or dislike button updates the button to reflect the user's choice by incrementing the count by one.                | Pass      |
| **Confirmation Message**     | After liking or disliking a review, a confirmation message is displayed to the user.                 | Upon successful liking or disliking of a review, a confirmation message appears indicating the action was completed.                 | Pass      |
| **Update Various Places**    | Various places such as (home, review detail and my reviews) reflect the updated like and dislike counts.   | After liking or disliking a review, the like and dislike counts are updated in the respective locations where they are displayed.    | Pass      |

### Sign Up
| Feature                   | Description                                                                                                        | Expected Outcome                                                                                                                              | Pass/Fail |
|---------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Sign-Up Form**          | Users can fill out the sign-up form with their username, password, and confirmation password.                      | Users are able to enter their desired username and password, along with confirming their password.                                            | Pass      |
| **Password Requirements** | Passwords must meet specified criteria, including being at least 8 characters long and not entirely numeric.       | Users receive prompts if their password is too short, too similar to personal information, entirely numeric.                                  | Pass      |
| **Sign-Up Button**        | Users can click the "Sign Up" button to submit their sign-up information.                                          | Clicking the "Sign Up" button submits the sign-up form with the provided information for account creation.                                    | Pass      |
| **Confirmation Message**  | After successfully signing up, a confirmation message is displayed to the user.                                    | Upon successful sign-up, users receive a confirmation message indicating that they have logged in sucessfully.                                | Pass      |

### Login
| Feature                     | Description                                                                                          | Expected Outcome                                                                                               | Pass/Fail |
|-----------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------|
| **Username Field**          | Users can enter their desired username.                                                              | The username field accepts input from the user.                                                                | Pass      |
| **Password Field**          | Users can enter their desired password.                                                              | The password field accepts input from the user.                                                                | Pass      |
| **Username Placeholder**    | The username field displays a placeholder text to indicate where users should enter their username.  | The placeholder text is visible in the username field until the user starts typing their username.             | Pass      |
| **Password Placeholder**    | The password field displays a placeholder text to indicate where users should enter their password.  | The placeholder text is visible in the password field until the user starts typing their password.             | Pass      |
| **Remember Me Option** | Users have the option to select "Remember Me" to stay logged in on subsequent visits.                     | Users can choose to enable or disable the "Remember Me" option to stay logged in.                              | Pass      |
| **Forgot Password Link** | Users have the option to reset their password via a "Forgot Password?" link.                            | Clicking the "Forgot Password?" link redirects users to a password reset page.                                 | Pass      |
| **Login Form**         | Registered users can log in with their username and password.                                             | Users are unable to login if the fields are empty or not field entirely upon pressing log in.                  | Pass      |
| **Confirmation Message (Login)**       | After successfully logging in, a confirmation message is displayed to the user.           | Upon successful login, users receive a confirmation message indicating that they have successfully logged in.  | Pass      |

### Logout
| Feature                   | Description                                                                                           | Expected Outcome                                                                                                      | Pass/Fail |
|---------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| **Logout Button**         | Users can click the "Logout" button to log out of their account.                                       | Clicking the "Logout" button triggers the logout process, ending the user session and redirecting to the home page.  | Pass      |