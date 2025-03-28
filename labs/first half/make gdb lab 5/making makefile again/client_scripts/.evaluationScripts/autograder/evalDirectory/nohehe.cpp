#include "deck.h"
#include <algorithm>
#include <random>

Deck::Deck() {
    // Initialize the deck with all 52 playing cards
    for (int i = 1; i <= 13; ++i) {
        for (int j = 0; j < 4; ++j) {
            cards.emplace_back(i, static_cast<Suit>(j));
        }
    }
}

void Deck::shuffle() {
    // Shuffle the deck
    // Fix a random seed for reproducibility
    std::mt19937 g(123);
    std::shuffle(cards.begin(), cards.end(), g);
}

Card Deck::dealCard() {
    // Deal a card from the top of the deck
    Card topCard = cards.back();
    cards.pop_back();
    return topCard;
}

void Deck::printDeck() const {
    // Print all the cards in the deck
    for (const auto& card : cards) {
        card.print();
    }
}
