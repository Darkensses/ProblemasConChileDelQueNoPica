#include <bits/stdc++.h>
using namespace std;

int main() {
    double a, b, media;
    cin>>a;
    cin>>b;
    media = ((a*3.5) + (b*7.5)) / 11;
    cout<<setprecision(5)<<fixed;
    cout<<"MEDIA = "<<media<<'\n';
    return 0;
}