###Holden Anderson
### bill of sale 
###9-21

import random

#data
company_name=Tesla
int current_year 2021
float sales_tax = 0.854
int prop_tax = .058
int restock_fee = 1200
int insp_fee = 380
int cleaning_fee = 200
int ext_warr = 2000
float gap_insu = .010

#collect info
make=input("enter the Make of the Car:")
model=input("enter the Model of the Car:")

#calculate registration fees
int car_year = input("enter the year of the Car:")
int current_year = input("enter the current year:")

if current_year-car_year < 3:
    int reg_fees = 150
elif current_year-car_year <= 6:
        int reg_fees = 110
else:
    int reg_fees = 80

int miles = input("enter the milage of the Car:")
int sales_price = input("enter the sales price:")
buyers_name = input("enter name of buyer:")
new = current_year-car_year < 1

if not new:
   int repair_fee = 500

total-fees = repair_fee+reg_fee+restock_fee+insp_fee+cleaning_fee+ext_warr+((sale_price*gap_insu)
total_tax = (sale_price*prop_tax)


billofsale=str.format("""
@====================@====================@====================@====================
{0:^81}

\t Buyer Info
\t Buyer Phone
\t Buyer Email
\t Buyer Car

@====================@====================@====================@====================
{0:^81}


\t Make: \t{}
\t Model: \t{}
\t Year: \t{}
\t Mileage:\t{}
\t Make: \t{}"""
print(billofsales)

