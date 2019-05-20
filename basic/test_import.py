import test_mod 

test1=test_mod.Test_mod()
test1.test_method(1)


from test_mod import Test_mod as T

test2=T()
test2.test_method("2")
    
