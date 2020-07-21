#include <bits/stdc++.h>
#include<queue>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,z,temp;
        cin>>n>>z;
        priority_queue<int> A;
        for(int i = 0; i < n; i++)
        {
            cin>>temp;
            A.push(temp);
        }
        int ans = 0;
        while(A.top()!=0 && z>0)
        {
            ans++;
            temp = A.top();
            z -= temp;
            A.pop();
            A.push(temp/2);
        }
        if(z>0)
            cout<<"Evacuate"<<endl;
        else
            cout<<ans<<endl;
    }
} 
