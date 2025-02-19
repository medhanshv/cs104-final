#include "find.h"

int find(const std::vector<int>& v, int n) {
    for (std::size_t i = 0; i < v.size(); i++) {
        if (v[i] == n) {
            return i;
        }
    }
    return -1;
}

int get(const std::vector<int>& v, int idx) {
    return v[idx];
}