import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.pop()
            self.__number_items-= 1

    def check_amount(self):
        total = []
        for items in self.__name_items:
            total.append(self.__item_price[items]) 

        amount = sum(total)
        if self.__number_items > 10:
            amount *= 0.9
        return amount

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for items in self.__name_items:
            if self.__tax_rate[items] == 20:
                twenty_percent_tax.append(items)
        total = []
        for items in twenty_percent_tax:
            total.append(self.__item_price[items])

        amount = sum(total)

        if self.__number_items > 10:
            amount*= 0,9
        vat = amount * 0.2
        return vat
        
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for items in self.__name_items:
            if self.__tax_rate[items] == 10:
                ten_percent_tax.append(items)
        total = []
        for items in ten_percent_tax:
            total.append(self.__item_price[items])

        amount = sum(total)

        if self.__number_items > 10:
            amount*=0.9
        vat = amount*0.1
        return vat

    def total_tax(self):
        tax10 = self.ten_percent_tax_calculation()
        tax20 = self.twenty_percent_tax_calculation()
        total_tax = tax10 + tax20
        return total_tax

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            int(telephone_number)
        except:
            raise ValueError('Необходимо ввести цифры')
        tel_str = str(telephone_number)
        if len(tel_str) > 10:
            raise ValueError ('Необходимо ввести 10 цифр после "+7"')
        return f'+7{tel_str}'

    



