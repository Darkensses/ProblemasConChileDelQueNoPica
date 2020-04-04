#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    double x,y,z,r;
    cin>>x>>y>>z;
    r = y*z;
    cin>>x>>y>>z;
    r += y*z;
    cout<<setprecision(2)<<fixed;
    cout<<"VALOR A PAGAR: R$ "<<r<<'\n';
    return 0;
}