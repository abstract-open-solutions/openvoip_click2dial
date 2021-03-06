# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Abstract
#    (<http://abstrat.it).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
from openerp.osv import fields, osv


# Specific paremeters for each user
class res_users(osv.osv):
    _name = "res.users"
    _inherit = "res.users"

    _columns = {
        # formerly id_call_gr
        "voip_id_call_gr": fields.char('Call Group Id', size=6),
        # formerly internal_number
        "voip_user_number": fields.char('Voip user number', size=15),
        # formerly secret_key_password
        "voip_password": fields.char('Voip user password', size=64),
    }
