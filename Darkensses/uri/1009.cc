#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string n;
    double s,g,r;
    cin>>n>>s>>g;
    r = s + ((15 * g)/100);
    cout<<setprecision(2)<<fixed;
    cout<<"TOTAL = R$ "<<r<<'\n';
    return 0;
}