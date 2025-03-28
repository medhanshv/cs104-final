#include "ops.h"
#include <iostream>

int sum(const std::vector<int>& v) {
    int sum = 0;
    for (int i : v) {
        sum += i;
    }
    return sum;
}

int product(const std::vector<int>& v) {
    int product = 1;
    for (int i : v) {
        product *= i;
    }
    return product;
}