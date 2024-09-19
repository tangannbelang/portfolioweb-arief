temperature:float = float(input("Masukkan suhu (dalam derajat Celsius): "))

# Pengecekan variabel temperature sesuai dengan kebutuhan.
if temperature > 100:
    print("Air berubah menjadi gas.")
elif 0.0 <= temperature <= 100:
    print("Air tetap berupa cairan.")
else:
    print("Air berubah menjadi padat.")