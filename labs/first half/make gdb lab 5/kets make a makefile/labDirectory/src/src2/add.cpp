#include "add.h"
#include <iostream>

void add_front(std::vector<int>& v, int n) {
    v.insert(v.begin(), n);
}

void add_back(std::vector<int>& v, int n) {
    v.push_back(n);
}