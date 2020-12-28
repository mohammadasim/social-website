# social-website
A django application to be used as a social website for sharing books amongst users.
This site was developed to do a POC for social authentication using the package `python-social-auth`
## How to install `python-social-auth`
To install and setup follow the below steps:
* Install the package using the command `pip install social-auth-app-django==3.1.0`
* Add `social_django` to the list of `INSTALLED_APPS` in your `settings.py` file.
* Run the command `python manage.py migrate`
* Add to your main `url.py` `path('social-auth/', include('social_django.urls', namespace='social'))`
<p>
Several social service will not allow redirecting to <code>127.0.0.1</code> or <code>localhost</code> after a successful
authentication; they expect a domain name. In order to make social authentication work, we will need a domain. To fix 
this problem on Linux or macOS, edit <code>/etc/hosts</code> file and add this line <code>127.0.0.1 mysite.com</code>
</p>
<p>
To verify that your hostname association worked, start the development server with <code>python manage.py runserver</code>
and open <code>http://mysite.com:8000</code> in your browser. Ensure that you have updated your <code>ALLOWED_HOSTS</code>
and looks like <code>ALLOWED_HOST = [''mysite.com', 'localhost', '127.0.0.1']</code>
</p>

## Running the development server through HTTPS
<p>
Some of the social authentication methods require an HTTPS connection. The Django development server is not able
to server our site through HTTPS, since it is not intended for such usage. In order to test the social authentication
functionality serving our site through HTTPS, we are going to user the <code>RunServerPlus</code> extension of the package
<code>Django Extensions</code>. This is a third party collection of custom extensions for Django. Please note this is 
not the way to server a django app in production.
</p>

### Setting up Django Extensions
* Install the package using the command `pip install django-extension=2.2.5`
* We will also need to install Werkzeug, which contain a debugger layer required by the RunServerPlus extension.
* `pip install werkzeug==0.16.0`
* Finally we need to install `pyOpenSSL` which is required to use the TLS functionality of RunServerPlus.
* `pip install pyOpenSSL==10.0.0`
* Add `django-extensions` to your `INSTALLED_APPS` in `settings.py`.
* Use the management command `runserver_plus` provided by Django Extensions to run the development server as follows:
* `python manage.py runserver_plus --cert-file cert.crt`
* You provide a file name to the `runserver_plus` command for the TLS certificate. Django Extensions will generate
a key and certificate automatically.
