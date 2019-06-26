# Type your code here

servicelist = {"Oil change" : 35, "Tire rotation" : 19, "Car wash" : 7}
service = input('Enter desired auto service:\n')
#lower_service = lower(service)
if service in servicelist:
    print('You entered: %s' % service)
    print('Cost of %s: $%d' % (service.lower(), servicelist[service]))
else:
    print('You entered: %s' % service)
    print('Error: Requested service is not recognized')
