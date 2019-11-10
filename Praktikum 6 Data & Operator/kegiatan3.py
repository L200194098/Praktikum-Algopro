Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Zhen Haydar Raffly Aulia Bachtiar'
>>> Nim = 'L200194098'
>>> X = '1' + Nim[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #because the 'X' data had changed to integer data type
>>> type(b)
<class 'int'>
>>> #because the 'Nama' data has a 'len'intruction
>>> a / b
33,27272727272727‬
>>> #because the result of 1098 devided by 33 is 33,27272727272727‬
>>> a // b
33
>>> #because the meaning of '//' is division with rounding down
>>> 10 * (a-999)
99
>>> #because the value of 'a' minus 999 is 99, after that it will multipled
>>> b ** 2
1089
>>> #because the value of 'b' square is 1089
>>> a % b
3.3
>>> #because the meaning of '%' is the remainder of the division result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #because the 'c' data is a float
>>> a / c
87.84
>>> #because the result of 1098 devided by 12.5 is 87.84
>>> a // c
88
>>> #because the meaning '//' is division with rounding down
>>> a % c
1
>>> #because the meaning of '%' is the reminder of the division result
>>> c > b
False
>>> #because the value of 'c' < value of 'b'
>>> type(c > b)
<class 'bool'>
>>> #because the 'c > b' data had changed to boolean data type
>>> a > b and b > c
True
>>> #because 'a > b' is true and 'b > c' is true
>>> a > 1100 or b < 10
False
>>> #because 'a > 1100' is false or 'b < 10' is false

