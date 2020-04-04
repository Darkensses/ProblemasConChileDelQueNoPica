#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    double x, y, xx, yy, r;
    cin >> x >> y >> xx >> yy;

    r = sqrt(pow(xx-x,2) + pow(yy-y,2));
    cout << setprecision(4) << fixed;
    cout << r << '\n';
    return 0;
}