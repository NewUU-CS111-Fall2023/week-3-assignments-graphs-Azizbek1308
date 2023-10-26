class Genome():
    def Genome(self,n,string):
        res = set()
        for j in string:
            res.add(j)
        for i in range(1, n, 1):
            string = str(input(f"Please enter {i+1} descriptions of a fragment\n"))
            for j in string:
                res.add(j)
        res = "".join(sorted(list(res)))
        return print(res)

if __name__=="__main__":
    obj=Genome()
    obj.Genome(int(input("Please enter the number of genome fragments \n")),str(input("Please enter 1 descriptions of a fragment\n")))

