#include "../src/src1/comp.h"
#include "../src/src1/ops.h"
#include "../src/src1/find.h"
#include "../src/src2/rem.h"
#include "../src/src2/add.h"

#include <iostream>
using namespace std;

int main(){
    vector<int> v = {1, 2, 4, 2};
    cout << "sum: " << sum(v) << endl;
    cout << "Min: " << min(v) << endl;
    cout << "4th Element: " << get(v, 3) << endl;
    add_back(v,3);
    rem_front(v);
    cout << "Sum" << sum(v) << endl;
}