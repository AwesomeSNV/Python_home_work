names = ["Nikolaj", "Evgenij", "Maxim"]
salaries = [1500, 2500, 3500]
awards  = ["12.5%", "1.5%", "17.5%"]

print({name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salaries, awards)})