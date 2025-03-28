#include "card.h"

int main() {
    Card c1(5, Suit::Hearts);
    c1.print();
    Card c2(10, Suit::Diamonds);
    c2.print();
    Card c3(13, Suit::Clubs);
    c3.print();

    return 0;
}
