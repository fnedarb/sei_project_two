# wayfarer - travel site and event finder

### context:<br />
this is a weeklong group project intended to showcase 
* the creation of a django application 
* full implementation of ground-up responsive web design
* successful planning of model relationships in an ERD diagram
* full user authentication with permissions
* full CRUD for Posts attached to Cities
* admin-side creation of Events that users can research and attend
* successful project execution in a group using github and jira


### concept: <br />


### process: <br />
* our process began with consesnsus on the axios-inspired concept, followed by basic wireframing and user story creation in figma, and the drafting of an ERD <br />
![figma](https://i.ibb.co/dK6vkxc/Screen-Shot-2021-10-14-at-2-32-52-PM.png)
* we divided work by creating a backlog of epics and stories in jira. we then started a mini-sprint to execute our assigned tickets <br />
![jira](https://i.ibb.co/rpwBWXp/Screen-Shot-2021-10-12-at-11-33-21-AM.png)

### user steps:<br />
* anyone can view the homepage to see/search all posted articles along with a quick summary of each story <br />
![homepage](https://i.ibb.co/TqCPJp6/Screen-Shot-2021-10-14-at-2-59-27-PM.png)
* in order to view the full text, like, comment on, edit, or delete articles, the user must create an account or log in
* during account creation, the user is asked to provide a name, email, and password, as well as select a "reader" or "writer" account type <br />
![account creation](https://i.ibb.co/dB5DTkt/Screen-Shot-2021-10-14-at-2-56-52-PM.png)
* upon login, writers can access full functionality as outlined above, and they may only edit and delete articles they themselves have written <br />
![account creation](https://i.ibb.co/pJ6nBFh/Screen-Shot-2021-10-14-at-3-01-25-PM.png)
* reader accounts may only read, like, and comment on existing articles - they cannot post, edit or delete articles

### code: <br />
* zashlios is a MEN application 
* the app uses 3 connected db models: Article, Comment, and User
* methods used: node, express, RESTful routes, templating with ejs, MongoDB/mongoose, git, flexbox, sass, bootstrap, heroku, method-override, & authentication with express-session and bcrypt

### future features: <br/>
* user dashboards: pages all users can view a list of any article they've written or liked - they should be able to view other writers' pages as well
* full site searchability and article filtering
* further authentication for those applying to have writer accounts
* comment liking and flagging