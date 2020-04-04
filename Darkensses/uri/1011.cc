#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    double x,r;

    cin>>x;
    x = pow(x,3);
    r = (4.0/3.0) * 3.14159 * x;
    
    cout << setprecision(3) << fixed;
    cout << "VOLUME = " << r << '\n';
    return 0;
}