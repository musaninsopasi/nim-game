import random

def game_of_nim():
    # 10 ile 100 arasında rastgele sayıda misket üret
    number_of_marbles = random.randint(10, 100)
    # oyunu kimin başlattığına rastgele karar verin (oyuncu için 0, bilgisayar için 1)
    current_player = random.randint(0, 1)
    # bilgisayarın akıllı mı yoksa aptal mı oynayacağına rastgele karar verin (aptal için 0, smart için 1)
    comp_level = random.randint(0, 1)
    print("Mermer sayısı: ", number_of_marbles)

    while number_of_marbles > 0:
        # oyuncunun sırası
        if current_player == 0:
            player_choice = int(input("Sıra senin kaç bilye almak istersin? (1-" + str(number_of_marbles//2) + "): "))
            if player_choice >= 1 and player_choice <= number_of_marbles//2:
                number_of_marbles -= player_choice
                if number_of_marbles == 0:
                    print("Kazandınız!")
                    break
                else:
                    print("Kalan misket sayısı ", number_of_marbles)
                    current_player = 1
            else:
                print("Geçersiz Giriş. Lütfen 1 ile arasında bir sayı seçin" + str(number_of_marbles//2))
        else:
           # bilgisayarın sırası
            if comp_level == 0:
                # aptal mod: bilgisayar, kalan bilyelerin 1 ile yarısı arasında rastgele sayıda misket alır
                computer_choice = random.randint(1, number_of_marbles//2)
            else:
                #akıllı mod: bilgisayar kalan miktarı 2 eksi 1'in kuvveti yapmak için misket alır
                if number_of_marbles % 2 == 0:
                    computer_choice = random.randint(1, number_of_marbles//2)
                else:
                    computer_choice = number_of_marbles - (number_of_marbles // 2)
            number_of_marbles -= computer_choice
            if number_of_marbles == 0:
                print("Bilgisayar Kazandı!")
                break
            else:
                print("Bilgisayarı aldı", computer_choice, " Mermerler. Kalan Misket sayısı ", number_of_marbles)
                current_player = 0

game_of_nim()
