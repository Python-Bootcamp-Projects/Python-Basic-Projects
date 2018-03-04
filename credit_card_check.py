#-----------------------------------class credit_card---------------------------

class credit_card:

    def __init__(self,card):

        self.card_type = ''
        self.card_valid = False
        self.card_num = card
        self.cardholder_name = None
        self.cardholder_bank=None
        self.cardholder_phone=None
        self.cardholder_location=None
        self.cardholder_spend_avg=None


    def check_type(self):

        if self.card_num[0] == '4' : self.card_type = 'Visa'
        elif self.card_num[0:2] in ['51','52','53','54','55'] : self.card_type = 'Mastercard'
        elif self.card_num[0:2] in ['34','37'] : self.card_type = 'AMEX'
        elif self.card_num[0:4] == '6011' : self.card_type = 'Discover'
        else: self.card_type = 'International'


    def check_len(self):

        if len(self.card_num)<15 or len(self.card_num)>16:
            self.card_valid = False
            print (" Incorrect Card Number - Check Again! ")


    def get_type(self):
        return self.card_type

    def get_valid(self):
        return self.card_valid

    def get_num(self):
        return self.card_num


    def validate(self, card):

        temp=[]
        rev_str=card[::-1]
        for i in rev_str :
            temp.append(int(i))

        for i in range(1, len(temp), 2):
            if (2*temp[i]>9):
                temp[i]= (2*temp[i])-9
            else: temp[i]=(2*temp[i])

        if (sum(temp)%10==0):
            self.card_valid= True
            return True

        else: return False


#------------------------class shop---------------------------------------------

class shop:

    def __init__(self, checker = 'Unknown'):

        self.id = checker
        self.card_list={}


    def addcard(self, num):

        new_card = credit_card(num)
        new_card.validate(num)
        new_card.check_type()
        self.card_list[num] = new_card

        print(' card - added ')

    def get_validated(self, num):

        if num not in self.card_list: self.addcard(num)
        print(self.card_list[num].get_valid())


    def deletecard(self, num):

        if num not in self.card_list.keys(): print( " Card Doesnot Exist in System " )

        else:
            del(self.card_list[num])
            print( ' Card Deleted Succesfully ')


    def search(self, num):

        if num not in self.card_list.keys():
            print( " Card Doesnot Exist in System " )
            x= input( ' Press - Y to add this card to system or N to not add ' ).upper()
            if x=='Y': self.addcard(num)


        else:
            print('card No.->', self.card_list[num].get_num(),end=', ')
            print('Type->', self.card_list[num].get_type(),end=', ')
            print('Validity->' , self.card_list[num].get_valid(),end=', ')



    def __iter__(self):
        return iter(self.card_list.values())

#-----------------------------user interface------------------------------------

#initializing



def print_all():

    for i in pullnbear:
        #print('\n
        print('card No.->', i.get_num(),end=', ')
        print('Type->', i.get_type(),end=', ')
        print('Validity->' , i.get_valid(),end=', ')
        print('\n')


def take_num():

    print('\n')
    card=input(" Please Enter the Credit/Debit Card Number:  ")
    print('\n')
    return card

def display():
    print("\n")
    print("\n")
    print("\n")
    print( ' WELCOME TO LIGIT CREDIT CARD DATA MANAGEMENT COMPANY ')
    print("\n")
    print(' Currently We are only working with Pull n bear  ')
    print(' Incase of any other retail outlet please contact our' , end='')
    print(' Business Developement Department ')

    x = None

    while(x!=0):

        print('\n')
        print('________________________________________________________________')
        #print( '       LIGIT CREDIT CARD DATA MANAGEMENT COMPANY   ')
        print('________________________________________________________________')
        print( ' Press - 1  Add Credit card ')
        print( ' Press - 2  Delete Credit card ')
        print( ' Press - 3  Print Credit Card details in system ')
        print( ' Press - 4  Validate Card ' )
        print( ' Press - 5  Search Card ')
        print( ' Press - 0  Quit ')
        print('________________________________________________________________')
        print('________________________________________________________________')
        print( '\n')

        x = input("  Enter your choice Now --> " )
        print('\n')
        try: x=int(x)
        except: x=int(input (" Invalid Entry Please Try again! "))


        if x==1: pullnbear.addcard(take_num())

        if x==2: pullnbear.deletecard(take_num())

        if x==3: print_all()

        if x==4: pullnbear.get_validated(take_num())

        if x==5: pullnbear.search(take_num())

        if x==0 :
            print( ' \n ')
            print( ' Thanks for Using our Services!! ')
            print(' \n ')
            print(' \n ')
            break




pullnbear=shop()
#print(pullnbear.card_list)
pullnbear.addcard('5134567890123456')
pullnbear.addcard('3434000000000000')
pullnbear.addcard('6011000000000000')
pullnbear.addcard('4797451564189268')
pullnbear.addcard('371449635398431')
pullnbear.addcard('4222222222222')
pullnbear.addcard('3530111333300000')
pullnbear.addcard('38520000023237')
pullnbear.addcard('5019717010103742')
#pullnbear.deletecard('5019717010103742')
#print_all()
display()
