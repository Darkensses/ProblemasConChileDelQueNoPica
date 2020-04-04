#include <bits/stdc++.h>
using namespace std;

int main()
{
    double a, b, c, media;
    cin >> a;
    cin >> b;
    cin >> c;
    media = ((a * 2) + (b * 3) + (c * 5)) / 10;
    cout << setprecision(1) << fixed;
    cout << "MEDIA = " << media << '\n';
    return 0;
}