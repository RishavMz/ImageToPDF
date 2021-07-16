#include<windows.h>
#include<iostream>
#include<string>
#include<fstream>
#include <commdlg.h>      // To allow GetOpenFileName

#define CONVERT 1 
#define ADD_IMAGE 2
#define MAX_IMAGES 200

LRESULT CALLBACK windowProcedure(HWND, UINT, WPARAM, LPARAM);     // Declare event loop

void AddControls(HWND);
void openFile(HWND);
int lastIndexOf(std::string, char);
std::string getPath();
void addToFile();
void convert();

HWND hEdit;
HWND Selected;
wchar_t IMAGES_ADDED[5000];
char images_selected[5000];
int imptr = 0;
int imgs = 0;
char filename[200];
std::string PATH;
std::string imfilepath;

// Main method for GUI application
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow)
{
    // Initializing data for creating window
    WNDCLASSW w = {0};
    w.hbrBackground = (HBRUSH)COLOR_WINDOW;
    w.hCursor = LoadCursor(NULL, IDC_ARROW);
    w.hInstance = hInst;
    w.lpszClassName = L"PDFconverter";
    w.lpfnWndProc = windowProcedure;

    // Create window if everything OK
    if(!RegisterClassW(&w))
        return -1;
    CreateWindow("PDFconverter","Image To PDF Converter", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100, 100, 500, 500, NULL, NULL, NULL, NULL);
    
    MSG msg = {0};
    while(GetMessage(&msg, NULL, NULL, NULL))       // Run event loop and handle messages and events
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK windowProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp)       // Define event loop
{
    switch (msg)                                // Handles messages
    {
        case WM_COMMAND:                        // Handles specific commands
            switch(wp)
            {
                case CONVERT:              // Prints the filename
                    wchar_t text[200];
                    GetWindowTextW(hEdit, text, 200);
                    for(int i=0; i<200; i++)
                    {
                        if(text[i]=='\0')
                            break;
                        filename[i] = text[i];
                    }
                    addToFile();                // Uploading filenames in a file
                    convert();
                    break;

                case ADD_IMAGE:                 // Adds one image at once to the temporary variable
                    openFile(hWnd);
                    break;    
            }
            break;
        case WM_CREATE:                         // Called when the window created
            AddControls(hWnd);
            PATH = getPath();
            imfilepath = PATH + "\\data\\database\\imageselected.txt";
            break;
        case WM_DESTROY:                        // Called when the Window closed
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProcW(hWnd, msg, wp, lp);   // Ignore event
    }


}

void AddControls(HWND hWnd)                     // Add elements to window
{
    CreateWindowW(L"Static", L"Enter filename : ", WS_VISIBLE | WS_CHILD, 70, 50, 150, 50, hWnd, NULL, NULL, NULL);
    hEdit = CreateWindowW(L"Edit", L"sample", WS_VISIBLE | WS_CHILD, 210, 47, 200, 25, hWnd, NULL, NULL, NULL );
    Selected = CreateWindowW(L"Static", IMAGES_ADDED, WS_VISIBLE | WS_CHILD | WS_BORDER, 70, 100, 350, 250, hWnd, NULL, NULL, NULL);
    CreateWindowW(L"Button", L"CONVERT", WS_VISIBLE | WS_CHILD, 300, 400, 100, 25, hWnd, (HMENU) CONVERT , NULL, NULL );
    CreateWindowW(L"Button", L"ADD IMAGE", WS_VISIBLE | WS_CHILD, 100, 400, 100, 25, hWnd, (HMENU) ADD_IMAGE , NULL, NULL );
}

void openFile(HWND hWnd)                        // Handle opening of file
{
    OPENFILENAME op;
    char file_name[200];                        // Individual file path size

    ZeroMemory(&op, sizeof(OPENFILENAME));
    op.lStructSize = sizeof(OPENFILENAME);
    op.hwndOwner = hWnd;
    op.lpstrFile = file_name;
    op.lpstrFile[0] = '\0';
    op.nMaxFile = 400;                          // Buffer size (MAX)
    op.lpstrFilter = "All files\0*.*\0PNG\0*.png\0JPEG\0*.jpeg\0JPG\0jpg\0";
    op.nFilterIndex = 1;

    if(imgs++ < MAX_IMAGES)
        GetOpenFileName(&op);                       // Opens the SELECT FILE window

    for(int i=0; i<200; i++)                        // Insert characters from buffer to required character array
    {
        if(op.lpstrFile[i]=='\0')
        {
            images_selected[imptr++] = '\n';
            break;
        }
        images_selected[imptr++] = op.lpstrFile[i];
    }

    SetWindowText(Selected, images_selected);   // Update contents of the Images Added
}

int lastIndexOf(std::string str, char x)
{
    for (int i = str.length() - 1; i >= 0; i--)
        if (str[i] == x)
            return i;
    return -1;
}

std::string getPath() {
    char buffer[MAX_PATH];
    GetModuleFileName( NULL, buffer, MAX_PATH );
    std::string::size_type pos = std::string( buffer ).find_last_of( "\\/" );
    if ( pos == std::string::npos ) 
        return "";
    else 
        return std::string( buffer ).substr( 0, pos);
    
}

void addToFile()
{
    std::ofstream fout;
    std::string line;
    fout.open(imfilepath);
    fout<<images_selected<<std::endl;
    fout.close();
}

void convert()
{
    char command1[100] = "python scripts/image2docx.py ";
    char command2[100] = "python scripts/convert.py ";
    char command3[100] = "cd ";
    for(int i=0; i<PATH.length(); i++)
        command3[strlen(command3)] = PATH[i];
    std::cout<<command3<<std::endl;
    int l1 = strlen(command1), l2 = strlen(command2), ld = strlen(filename);
    for(int i=0; i<ld; i++)
    {
        command1[l1+i] = filename[i];
        command2[l2+i] = filename[i];
    }
    command1[l1+ld]='\0';
    command2[l2+ld]='\0';

    std::cout<<"\n Step 1 : success => Successfully added all images\n"<<std::endl;
    system(command3);
    system("timeout 1");
    system("dir ");
    system(command1);
    std::cout<<"\n Step 2 : success => Successfully converted docx file\n"<<std::endl;
    std::cout<<"\n Please wait... converting a PDF file...\n"<<std::endl;
    system(command2);
    std::cout<<"\n Step 3 : success => Successfully created file\n"<<std::endl;
}