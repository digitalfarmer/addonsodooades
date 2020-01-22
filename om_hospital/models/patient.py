from odoo import  models, fields,api , _

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Partient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Photo')
    name = fields.Char(string='Test')
    # sequence fields
    name_seq = fields.Char(string='Patient ID',reuired=True, copy=False, readonly=True,
                           index=True, default=lambda self: _("New"))
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female'),
        ('trans', 'Transgender')
    ],default='male',string='Gender')
    # sequence label
    @api.model
    def create(self, vals):
        if vals.get('name_seq',_('New')) == _('New'):
            vals['name_seq']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result