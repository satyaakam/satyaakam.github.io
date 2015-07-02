title: Setting up the Dev environment and working on the Fork
link: http://satyaakam.net/?p=397
author: satya
description: 
post_id: 397
created: 2011/06/01 09:40:46
created_gmt: 2011/06/01 04:10:46
comment_status: open
post_name: setting-up-the-dev-environment-and-working-on-the-fork
status: publish
post_type: post

# Setting up the Dev environment and working on the Fork

Khanacademy.org code is lying here [Source](http://code.google.com/p/khanacademy/wiki/Source?tm=4) , the link from here will point us to the [Source Link ](https://khanacademy.kilnhg.com/Repo/Website/Group/stable) i have checked and tried getting kinhg account looks like it a paid site and we need to pay after 45 days , my initial though before visiting this site was to branch and maintain a tree there itself looks like it is not as open as it claims. So the other option is to fork since the code is anyway licensed under [ BSD2 ](http://www.opensource.org/licenses/bsd-license.php) lincense . We are going to maintain two Repos one of Khanacademy ( KA) and one of Fossacademy (FA) . why maintain KA code , because initially when we start off as FA we will have just KA code but over time it is going to differ and change in ways , but also we will have some changes upstream in KA which we will be needing from time to time to fix bugs which must have already crept in. yes it is a overhead we have to live with for the time being . coming back to the FA we will be maintaining the code on [Bitbucket](https://bitbucket.org/) , and everyone will pull from the stable FA and start maintaining the FA trunkc or fork they will be free to take the call . on maintaining the dev environment , i found any variant of [ Eclipse ](http://www.eclipse.org/downloads/) to be a good[ IDE ](http://en.wikipedia.org/wiki/Integrated_development_environment) to maintain the code , you are free to maintain any IDE/Editor you are comfortable with . this video explains it all [Setting Dev environment ](http://www.youtube.com/watch?v=qhBeXhZJMUw)using eclipse . i will be writing on the goals and specs for the project as we move along keep watching this space ...