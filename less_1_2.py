time=int(input("enter time in a seconds:"))
hours=time//3600
minutes=(time-(hours*3600))//60
seconds=time%60
print(f"{hours:02}:{minutes:02}:{seconds:02}")