# This takes a large GEOIP ranges txt file and splits it into several txt files which have 50,000 ip network ranges in them.
# It does this because Ubiquiti ACL firewall rules can only hold around that number of network ranges.

# Reads all IP ranges into a list

File_OBJ = open('IP_Block_List.txt', 'r')
MASTER_IP_BLACKLIST_LIST = File_OBJ.readlines()
File_OBJ.close()

#######

#IP RANGE 0-50K
####################################

File_OBJ1 = open('output1.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 0 and count <= 50000):
        File_OBJ1.write(i)
    count += 1

    if (count == 50000):
        break

File_OBJ1.close()

##################################

#IP RANGE 50K-100K
####################################

File_OBJ1 = open('output2.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 50000 and count <= 100000):
        File_OBJ1.write(i)
    count += 1

    if (count == 100000):
        break

File_OBJ1.close()

##################################

#IP RANGE 100K-150K
####################################

File_OBJ1 = open('output3.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 100000 and count <= 150000):
        File_OBJ1.write(i)
    count += 1

    if (count == 150000):
        break

File_OBJ1.close()

##################################

#IP RANGE 100K-200K
####################################

File_OBJ1 = open('output4.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 150000 and count <= 200000):
        File_OBJ1.write(i)
    count += 1

    if (count == 200000):
        break

File_OBJ1.close()

##################################

#IP RANGE 200K-250K
####################################

File_OBJ1 = open('output5.txt', 'w')

count = 0
for i in MASTER_IP_BLACKLIST_LIST:
    if (count >= 200000 and count <= 250000):
        File_OBJ1.write(i)
    count += 1

    if (count == 250000):
        break

File_OBJ1.close()

##################################
