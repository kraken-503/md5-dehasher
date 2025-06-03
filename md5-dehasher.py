import time

hash_list = open('common-hashes.txt','r')
inp_hash = input("Enter Hash : ").strip()

j=0
found = False

for line in hash_list.readlines():
    line = line.strip()
    if line:
        j+=1
    if line == inp_hash:
        found = True
        break
if not found:
    print("Hash not found in rainbow table")


passwd_list = open('pass.txt','r')
passwd_read = passwd_list.readlines()

print(f"Time took : ",{time.process_time()},'sec')
if found:
    print(f"Pasword Found : ",{passwd_read[j-1].strip()})


hash_list.close()
passwd_list.close()
