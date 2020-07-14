#include<iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t > 0)
	{
		int n;
		cin>>n;
		int maxi = 0;
		for(int i = 0; i < n; i++)
		{
			int a,b,c;
			cin>>a>>b>>c;
			int temp = b/(a+1) * c;
			if (temp > maxi)
				maxi = temp;
		}
		cout<<maxi<<endl;
		t--;
	}
}
