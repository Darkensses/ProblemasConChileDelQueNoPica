#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t,r;
    stringstream tt;
    cin>>t;
    r = t / 3600;
    tt << r << ":";
    t = t%3600;
    r = t/60;
    tt << r << ":";
    r = t%60;
    tt << r;
    cout<<tt.str()<<'\n';
    return 0;
}