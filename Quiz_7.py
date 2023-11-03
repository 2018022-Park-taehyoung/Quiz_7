high = int(input('별의 높이를 입력하세요: '))
for i in range(1, high+1):
    A = (high-i) * (" ")
    B = (2*i-1) * ('*')
    print(A+B)
    end="\n"
