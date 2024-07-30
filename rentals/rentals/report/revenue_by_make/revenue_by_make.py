# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	#bench start console this will print
	#print("----"*20)
	#print(filters)
	#below line gets printed in console
	#frappe.errprint(filters)
	columns = [
		{
			"fieldname" : "make",
			"label" : "Make",
			"fieldtype" : "Data"
		}, {
			"fieldname" : "total_revenue",
			"label" : "Total Revenue",
			"fieldtype" : "Currency",
			"options" : "RS"
		},]
	data = frappe.get_all(
		   "Ride Booking",
	       fields=["SUM(total_amount) AS total_revenue","vehicle.make"],
		   filters={"docstatus": 1},group_by = "make")
	
	chart = {
		"data" : {
			"labels" : [x.make for x in data],
			"datasets" : [{ "values" : [x.total_revenue for x in data]}],
		},
		#"type" : "pie", donut, line
		"type" : "bar"
			}
	#return columns,data,some_message,chart,
	return columns, data, "Message Summary", chart
