#List Barang
barang = [ 
    ["kipas Angin", "TV", "Mesin Cuci", "Ac", "kulkas", "Cancel" ],
    [1000000, 2000000, 3000000, 4000000, 5000000],
    [5,10,20]
] 


print("\n====Selamat Datang di Toserba Elektronik====")
nama = input("\nNama Pelanggan : ")

print("\n===============Menu Barang==================")
bar = barang[0]
for nabar in bar:
    no = bar.index(nabar)+1
    print(no,nabar)
print("===============================================")

#Muhammad Syamil Al Faqih
#0110221218
selectmenu = input("Silahkan Pilih Barang: ")

#Logic
if selectmenu == "4":
    print("\nNote: mendapatkan diskon",barang[2][2],"% jika jumlah beli 5 atau lebih")
elif selectmenu =="5":
    print("\nNote: mendapatkan diskon",barang[2][1],"% jika jumlah beli 3 atau lebih")

elif selectmenu != "1" and selectmenu !="2" and selectmenu !="3" and selectmenu !="4" and selectmenu !="5"and selectmenu !="6": 
   print("Error. Maaf, permintaan tidak tersedia")  
   exit()

elif selectmenu == "6":
 print("====================================================")
 print("TERIMAKASIH TELAH MELIHAT TOKO KAMI")
 print("====================================================")
 exit()

jumbar = int(input("\nBerapa jumlah barang yang diinginkan :"))
konfir = input("Konfirmasi: Apakah anda ingin melanjutkan transaksi/ y/n")

if konfir == "n":
    print("====================================================")
    print("TERIMAKASIH TELAH MELIHAT TOKO KAMI")
    print("====================================================")
    exit()

elif konfir != "n" and konfir != "y" :
    print("Error, enter only the letter y or n")
    exit()

print("====================================================")
#Kipas Angin
if selectmenu == "1":
    print(
        "Nama Produk \t:",barang[0][0],
        "\nHarga Produk \t: Rp.",barang[1][0],
    )
#TV
elif selectmenu == "2":
    print(
        "Nama Produk \t:",barang[0][1],
        "\nHarga Produk \t: Rp.",barang[1][1],
    )
#Mesin Cuci
elif selectmenu == "3":
    print(
        "Nama Produk \t:",barang[0][2],
        "\nHarga Produk \t: Rp.",barang[1][2],
    )
#AC
elif selectmenu == "4":
    print(
        "Nama Produk \t:",barang[0][3],
        "\nHarga Produk \t: Rp.",barang[1][3],
    )
#Kulkas
elif selectmenu == "5":
    print(
        "Nama Produk \t:",barang[0][4],
        "\nHarga Produk \t: Rp.",barang[1][4],
    )

print("====================================================")

if selectmenu == "1" and konfir =="y" :
    harko = jumbar * barang[1][0]
    disc = harko * barang[2][0] / 100

elif selectmenu == "2" and konfir =="y" :
    harko = jumbar * barang[1][1]
    disc = harko * barang[2][0] / 100

elif selectmenu == "3" and konfir =="y" :
    harko = jumbar * barang[1][2]
    disc = harko * barang[2][0] / 100

elif selectmenu == "4" and konfir =="y" :
    if jumbar >= 5:
        harko = jumbar * barang[1][3]
        disc = harko * barang[2][2] / 100
    else:
        harko = jumbar * barang[1][3]
        disc = harko * barang[2][0] / 100

elif selectmenu == "5" and konfir =="y" :
    if jumbar >= 3:
        harko = jumbar * barang[1][4]
        disc = harko * barang[2][1] / 100
    else:
        harko = jumbar * barang[1][4]
        disc = harko * barang[2][0] / 100

ppn = (harko-disc) * barang[2][1] / 100
haber = (harko-disc) + ppn

if selectmenu =="4"and konfir =="y" and jumbar >= 5:
    print(
        "Nama Pelanggan \t:",str(nama),
        "\nJumlah Beli \t:",int(jumbar),
        "\nHarga Kotor \t: Rp.",float(harko),
        "\nDiskon \t\t: Rp.",float(disc),"(",barang[2][2],"%)"
        "\nPPn 10% \t: Rp.",ppn,
        "\nHarga Bersih \t: Rp.",haber
    )   

elif selectmenu =="5"and konfir =="y" and jumbar >= 3:
    print(
        "Nama Pelanggan \t:",str(nama),
        "\nJumlah Beli \t:",int(jumbar),
        "\nHarga Kotor \t: Rp.",float(harko),
        "\nDiskon \t\t: Rp.",float(disc),"(",barang[2][1],"%)"
        "\nPPn 10% \t: Rp.",ppn,
        "\nHarga Bersih \t: Rp.",haber
    )   

elif konfir =="y":
    print(
        "Nama Pelanggan \t:",str(nama),
        "\nJumlah Beli \t:",int(jumbar),
        "\nHarga Kotor \t: Rp.",float(harko),
        "\nDiskon \t\t: Rp.",float(disc),"(",int(barang[2][0]),"%)"
        "\nPPn 10% \t: Rp.",ppn,
        "\nHarga Bersih \t: Rp.",haber
    ) 
print("====================================================") 
    


        



























































