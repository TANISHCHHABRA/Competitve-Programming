#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long n , x , ans, q;
        cin>>n>>x;
        ans = x;
        for(int j = 1 ; j < n ; j++)
        {
            cin>>q;
            x = min(q , x);
            ans += x;
        }
        cout<<ans<<endl;
    }
} 
