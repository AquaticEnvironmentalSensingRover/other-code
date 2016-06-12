import threading, time

class testClass:
    thread = None
    running = None
    
    def __init__(self):
        self.thread = threading.Thread(target=self.runThis)
        self.thread.daemon = False
        self.thread.start()
        self.running = True
    
    def runThis(self):
        while True:
            print("hello")
            
            if not self.running == False:
                time.sleep(1)
            else:
                break

        
if __name__ == "__main__":
    x = testClass()
    
    #time.sleep(2)
    x.running = False
    x.thread.join()