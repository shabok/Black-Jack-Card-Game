import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards(card_list):
    return random.choice(card_list)

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)

def compare_scores(p_score, c_score):
    if p_score == c_score:
        return "Its a Draw!"
    elif c_score == 0:
        return "Opponent got Black Jack! You lose."
    elif p_score == 0:
        return "You got Black Jack! You win."
    elif p_score > 21:
        return "You went over 21! You lose."
    elif c_score > 21:
        return "Opponent went over 21! You win."
    elif p_score > c_score:
        return "You have a higer score! You win."
    else:
        return "Opponent has a higer score! You lose."


def play_Black_Jack():
    print(logo)
    player_cards = []
    computer_cards = []
    game_over = False

    for i in range (2):
        player_cards.append(draw_cards(cards))
        computer_cards.append(draw_cards(cards))
        draws_counter = 0 

    while not game_over:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards are: {player_cards} and your score is: {player_score}")
        print(f"Opponent's first card is: {computer_cards[0]} \n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True

        else:
            player_input = input("Type 'y' to draw another card, type 'n' to pass: ").lower()

            if player_input == "y":
                player_cards.append(draw_cards(cards))
                draws_counter+=1
            elif player_input == "n":
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_cards(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your cards are: {player_cards} and your score is: {player_score}")
    print(f"Opponent's cards are: {computer_cards} and opponent's score is: {computer_score} \n")

    result = compare_scores(player_score, computer_score)
    print(result)


wants_to_play = True

while wants_to_play:
    player_decision  = input("Do you want to play a game of Black Jack? Type 'y' for yes and 'n' for no: ").lower()
    print()
    if player_decision == "n":
        wants_to_play = False
    else:
        print("\n" * 20)
        play_Black_Jack()





