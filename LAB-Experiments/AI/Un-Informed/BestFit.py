#Best fit
def best_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_idx = -1

        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]

    return allocation

blocks = [100, 500, 200, 300, 600]

processes = [212, 417, 112, 426]

allocation = best_fit(blocks, processes)

for i in range(len(processes)):
    if allocation[i] != -1:
        print(f"Process {i+1} allocated to block {allocation[i]+1}")
    else:
        print(f"Process {i+1} not allocated")
