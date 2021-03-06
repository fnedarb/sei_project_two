# wayfarer - travel site and event finder

### context:<br />
this is a weeklong group project intended to showcase:
* the creation of a django application with a postgresSQL database
* full implementation of ground-up responsive web design
* successful planning of model relationships in an ERD diagram
* use of bootstrap5 for styling
* full user authentication with permissions
* full CRUD for Posts attached to Cities
* admin-side creation of Events that users can research and attend
* successful project execution in a group using github and jira


### concept: <br />
the group was given a list of client requirements to execute. these included:
* a travel site called Wayfarer that displayed cities of interest and posts attached to cities from authentiicated users
* sign in/up process
* full CRUD functionality on posts a user has made with authorization limited to the user's own posts
* ability for users to edit profile information<br />
we also added:
* a home page displaying top cities and events
* index pages for all cities and all events on the site
* search functionality by country, state, and city
<br />
in addition, we added the concept of "Events" going on in each city that our site's users can learn about. they can say they are attending and see a guest list. Events are admin generated.



### process: <br />
* our process began by discussing the overall concept and requirements, followed by basic wireframing and user story creation in figma and the drafting of an ERD to plan our models and relationships <br />
![figma](https://i.ibb.co/x2nwzVs/Screen-Shot-2021-11-04-at-3-36-32-PM.png)<br />
![ERD](https://i.ibb.co/PW1K3pQ/Screen-Shot-2021-11-04-at-3-38-38-PM.png)
* we divided work by creating a backlog of stories in jira. we then started a mini-sprint to execute our assigned tickets <br />
![jira](https://i.ibb.co/GvzJMY5/Screen-Shot-2021-11-04-at-3-40-18-PM.png)

### user stories:<br />
* users land on a homepage where they can see top cities and events, as well as sign up/log in <br />
![homepage](https://i.ibb.co/F0X1zkc/Screen-Shot-2021-11-04-at-7-09-23-PM.png)
* in order to add posts or attend events, the user must create an account or log in <br />
![account creation](https://i.ibb.co/p2x65tN/Screen-Shot-2021-11-04-at-7-15-15-PM.png)
* on city pages, users can see upcoming events and read recommendations posted by other users <br />
![city page](https://i.ibb.co/Vvt7sMb/Screen-Shot-2021-11-04-at-7-11-47-PM.png)<br />
![city page posts](https://i.ibb.co/gd8Rwwb/Screen-Shot-2021-11-04-at-7-12-14-PM.png)
* on event pages, users can learn more about events, mark themselves as attending, and see the current guest list <br />
![event page](https://i.ibb.co/F68zwhL/Screen-Shot-2021-11-04-at-7-10-49-PM.png)<br />
![event page guests](https://i.ibb.co/pPh0pNz/Screen-Shot-2021-11-04-at-7-11-03-PM.png)
* users can see events they're attending and any posts they've made on their profile pages ??? they can also edit or delete their own posts, or view other user profiles without edit/delete permissions <br />
![profile](https://i.ibb.co/1KCL2n1/Screen-Shot-2021-11-04-at-7-11-35-PM.png)<br />
![edit post](https://i.ibb.co/jg7Gywf/Screen-Shot-2021-11-04-at-7-12-37-PM.png)
* users can also browse a page of all featured cities <br />
![all cities](https://i.ibb.co/Qd3PM3q/Screen-Shot-2021-11-04-at-7-09-47-PM.png)
* finally, we've provided a quick look index of all events categorized by city <br />
![all events](https://i.ibb.co/GtxVV9h/Screen-Shot-2021-11-04-at-7-10-11-PM.png)<br />

### code: <br />
* wayfarer is a django app
* our database is postgresSQL
* the app uses 4 db models: User, Event, City, and Post
* methods used: django, python, html, css, bootstrap, postgresSQL