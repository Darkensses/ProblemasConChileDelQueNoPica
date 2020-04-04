#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t,cc=1, p;
    string s, sr;
    cin>>t;
    while(t--) {
        cin>>s;
        sr="";
        p=0;
        for(int i=0; i<s.size(); i++) {
            int n = s[i] - '0';
            while(p < n) {
                sr += "(";
                p++;
            }
            while(p>n) {
                sr += ")";
                p--;
            }
            sr += s[i];
        }
        for(int i=0; i<p; i++) {
            sr+= ")" ;
        }

        cout<<"Case #"<<cc<<": "<<sr<<'\n';
        cc++;
    }
    return 0;
}