
import random
win=0
lose=0
tie=0

print('enter your choice')
print('r-rock,p-paper,s-scissor')
us=input()

print('user choice is')
if us=='r':
    print('you have selected rock')
elif us=='p':
    print('you have selected paper')
elif us=='s':
    print('you have selected scissor')

computer=["rock","paper","scissor"]
cc=random.choice(computer)
print("computer selected :"+(cc))

if us==cc:
    print('it is tie')
    tie=tie+1

elif us=='r' or cc=='p':
    print('it is win')
    win=win+1
elif us=='p' or cc=='s':
    print('it is win')
    win=win+1
elif us=='s' or cc=='r':
    print('it is win')
    win=win+1

elif us=='s' or cc=='r':
    print('it is lose')
    lose=lose+1
elif us=='r' or cc=='p':
    print('it is lose')
    lose=lose+1
elif us=='p' or cc=='s':
    print('it is lose')
    lose=lose+1
