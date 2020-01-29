from odoo import  models, fields,api , _
from odoo import exceptions

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Partient Record'
    _rec_name = 'name_seq'

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age<17:
                raise ValueError(_('Usia Minimal 17 tahun'))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self :
            if rec.patient_age:
                if rec.patient_age< 25:
                    rec.age_group='minor'
                else :
                    rec.age_group='mayor'
    @api.multi
    def open_patient_appointments(self):
        return {
            'name': _('Appointment'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.count = count

    patient_name = fields.Char(string='Name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always')
    notes = fields.Text(string='Registrtion Notes')
    image = fields.Binary(string='Image' , attachment=True)
    name = fields.Char(string='Test')
    appointment_count= fields.Integer('Appointment', compute='get_appointment_count')
    # sequence fields
    name_seq = fields.Char(string='Patient ID',reuired=True, copy=False, readonly=True,
                           index=True, default=lambda self: _("New"))
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female'),
        ('trans', 'Transgender')
    ],default='male',string='Gender')
    age_group = fields.Selection([
        ('mayor','Mayor'),
        ('minor','Minor')
    ],string='Age Group', compute='set_age_group')

    # sequence label
    @api.model
    def create(self, vals):
        if vals.get('name_seq',_('New')) == _('New'):
            vals['name_seq']=self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result