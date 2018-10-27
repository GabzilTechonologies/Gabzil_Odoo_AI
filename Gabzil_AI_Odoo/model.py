from odoo import models, fields, api
from odoo.exceptions import UserError
import requests

class gabzilAi(models.Model):
    _name = 'odoo.gabai'
    _description = 'Gabzil Odoo Module'
    file_url = fields.Char("Enter URL", size=80, default="http://cake.gabzil.com/api/valuesd")
    some_data = fields.Binary("Select File")
    my_field = fields.Text("Returned data", size=10000)

    @api.multi
    def set_data(self):
        data = {"file": self.some_data}
        try:
            myReq = requests.post(url=self.file_url, data=data)
        except:
            raise UserError("Please enter valid URL or select proper file type (PDF/ jpg).")
        self.my_field = myReq.content
        return True

    @api.multi
    def send_data(self):
        raise UserError("Hello there, to proceed further please contact Admin.")
        return True

