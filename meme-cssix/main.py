import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        the_variable_dict = {
            "greeting": "Welcome!!!", 
            "adjective": "splendid"
        }
        
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render(the_variable_dict))


class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        results_template = the_jinja_env.get_template('templates/results.html')
        the_variable_dict = {
            "line1": "Hurrah for Utsab!", 
            "line2": "Hurrah!!!!!!!!", 
            "img_url": "http://www.atozpictures.com/admin/uploads/2016/11/cute-cockatiel-wallpapers.jpg"
        }
        self.response.write(results_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/showmeme', ShowMemeHandler),
], debug=True)