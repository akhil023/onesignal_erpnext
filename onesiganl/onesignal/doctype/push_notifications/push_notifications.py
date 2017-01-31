# -*- coding: utf-8 -*-
# Copyright (c) 2015, ECIT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PushNotifications(Document):
	def on_update(self):
		send_msg_with_onesignal(self.title,self.message,sLink=self.link_url,sChromeIcon=self.chrome_icon,sFirefoxIcon=self.firefox_icon)
		
	def on_save(self):
		send_msg_with_onesignal(self.title,self.message,sLink=self.link_url,sChromeIcon=self.chrome_icon,sFirefoxIcon=self.firefox_icon)

def send_msg_with_onesignal(sTitle,sMessage,sLink=None,sChromeIcon=None,sFirefoxIcon=None):
	print "**********************************************************************************************************"
	import requests
	import json
	sAppId = frappe.db.get_single_value("Push Settings","app_id")
	sAuthoization = frappe.db.get_single_value("Push Settings","authorization")
	if not (sAppId and sAuthoization):
		frappe.throw("Please provide App Id and Authorization tokens from one signal account in settings.")

	sLink 			= sLink if sLink else frappe.db.get_single_value("Push Settings","default_on_click_link_url")
	sChromeIcon 	= sChromeIcon if sChromeIcon else frappe.db.get_single_value("Push Settings","default_chrome_icon_url")
	sFirefoxIcon 	= sFirefoxIcon if sFirefoxIcon else frappe.db.get_single_value("Push Settings","default_firefox_icon_url")

	dHeader 		= {
						"Content-Type"	: "application/json; charset=utf-8",
						"Authorization"	: "Basic "+sAuthoization
						}

	dPayload 		= {
						"app_id"			: frappe.db.get_single_value("Push Settings","app_id"),
						"included_segments"	: ["All"],
						"headings"			: {"en": sTitle},
						"contents"			: {"en": sMessage},
						"url"				: sLink,
						"chrome_web_icon"	: sChromeIcon,
						"firefox_icon"		: sFirefoxIcon
	           }
	 
	oReq = requests.post("https://onesignal.com/api/v1/notifications", headers=dHeader, data=json.dumps(dPayload))
	 
	print(oReq.status_code, oReq.reason)