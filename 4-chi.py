class Phone:
    def __init__(self, brand, model, battery_capacity, color, storage):
        self.__brand = brand
        self.__model = model
        self.__battery_capacity = battery_capacity
        self.__color = color
        self.__storage = storage

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand
        return self.__brand

    @brand.deleter
    def brand(self):
        del self.__brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model
        return self.__model

    @model.deleter
    def model(self):
        del self.__model

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity
        return self.__battery_capacity

    @battery_capacity.deleter
    def battery_capacity(self):
        del self.__battery_capacity

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        return self.__color

    @color.deleter
    def color(self):
        del self.__color

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, storage):
        self.__storage = storage
        return self.__storage

    @storage.deleter
    def storage(self):
        del self.__storage

def Make_call(phnumber):

        return f"{phnumber} ga qongiroq amalga oshirildi"

def charge(n):
        return f"telefoninngiz zaryadlanmoqda"

def get_storge(self):
        return f"Telefon xotirasi.\n>>> {self.__storage}"
print("commands add telefon qoshish\n call qongiroq qilish\n charge zaryadlash\n get storge xotirani korish\nstop chiqish")
while True:

    comand=input("Buyruqni kiriting:")
    if comand == 'add':
            brand = input("brand: ")
            model = input("modeli: ")
            while True:
                batery = input('batareya quvattini kiriting: ')
                if  batery.isdigit():
                    break
                else:
                    print('batreya faqathariflardan iborat boladi')

            while True:
                colour = input('rangini kiriting: ')
                if colour.isalpha():
                    break
                else:
                    print('rang faqat hariflardan iborat bolishi kerak!!!!')

            while True:
                storge = input('xotirasini kiriting: ')
                if storge.isnumeric():
                    break
                else:
                    print('xotira faqat raqamlardan iborat bolishi kerak!!!!')

            phone=Phone(brand,model,batery,colour,storge)

    elif comand == 'call':
        while True:
            phone = input('telefon raqamingizni kiriting: ')
            if phone.startswith("+998") and phone[1:].isdigit() and len(phone) == 13:
                print(Make_call(phone))
                break
            else:
                print('telefon raqam faqat +998 dan boshlanishi va + dan so\'ng barcha raqamlar bo\'lishi kerak')
    elif comand=="charge":
        print(charge(100))
    elif comand=="get storge":
        print(get_storge)

    elif comand == 'stop':
        break

    else:
        print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")