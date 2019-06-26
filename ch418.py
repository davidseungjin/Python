# Type your code here

print("Davy's auto shop services")
servicelist = {"Oil change" : 35, "Tire rotation" : 19, "Car wash" : 7, "Car wax" : 12}

print('%s -- $%d' % ('Oil change', servicelist['Oil change']))
print('%s -- $%d' % ('Tire rotation', servicelist['Tire rotation']))
print('%s -- $%d' % ('Car wash', servicelist['Car wash']))
print('%s -- $%d' % ('Car wax', servicelist['Car wax']))

service1 = input('\nSelect first service:')
service2 = input('\nSelect second service:')

print("\n\nDavy's auto shop invoice\n")
if service1 in servicelist:
    print("Service 1: %s, $%d" % (service1, servicelist[service1]))
else:
    print("Service 1: No service")
if service2 in servicelist:
    print("Service 2: %s, $%d" % (service2, servicelist[service2]))
else:
    print("Service 2: No service")

if (service1 in servicelist) and (service2 in servicelist):
    print("\nTotal: $%d" % (servicelist[service1] + servicelist[service2]))
elif (service1 in servicelist):
    print("\nTotal: $%d" % (servicelist[service1]))
elif (service2 in servicelist):
    print("\nTotal: $%d" % (servicelist[service2]))
else:
    print("\nTotal: $0")
#lower_service = lower(service)
#if service in servicelist:
#    print('You entered: %s' % service)
#    print('Cost of %s: $%d' % (service.lower(), servicelist[service]))
#else:
#    print('You entered: %s' % service)
#    print('Error: Requested service is not recognized')
