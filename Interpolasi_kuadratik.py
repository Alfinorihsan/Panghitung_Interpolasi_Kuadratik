# Soal

# Tentukan Nilai y dengan titik x = 2.6 yang berada 
# di antara titik (0;0.2), (1;1.7) dan (4;3.2) dengan menggunakan 
# rumus interpolasi kuadratik berserta grafiknya!


#import library untuk dataset x dan y
import numpy as np

#Import library matplotlib untuk grafik cartesius
import matplotlib.pyplot as plt

#import library dari scipy untuk membuat garis curvy
from scipy.interpolate import make_interp_spline


#Identitas
print("""
Nama         : Alfi Nor Ihsan
NIM          : 2109106018
Mata Kuliah  : Alogaritma dan Pemrograman Lanjut
""")

#Deklarasi variabel dan Awal Program
P = [[], [], []]
x = 0
print("\n--- Program Penghitung Interpolasi Kuadrattik ---")

#Perulangan Input 3 titik dan niai x untuk mencari nilai y
for x in range(3):
    inp = float(input(
        "\n Silahkan Masukan nilai x titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    inp = float(input(
        " Silahkan Masukan nilai y titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    print(" Diketahui : Titik "+str(x+1), "(P"+str(x+1)+") = (", P[x][0], ";", P[x][1], ")")
x = float(input(
    "\n Silahkan Masukan nilai x : "
))
print(" > Nilai x = "+str(x))

#Penerapan Rumus
x1 = P[0][0]
y1 = P[0][1]
x2 = P[1][0]
y2 = P[1][1]
x3 = P[2][0]
y3 = P[2][1]
y = (y1*(x-x2)*(x-x3)) / ((x1-x2)*(x1-x3)) + (y2*(x-x1)*(x-x3)) / ((x2-x1)*(x2-x3)) + (y3*(x-x1)*(x-x2)) / ((x3-x1)*(x3-x2))

#Penerapan Grafik Kordinat
data_x = [x1, x2, x3, x]
data_y = [y1, y2, y3, y]

#prosedur partisi quicksort
def partisi(kiri, kanan, arrayx, arrayy):
    pivot, ptr = arrayx[kanan], kiri
    for i in range(kiri, kanan):
        if arrayx[i] <= pivot:
            arrayx[i], arrayx[ptr] = arrayx[ptr], arrayx[i]
            arrayy[i], arrayy[ptr] = arrayy[ptr], arrayy[i]
            ptr += 1
    arrayx[ptr], arrayx[kanan] = arrayx[kanan], arrayx[ptr]
    arrayy[ptr], arrayy[kanan] = arrayy[kanan], arrayy[ptr]
    return ptr

#prosedur untuk mengurutkan garis titik
def quicksort(kiri, kanan, arrayx, arrayy, xy):
    if len(arrayx) == 1:
        return arrayx
    if kiri < kanan:
        pi = partisi(kiri, kanan, arrayx, arrayy)
        quicksort(kiri, pi-1, arrayx, arrayy, "x")
        quicksort(pi+1, kanan, arrayx, arrayy, "x")
    if xy == "x":
        return arrayx
    else:
        return arrayy

data_x = quicksort(0, len(data_x)-1, data_x, data_y, "x")
data_y = quicksort(0, len(data_x)-1, data_x, data_y, "y")
X = np.array(data_x)
Y = np.array(data_y)

X_Y_Spline = make_interp_spline(X, Y)
X_ = np.linspace(X.min(), X.max(), 500)
Y_ = X_Y_Spline(X_)


#program yang digunakan untuk menampilkan grafik hasil 
plt.title("Grafik Hasil")
plt.scatter(data_x, data_y, color="darkblue", marker='o', label='Titik(P)')
plt.plot(X_, Y_)

plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.grid(True)
plt.legend()

#Hasil dari seluruh operasi
print("\n Nilai y adalah : "+str(y)+"\n > Titik ( "+str(x)+"; "+str(y)+" )")
plt.show()
