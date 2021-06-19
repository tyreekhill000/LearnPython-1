appleTree=1

fruits=["bananana","orange"]
def scope():
    def toCheckLocal():
        fruits.append("apple")
        appleTree=2
        print(appleTree)

    def tocheckGlobal():
        print(appleTree)
    toCheckLocal()   
    tocheckGlobal()
scope()



print (fruits)


