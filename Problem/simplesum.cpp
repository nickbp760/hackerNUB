#include <iostream>
#include <vector>
using namespace std;
int main()
{
int input;
cin >> input;
int lol;
vector <int> ea;
for (int i=0;i <=input;i++)
    {
    cin >> lol;
    ea.push_back(lol);
    }
lol=0;
//cout<<ea.size()<<endl;
for (int i=0;i < ea.size()-1; i++)
    {
    lol=ea[i]+lol;
    }
cout<<lol;
}
