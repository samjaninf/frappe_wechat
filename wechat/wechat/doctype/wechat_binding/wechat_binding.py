# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from frappe.model.document import Document


class WechatBinding(Document):
	def autoname(self):
		self.name = '[' + self.app + '].' + self.user


@frappe.whitelist()
def wechat_bind(app, user, openid, expires=None):
	doc = frappe.get_doc({
		"doctype": "Wechat Binding",
		"user": user,
		"app": app,
		"openid": openid,
		"expires": expires
	})
	doc.insert()
	frappe.db.commit()

	return _("Binding is done")


@frappe.whitelist()
def wechat_unbind(app, user):
	name = frappe.get_value("Wechat Binding", {"app": app, "user": user})
	if not name:
		throw(_("There is no binding for App{0} User{1}").format(app, user))

	frappe.delete_doc("Wechat Binding", name)
	frappe.db.commit()

	return _("Binding has ben deleted")