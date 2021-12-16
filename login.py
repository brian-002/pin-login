print("enter your pin")
logo=int(input(" pin:"))
no_of_times=0
max=9999
min=1000
limit=1
while logo <=min or (logo)>=max and (no_of_times)<=(limit):
  if   (no_of_times)<=(limit):
     logo=int(input(" pin:"))
     no_of_times+=1
     if no_of_times>limit:
        print("confirm and try again")
     elif logo>max:
       print("enter a four digit number")
print("welcome")
print("congratulations for reaching this far:clap:")