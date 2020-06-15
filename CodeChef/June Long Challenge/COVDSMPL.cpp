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
int solve()
{
    int n,p;
    cin>>n>>p;
    int **arr=new int*[n];
    for (int i = 0; i < n; i++)
    {
        arr[i]=new int[n];
    }int o=1;
    for (int i = 0; i < n; i+=2)
    {
        for (int j = 0; j < n; j+=2)
        {
            int x;
            cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+1+o<<" "<<j+1+o<<endl;
            cin>>x;
            if(x==4)
            {
            arr[i][j]=1;
            arr[i+1][j]=1;
            arr[i][j+1]=1;
            arr[i+1][j+1]=1;
            }
            else if (x==3)
            {
                int y;
                cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+1+o<<" "<<j+o<<endl; 
                cin>>y;
                if (y==2)
                {   int z;
                    arr[i][j]=1;
                    arr[i+1][j]=1;
                    cout<<1<<" "<<i+o<<" "<<j+1+o<<" "<<i+o<<" "<<j+1+o<<endl; 
                    cin>>z;
                    if (z==1)
                    {
                        arr[i][j+1]=1;
                        arr[i+1][j+1]=0;
                    }
                    else
                    {
                        arr[i][j+1]=0;
                        arr[i+1][j+1]=1;
                    }
                    
                    
                }
                else
                {
                    int z;
                    arr[i][j+1]=1;
                    arr[i+1][j+1]=1;
                    cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+o<<" "<<j+o<<endl; 
                    cin>>z;
                    if (z==1)
                    {
                        arr[i][j]=1;
                        arr[i+1][j]=0;
                    }
                    else
                    {
                        arr[i][j]=0;
                        arr[i+1][j]=1;
                    }
                     
                }
                
                
            }
            else if (x==2)
            {
                int y;
                cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+1+o<<" "<<j+o<<endl; 
                cin>>y;
                if (y==2)
                {
                    arr[i][j]=1;
                    arr[i+1][j]=1;
                    arr[i][j+1]=0;
                    arr[i+1][j+1]=0;
                }
                else if(y==0)
                {
                    arr[i][j]=0;
                    arr[i+1][j]=0;
                    arr[i][j+1]=1;
                    arr[i+1][j+1]=1;
                }
                int yyy;
                cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+o<<" "<<j+1+o<<endl; 
                cin>>yyy;
                if(yyy==2)
                {
                    arr[i][j]=1;
                    arr[i][j+1]=1;
                    arr[i+1][j]=0;
                    arr[i+1][j+1]=0;
                }
                else if (yyy==0)
                {
                    arr[i][j]=0;
                    arr[i][j+1]=0;
                    arr[i+1][j+1]=1;
                    arr[i+1][j]=1;
                }
                else if(y==1 && yyy==1)
                {   int zz;
                    cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+o<<" "<<j+o<<endl;
                    cin>>zz;    
                    if (zz==1)
                    {
                        arr[i][j]=1;
                        arr[i+1][j]=0;
                        arr[i][j+1]=0;
                        arr[i+1][j+1]=1;
                    }
                    else
                    {
                        arr[i][j]=0;
                        arr[i+1][j]=1;
                        arr[i][j+1]=1;
                        arr[i+1][j+1]=0;
                    }
                    
                    
                }
                
            }
            else if(x==1)
            {
                int y;
                cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+1+o<<" "<<j+o<<endl; 
                cin>>y;
                if(y==1)
                {
                    arr[i+1][j+1]=0;
                    arr[i][j+1]=0;int yy;
                    cout<<1<<" "<<i+o<<" "<<j+o<<" "<<i+o<<" "<<j+o<<endl;
                    cin>>yy;
                    if (yy==1)
                    {
                        arr[i][j]=1;
                        arr[i+1][j]=0;
                    }
                    else
                    {
                        arr[i][j]=0;
                        arr[i+1][j]=1;
                    }
                    
                }
                else
                {
                    arr[i][j]=0;
                    arr[i+1][j]=0;int yy;
                    cout<<1<<" "<<i+o<<" "<<j+1+o<<" "<<i+o<<" "<<j+1+o<<endl;
                    cin>>yy;
                    if (yy==1)
                    {
                        arr[i][j+1]=1;
                        arr[i+1][j+1]=0;
                    }
                    else
                    {
                        arr[i][j+1]=0;
                        arr[i+1][j+1]=1;
                    }
                    
                }
                
            }
            else if(x==0)
            {
                arr[i][j]=0;
                arr[i+1][j]=0;
                arr[i][j+1]=0;
                arr[i+1][j+1]=0;
            }
        }
        
    }
    cout<<2<<endl;int aa;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
    
    cin>>aa;

    for(int i=0;i<n;i++)
        { 
           delete []arr[i];
        }
    delete []arr;
    return aa;
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int t = 1;
    cin >> t;
    while(t--) {
      int cc=solve();
      if(cc==-1)
      {
          break;
      }
    }

    return 0;
}
