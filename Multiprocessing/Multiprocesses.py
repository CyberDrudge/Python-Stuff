import multiprocessing

def spawn(num):
    print("spawned! {}".format(num))
    
if __name__ == '__main__':
    for i in range(10):
        P = multiprocessing.Process(target=spawn, args=(i,))
        P.start()
        P.join()      