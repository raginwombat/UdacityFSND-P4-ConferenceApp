App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool


## Problem Set
-[Task 1][3]
- [Session Forms][4]
1. Session duration has been stored as start and end time to allow non standard session lengths. Duration can be computed from start and end time
1. Speakers has been stored as a repeated value in the model to support multiple speakers and panel members being stored for sessions. 
1. Type of Session stores the string value for the session types. While there are no specific set values restrictions are set in the API usage.
1. The conference the session  belongs to is set as an ancestor rather than being explicitly stored in a a property of the session entity. This is to leverage the ancestor attribute of Datastore and, presumably, any efficiencies in the queries.
1. Wishlist is stored as a key list proptery in the profile entity. This reduces the complexity with adding and removing saved sessions.
1. Start/End dates, seats available, max attendes are to handle cases of large multi-day conferences and sessions.
1. Speakers are just stored as a repeated property in the Session. This simplifies the entity relationships for Sessions, speakers and conferences.



##Describe 2 new types of queries
-[Task 3][3]

1. Get Session before a certain time - This endpoint allows the user to search for before before a certain time
1. Get Session after a certain time - This endpoint allows the user to search for session before a certain time

Solve query problem:
2. Problem:
Solve the following query related problem: Let’s say that you don't like workshops and you don't like sessions after 7 pm. How would you handle a query for all non-workshop sessions before 7 pm? What is the problem for implementing this query? What ways to solve it did you think of?

2. Solution:
If one wanted to find all of the sessions before a certain time an approach would be to first run a query to filter the returned sessions by  sessionType != workshop, this will give you a list of all of the non workshop sessions. Next another query can be run where the startTime < 7pm. By comparing the list of sessions returned by both queries you can find the sessions that are in both, this will be the union of the two sessions and be teh solution to the problem.

This approach is necessary because you can only run a query on 1 property using inequality comparisions per query. This problem requires ineqaulity filters being run on 2 seperate proeprties.

## Submission 2 edits
-[Submission Notes][3]
1. Sessions refactored to only allow conference creator to create and or edit session
2. _createSessionObject valid conference check chagned from a None type check to a try except block
3. 