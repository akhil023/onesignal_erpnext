# -*- coding: utf-8 -*-
# Copyright (c) 2015, ECIT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PushNotifications(Document):
	def on_update(self):
		print "*"*200
		import requests
		import json
		print 
		header = {"Content-Type": "application/json; charset=utf-8",
		          "Authorization": "Basic ZTYzYzU2ZmYtMTMxMy00MjZlLTllNjUtODBmYzZiM2QxOTUy"}

		payload = {"app_id": "38209b35-8905-4e32-8437-f8ecc511a0be",
		           "included_segments": ["All"],
		           "headings": {"en": self.title},
		           "contents": {"en": self.message}}
		 
		req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
		 
		print(req.status_code, req.reason)
		
	def on_save(self):
		print "*"*200
		import requests
		import json
		print 
		header = {"Content-Type": "application/json; charset=utf-8",
		          "Authorization": "Basic ZTYzYzU2ZmYtMTMxMy00MjZlLTllNjUtODBmYzZiM2QxOTUy"}

		payload = {"app_id": "38209b35-8905-4e32-8437-f8ecc511a0be",
		           "included_segments": ["All"],
		           "headings": {"en": self.title},
		           "contents": {"en": self.message}}
		 
		req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
		 
		print(req.status_code, req.reason)
