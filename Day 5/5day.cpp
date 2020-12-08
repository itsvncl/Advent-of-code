#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

void read_vector_from_file(vector<string> &v)
{   
    ifstream file("5day_in.txt");
    string line;
    
    while(getline(file, line))
        v.push_back(line);

    file.close();
}
pair<int, int> seat_index(string pass)
{
    pair<int, int> seatInd = {0,0};
    int rowUp = 127;
    int rowLow = 0;
    int colUp = 7;
    int colLow = 0;

    for(int i = 0; i < pass.length(); i++)
    {
        if(pass[i] == 'F')
            rowUp = (rowUp + rowLow) / 2;
        else if(pass[i] == 'B')
            rowLow = (rowLow + rowUp + 1) / 2;
        else if(pass[i] == 'L')
            colUp = (colUp + colLow) / 2;
        else if(pass[i] == 'R')
            colLow = (colLow + colUp + 1) / 2;
        else
            return seatInd;
    }

    seatInd.first = rowLow;
    seatInd.second = colLow;

    return seatInd;
}

int main()
{
    vector<int> seatIDS;
    vector<string> pass;
    read_vector_from_file(pass);

    for(int i = 0; i < pass.size(); i++)
        seatIDS.push_back( seat_index(pass.at(i)).first * 8 + seat_index(pass.at(i)).second );

    sort(seatIDS.begin(), seatIDS.end());
    
    int ix = 0;
    while(seatIDS.at(ix) == (seatIDS.at(ix+1) - 1)) ix++;

    cout << seatIDS.back() << '\n' << (seatIDS.at(ix) + 1) << '\n';

    return 0;
}