from f5.bigip import ManagementRoot

# Connect to the BigIP
mgmt = ManagementRoot("172.16.122.131", "admin", "admin")

virtual = mgmt.tm.ltm.virtuals.virtual.load(partition='Common', name='vshttp')
print(virtual.name)
print(virtual.rules)



