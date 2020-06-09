#include<bits/stdc++.h>

using namespace std;

int main()
{
	long long t;
	cin>>t;
	long long a[t];
	for(long long i = 0; i < t; i++)
		cin>>a[i];
	
	sort(a, a+t);
	
	long long c = t, maxi = 0;
	for(long long i = 0; i < t; i++)
	{
		if(a[i]*c > maxi)
			maxi = a[i]*c;
		c--;
	}
	cout<<maxi;
	
	return 0;
}
