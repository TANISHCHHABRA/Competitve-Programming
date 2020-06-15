#include<bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define ll long long int
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pl;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pl>		vpl;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;

//=======================

void tra(ll **arr,ll n,ll i,ll j)
{

    if (j<n-1)
    {
        if (arr[i][j+1]==0)
        {
            arr[i][j+1]=arr[i][j]+1;
            j++;
            tra(arr,n,i,j);
            return;
        }
    }
    if (i<n-1)
    {
        if (arr[i+1][j]==0)
        {
            arr[i+1][j]=arr[i][j]+1;
            i++;
            tra(arr,n,i,j);
            return;
        }
    }
    if (j>=1)
    {
        if (arr[i][j-1]==0)
        {
            arr[i][j-1]=arr[i][j]+1;
            j--;
            tra(arr,n,i,j);
            return;
        }
        
    }
    if (i>=1)
    {
        if (arr[i-1][j]==0)
        {
            arr[i-1][j]=arr[i][j]+1;
            i--;
            tra(arr,n,i,j);
            return;
        }
        
    }
    return;
    
    
}
void solve()
{
    ll n;
    cin>>n;
   ll **arr=new ll*[1000];
   for (int i = 0; i <1000; i++)
   {
       arr[i]=new ll[1000]();
   }
   
//    std::memset(arr,0,sizeof(arr));
   arr[0][0]=1;
    tra(arr,n,0,0);
    for (ll i = 0; i < n; i++)
    {
        for (ll j = 0; j<n; j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
    for(int i = 0; i < 1000; i++)
        delete[] arr[i];
    delete[] arr;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    //srand(chrono::high_resolution_clock::now().time_since_epoch().count());

    int t = 1;
    cin >> t;
    while(t--) {
      solve();
    }

    return 0;
}
