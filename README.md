# django_project_upload
To try django_project_uploader go step by step through this tutorial.
1. Change to your directory
mkdir test
cd test
2. Clone git repository
git clone https://github.com/lazaa32/django_project_upload.git
3. Change to glwp_up directory
cd django_project_upload/glwp_up/
4. Create database
python manage.py migrate
5. Create admin user
python manage.py createsuperuser
6. Run server
python manage.py runserver
7. Go to localhost:8080/uploader/. If everything is OK you shold see "GISlab.web projects uploader works!"
8. Go to localhost:8080/uploader/upload to upload project
9. Go to localhost:8080/uploader/projects to see a list of uploaded projects
10. Go to localhost:8080/admin to enter admin site.
