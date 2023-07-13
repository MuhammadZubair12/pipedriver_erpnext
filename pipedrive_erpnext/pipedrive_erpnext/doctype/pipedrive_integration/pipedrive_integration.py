# Copyright (c) 2023, zubair and contributors
# For license information, please see license.txt
import requests
import frappe
import json
from frappe.model.document import Document

class PipedriveIntegration(Document):
	pass


@frappe.whitelist(allow_guest=True)
def create_connect(name):
	if name == "ok":
		doc = frappe.get_doc("Pipedrive Integration")
		doc.status = "Connected"
		doc.save()
		frappe.msgprint(
			msg='Connected Successfuylly!!',
			title='Notification',
			indicator='green'
		)
	else:
		doc = frappe.get_doc("Pipedrive Integration")
		doc.status = "Not-Connected"
		doc.save()
		frappe.msgprint(
			msg='Unauthroized Access',
			title='Error'
		)
@frappe.whitelist(allow_guest=True)
def test_pipedrive_token():
	doc = frappe.get_doc("Pipedrive Integration")
	tok = doc.api_token
	url = f"https://api.pipedrive.com/v1/leads?api_token={tok}"
	response = requests.get(url)
	d = response.json()
	if response.status_code == 200:
		# return d
		for a in d["data"]:
			check = frappe.db.exists('Lead', dict(lead_id = a["id"]))
			if check:
				pass
				# upd = frappe.get_doc("Lead", dict(name = check))
				# upd.first_name = a["title"]
				# # upd.last_name = "test"
				# upd.save()
			else:
				lead = frappe.new_doc("Lead")
				lead.lead_id = a["id"]
				lead.first_name = a["title"]
				lead.save()
			# return a["title"]
	else:
		return 'Token is invalid or there was an error.'
	# return response.json()