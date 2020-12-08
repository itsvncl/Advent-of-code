#include <bits/stdc++.h>
using namespace std;

pair<string, int> parse_instruction(string &instruction)
{
    pair<string, int> paresedInstruction;

    paresedInstruction.first = instruction.substr(0,3); //Parse the operation
    
    int sign = 1;
    if(instruction[4] == '-')    //Determine the sign of the argument
        sign = -1;
    
    paresedInstruction.second = sign * atoi(instruction.substr(5).c_str()); //Parse the argument

    return paresedInstruction;
}

pair<bool, int> compjutor(vector<pair<string, int>> &instructions)   //https://youtu.be/8d4RtvMQp10   yep yep yep
{
    bool infinite = false;
    int value = 0;
    vector<int> finishedInstruction;
    pair<bool, int> stateAndValue;  //If the bool value is 1 then the code is infinite, either way it return the value;

    int i = 0;
    while( i < instructions.size() && !infinite )   //Running the code
    {
        for(const int &k : finishedInstruction)            //Checking if a code has executed before, probabbly a stupid implemention idk
        {
            if(k == i)
                infinite = true;
        }

        if(instructions[i].first == "acc")
        {
            finishedInstruction.push_back(i);
            value += instructions[i++].second;
        }
        else if(instructions[i].first == "jmp")
        {
            finishedInstruction.push_back(i);
            i += instructions[i].second;
        }
        else
        {
            finishedInstruction.push_back(i++);
        }
    }

    stateAndValue.first = infinite;
    stateAndValue.second = value;
    
    return stateAndValue;
}
int fixed_value_brute(vector<pair<string, int>> &instructions, int lineIndex)   //Brute force
{
    pair<bool, int> current = {1,0};
    for(size_t i = 0; i < instructions.size() && current.first; i++)
    {
        if(instructions[i].first == "jmp")
        {
            instructions[i].first = "nop";
            current = compjutor(instructions);
            instructions[i].first = "jmp";
        }
        else if(instructions[i].first == "nop")
        {
            instructions[i].first = "jmp";
            current = compjutor(instructions);
            instructions[i].first = "nop";
        }
    }

    return current.second;
}

int main()
{
    ifstream file("8day_in.txt");
    vector<pair<string, int>> instructions; //Storing the instructions as pairs
    string instruction;

    while(getline(file, instruction))
        instructions.push_back(parse_instruction(instruction)); //Reading from file

    cout << compjutor(instructions).second << '\n'
         << fixed_value_brute(instructions, 0) << '\n';

    return 0;
}