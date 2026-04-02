from odoo import fields, models


class HrEmployeeChild(models.Model):
    _name = "hr.employee.child"
    _description = "Employee Child"

    employee_id = fields.Many2one("hr.employee", required=True, ondelete="cascade")
    name = fields.Char(string="Child Name", required=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        string="Gender",
    )


class HrEmployeeChildEducation(models.Model):
    _name = "hr.employee.child.education"
    _description = "Employee Child Education"

    employee_id = fields.Many2one("hr.employee", required=True, ondelete="cascade")
    name = fields.Char(string="Child Name", required=True)
    class_name = fields.Char(string="Class")
    school_name = fields.Char(string="School Name")


class HrEmployeeEmergencyContact(models.Model):
    _name = "hr.employee.emergency.contact"
    _description = "Employee Emergency Contact"

    employee_id = fields.Many2one("hr.employee", required=True, ondelete="cascade")
    name = fields.Char(string="Name", required=True)
    relationship = fields.Char(string="Relationship")
    phone = fields.Char(string="Phone")


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

    resume_file = fields.Binary(string="CV / Resume", attachment=True, groups="hr.group_hr_user")
    resume_filename = fields.Char(string="CV / Resume Filename")
    appointment_letter_file = fields.Binary(string="Appointment Letter", attachment=True, groups="hr.group_hr_user")
    appointment_letter_filename = fields.Char(string="Appointment Letter Filename")
    contract_agreement_file = fields.Binary(string="Contract Agreement", attachment=True, groups="hr.group_hr_user")
    contract_agreement_filename = fields.Char(string="Contract Agreement Filename")
    id_card_filename = fields.Char(string="NID Filename")
    passport_copy_file = fields.Binary(string="Passport Copy", attachment=True, groups="hr.group_hr_user")
    passport_copy_filename = fields.Char(string="Passport Copy Filename")
    academic_certificates_file = fields.Binary(string="Academic Certificates", attachment=True, groups="hr.group_hr_user")
    academic_certificates_filename = fields.Char(string="Academic Certificates Filename")
    photograph_file = fields.Binary(string="Photograph", attachment=True, groups="hr.group_hr_user")
    photograph_filename = fields.Char(string="Photograph Filename")
    driving_license_filename = fields.Char(string="Driving License Filename")
    others_certificate_file = fields.Binary(string="Others Certificate", attachment=True, groups="hr.group_hr_user")
    others_certificate_filename = fields.Char(string="Others Certificate Filename")

    spouse_occupation = fields.Char(string="Spouse Occupation (optional)", help="Enter the occupation of the partner's spouse")

    total_dependents = fields.Integer(string="Total Dependents (number)", default=0,
                                      help="Number of people dependent on this person")
    child_line_ids = fields.One2many("hr.employee.child", "employee_id", string="Name of the Children (With Gender)")
    child_education_line_ids = fields.One2many(
        "hr.employee.child.education",
        "employee_id",
        string="Education of Children (With Class and School Name)",
    )
    emergency_contact_line_ids = fields.One2many(
        "hr.employee.emergency.contact",
        "employee_id",
        string="Emergency Contact (Name, Relationship, Phone)",
    )
