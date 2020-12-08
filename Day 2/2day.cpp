#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

struct Password
{
    string bound;
    string character;
    string password;
};

void read_vector(vector<Password> &v)
{
    Password temp;
    cin >> temp.bound >> temp.character >> temp.password;
    
    while(temp.bound != "exit")
    {
        v.push_back(temp);
        cin >> temp.bound >> temp.character >> temp.password;
    }
}
int valid_passwords(vector<Password> v)
{
    int valid = 0;
    char lower[50];
    char upper[50];
    
    for(int i = 0; i < v.size(); i++)
    {
        memset(lower, '\0', 50);
        memset(upper, '\0', 50);
        
        int j = 0;
        bool up = false;
        for( int k = 0; k < v[i].bound.length(); k++)
        {
            if(!up)
            {
                lower[k] = v[i].bound[k];
            }
            else
            {
                upper[j] = v[i].bound[k];
                j++;
            }

            if(v[i].bound[k] == '-')
                up = true;
        }
        
        int count = 0;
        for(int j = 0; j < v[i].password.length(); j++)
        {
            if(v[i].password[j] == v[i].character[0])
                count++;
        }

        if(count >= atoi(lower) && count <= atoi(upper))
            valid++;
    }
    return valid;
}
int valid_passwords_2(vector<Password> v)
{
    int valid = 0;
    char lower[50];
    char upper[50];
    
    for(int i = 0; i < v.size(); i++)
    {
        memset(lower, '\0', 50);
        memset(upper, '\0', 50);
        
        int j = 0;
        bool up = false;
        for( int k = 0; k < v[i].bound.length(); k++)
        {
            if(!up)
            {
                lower[k] = v[i].bound[k];
            }
            else
            {
                upper[j] = v[i].bound[k];
                j++;
            }
               
            if(v[i].bound[k] == '-')
                up = true;
        }

        if((v[i].password[atoi(lower) - 1] == v[i].character[0] && v[i].password[atoi(upper) - 1] != v[i].character[0]) ||
           (v[i].password[atoi(lower) - 1] != v[i].character[0] && v[i].password[atoi(upper) - 1] == v[i].character[0]))
        {
            valid++;
        }
    }
    return valid;
}

int main()
{
    vector<Password> data;
    read_vector(data);

    cout << valid_passwords(data) << endl
         << valid_passwords_2(data) << endl;


    return 0;
}