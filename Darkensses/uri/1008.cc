#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    double w,a,s;
    cin>>n>>w>>a;
    s = w*a;
    cout<<setprecision(2)<<fixed;
    cout<<"NUMBER = "<<n<<'\n'<<"SALARY = U$ "<<s<<'\n';
    return 0;
}