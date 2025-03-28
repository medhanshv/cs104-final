#include "../src/src1/comp.h"
#include "../src/src1/ops.h"
#include "../src/src1/find.h"
#include "../src/src2/rem.h"
#include "../src/src2/add.h"

#include <iostream>
using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    cout << "Sum: " << sum(v) << endl;
    cout << "Max: " << max(v) << endl;
    cout << "2nd Element" << get(v, 1) << endl;
    add_front(v, 0);
    rem_front(v);
    cout << "Sum: " << sum(v) << endl;
}