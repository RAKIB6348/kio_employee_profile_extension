from odoo import api, fields, models


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


class HrEmployeeQualification(models.Model):
    _name = "hr.employee.qualification"
    _description = "Employee Qualification"

    employee_id = fields.Many2one("hr.employee", required=True, ondelete="cascade")
    highest_education_level = fields.Char(string="Highest Education Level")
    degree_certificate_name = fields.Char(string="Degree / Certificate Name")
    institution_name = fields.Char(string="Institution Name")
    passing_year = fields.Char(string="Passing Year")
    major_subject = fields.Char(string="Major / Subject")
    professional_training = fields.Selection(
        [("yes", "Yes"), ("no", "No")],
        string="Professional Training",
    )
    training_details = fields.Char(string="Training Details")


class HrEmployeePreviousPosition(models.Model):
    _name = "hr.employee.previous.position"
    _description = "Employee Previous Position"

    employee_id = fields.Many2one("hr.employee", required=True, ondelete="cascade")
    name = fields.Char(string="Position", required=True)
    company = fields.Char(string="Company")
    from_date = fields.Date(string="From")
    to_date = fields.Date(string="To")




class HrEmployee(models.Model):
    _inherit = "hr.employee"

    staff_id = fields.Char(string="Staff ID")
    full_name = fields.Char(string="Full Name")
    mother_name = fields.Char(string="Mother's Name")
    father_name = fields.Char(string="Father's Name")

    emergency_contact_relationship = fields.Char(string="Emergency Contact Relationship")
    date_of_joining = fields.Datetime(string="Date of Joining")
    employment_status = fields.Selection(
        [
            ("active", "Active"),
            ("on_leave", "On Leave"),
            ("resigned", "Resigned"),
            ("terminated", "Terminated"),
        ],
        string="Employment Status",
        help="Current employment status (Active / On Leave / Resigned / Terminated).",
    )
    employment_type = fields.Selection(
        [
            ("full_time", "Full-time"),
            ("part_time", "Part-time"),
            ("contract", "Contract"),
            ("volunteer", "Volunteer"),
        ],
        string="Employment Type",
        help="Employment type (Full-time / Part-time / Contract / Volunteer).",
    )
    profile_completion = fields.Float(
        string="Profile Completion %",
        compute="_compute_profile_completion",
        help="Percentage of completed employee profile fields.",
    )
    total_years_experience = fields.Float(string="Total Years of Experience")
    previous_organization_name = fields.Char(string="Previous Organization Name")
    previous_designation = fields.Char(string="Previous Designation")
    work_location = fields.Char(string="Work Location")
    previous_position = fields.One2many(
        "hr.employee.previous.position",
        "employee_id",
        string="Previous Positions",
    )
    duration_from = fields.Date(string="Duration From")
    duration_to = fields.Date(string="Duration To")
    key_responsibilities = fields.Char(string="Key Responsibilities")
    mobile_alt = fields.Char(string="Mobile Number (Alternative)")
    personal_email = fields.Char(string="Personal Email")
    mobile_primary = fields.Char(string="Mobile Primary")
    payment_mode = fields.Selection(
        [("bank", "Bank"), ("cash", "Cash"), ("mfs", "MFS")],
        string="Payment Mode (Bank / Cash / MFS)",
    )
    bank_name = fields.Char(string="Bank Name")
    account_number = fields.Char(string="Account Number")
    mobile_banking_number = fields.Char(string="Mobile Banking Number (if any)")
    salary_currency_id = fields.Many2one(
        "res.currency",
        related="company_id.currency_id",
        readonly=True,
    )
    monthly_gross_salary = fields.Monetary(
        string="Monthly Gross Salary",
        related="contract_id.wage",
        currency_field="salary_currency_id",
        readonly=True,
        groups="hr.group_hr_user",
    )

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
    qualification_line_ids = fields.One2many(
        "hr.employee.qualification",
        "employee_id",
        string="Academic & Professional Qualifications",
    )

    showcause_active = fields.Boolean(string="Showcause Active", default=False)

    def action_employee_showcause(self):
        """Mark employee as showcause"""
        for rec in self:
            rec.showcause_active = True
        return True

    def action_employee_clear_showcause(self):
        """Clear showcause from employee"""
        for rec in self:
            rec.showcause_active = False
        return True

    @api.depends(
        "name",
        "company_id",
        "job_id",
        "work_email",
        "work_phone",
        "mobile_phone",
        "job_title",
        "department_id",
        "parent_id",
        "coach_id",
        "staff_id",
        "full_name",
        "mother_name",
        "father_name",
        "date_of_joining",
        "employment_status",
        "employment_type",
        "private_email",
        "private_street",
        "private_city",
        "private_state_id",
        "private_country_id",
        "private_phone",
        "mobile_alt",
        "present_street",
        "present_street2",
        "present_city",
        "present_state_id",
        "present_zip",
        "present_country_id",
        "gender",
        "birthday",
        "marital",
        "spouse_complete_name",
        "children",
        "total_dependents",
        "visa_no",
        "permit_no",
        "payment_mode",
        "bank_name",
        "account_number",
        "mobile_banking_number",
        "identification_id",
        "passport_id",
        "resume_filename",
        "appointment_letter_filename",
        "contract_agreement_filename",
        "id_card_filename",
        "passport_copy_filename",
        "academic_certificates_filename",
        "photograph_filename",
        "driving_license_filename",
        "others_certificate_filename",
        "resume_file",
        "spouse_occupation",
        "total_years_experience",
        "previous_organization_name",
        "previous_designation",
        "work_location",
        "previous_position",
        "duration_from",
        "duration_to",
        "key_responsibilities",
    )
    def _compute_profile_completion(self):
        tracked_fields = [
            "name",
            "company_id",
            "job_id",
            "work_email",
            "work_phone",
            "mobile_phone",
            "job_title",
            "department_id",
            "parent_id",
            "coach_id",
            "staff_id",
            "full_name",
            "mother_name",
            "father_name",
            "date_of_joining",
            "employment_status",
            "employment_type",
            "private_email",
            "private_street",
            "private_city",
            "private_state_id",
            "private_country_id",
            "private_phone",
            "mobile_alt",
            "present_street",
            "present_street2",
            "present_city",
            "present_state_id",
            "present_zip",
            "present_country_id",
            "gender",
            "birthday",
            "marital",
            "spouse_complete_name",
            "children",
            "total_dependents",
            "visa_no",
            "permit_no",
            "payment_mode",
            "bank_name",
            "account_number",
            "mobile_banking_number",
            "identification_id",
            "passport_id",
            "resume_filename",
            "appointment_letter_filename",
            "contract_agreement_filename",
            "id_card_filename",
            "passport_copy_filename",
            "academic_certificates_filename",
            "photograph_filename",
            "driving_license_filename",
            "others_certificate_filename",
            "resume_file",
            "spouse_occupation",
            "total_years_experience",
            "previous_organization_name",
            "previous_designation",
            "work_location",
            "previous_position",
            "duration_from",
            "duration_to",
            "key_responsibilities",
        ]
        total = len(tracked_fields)
        for employee in self:
            completed = sum(1 for field_name in tracked_fields if employee[field_name])
            employee.profile_completion = round((completed / total) * 100, 2) if total else 0.0

    personal_email = fields.Char(string="Personal Email")
    mobile_primary = fields.Char(string="Mobile Primary")
