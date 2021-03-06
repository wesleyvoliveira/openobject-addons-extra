# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Portal Management - Service",
    "version" : "0.1",
    "author" : "Tiny",
    "website" : "http://www.openerp.com",
    "depends" : ["base", "portal","project","crm",
                 "account_analytic_analysis","hr_timesheet_invoice",
                 "scrum",],
    "category" : "Generic Modules/Others",
    "description": "Potal Management - Service company specific data.",
    "init_xml" : [],
    "update_xml" : [
                    "portal_project_view.xml",
                    "portal_project_data.xml",
                    "portal_crm_view.xml","portal_crm_data.xml",
                    "portal_scrum_view.xml","portal_scrum_data.xml",
                    "security/ir.model.access.csv"
                    ],
    "demo_xml" : [],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

