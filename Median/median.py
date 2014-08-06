import heapq

def clean_remove_dict(my_heap, remove_dict, converter):
    if my_heap:
        while converter(my_heap[0]) in remove_dict:
            temp = converter(heapq.heappop(my_heap))
            remove_dict[temp] -= 1
                          
            if remove_dict[temp] == 0:
                del remove_dict[temp]
            
            if not my_heap:
                break

def get_median(x, my_heap, remove_dict, converter):
    median = converter(heapq.heappop(my_heap))
    heapq.heappush(my_heap, converter(x))
                        
    clean_remove_dict(my_heap, remove_dict, converter)
            
    return median

def median(a,z):
    lower_heap = []
    greater_heap = []

    add_dict = {}
    remove_dict = {}

    median = None
    
    for i in range(0, N):
        x = z[i]
        if a[i] == 'a':
            add_dict[x] = add_dict.get(x, 0) + 1
            
            if median is None:
                if not greater_heap and not lower_heap:
                    median = x
                else:
                    if x <= greater_heap[0] and x >= 0 - lower_heap[0]:
                        median = x
                    elif x > greater_heap[0]:
                        median = get_median(x, greater_heap, remove_dict, lambda y: y)
                    else:
                        median = get_median(x, lower_heap, remove_dict, lambda y: -y)
                
                print median
            else:
                if x < median:
                    heapq.heappush(lower_heap, -x)
                    heapq.heappush(greater_heap, median)
                else:
                    heapq.heappush(lower_heap, -median)
                    heapq.heappush(greater_heap, x)
                
                median = None
                result = float(greater_heap[0] - lower_heap[0]) / 2
                
                if result.is_integer():
                    print int(result)
                else:
                    print result
        else:
            if x not in add_dict:
                print 'Wrong!'
            else:
                add_dict[x] -= 1
                if add_dict[x] == 0:
                    del add_dict[x]
                
                if median is None:
                    median_from_lower = False
                    
                    if x == greater_heap[0]:
                        heapq.heappop(greater_heap)
                        clean_remove_dict(greater_heap, remove_dict, lambda y: y)
                        median_from_lower = True
                    elif x == -lower_heap[0]:
                        heapq.heappop(lower_heap)
                        clean_remove_dict(lower_heap, remove_dict, lambda y: -y)
                    else:
                        remove_dict[x] = remove_dict.get(x, 0) + 1
                        
                        if x > greater_heap[0]:
                            median_from_lower = True
                        
                    if median_from_lower:
                        median = 0 - heapq.heappop(lower_heap)
                        clean_remove_dict(lower_heap, remove_dict, lambda y: -y)
                    else:
                        median = heapq.heappop(greater_heap)
                        clean_remove_dict(greater_heap, remove_dict, lambda y: y)
                    
                    print median
                else:
                    if x != median:
                        remove_dict[x] = remove_dict.get(x, 0) + 1
                    
                        if x >= greater_heap[0]:
                            heapq.heappush(greater_heap, median)
                        else:
                            heapq.heappush(lower_heap, -median)
                        
                    median = None
                    
                    if not greater_heap and not lower_heap:
                        print 'Wrong!'
                    else:
                        result = float(greater_heap[0] - lower_heap[0]) / 2
                        if result.is_integer():
                            print int(result)
                        else:
                            print result
                    
N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
median(s,x)