#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie();

    int t,n,k,r,c,cc=1;
    cin>>t;
    while(t--) {
        cin>>n;
        int a[n][n];
        k = 0; 
        r = 0;
        c = 0;       
        for(int i=0; i<n; i++) {            
            set<int> row;
            for(int j=0; j<n; j++) {
                cin>>a[i][j];
                row.insert(a[i][j]);
                if(i==j) { //suma diagonal
                    k += a[i][j];
                }
            }
            if(row.size()<n) {
                r++;
            }
        }
        
        for(int i=0; i<n; i++) {
            set<int> col;
            for(int j=0; j<n; j++) {
                col.insert(a[j][i]);
            }
            if(col.size()<n)
                c++;
        }

        cout << "Case #" << cc << ": " << k << " " << r << " " << c << '\n';
        cc++;
    }
    return 0;
}