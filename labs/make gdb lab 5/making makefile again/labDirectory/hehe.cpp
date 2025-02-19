#include "card.h"
#include <iostream>

Card::Card(int value, Suit suit) : value(value), suit(suit) {}

void Card::print() const {
    // Print the card value and suit
    // You can define how you want to print it
    std::cout << value << " of ";
    switch (suit) {
        case Suit::Hearts:
            std::cout << "Hearts";
            break;
        case Suit::Diamonds:
            std::cout << "Diamonds";
            break;
        case Suit::Clubs:
            std::cout << "Clubs";
            break;
        case Suit::Spades:
            std::cout << "Spades";
            break;
    }
    std::cout << std::endl;
}
