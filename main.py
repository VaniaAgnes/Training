money = float(input("amount of bill: $ "))
number_of_people = int(input("people: "))
amount_of_tips = float(input("tips: "))

tip_per_person = money * (amount_of_tips /100) / number_of_people
print(tip_per_person)
total_amount_per_person = (money / number_of_people + tip_per_person)
print(total_amount_per_person)















