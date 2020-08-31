
import unittest 
import primeornot    

class unittestprime(unittest.TestCase):    
    def testprime1(self):     
        num = 36     
        result = primeornot.isprimeornot(num)  
        self.assertAlmostEqual(result,False)    
    def testprime2(self):   
        num = 9719      
        result = primeornot.isprimeornot(num)     
        self.assertAlmostEqual(result,True)       
if __name__ == "__main__":
    unittest.main()
