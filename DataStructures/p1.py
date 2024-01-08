class Problem:
    def separateEvenOdd():
        arr = list(map(int, input('Enter elements with space : ').split()))

        even_arr = []
        odd_arr = []
        
        for num in arr:
            if num%2==0:
                even_arr.append(num)
            else:
                odd_arr.append(num)

        ans = []
        ans = even_arr+odd_arr
        return ans

answer = Problem.separateEvenOdd()
print(answer)