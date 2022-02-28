#mobile store application 
class OnlinePortal:
   item_list=['samsung','apple','karbon'] #list of mobiles in store
   quantity_list=[10,3,2]  #list of quantity of mobiles
   price_list=[2323,4343,5343] #prices of each mobiles 
   # above all are one - to - one correspondence
   # search_item method is used to search the item in store
   def search_item(self,item):
       if item in OnlinePortal.item_list:
           return OnlinePortal.item_list.index(item)
       return -1
   # place_order is used to place the order in store 
   def place_order(self,index,emi,quantity):
       self.ind=self.search_item(index)
       OnlinePortal.quantity_list[self.ind]-=quantity 
       self.total_cost=(quantity*OnlinePortal.price_list[self.ind])
       if OnlinePortal.quantity_list[self.ind]>0:
           if emi == True :
               self.total_cost+=(2/self.total_cost)*100 
               return round(self.total_cost,2)
           else:
               self.total_cost-=(2/self.total_cost)*100 
               return format(self.total_cost,".2f")
   # to add the stock in store 
   def add_stock(self,item_name,quantity):
       if item_name in OnlinePortal.item_list:
           if OnlinePortal.quantity_list[OnlinePortal.item_list.index(item_name)]>=10:
               OnlinePortal.quantity_list[OnlinePortal.item_list.index(item_name)]+=quantity
           return -1 
       return -2
   # to add new item in store
   def add_item(self,item_name,price,quantity):
       if item_name not in OnlinePortal.item_list:
           OnlinePortal.item_list.append(item_name)
           OnlinePortal.quantity_list.append(quantity) 
           OnlinePortal.price_list.append(price) 
           print("stock added")
           print("item alread existed in store..")
       return -2 

# buyer class identified with username and emailid
class Buyer:
    def __init__(self,name,email_id):
        self.__name=name 
        self.__email_id=email_id 
    def get_email_id(self):
        return self.__email_id 
    def get_name(self):
        return self.__name 
    def purchase(self,item_name,quantity,emi):
        new_object=OnlinePortal() 
        if item_name in new_object.item_list:
            if quantity<=new_object.quantity_list[new_object.item_list.index(item_name)]:
                new_object.place_order(item_name,emi,quantity)
                print("order placed")
            return -1 
        return -2 
print(Buyer('ramesh','ramesh12@gmail.com').purchase('samsung',True,3))