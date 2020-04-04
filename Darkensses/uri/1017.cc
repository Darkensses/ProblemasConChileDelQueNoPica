#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    double a,b,r;
    cin >> a >> b;
    r = a * b / 12.0;
    cout<<setprecision(3)<<fixed;
    cout << r << '\n';
    return 0;
}