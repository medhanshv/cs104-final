#ifndef CARD_H
#define CARD_H

enum class Suit { Hearts, Diamonds, Clubs, Spades };

class Card {
private:
    int value;
    Suit suit;
public:
    Card(int value, Suit suit);
    void print() const;
};

#endif
