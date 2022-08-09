# Auction WebApp
___
The Auction WebApp is a web-application developed with the django framework. It displays the auctions stored in the database.
Normal Users can only view the auctions that are ongoing, the admin can view all the auctions (ongoing and complete).  

## Description
___
The Auction model consists of the following fields:  
* `auctionId` - Identification number of an auction  
* `itemName` - Name of the item put up for auction  
* `startTime` - Starting date-time of the auction  
* `endTime` - ending date-time of the auction  
* `highestBid` - The Highest amount bid on the auction  
* `highestBidder` - User ID of the user who made the highest bid  
* `isActive` - This flag is True if the auction is ongoing, False when  the auction is complete, i.e., when current time >= endTime.  

For demo purposes, one more model - user has been used. The user model consist of the following fields
* userID - An UUID for each user  
* userName - name of the user

The application has two views *"homepage"* at *""* and *"admin"* at *"auctionAdmin/"*. The *homepage* displays all the
auctions that are currently ongoing and is available to all users. The *admin* page displays all the auctions regardless 
of their status. The admin page is only available after logging in. The admin can log in with their superuser credentials. 
For authenticating logins, django's built-in *Django authentication system* has been used.

* *homepage* ![homepage](images/homapage.PNG)  
* *admin* ![adminPanel](images/admin.PNG)  

A management command **update_status** is used to update the `isActive`flag of each auction. It checks the current time 
and compares it to the `endTime` of the auction. If the difference between the two times is less than or equal to 0, it 
sets the `isActive` flag to false, marking the auction as complete

## Installation
___
1. Clone the repository  
`git clone https://github.com/BhaskarS1ngha/AuctionApp.git`  
2. install requirements  
`pip install -r requirements.txt`  
3. Create superuser (Admin)  
   `python manage.py createsuperuser`
4. start server  
`python manage.py runserver`  
5. schedule a cron job or windows task scheduler to execute the following command every minute.  
`python manage.py update_status`
   
## Miscellaneous
___
A couple of management commands are provided for feeding data into the database. The command `addUsers` adds 10 randomly generated users to
the database while the command `addauctions`feeds 50 randomly generated auctions into the database. They can be executed using:  
* To add users `python manage.py addUsers`  
* To add auctions `python manage.py addauctions`

**NOTE:** Executing `addauctions` will automatically add 10 users if no users exist in the database.