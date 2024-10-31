import frappe

def clear_invoice_missing_error_logs():
    # Modify the query to target specific logs if needed
    frappe.db.sql("""
        DELETE FROM `tabError Log`
        WHERE error LIKE '%Current invoice is missing%'
    """)
    frappe.db.commit()
    frappe.logger().info("Error logs with 'Current invoice is missing' have been cleared.")
