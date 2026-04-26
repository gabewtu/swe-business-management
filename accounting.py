from datetime import datetime, timedelta
from database import get_connection

class Accounting:
    # Constructor
    def __init__(self):
        pass

    # Helper methods
    @staticmethod
    def getLastMonthDateRange():
        """Returns a simple 30-day date range ending today"""
        endDate = datetime.now()
        startDate = endDate - timedelta(days=30)
        return startDate.strftime("%Y-%m-%d"), endDate.strftime("%Y-%m-%d")

    # Report methods
    @staticmethod
    def getRevReportLastMonth():
        startDate, endDate = Accounting.getLastMonthDateRange()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT SUM(service_cost) as total
            FROM invoices
            WHERE date BETWEEN ? AND ?
        ''', (startDate, endDate))

        row = cursor.fetchone()
        conn.close()

        total = row["total"] if row["total"] else 0.0

        return {
            "reportType": "Revenue",
            "startDate": startDate,
            "endDate": endDate,
            "totalRevenue": total
        }

    @staticmethod
    def getExpReportLastMonth():
        startDate, endDate = Accounting.getLastMonthDateRange()

        conn = get_connection() 
        cursor = conn.cursor()

        cursor.execute('''
            SELECT SUM(a.additional_expenses) as total
            FROM invoices i
            JOIN appointments a ON i.Appointment_ID = a.Appointment_ID
            WHERE i.invoice_date BETWEEN ? AND ?
        ''', (startDate, endDate))

        row = cursor.fetchone()
        conn.close()
        
        total = row["total"] if row["total"] else 0.0

        return {
            "reportType": "Expenses",
            "startDate": startDate,
            "endDate": endDate,
            "totalExpenses": total
        }

    @staticmethod
    def generateMasterReportLastMonth():
        # Combines revenue, expenses, and income into one report
        revenueReport = Accounting.getRevReportLastMonth()
        expenseReport = Accounting.getExpReportLastMonth()

        totalRevenue = revenueReport["totalRevenue"]
        totalExpenses = expenseReport["totalExpenses"]
        totalIncome = totalRevenue - totalExpenses

        return {
            "reportTitle": "Last Month Financial Summary",
            "startDate": revenueReport["startDate"],
            "endDate": revenueReport["endDate"],
            "revenue": revenueReport["totalRevenue"],
            "expenses": expenseReport["totalExpenses"],
            "income": totalIncome
        }
