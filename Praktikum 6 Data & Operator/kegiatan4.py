Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Zhen Haydar Raffly Aulia Bachtiar"
>>> NIM = 4098
>>> Tinggi = 1.76
>>> Berat = 87
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Because the "Aku" data is written in perentheses
>>> Aku[0]
2001
>>> # Because the first object in "Aku" data is "TahunLahir", the value of "TahunLahir" is 2001
>>> a = NIM % 4; Aku[a]
87
>>> # Because the remaining result of 4098 divided by 4 is 2, so the result of Aku[1] is 87
>>> type(Aku[a])
<class 'int'>
>>> # Because the value of "Berat" is 1, 1 is an integer data type
>>> Aku[a:4}
(87, 1.76, 4098)
>>> # Because the object in "Aku" start from "Berat, Tinggi, NIM, Nama"
>>> type(Aku[4])
<class 'str'>
>>> # Because the "Aku[4]" data is string
>>> Aku[0] = "ok"
Traceback (most recent call last):
    File "<pyshell#19>", line 1, in <module>
      Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> # Because "Aku" data type is tuple, so can't changed with another data
>>> type(Data)
>>> # Because the object in "Aku" start "Berat, Tinggi, NIM, Nama"
>>> type(Aku[4])
<class 'str'>
>>> # Because the "Aku[4]" data is string
>>> Aku[0] = "ok"
Traceback (most recent call last):
    File "<pyshell#19>", line 1, in <module>
      Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> # Because "Aku" data type is tuple, so can't be changed with another data
>>> type(Data)
<class 'list'>
>>> # Because the "Data" data is written in brackets
>>> type(Data[4])
<class 'str'>
>>> # Because the value of "Data[4]" data is string
>>> Data[4][5]
' '
>>> # Because in value of "Data[4]" object in the value start in 5, and this is "space"
>>> Data[4][a:6]
'ehn '
>>> # Because in value "Data[4]" object in the value start from "a" until "5" is "ehn "
>>> Data[0] = "ok": Data
['ok', 87, 1.76, 4098, 'Zhen Haydar Raffly Aulia Bachtiar']
>>> # Because the first object has changed by "ok", and it call all list in "Data"
>>> Data[-1]
'Zhen Haydar Raffly Aulia Bachtiar'
>>> # Because it is call from rear list
>>> range(1)
range (0, 1)
>>> # Because range of 1 is (0,1)





























