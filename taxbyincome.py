from datetime import datetime
from utm import find_utm


class TaxableSalary:
    afps = {
        "CAPITAL": 1.44,
        "CUPRUM": 1.44,
        "HABITAT": 1.27,
        "MODELO": 0.58,
        "PLANVITAL": 1.45,
        "UNO": 0.69,
    }


PENSION_LIMIT = 81.6
UNEMPLOYMENT_LIMIT = 122.6


class TaxByIncome:
    tranches = [0, 13.5, 30, 50, 70, 90, 120, 150]
    taxes_tranches = [0, 4, 8, 13.5, 23, 30.4, 35, 40]
    reduce_tranches = [0, 0.54, 1.74, 4.49, 11.14, 17.8, 23.92, 30.67]

    def __init__(
        self, imponible_income: int, date_calc: datetime = datetime.now()
    ) -> None:
        self.utm = find_utm(date_utm=date_calc)
        self.income = round(imponible_income / self.utm, 2)
        self.tranch = self.find_closest_position(self.tranches, self.income)
        self.tax_rate = self.taxes_tranches[self.tranch]
        self.reduce_rate = self.reduce_tranches[self.tranch]
        self.taxes = round((self.income * self.tax_rate) / 100, 2) - self.reduce_rate

    @staticmethod
    def find_closest_position(input_list, value):
        return min(range(len(input_list)), key=lambda i: abs(input_list[i] - value))

    def details(self):
        for k in self.__dict__:
            print (f"{k}={getattr(self, k)}")

    def __str__(self):
        return f"[TaxByIncome (income={self.income})]"
