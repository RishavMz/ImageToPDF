#include<iostream>
#include<windows.h>
#include<string>
#include<fstream>

using namespace std;


int lastIndexOf(string str, char x)
{
    for (int i = str.length() - 1; i >= 0; i--)
        if (str[i] == x)
            return i;
    return -1;
}


int main(int argc, char** argv)
{
    string path;
    path = argv[0];
    path = path.substr(0, lastIndexOf(path, '\\'))+"\\data\\database\\imageselected.txt";
    
    
    // Uploading filenames in a file
    ofstream fout;
    string line;
    fout.open(path);
    while (fout) {
        getline(cin, line);
        if (line == "-1")
            break;
        fout << line << endl;
    }
    fout.close();

    // Modifying and making script calls
    string data= "Biscut";
    char command1[100] = "python scripts/image2docx.py ";
    char command2[100] = "python scripts/convert.py ";

    int l1 = strlen(command1), l2 = strlen(command2), ld = data.length();
    for(int i=0; i<ld; i++)
    {
        command1[l1+i] = data[i];
        command2[l2+i] = data[i];
    }
    command1[l1+ld]='\0';
    command2[l2+ld]='\0';
    system(command1);
    system(command2);



    return 0;
}
