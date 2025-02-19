#include "comp.h"
#include <iostream>

int max(const std::vector<int>& v) {
    int max = v[0];
    for (int i : v) {
        if (i > max) {
            max = i;
        }
    }
    return max;
}

int min(const std::vector<int>& v) {
    int min = v[0];
    for (int i : v) {
        if (i < min) {
            min = i;
        }
    }
    return min;
}