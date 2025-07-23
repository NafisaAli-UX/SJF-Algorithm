n = int(input("Enter number of processes: "))
p = []
at = []
bt = []

for i in range(n):
    p_name = input(f"Enter name of process {i+1}: ")
    a = int(input(f"Enter arrival time of {p_name}: "))
    b = int(input(f"Enter burst time of {p_name}: "))
    p.append(p_name)
    at.append(a)
    bt.append(b)

ct = [0] * n
tat = [0] * n
wt = [0] * n
done = [False] * n

current_time = 0
completed = 0

while completed < n:
    ready = []
    for i in range(n):
        if at[i] <= current_time and not done[i]:
            ready.append(i)

    if not ready:
        current_time += 1
        continue

    min_index = ready[0]
    for i in ready:
        if bt[i] < bt[min_index]:
            min_index = i

    current_time += bt[min_index]
    ct[min_index] = current_time
    tat[min_index] = ct[min_index] - at[min_index]
    wt[min_index] = tat[min_index] - bt[min_index]
    done[min_index] = True
    completed += 1

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{p[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
