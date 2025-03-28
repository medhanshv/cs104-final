#include "rem.h"

void rem_front(std::vector<int>& v) {
    v.erase(v.begin());
}

void rem_back(std::vector<int>& v) {
    v.pop_back();
}