word = "height=170,weight=60"
print(word)
# bmi = ? (利用 spilt)
array = word.spilt(",")
print(array, array[0], array[1])

h_array = array[0].spilt("=")
print(h_array, h_array[0], h_array[1])

h = float(h_array[1])
print(h, type(h))

w_array = array[1].spilt("=")
print(w_array, w_array[0], w_array[1])
w = float(w_array[1])
print(w, type(w))

bmi = w / ((h/100)**2)
print(bmi)

