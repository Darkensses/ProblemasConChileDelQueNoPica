#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t, r;
    stringstream tt;
    cin >> t;
    r = t / 365;
    cout << r << " ano(s)" << '\n';
    t = t % 365;
    r = t / 30;
    cout << r << " mes(es)" << '\n';
    r = t % 30;
    cout << r << " dia(s)" << '\n';    
    return 0;
}