from multiprocessing import Pool

def func(num):
    return (num+100)

if __name__ == '__main__':
    p = Pool(processes = 5)
    lis = p.map(func, range(10))
    p.close()
    print(lis)
