#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

void read_vector(vector<string> &v)
{
    string test;
    string out;
    
    getline(cin, test);

    while(test != "exit")
    {
        while(test.length() != 0)
        {
            out += ' ';
            out += test;
            getline(cin, test);
        }
        
        out += ' ';
        v.push_back(out);
        out.clear();
        getline(cin, test);
    }
}
int valid_passports(vector<string> passports)
{
    int validPassports = 0;

    for(int i = 0; i < passports.size(); i++)
    {
        string currPass=passports.at(i);
        int dataCount = 0;
        bool containsCID = false;

        for(int k = 0; k < currPass.length(); k++)
        {
            if( currPass[k] == ':' )
                dataCount++;
            
            if( k < currPass.length()-4 )
                if( currPass[k] == 'c' && currPass[k+3] == ':' )
                    containsCID = true;
        }

        if(dataCount == 8 || (dataCount == 7 && !containsCID))
            validPassports++;
    }
    
    return validPassports;
}
bool valid_data(int data, int min, int max)
{
    return data >= min && data <= max;
}
string get_sub_str(string data, int i)
{
    string str;
    int length = 0;

    while(data[i+1+length] != ' ')
    {
        str += data[i+1+length];
        length++;
    }

    return str;
}
bool valid_height(string data, int i)
{
    string height = get_sub_str(data,i);
    char lastChar = height.back();

    if(height.length() < 4 || lastChar < 'm' || lastChar > 'n') 
        return false;
    
    else if(lastChar == 'n')
        return valid_data(atoi(height.c_str()), 59, 76);
    
    else
        return valid_data(atoi(height.c_str()), 150, 193);
}
bool valid_hair(string data, int i)
{
    if(data[i+1] != '#')
        return false;
    
    string color = get_sub_str(data, i);

    if(color.length() != 7)
        return false;

    for(int k = 1; k < 7; k++)
    {
        if((color[k] < '0' || color[k] > 'f') || (color[k] < 'a' && color[k] > '9'))
            return false;
    }

    return true;
}
bool valid_eye(string data, int i)
{
    string color = get_sub_str(data, i);

    return color == "amb" || color == "blu" || color == "brn" || color == "gry" || color == "grn" || color == "hzl" || color == "oth";
}
bool valid_pid(string data, int i)
{
    string id = get_sub_str(data, i);

    if(id.length() != 9)
        return false;
    
    for(int k = 0; k < 9; k++)
    {
        if(id[k] < '0' || id[k] > '9')
            return false;
    }

    return true;
}
int super_valid_passports(vector<string> passports)
{
    int validPassports = 0;

    for(int i = 0; i < passports.size(); i++)
    {
        string currPass=passports.at(i);
        int dataCount = 0;
        bool byr = false, iyr = false, eyr = false, hgt = false, hcl = false, ecl = false, pid = false;
        bool containsCID = false;

        for(int k = 0; k < currPass.length(); k++)
        {
            if( currPass[k] == ':' )
                dataCount++;
            
            if( k < currPass.length()-4 )
                if( currPass[k] == 'c' && currPass[k+3] == ':' )
                    containsCID = true;
        }

        if(dataCount == 8 || (dataCount == 7 && !containsCID))
        {
            for(int k = 3; k < currPass.length(); k++)
            {
                if(currPass[k] == ':' && currPass[k-3] == 'b' )
                {
                    string date = get_sub_str(currPass, k);
                    byr = valid_data(atoi(date.c_str()), 1920, 2002);
                }
                else if(currPass[k] == ':' && currPass[k-3] == 'i')
                {
                    string date = get_sub_str(currPass, k);
                    iyr = valid_data(atoi(date.c_str()), 2010, 2020);
                }
                else if(currPass[k] == ':' && currPass[k-3] == 'e' && currPass[k-2] == 'y')
                {
                    string date = get_sub_str(currPass, k);
                    eyr = valid_data(atoi(date.c_str()), 2020, 2030);
                }
                else if(currPass[k] == ':' && currPass[k-2] == 'g')
                {
                    hgt = valid_height(currPass, k);
                }
                else if(currPass[k] == ':' && currPass[k-3] == 'h' && currPass[k-2] == 'c')
                {
                    hcl = valid_hair(currPass, k);
                }
                else if(currPass[k] == ':' && currPass[k-3] == 'e' && currPass[k-2] == 'c')
                {
                    ecl = valid_eye(currPass, k);
                }
                else if(currPass[k] == ':' && currPass[k-3] == 'p')
                {
                    pid = valid_pid(currPass, k);
                }
            }

            if(byr && iyr && eyr && hgt && hcl && ecl && pid)
                validPassports++;
        }
    }
    
    return validPassports;
}

int main()
{
    vector<string> passports;
    read_vector(passports);

    cout << valid_passports(passports) << endl
         << super_valid_passports(passports);

    return 0;
}