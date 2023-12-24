class RollNumbers:
    def __init__(self):
        pass
    def get(self,n,year,Branch):
        AllRollNUMBERS = []
        AlpsList = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if(year == 23 and Branch == "05"):
            count = 0
            j = 0
            for i in range(1,min(100,n)):
                count+=1
                j+=1
                if(i%10 == 0):
                    j = 0
                if(i<10):
                    # print(f"{year}951A{Branch}0{i}")
                    AllRollNUMBERS.append(f"{year}951A{Branch}0{i}")
                elif(i==10):
                    # print(f"{year}951A{Branch}10")
                    AllRollNUMBERS.append(f"{year}951A{Branch}10")
                elif(i>10 and i<100):
                    # print(f"{year}951A{Branch}{i}")
                    AllRollNUMBERS.append(f"{year}951A{Branch}{i}")
            j=0
            while(count < n):
                for alp in AlpsList:
                    if(j<10):
                        count+=1
                        # print(f"{year}951A{Branch}{j}{alp}")
                        AllRollNUMBERS.append(f"{year}951A{Branch}{j}{alp}")
                    else:
                        for a in AlpsList:
                            for b in AlpsList:
                                count+=1
                                if(count > n-1):
                                        return AllRollNUMBERS
                                if(a != b):
                                    AllRollNUMBERS.append(f"{year}951A{Branch}{a}{b}")
                                    # print(f"{year}951A{Branch}{a}{b}")
                j+=1
        else: 
            j = 0
            z = 0
            for i in range(1,n+1):
                j+=1
                if(i%10 == 0):
                    j = 0
                    if(i>100):
                        z+=1
                if(i<10):
                    AllRollNUMBERS.append(f"{year}951A{Branch}0{i}")
                elif(i==10):
                    AllRollNUMBERS.append(f"{year}951A{Branch}10")
                elif(i>10 and i<100):
                    AllRollNUMBERS.append(f"{year}951A{Branch}{i}")
                elif(i>=100):
                    AllRollNUMBERS.append(f"{year}951A{Branch}{AlpsList[z]}{j}")
        return AllRollNUMBERS

# n = int(input("Enter no: "))
# year = int(input("Year ( 23 || 22 || 21 || 20 ): "))
# Branch = input("Branch ( 01 || 02 || 03 || 04 || 05 || 12 || 66 || 67 ): ")

# RN = RollNumbers()
# print(RN.get(n,year,Branch))