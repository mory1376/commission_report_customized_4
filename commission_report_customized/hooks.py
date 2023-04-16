from . import __version__ as app_version

app_name = "commission_report_customized"
app_title = "erpnext commission report customzied"
app_publisher = "morteza"
app_description = "test"
app_email = "mohebi@duck.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/commission_report_customized/css/commission_report_customized.css"
# app_include_js = "/assets/commission_report_customized/js/commission_report_customized.js"

# include js, css files in header of web template
# web_include_css = "/assets/commission_report_customized/css/commission_report_customized.css"
# web_include_js = "/assets/commission_report_customized/js/commission_report_customized.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "commission_report_customized/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "commission_report_customized.utils.jinja_methods",
#	"filters": "commission_report_customized.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "commission_report_customized.install.before_install"
# after_install = "commission_report_customized.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "commission_report_customized.uninstall.before_uninstall"
# after_uninstall = "commission_report_customized.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "commission_report_customized.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes



# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"commission_report_customized.tasks.all"
#	],
#	"daily": [
#		"commission_report_customized.tasks.daily"
#	],
#	"hourly": [
#		"commission_report_customized.tasks.hourly"
#	],
#	"weekly": [
#		"commission_report_customized.tasks.weekly"
#	],
#	"monthly": [
#		"commission_report_customized.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "commission_report_customized.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "commission_report_customized.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "commission_report_customized.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"commission_report_customized.auth.validate"
# ]
# doctype_js = {
#     "Sales Order": "commission_report_customized/public/js/sales_order.js"
# }
doc_events = {
    "Sales Order": {
        "before_update_after_submit": "commission_report_customized.erpnext_commission_report_customzied.controllers.overrides.before_update_after_submit",
        #  "before_save": "commission_report_customized.erpnext_commission_report_customzied.controllers.overrides.before_save"
    }
}
# override_doctype_class = {
# 	"SellingController": "commission_report_customized.controllers.overrides.SellingControllerOverride"
# }
