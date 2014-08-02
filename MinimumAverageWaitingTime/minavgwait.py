import heapq

def get_avg_wait_time(orders, num_customers):
	index = 0
	queue = []
	finish_time = 0
	running_tally = 0
	
	while index < len(orders) or queue:
		if not queue:
			finish_time, duration = orders[index]
			running_tally += duration
			finish_time += duration
			
			index += 1
		else:
			duration, order_time = heapq.heappop(queue)
			running_tally += duration + finish_time - order_time
			
			finish_time += duration
		
		while index < len(orders) and orders[index][0] <= finish_time:
			order_time, duration = orders[index]
			heapq.heappush(queue, (duration, order_time))
			
			index += 1
	
	return running_tally / num_customers

orders = []
num_customers = int(raw_input())
for i in range(num_customers):
	orders.append(map(long, raw_input().split()))

orders.sort()
print(get_avg_wait_time(orders, num_customers))