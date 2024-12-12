#Day 2, Part 1
##SOLVED

import pandas as pd

#Testing file
#input_file = (r"C:\Users\amcguire\Desktop\test.xlsx")

#Day2 file
input_file = (r"C:\Users\amcguire\Desktop\day2.xlsx")
df = pd.read_excel(input_file, header = None)

safe_count = 0
unsafe_count = 0
bad_rows = []
for index,row in df.iterrows():
    row.dropna(inplace = True)
    safe = False
    inc = row.is_monotonic_increasing
    dec = row.is_monotonic_decreasing
    unique = row.is_unique
    if not ((inc or dec) and unique):
        unsafe_count = unsafe_count + 1
        print("Row ",index+1,":",safe,"not increasing/decreasing")
        bad_rows.append(row.to_list())
    else:
        for i,j in enumerate(row):
            if i == 0:
                pass
            else:
                diff = abs(j - row[i-1])
                if diff == 0 or diff > 3:
                    unsafe_count = unsafe_count + 1
                    print("Row ", index+1, ":", safe, "difference too large/small")
                    bad_rows.append(row.to_list())
                    break
                elif i == len(row)-1:
                    safe = True
                    safe_count = safe_count +1
                    print ("Row ",index + 1,safe)

print(len(bad_rows),"to retest")
retest_true = 0
for i in bad_rows:
    test_rows = []
    temp_df = pd.DataFrame(None)
    j = 0
    while j < len(i):
        temp1 = i.copy()
        del temp1[j]
        test_rows.append(temp1)
        j= j + 1
    temp_df = pd.DataFrame(test_rows)

    results3 = []
    for index3, row3 in temp_df.iterrows():
        row3.dropna(inplace=True)
        fail = False
        inc3 = row3.is_monotonic_increasing
        dec3 = row3.is_monotonic_decreasing
        unique3 = row3.is_unique
        if not ((inc3 or dec3) and unique3):
            fail = True
        else:
            for i3, j3 in enumerate(row3):
                if i3 == 0:
                    pass
                else:
                    diff3 = abs(j3 - row3[i3 - 1])
                    if diff3 == 0 or diff3 > 3:
                        fail = True
                    elif i3 == len(row3)-1 and not fail:
                        results3.append(True)
    if True in results3:
        print(i,"passes retest")
        retest_true = retest_true + 1
    else:
        print(i,"FAIL")

print("Safe Round 1: ",safe_count)
print("Safe Round 2: ",retest_true)
print("Total Safe: ",safe_count+retest_true)
