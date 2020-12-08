#include <bits/stdc++.h>

int main(){
    std::ifstream file("5day_in.txt");
    std::vector<int> seatIDS;
    std::string seat;
    
    while(file >> seat){
        for(int i = 0; i < seat.length(); i++) seat[i] == 'B' || seat[i] == 'R'  ?  seat[i] = '1' : seat[i] = '0'; 
        seatIDS.push_back(stoi(seat, nullptr, 2));
    }
    sort(seatIDS.begin(), seatIDS.end());
    
    int ix = 0;
    while(seatIDS.at(ix) == (seatIDS.at(ix+1) - 1)) ix++;
    
    std::cout << seatIDS.back() << '\n' << (seatIDS.at(ix) + 1) << '\n';
    return 0;
}