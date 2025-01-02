from odoo import api, models, fields
from odoo.exceptions import UserError

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    course = fields.Many2one('student.course', string='Course')
    active = fields.Boolean(string='Active', default=True)

    def action_confirm_create(self):
        """
        This method will be executed when the 'Confirm' button is clicked.
        Add your custom logic here.
        """
        for record in self:
            # Example: Mark the student as active and log a message
            record.active = True
            message = f"Student '{record.name}' has been confirmed successfully."
            # You can also add a notification to the UI
            record.message_post(body=message)

class Course(models.Model):
    _name = 'student.course'
    _description = 'Student Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')