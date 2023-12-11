from luo_peli import Pelitehdas

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            kaksinpeli = Pelitehdas.luo_helppo_yksinpeli()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            yksinpeli = Pelitehdas.luo_helppo_yksinpeli()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            haastava_yksinpeli = Pelitehdas.luo_vaikea_yksinpeli()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
