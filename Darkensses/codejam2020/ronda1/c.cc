#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie();

    int t,n,cc = 1;        
    cin>>t;
    while(t--) {
        string ss = "";
        int s,e;
        vector<pair<int, int>> v;
        cin>>n;
        
        for(int i=0; i<n; i++) {
            cin >> s >> e;
            v.push_back(make_pair(s,e));
        }
        vector<pair<int, int>> va = v;
        sort(v.begin(),v.end());                

        int cs = 0, js = 0;

        for(int i=0; i<n; i++) {            

            if(cs <= v[i].first) {
                cs = v[i].second;
                ss += "C";                
            }
            else if(js <= v[i].first) {
                js = v[i].second;
                ss += "J";
            }
            else {
                ss = "IMPOSSIBLE";
                break;
            }

        }


        if(ss == "IMPOSSIBLE") {
            cout << "Case #" << cc << ": IMPOSSIBLE" << '\n';
        }
        else {
            string sss = "";
            vector<int> vi;
            for(int i = 0; i<n; i++) {
                int nn = 0;
                for(int j=0; j<n; j++) {          
                    if (va[i] == v[j] && !(find(vi.begin(),vi.end(),nn) != vi.end())) {
                        sss += ss[nn];
                        vi.push_back(nn);
                        break;
                    }
                    nn++;
                }
            }
            
            cout << "Case #" << cc << ": " << sss << '\n';
        }
        cc++;
    }
    return 0;
}