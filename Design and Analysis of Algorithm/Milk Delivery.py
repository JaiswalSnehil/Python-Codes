'''Milk Delivery
A private dairy has n milk delivery vans. The company has mapped out n delivery routes. Each route has to be served once in 
the morning and once in the evening. Each van covers one morning route and one evening route, but these may be different 
routes. Each route has fixed delivery volumes in the morning and evening, possibly different.
The dairy's license limits the number of packets a van can deliver to p packets per day. If a van delivers more than p 
packets, the company has to pay a fine of f per additional packet.
Given the delivery volumes of the morning and evening routes, your task is to find the minimum fine the company has to pay 
if it optimally allocates morning and evening routes to each delivery van.
For instance, suppose there are 3 routes, the packet limit per day is 24, the fine per additional packet is 4, the morning 
volumes for the three routes are [10,17,12] and the evening volumes for the three routes are [11,9,24]. Then, the minimum 
fine to be paid is 48. This can be achieved by pairing the routes as follows: (10,24), (17,9), (12,11).

Solution hint
Minimize the average morning plus evening volume by pairing up small volumes with large volumes.

Input format
The first line of the input has three space-separated integers n, p and f, where n is the number of milk routes, p is the 
daily packet limit and f is the fine to be paid for each packet above the limit.
The second line has n space-separated integers, corresponding to the morning delivery volumes of delivery routes 1,2,…n.
The third line has n space-separated integers, corresponding to the evening delivery volumes of delivery routes 1,2,…n.

Output format
Your output should be a single integer, the minimum fine to be paid if the routes are paired up optimally.

Test Data:
You may assume that 1 ≤ n ≤ 5000. All values are positive integers.

Sample Input:
3 24 4
10 17 12
11 9 24
Sample Output:
48'''

'''def calculate_min_fine():
    # Read n, p, f
    n, p, f = map(int, input().split())
    
    # Read morning and evening volumes
    morning = list(map(int, input().split()))
    evening = list(map(int, input().split()))
    
    # Sort morning ascending, evening descending
    morning.sort()
    evening.sort(reverse=True)
    
    total_fine = 0
    
    for i in range(n):
        daily_total = morning[i] + evening[i]
        if daily_total > p:
            excess = daily_total - p
            total_fine += excess * f
            
    print(total_fine)'''

import sys

def minimum_fine(n, p, f, morning, evening):
    # Sort morning ascending
    morning.sort()
    # Sort evening descending
    evening.sort(reverse=True)

    total_fine = 0

    for i in range(n):
        total_packets = morning[i] + evening[i]
        if total_packets > p:
            total_fine += (total_packets - p) * f

    return total_fine


# -------- Input --------
n, p, f = map(int, input().split())
morning = list(map(int, input().split()))
evening = list(map(int, input().split()))

# -------- Output --------
print(minimum_fine(n, p, f, morning, evening))