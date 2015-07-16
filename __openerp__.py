# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'TYPO3 Service Profile Template',
    'version': '0.1',
    'description': """
TYPO3 Service Profile Template
====================================

Template for basic Setup/Profile as a TYPO3 Service company
--------------------------------------------
Module Dependencies

This module defines a basic set of odoo apps and modules for faster deploment on new instances.

At this point the following modules will be installed:
        'account_accountant',
        'account_voucher',
        'contacts',
        'project',
        'sale',
        'sale_service',
        'calendar',
        'note',
        'project_issue',
        'hr',
        'hr_holidays',
        'hr_timesheet_sheet',
        'project_timesheet',

And brings the following data:
User:
max hellwig

    """,
    'author': 'Datenbetrieb - Max Hellwig/Peter Niederlag',
    'website': 'http://www.datenbetrieb.de',
    'category': 'Profile',
    'depends': [
        'base',
        'account_accountant',
        'account_voucher',
        'contacts',
        'project',
        'sale',
        'sale_service',
        'calendar',
        'note',
        'project_issue',
        'hr',
        'hr_holidays',
        'hr_timesheet_sheet',
        'project_timesheet',
    ],
    'data': [
      'data/users.xml',
      'data/country_state.xml',
      'data/bank_account.xml',
      'data/company.xml'
    ],
    'demo': [
    ],
    'auto_install': True,
}
