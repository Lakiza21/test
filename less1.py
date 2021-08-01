#okay

a = int(input("введите длительность эксперимента (сек): ")) 
print(a)

b = (int(a // 0))
c = (a % 60) * 60
d = (a // 3600)

simple_str = f"Okay, your experiment lasted for {a} seconds. You've spend {d}:{b}:{c} doing this shit"