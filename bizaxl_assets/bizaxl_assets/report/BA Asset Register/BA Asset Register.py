import frappe
from frappe.utils import flt
def execute(filters=None):
    filters = filters or {}
    columns = [
        {"fieldname": "name", "label": "Asset", "fieldtype": "Link", "options": "BA Asset", "width": 180},
        {"fieldname": "asset_name", "label": "Asset Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "asset_category", "label": "Category", "fieldtype": "Link", "options": "BA Asset Category", "width": 140},
        {"fieldname": "purchase_date", "label": "Purchase Date", "fieldtype": "Date", "width": 110},
        {"fieldname": "gross_purchase_amount", "label": "Purchase Amount", "fieldtype": "Currency", "width": 140},
        {"fieldname": "accumulated_depreciation", "label": "Acc. Depreciation", "fieldtype": "Currency", "width": 150},
        {"fieldname": "net_asset_value", "label": "Net Value", "fieldtype": "Currency", "width": 130},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 100},
    ]
    conditions = "WHERE 1=1"
    values = {}
    if filters.get("asset_category"):
        conditions += " AND asset_category = %(asset_category)s"
        values["asset_category"] = filters["asset_category"]
    if filters.get("company"):
        conditions += " AND company = %(company)s"
        values["company"] = filters["company"]
    data = frappe.db.sql(f"""
        SELECT name, asset_name, asset_category, purchase_date,
               gross_purchase_amount, accumulated_depreciation,
               gross_purchase_amount - accumulated_depreciation as net_asset_value,
               status
        FROM `tabBA Asset`
        {conditions}
        ORDER BY asset_category, asset_name
    """, values, as_dict=True)
    return columns, data
