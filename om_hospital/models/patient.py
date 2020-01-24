from odoo import  models, fields,api , _

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Partient Record'
    _rec_name = 'name_seq'

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self :
            if rec.patient_age:
                if rec.patient_age< 18:
                    rec.age_group='minor'
                else :
                    rec.age_group='mayor'

    patient_name = fields.Char(string='Name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always')
    notes = fields.Text(string='Registrtion Notes')
    image = fields.Binary(string='Image' , attachment=True)
    name = fields.Char(string='Test')
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