class transformation():
    def transformation(self, a, b, res, step):
        res.append(b)
        step += 1
        if a < b and (b % 2 != 0 or b % 10 != 1):
            if b % 2 == 0:
                b //= 2
            elif b % 10 == 1:
                b = (b - 1) // 10
            return transformation().transformation(a, b, res, step)
        elif a > b:
            return print("No")
        elif a < b and b % 2 != 0 and b % 10 != 1:
            return print("No")
        elif a == b:
            return print('Yes\n', step, "\n", *res[::-1])
if __name__ == "__main__":
    number=transformation()
    x,y=map(int,input("Please enter the two numbers! For example: 2 162 \n").split(' '))
    res1=[]
    step1=0
    number.transformation(x,y,res1,step1)


