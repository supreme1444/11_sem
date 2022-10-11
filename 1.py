class Person:
    def __init__(self, name,lname,sname,dict_ph):

        self.name = name
        self.lname = lname
        self.sname = sname
        self.dict_ph = dict_ph
       
    def get_phone(self):
        return dict(self.dict_ph).get('privat')
    def get_name(self):
        return self.name
    def get_work_phone(self):
         return dict(self.dict_ph).get('work') 
    def get_sms_text(self):
        a=self.dict_ph.get('private')
        return f'Отправлено смс на номер {a} :с текстом:Уважаемый {self.name} {self.lname}! Примите участие в конкурсе!'
p=Person('Дмитрий','Максимович','Егоров',{'private':89006,'work':8901033})
p2=Person('Иван','Петрович','Петров',{'private':89005,'work':8901033})
p3=Person('Семен','Робертович','Сидоров',{'private':89005,'work':8901033})
#print (p.get_name())
#print(p.get_phone())
#print (p.get_work_phone())

class Company:
    def __init__(self,name_c,type_c,dict_cont,*person):
        self.name_c = name_c
        self.dict_cont = dict_cont
        self.type_c = type_c
        self.dict_cont = dict_cont
        self.person_list = list(person)
    def get_phone(self):
        if self.dict_cont.get('contact'):
            return self.get_sms_text()          
        elif self.dict_cont.get('noncontact'):
            return f'Не удалось отправить сообщение на номер {self.name_c}'    
    def get_name(self):
        return self.name_c       
    def get_sms_text(self):
        #a=Person(self.person_list[0].get_phone())
        return f'Отправлено смс на номер {?????????}:с текстом:Для компании {self.name_c} есть супер предложение!Примите участие в нашем беспроигрышном конкурсе для {self.type_c}'
        
c1 = Company('Ромашка','ООО',{'contact':111})
c2 = Company('Яблочный комбинат','ООО',{'noncontact':111})
def send_sms():
    k1=c2.get_phone()
    k2=c1.get_phone()
    k3=p. get_sms_text()
    k4=p2. get_sms_text()
    k5=p3. get_sms_text()
    return k1,k2,k3,k4,k5
a=send_sms()
print(a, sep=',', end='\n'){?????}

