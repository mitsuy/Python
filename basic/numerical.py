############################################
#
#  How to treat numerical values
#
#
#  Written by M.YAGYU 10 May 2019
#
############################################

# program numerical

###
### Convert string to numerical value
###

tmp_str='100'
print(int(tmp_str)+200)

fstr='1.08'
print(float(fstr)+int(tmp_str))


###
### Complex number
###

tmp_complx=5+3j
print(tmp_complx)
print('real : ',tmp_complx.real)
print('imag : ',tmp_complx.imag)


# end program numerical
