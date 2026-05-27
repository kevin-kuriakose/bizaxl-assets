import frappe
def execute(filters=None):
    filters = filters or {}
    columns = [
        {"fieldname": "asset", "label": "Asset", "fieldtype": "Link", "options": "BA Asset", "width": 180},
        {"fieldname": "asset_name", "label": "Asset Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "schedule_date", "label": "Schedule Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "depreciation_amount", "label": "Depreciation", "fieldtype": "Currency", "width": 140},
        {"fieldname": "accumulated_depreciation", "label": "Acc. Depreciation", "fieldtype": "Currency", "width": 150},
        {"fieldname": "journal_entry", "label": "Journal Entry", "fieldtype": "Data", "width": 140},
    ]
    conditions = "WHERE 1=1"
    values = {}
    if filters.get("asset"):
        conditions += " AND ds.asset = %(asset)s"
        values["asset"] = filters["asset"]
    if filters.get("from_date"):
        conditions += " AND ds.schedule_date >= %(from_date)s"
        values["from_date"] = filters["from_date"]
    if filters.get("to_date"):
        conditions += " AND ds.schedule_date <= %(to_date)s"
        values["to_date"] = filters["to_date"]
    data = frappe.db.sql(f"""
        SELECT ds.asset, a.asset_name, ds.schedule_date,
               ds.depreciation_amount, ds.accumulated_depreciation,
               ds.journal_entry
        FROM `tabBA Asset Depreciation Schedule` ds
        LEFT JOIN `tabBA Asset` a ON a.name = ds.asset
        {conditions}
        ORDER BY ds.schedule_date
    """, values, as_dict=True)
    return columns, data
