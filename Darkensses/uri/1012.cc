#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    double a,b,c,r;
    cin>>a>>b>>c;

    cout<<setprecision(3)<<fixed;
    r = a*c/2;
    cout<<"TRIANGULO: "<<r<<'\n';
    r = 3.14159 * pow(c,2);
    cout<<"CIRCULO: "<<r<<'\n';
    r = ((a+b)/2)*c;
    cout<<"TRAPEZIO: "<<r<<'\n';
    r = b*b;
    cout<<"QUADRADO: "<<r<<'\n';
    r = a*b;
    cout<<"RETANGULO: "<<r<<'\n';
    return 0;
}