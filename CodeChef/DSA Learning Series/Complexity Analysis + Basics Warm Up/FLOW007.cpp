#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	while(n > 0)
	{
	    int t, rev=0;
	    cin>>t;
	    while (t > 0)
	    {
	        rev = (t%10 + rev)*10;
	        t = t/10;
	    }
	    cout<<rev/10<<endl;
	    n--;
	}
	return 0;
}
