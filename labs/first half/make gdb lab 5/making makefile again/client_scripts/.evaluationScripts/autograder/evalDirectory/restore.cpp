#include "deck.h"
#include "player.h"
#include <iostream>

int main() {
    Deck deck;
    deck.shuffle();
    deck.printDeck();
    std::cout << "____________________________" << std::endl; 
    Player player;
    player.addToHand(deck.dealCard());
    player.printHand();
    return 0;
}
