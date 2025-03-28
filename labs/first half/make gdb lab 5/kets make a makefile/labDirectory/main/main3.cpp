#include "../src/src1/ops.h"
#include "../src/src1/find.h"
#include "../src/src2/add.h"

#include <iostream>
using namespace std;

int main(){
    vector <int> v = {1, 2, 3};
    int idx = find(v, 2);
    cout << "Index: " << idx << endl;
    cout << "Element: " << get(v, idx) << endl;
    add_back(v, 4);
    cout << "Sum: " << sum(v) << endl;
}