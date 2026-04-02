from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    staff_id = fields.Char(string="Staff ID")
    full_name = fields.Char(string="Full Name")
    mother_name = fields.Char(string="Mother's Name")
    father_name = fields.Char(string="Father's Name")

    emergency_contact_relationship = fields.Char(string="Emergency Contact Relationship")
    date_of_joining = fields.Datetime(string="Date of Joining")
    mobile_alt = fields.Char(string="Mobile Number (Alternative)")

    # present address
    present_street = fields.Char(string="Street")
    present_street2 = fields.Char(string="Street2")
    present_zip = fields.Char(string="Zip")
    present_city = fields.Char(string="City")
    present_state_id = fields.Many2one(
        "res.country.state",
        string="State",
        domain="[('country_id', '=?', present_country_id)]",
    )
    present_country_id = fields.Many2one("res.country", string="Country")
