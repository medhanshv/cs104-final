#ifndef PLAYER_H
#define PLAYER_H

#include "card.h"
#include <vector>

class Player {
private:
    std::vector<Card> hand;
public:
    Player();
    void addToHand(Card card);
    void printHand() const;
};

#endif
