#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, bn[7] = {100,50,20,10,5,2,1},r;
    cin >> n;
    r = n ;
    cout << n << '\n';
    for (int i = 0; i < sizeof(bn) / sizeof(bn[0]); i++) {
        r = n / bn[i];        
        cout << r << " nota(s) de R$ "<< bn[i] << ",00" << '\n';
        n = n%bn[i];
    }
        
    return 0;
}