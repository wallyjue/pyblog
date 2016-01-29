pyblog
======

A simple blog written in django

    $git clone https://github.com/wallyjue/pyblog.git
    $cd pyblog
    $source bin/activate
    $cd sites
    $python runserver

launch your browser and visit http://localhost:8000
admin page at http://localhost:8000/admin

functions implemented:
----------------------
0. view post/blog
0a. private setting: if a blog is set to private, only author can visit that blog
0b. filter post with category/tag

1. create post
1a. create post with attachment file (video and images)
1b. create tags when creating a post
1c. add category to post

2. edit post
2a. edit title,content,category,tags of a post

3. delete post

accounts created for demo:
--------------------------
username: public
password: pythonjp

username: private
password: pythonjp

admin page username: admin
admin page password: password12345
