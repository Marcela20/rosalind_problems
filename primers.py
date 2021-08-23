forward = 'gGACGGAGGCGCGCCCGAGAUGAGUAGGCUGUCCCAUCAGGGGAGGAAUCGGGGACGGCUGAAAGGCGAGGGCGCCGAAGCGAGCAGAGUUCCUCCCGCUCUGCUUGGCUGGGGGUGAGGGGAAUACCCUUACCACUGUCGCGAAAGCGGAGAGCCGUCCA'.upper()
reverse = 'GATGAGTCAGATGAAGATACTTTCTAAgcGAATTC'.upper()

ready_rev = reverse[::-1].translate(str.maketrans("ATGC", "TACG"))

print("starter reverse: ", ready_rev.upper())


def GC_content(primer):
    proc_GC = 0
    proc_mut = (3 * 100) / len(primer)
    for i in primer:
        if i == 'G' or i == 'C':
            proc_GC += 1
    Tm: int = 2 * (len(primer) - proc_GC) + 4 * proc_GC
    Tm_mut_sub: int = 81.5 + (0.41 * (proc_GC * 100) / len(primer)) - (675 / len(primer)) - proc_mut

    return (proc_GC * 100) / len(primer), len(primer), Tm, Tm_mut_sub


print("for forward: ", GC_content(forward.upper()))
print("for reverse: ", GC_content(ready_rev.upper()))
