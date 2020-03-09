# This takes a large GEOIP ranges txt file and splits it into several txt files which have 50,000 ip network ranges in them.
# It does this because Ubiquiti ACL firewall rules can only hold around that number of network ranges.

# Reads IP ranges into a list

File_OBJ = open('IP_Block_List.txt', 'r')
MASTER_IP_BLACKLIST_LIST = File_OBJ.readlines()
File_OBJ.close()

#Create IP lists
####################################
File_OBJ1 = open('ipblacklist1.txt', 'w')
File_OBJ2 = open('ipblacklist2.txt', 'w')
File_OBJ3 = open('ipblacklist3.txt', 'w')
File_OBJ4 = open('ipblacklist4.txt', 'w')
File_OBJ5 = open('ipblacklist5.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 0 and count <= 49999):
        File_OBJ1.write(i)
        count += 1
    elif (count >= 50000 and count <= 99999):
        #close previous txt file
        File_OBJ1.close()
        File_OBJ2.write(i)
        count += 1
    elif (count >= 100000 and count <= 149999):
        #close previous txt file
        File_OBJ2.close()
        File_OBJ3.write(i)
        count += 1
    elif (count >= 150000 and count <= 199999):
        #close previous txt file
        File_OBJ3.close()
        File_OBJ4.write(i)
        count += 1
    elif (count >= 200000 and count <= 250000):
        #close previous txt file
        File_OBJ4.close()
        File_OBJ5.write(i)
        count += 1
    else:
        File_OBJ5.close()
        break
