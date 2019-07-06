from StoreData import StoreData

my_service_call_data_store = StoreData()

count_service_calls = my_service_call_data_store.get_data('count_service_calls')
print('Starting service Calls: ' + str(count_service_calls))

if str(count_service_calls) == '':
	count_service_calls = 1
else:
	count_service_calls += 1
my_service_call_data_store.set_data('count_service_calls', count_service_calls)

count_service_calls = my_service_call_data_store.get_data('count_service_calls')
print('Ending service Calls: ' + str(count_service_calls))
