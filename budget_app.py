class Category:
    def __init__(self,category):
        self.category = category
        self.balance = 0
        self.__deposit = 0
        self.ledger = []

    def deposit(self,dep=0,desc=""):
        if dep > 0 :
            depo = {}
            depo["amount"] = dep
            depo["description"] = desc
            self.balance += dep
            self.__deposit += dep
            self.ledger.append(depo)

    def withdraw(self,damount=0,description=""):
        if self.check_funds(damount) :
            draw = {}
            self.balance -= damount
            draw["amount"] = -damount
            draw["description"] = description
            self.ledger.append(draw)
        else :
            return False
        
        return True
    
    def transfer(self,tamount,cat):
        if self.check_funds(tamount) :
            draw = {}
            # draw["type"] = 'w'
            draw["amount"] = -tamount
            draw["description"] = "Transfer to " + cat.category
            self.ledger.append(draw)
            self.balance -= tamount
            cat.deposit(tamount,"Transfer from " + self.category)
        else:
            return False

        return True

    def check_funds(self,amount):
        if self.balance >= amount:
            return True
        else:
            return False
    

    def get_balance(self):
        return self.balance

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
        result = title + items + f"Total: {self.balance:.2f}"
        return result
    
    def total_spent(self):
        return self.__deposit - self.balance 
    

def create_spend_chart(categories):
    diag = []
    tspent = 0
    cspent = []
    clen =0
    result = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        diag.append([i,'|'])

    for c in categories:
        tspent += c.total_spent()

    for c in categories:
        pspent = (c.total_spent()/tspent)*100
        clen = len(c.category) if clen < len(c.category) else clen
        pspent = (pspent//10)*10
        cspent.append([c.category,pspent])

    for i in diag:
        i[1] = f"{i[0]: >3}{i[1]}"
        for j in cspent:
            if i[0] <= j[1]:
                i[1] += ' o '
            else:
                i[1] += '   '
        result += i[1]+' \n'
        
    line = f"{' '*4}"
    for c in range(len(cspent)):
        line += f"{'-'*3}"
    line += '-'
    for c in cspent:
        c[0] += ' '*(clen-len(c[0]))
    
    result += line + '\n'
    # print(cspent)
    line = ""
    for i in range(clen):
        line +=f"{' '*4}"
        for j in cspent:
            line+=(f" {j[0][i]} ")
        if i < clen-1 : line += ' \n' 
        else: line += ' '

    result +=line
    return(result)

def main():
    food = Category("food")
    entertainment = Category("entertainment")
    business = Category("business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([business,food,entertainment]))

if __name__=="__main__":
    main()
