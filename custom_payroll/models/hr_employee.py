from odoo import models,fields,api,_

class calendar_event(models.Model):
	_inherit = 'hr.employee'

	marital_status = fields.Selection([
									('Single','Single'),
									('Married','Married'),
									('Divorced','Divorced'),
									('Widowed','Widowec'),
									('Separated','Separated'),
									('Others','Others')
									])
	cititzenship = fields.Selection([
									('Singaporean','Singaporean'),
									('Singapore PR','Singapore PR'),
									('Foreigner','Foreigner'),
									])
	contributor_for_share = fields.Boolean(String="Contributor For SHARE")
	ethinic_race = fields.Selection([
									('Chinese','Chinese'),
									('Indian','Indian'),
									('Malay','Malay'),
									('Eurasian','Eurasian'),
									('Others','Others'),
									], string="Ethinic Race")
	religion = fields.Selection([
								('Buddhist','Buddhist'),
								('Christian','Christian'),
								('Catholicism','Catholicism'),
								('Freethinker','Freethinker'),
								('Hindu','Hindu'),
								('Muslim','Muslim'),
								('Sikh','Sikh'),
								('Taoist','Taoist'),
								('Others','Others')
								], string="Religion")
	singapore_pr_startdate = fields.Date(string="Singapore PR Start Date (DD/MMM/YYYY)*")
	qualification_permit = fields.Selection([
											('E Pass','E Pass'),
											('S Pass','S Pass'),
											('Work Permit','Work Permit')
											])
	e_pass_sdate = fields.Date(string='Permit / Pass Start Date')
	e_pass_edate = fields.Date(string="Permit / Pass End Date")
	worker_qualification = fields.Selection([
											('Construction','Construction'),
											('Harbour Craft','Harbour Craft'),
											('Manufactring','Manufactring'),
											('Marine','Marine'),
											('None','None'),
											('Others','Others'),
											('Process','Process'),
											('Services','Services')
										])
	contribution_for_sdl = fields.Boolean(string=" Contribution for SDL")
	contribution_for_share = fields.Boolean(string="Contribution for SHARE")
	contribution_for_mbmf = fields.Boolean(string="Contribution for MBMF")
	contribution_for_cdac = fields.Boolean(string=" Contribution for CDAC")
	contribution_for_sinda = fields.Boolean(string="Contribution for SINDA")
	contribution_for_ecf = fields.Boolean(string="Contribution for ECF")
	
	# statutory = fields.Boolean(string="Statutory Contributions (Please Un-tick if not contributing)")
