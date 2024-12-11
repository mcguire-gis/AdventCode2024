import pandas as pd

#Testing file
input_file = (r"C:\Users\amcguire\Desktop\test.xlsx")

#Day2 file
#input_file = (r"C:\Users\amcguire\Desktop\day2.xlsx")
df = pd.read_excel(input_file, header = None, na_filter=False)

safe_count = 0
unsafe_count = 0

for index,row in df.iterrows():
    safe = False
    inc = row.is_monotonic_increasing
    dec = row.is_monotonic_decreasing
    unique = row.is_unique
    if not ((inc or dec) and unique):
        unsafe_count = unsafe_count + 1
        print("Row ",index+1,":",safe,"not increasing/decreasing")
    else:
        for i,j in enumerate(row):
            if i == 0:
                pass
            else:
                diff = abs(j - row[i-1])
                if diff == 0 or diff > 3:
                    unsafe_count = unsafe_count + 1
                    print("Row ", index+1, ":", safe, "difference too large/small")
                    break
                elif i == len(row)-1:
                    safe = True
                    safe_count = safe_count +1
                    print ("Row ",index + 1,safe)


print("Safe: ",safe_count)
print("Unsafe: ",unsafe_count)
