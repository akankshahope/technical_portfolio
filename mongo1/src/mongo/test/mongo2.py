import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import smtplib

from tornado.options import define, options

define("port", default=9967, help="run on the given port", type=int)
class PortfolioHandler(tornado.web.RequestHandler):
    def get(self):
            self.render('Portfolio.html',title="Technical details")
                       
class ApplicationsHandler(tornado.web.RequestHandler):
    def post(self):
        con=pymongo.Connection("localhost",27017)
        db=con.technical_data
        db.collection_names()
        value = db.value  
             
        name = self.get_argument('n1')
        eid = self.get_argument('e1')
        num = self.get_argument('num1')
        dob = self.get_argument('dob1')
        gender= self.get_argument('gender1')
        exp= self.get_argument('exp1')
        quali= self.get_argument('quali1')
        ks= self.get_argument('ks1')
        adres = self.get_argument('a1')
        mstatus=self.get_argument('ms1')
        project=self.get_argument('project1')
        perc=self.get_argument('perc1')
        
        
        value.insert({"name": self.get_argument('n1'),"eid":self.get_argument('e1'),
                        "dob": self.get_argument('dob1'),"gender": self.get_argument('gender1'),
                        "num": self.get_argument('num1'),"mstatus": self.get_argument('ms1'),
                        "adres": self.get_argument('a1'),"exp": self.get_argument('exp1'),
                        "quali": self.get_argument('quali1'),"ks": self.get_argument('ks1'),
                        "project": self.get_argument('project1'),"perc": self.get_argument('perc1')})
        
        for doc in value.find():
            print(doc) 
            db.value.save(doc)
           
               
        self.render('Result.html', name1=name, eid1=eid,num1=num,dob2=dob,gender2=gender,mstatus1=mstatus,adres1=adres,exp2=exp,quali2=quali,perc2=perc,ks2=ks,project2=project)
        
        to = self.get_argument('e1')
        user = 'user@gmail.com'
        pwd = 'gmail password'
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(user, pwd)
        header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:Registration\n'
        print header
        msg = header + '\nYou are successfully registered\n\n'
        smtpserver.sendmail(user, to, msg)
        print 'done!'
        smtpserver.close()
        
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
                                  debug=True ,
                                  handlers=[(r'/',PortfolioHandler), (r'/Result',ApplicationsHandler)],template_path=os.path.join(os.path.dirname(__file__), 'mongo1/'.replace('\\','/'),)
                                  )
   
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    