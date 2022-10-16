
# include <bits/stdc++.h>
# include <algorithm>
# define ll long long
# define re register int
using namespace std;

// int ans[2000], now[2000];
long long ans[2000], now[2000];
long long a, b;
bool bj = false;
long long m = 1;
/*ll a, b, m=1, ans[2000], now[2000];
bool bj=false;*/
long long gcd(long long a, long long b)
{
    if(!b)
	    return a;
	return gcd(b, a%b);
}

void yf(long long &a, long long &b)
{
    int tmp;
    tmp = gcd(a, b);
    a /= tmp;
    b /= tmp;
    return;
}
/*void yf(ll &a, ll &b)
{
	int g=gcd(a, b);
	a/=g;
	b/=g;
	return;
}*/
void dfs(long long x, long long p, long long A, long long B)//待求和的分数是A/B
{
    long long a = A, b = B;
    yf(a, b);
    if(x == 1)//已经搜索到规定的深度了
    {
        //cout << "x == 1" << endl;
        //system("pause");
        if (a == 1 && b > p)//如果待求和的分数能够约分成1/x的形式，就判断是不是要的答案：如果b比当前要搜索的最大分数1/p还要大 
        {
            if(bj && b >= ans[1]) // 比之前最小的分数要小 那找到的就没意义
            {
                return;
            }
            now[1] = b;
            bj=1;
			memcpy(ans, now, (m+1)<<3);
			return;
        }
        return;
    }
    long long start;
    //start = max(ceil(b / a), p);
    for (register int i=p; ceil((double)b*x/a)>=i; i++)
    {
        now[x] = i;
        //cout << x-1 << " " << i << " " << a * i - b << " " << b * i << " " << a << " " << b << endl;
        //dfs(x-1, i, a * i - b, b * i);
        dfs(x-1, i, a * i - b, b * i);
        //system("pause");
    }
    //system("pause");
    return;
}
int main()
{
    cin>>a>>b;
	yf(a,b);
    //memset(ans, sizeof(ans), 0);
    //memset(now, sizeof(now), 0);
	while(!bj)
	{
        // cout << "in" << endl;
		dfs(m, 1, a, b);
		m++;
	}
	for(int i=m-1; i>=1;i--)
		cout<<ans[i]<<" ";
    //system("pause");
    return 0; 
    /*cin>>a>>b;
	yf(a,b);
	while(!bj)
	{
		dfs(m, 1, a, b);
		m++;
	}
	for(re i=m-1;i>=1;i--)
		cout<<ans[i]<<" ";
		//system("pause");
	return 0;*/
}