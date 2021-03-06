from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = 'id desc'

    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

    def action_done(self):
        for rec in self:
            rec.state='done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
            result = super(HospitalAppointment, self).create(vals)
            return result
    def _get_default_note(self):
        return "Patient Rujukan BPJS"

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    note = fields.Text('Registration Note', default=_get_default_note)
    doctor_note = fields.Text('Doctor Notes')
    pharmacy_note = fields.Text('Pharmacy Notes')
    appointment_date = fields.Date('Date', required=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], string='Status', readonly=True, default='draft')
