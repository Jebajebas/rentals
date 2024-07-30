#we can create this anywhere 
#we can also name this file as we want
import frappe

@frappe.whitelist()
def get_emoji():
    return "🥰"

def throw_emoji(doc,event):
    frappe.throw("🥰")


# if this method is not available 
# during migration it shows an error
def send_payment_remainders():
    pass 


def get_query_conditions_for_vehicle(user):
    pass 
    #return "name = 1 || name = 9"