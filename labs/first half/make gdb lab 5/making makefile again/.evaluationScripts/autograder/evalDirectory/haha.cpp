#include "player.h"

Player::Player() {}

void Player::addToHand(Card card) {
    hand.push_back(card);
}

void Player::printHand() const {
    for (const auto& card : hand) {
        card.print();
    }
}
