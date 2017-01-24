# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "onesiganl"
app_title = "OneSignal"
app_publisher = "ECIT"
app_description = "Send push notifications with onesignal"
app_icon = "octicon octicon-comment"
app_color = "green"
app_email = "akhilr@ergonomicscit.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/onesiganl/css/onesiganl.css"
# app_include_js = "/assets/onesiganl/js/onesiganl.js"

# include js, css files in header of web template
# web_include_css = "/assets/onesiganl/css/onesiganl.css"
# web_include_js = "/assets/onesiganl/js/onesiganl.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "onesiganl.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "onesiganl.install.before_install"
# after_install = "onesiganl.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "onesiganl.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"onesiganl.tasks.all"
# 	],
# 	"daily": [
# 		"onesiganl.tasks.daily"
# 	],
# 	"hourly": [
# 		"onesiganl.tasks.hourly"
# 	],
# 	"weekly": [
# 		"onesiganl.tasks.weekly"
# 	]
# 	"monthly": [
# 		"onesiganl.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "onesiganl.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "onesiganl.event.get_events"
# }

