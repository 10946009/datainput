import subprocess
import os
import random
import glob
#############################################################################

# 1. 請先把解答程式放在ans.py
# 2. 確定terminal開在generator.py同一層的資料夾 ex: C:/xxx/xxx/a001
# 3. 設定sample的資料
# 4. 設定測資範本
    
###############################################################################

#讀取sample的in檔案
sample = []
samplein = len(glob.glob(os.path.join(os.getcwd() +"\\data\sample\\", "*.in")))
for i in range(1,samplein+1):
    with open(os.getcwd() + f"\\data\sample\\{i}.in","r") as f :
        stamp = ""
        for i in f.readlines():
            stamp += i
    sample.append(stamp)

# 在這邊定義測資數量!!!
secret_count = 5

# 定義隱藏測資邏輯
secret = []
for i in range(secret_count):
    sample_input = ''
    inputlist = []
    M = random.randrange(1, 21)
    N = random.randrange(1,21)
    K = random.randrange(0,1000)
    sample_input = f"{M} {N} {K}"
    inputlist.append(sample_input+"\n")
    for r in range(0,M):
        sample_input = ''
        for n in range(0,N):
            zero = random.randrange(0,100)
            p = random.randrange(0,30)
            if zero > 90 :
                sample_input += f"{p} "
            else:
                sample_input += "0 "
        inputlist.append(sample_input+"\n")
    strinputlist = ''.join(inputlist)
    secret.append(strinputlist)


# 把測資跟secret放進ans.py並取出output
def generate_in_ans_file(input, path, number):
    p = subprocess.Popen(os.getcwd() + "\\ans.py",
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8', shell=True)

    output, error = p.communicate(input=input)
    print(input, output, path, number)
    with open(f"{path}\\{number}.in",'w', encoding = 'utf-8') as f:
        f.write(input)
    with open(f"{path}\\{number}.ans",'w', encoding = 'utf-8') as f:
        f.write(output)

# 定義路徑
sample_path = os.getcwd() + "\\data\\sample"
secret_path = os.getcwd() + "\\data\\secret"
path = [
    os.getcwd() + "\\data",
    sample_path,
    secret_path
]

# 建立sample跟secret資料夾
for p in path:
    if not os.path.isdir(p):
        os.mkdir(p)

# 產生input跟ans
number = 0
for i, d in enumerate(sample):
    number += 1
    generate_in_ans_file(d, sample_path, number)
for i, d in enumerate(secret):
    number += 1
    generate_in_ans_file(d, secret_path, number)

