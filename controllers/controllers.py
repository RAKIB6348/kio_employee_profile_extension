# -*- coding: utf-8 -*-
# from odoo import http


# class KioEmployeeProfileExtension(http.Controller):
#     @http.route('/kio_employee_profile_extension/kio_employee_profile_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kio_employee_profile_extension/kio_employee_profile_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kio_employee_profile_extension.listing', {
#             'root': '/kio_employee_profile_extension/kio_employee_profile_extension',
#             'objects': http.request.env['kio_employee_profile_extension.kio_employee_profile_extension'].search([]),
#         })

#     @http.route('/kio_employee_profile_extension/kio_employee_profile_extension/objects/<model("kio_employee_profile_extension.kio_employee_profile_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kio_employee_profile_extension.object', {
#             'object': obj
#         })

