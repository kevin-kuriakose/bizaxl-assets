import frappe
from frappe.model.document import Document
from frappe.utils import flt, add_months, add_years, getdate, today


class BAAsset(Document):

    def validate(self):
        self.value_after_depreciation = flt(self.gross_purchase_amount)
        if self.calculate_depreciation:
            self.make_depreciation_schedule()

    def make_depreciation_schedule(self):
        if not self.depreciation_start_date:
            return
        if not self.total_number_of_depreciations:
            return

        self.schedules = []
        depreciable_amount = flt(self.gross_purchase_amount) - flt(self.salvage_value)
        depreciation_per_period = depreciable_amount / int(self.total_number_of_depreciations)
        accumulated = 0
        date = getdate(self.depreciation_start_date)

        for i in range(int(self.total_number_of_depreciations)):
            accumulated += depreciation_per_period
            self.append("schedules", {
                "schedule_date": date,
                "depreciation_amount": round(depreciation_per_period, 2),
                "accumulated_depreciation_amount": round(accumulated, 2),
                "is_depreciated": 0,
            })
            if self.frequency_of_depreciation == "Monthly":
                date = add_months(date, 1)
            elif self.frequency_of_depreciation == "Quarterly":
                date = add_months(date, 3)
            else:
                date = add_years(date, 1)

    def on_submit(self):
        self.status = "In Location"

    def on_cancel(self):
        self.status = "Draft"
